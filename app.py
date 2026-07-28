from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config

from analyzers.syntax_checker import check_syntax
from analyzers.explanation_engine import explain_error
from analyzers.runtime_checker import check_runtime
from analyzers.runtime_explanation import explain_runtime_error
from analyzers.quality_checker import analyze_code_quality
from analyzers.marks_calculator import calculate_marks
from analyzers.advance_checker import advanced_review
app = Flask(__name__)

app.config.from_object(Config)

# Required for session handling
app.secret_key = "automated_code_review_secret"


mysql = MySQL(app)



# ---------------- HOME ----------------

@app.route("/")
def home():

    return render_template("home.html")



# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]


        hashed_password = generate_password_hash(password)


        cursor = mysql.connection.cursor()


        cursor.execute(
            """
            INSERT INTO users
            (name,email,username,password)

            VALUES(%s,%s,%s,%s)
            """,

            (
                name,
                email,
                username,
                hashed_password
            )
        )


        mysql.connection.commit()

        cursor.close()


        return redirect(
            url_for("login")
        )


    return render_template(
        "register.html"
    )




# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():


    if request.method == "POST":


        username = request.form["username"]

        password = request.form["password"]



        cursor = mysql.connection.cursor()


        cursor.execute(
            "SELECT * FROM users WHERE username=%s",
            (username,)
        )


        user = cursor.fetchone()


        cursor.close()



        if user and check_password_hash(
            user[4],
            password
        ):


            session["user_id"] = user[0]

            session["username"] = user[3]


            return redirect(
                url_for("dashboard")
            )



        return "Invalid Username or Password"



    return render_template(
        "login.html"
    )





# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():


    if "user_id" not in session:

        return redirect(
            url_for("login")
        )


    return render_template(

        "dashboard.html",

        username=session["username"]

    )





# ---------------- CODE REVIEW ----------------

@app.route("/review", methods=["GET", "POST"])
def review():

    if "user_id" not in session:
        return redirect(url_for("login"))

    reviewed_code = ""
    result = None


    if request.method == "POST":

        reviewed_code = request.form["code"]


        # Syntax Checking
        result = check_syntax(reviewed_code)


        # If syntax error
        if result["status"] == "error":

            result["details"] = explain_error(
                result["message"]
            )


            # Calculate marks
            result["marks"] = calculate_marks(result)



        else:

            # Runtime Checking
            runtime_result = check_runtime(
                reviewed_code
            )

            result["runtime"] = runtime_result



            # Runtime error explanation
            if runtime_result["status"] == "error":

                result["runtime_details"] = explain_runtime_error(
                    runtime_result["error"]
                )



            # Code Quality Checking
            quality_result = analyze_code_quality(
                reviewed_code
            )

            result["quality"] = quality_result



            # Advanced Code Analysis
            advanced_result = advanced_review(
                reviewed_code
            )

            result["advanced"] = advanced_result



            # Calculate marks
            result["marks"] = calculate_marks(result)




            # Save Review History

            cursor = mysql.connection.cursor()


            cursor.execute("""
                INSERT INTO review_history
                (
                    user_id,
                    code,
                    syntax_status,
                    runtime_status,
                    marks,
                    output
                )
                VALUES(%s,%s,%s,%s,%s,%s)
            """,
            (
                session["user_id"],
                reviewed_code,
                result["status"],
                runtime_result["status"],
                result["marks"],
                runtime_result.get("output", "")
            ))


            mysql.connection.commit()

            cursor.close()



    return render_template(
        "review.html",
        reviewed_code=reviewed_code,
        result=result
    )
# ---------------- OTHER MODULES ----------------


@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT review_id,
               review_date,
               syntax_status,
               runtime_status,
               marks
        FROM review_history
        WHERE user_id = %s
        ORDER BY review_date DESC
    """, (session["user_id"],))

    history_data = cursor.fetchall()

    cursor.close()

    return render_template(
        "history.html",
        history=history_data
    )




@app.route("/statistics")
def statistics():

    if "user_id" not in session:
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor()

    # Total Reviews
    cursor.execute("""
        SELECT COUNT(*)
        FROM review_history
        WHERE user_id=%s
    """, (session["user_id"],))

    total_reviews = cursor.fetchone()[0]

    # Highest Marks
    cursor.execute("""
        SELECT MAX(marks)
        FROM review_history
        WHERE user_id=%s
    """, (session["user_id"],))

    highest_marks = cursor.fetchone()[0]

    if highest_marks is None:
        highest_marks = 0

    # Average Marks
    cursor.execute("""
        SELECT AVG(marks)
        FROM review_history
        WHERE user_id=%s
    """, (session["user_id"],))

    average_marks = cursor.fetchone()[0]

    if average_marks is None:
        average_marks = 0
    else:
        average_marks = round(average_marks, 2)

    # Syntax Errors
    cursor.execute("""
        SELECT COUNT(*)
        FROM review_history
        WHERE user_id=%s
        AND syntax_status='error'
    """, (session["user_id"],))

    syntax_errors = cursor.fetchone()[0]

    # Runtime Errors
    cursor.execute("""
        SELECT COUNT(*)
        FROM review_history
        WHERE user_id=%s
        AND runtime_status='error'
    """, (session["user_id"],))

    runtime_errors = cursor.fetchone()[0]

    # Successful Programs
    cursor.execute("""
        SELECT COUNT(*)
        FROM review_history
        WHERE user_id=%s
        AND runtime_status='success'
    """, (session["user_id"],))

    successful_programs = cursor.fetchone()[0]

    cursor.close()

    return render_template(
        "statistics.html",
        total_reviews=total_reviews,
        highest_marks=highest_marks,
        average_marks=average_marks,
        syntax_errors=syntax_errors,
        runtime_errors=runtime_errors,
        successful_programs=successful_programs
    )




@app.route("/leaderboard")
def leaderboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor()

    cursor.execute("""
        SELECT
            users.username,
            ROUND(AVG(review_history.marks), 2) AS average_marks,
            COUNT(review_history.review_id) AS total_reviews
        FROM users
        JOIN review_history
            ON users.user_id = review_history.user_id
        GROUP BY users.user_id, users.username
        ORDER BY average_marks DESC
    """)

    leaderboard_data = cursor.fetchall()

    cursor.close()

    return render_template(
        "leaderboard.html",
        leaderboard=leaderboard_data
    )




@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor()

    # Get user information
    cursor.execute("""
        SELECT name, email, username, created_at
        FROM users
        WHERE user_id=%s
    """, (session["user_id"],))

    user = cursor.fetchone()


    # Total reviews
    cursor.execute("""
        SELECT COUNT(*)
        FROM review_history
        WHERE user_id=%s
    """, (session["user_id"],))

    total_reviews = cursor.fetchone()[0]


    # Highest marks
    cursor.execute("""
        SELECT MAX(marks)
        FROM review_history
        WHERE user_id=%s
    """, (session["user_id"],))

    highest_marks = cursor.fetchone()[0]

    if highest_marks is None:
        highest_marks = 0


    # Average marks
    cursor.execute("""
        SELECT AVG(marks)
        FROM review_history
        WHERE user_id=%s
    """, (session["user_id"],))

    average_marks = cursor.fetchone()[0]

    if average_marks is None:
        average_marks = 0
    else:
        average_marks = round(average_marks, 2)


    # Find leaderboard rank
    cursor.execute("""
        SELECT user_id, AVG(marks) AS avg_marks
        FROM review_history
        GROUP BY user_id
        ORDER BY avg_marks DESC
    """)

    ranking = cursor.fetchall()

    rank = "Not Ranked"

    for index, row in enumerate(ranking, start=1):

        if row[0] == session["user_id"]:
            rank = index
            break


    cursor.close()


    return render_template(
        "profile.html",
        user=user,
        total_reviews=total_reviews,
        highest_marks=highest_marks,
        average_marks=average_marks,
        rank=rank
    )



# ---------------- LOGOUT ----------------


@app.route("/logout")
def logout():

    session.clear()


    return redirect(
        url_for("home")
    )





if __name__ == "__main__":

    app.run(
        debug=True
    )
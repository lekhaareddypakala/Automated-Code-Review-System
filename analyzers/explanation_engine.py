def explain_error(error_message):
    print("Explanation engine called:", error_message)

    error_message = error_message.lower()


    if "expected ':'" in error_message:

        return {

            "issue": "Missing Colon",

            "explanation":
            "Python requires a colon (:) after statements like if, else, for, while, def, and class.",

            "reason":
            "The colon tells Python that a new block of code is starting.",

            "solution":
            "Add ':' at the end of the statement.",

            "example":
            "if age > 18:\n    print('Adult')"

        }


    elif "indent" in error_message:

        return {

            "issue": "Indentation Error",

            "explanation":
            "Python uses spaces or tabs to identify blocks of code.",

            "reason":
            "Incorrect indentation changes the structure of your program.",

            "solution":
            "Keep the code inside a block properly indented.",

            "example":
            "if x > 5:\n    print(x)"

        }


    elif "never closed" in error_message:

        return {

            "issue": "Missing Closing Bracket",

            "explanation":
            "Every opening bracket must have a matching closing bracket.",

            "reason":
            "Python cannot understand where the statement ends.",

            "solution":
            "Add the missing closing bracket.",

            "example":
            "print('Hello')"

        }


    else:

        return {

            "issue": "Syntax Error",

            "explanation":
            "Python found a mistake in the structure of your code.",

            "reason":
            "The interpreter cannot understand this statement.",

            "solution":
            "Check the line mentioned in the error message.",

            "example":
            "Review Python syntax rules."

        }
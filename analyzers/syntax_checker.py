import ast


def check_syntax(code):

    try:

        ast.parse(code)

        return {
            "status": "success",
            "message": "No syntax errors found."
        }

    except SyntaxError as e:

        return {

            "status": "error",

            "line": e.lineno,

            "message": e.msg

        }
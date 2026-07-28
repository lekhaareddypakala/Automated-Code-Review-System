def explain_runtime_error(error_message):

    error_message = error_message.lower()


    # Name Error
    if "nameerror" in error_message:

        return {

            "issue": "Undefined Variable",

            "explanation":
            "Python is trying to use a variable or name that has not been created.",

            "reason":
            "Python is case-sensitive. Check whether the variable name is declared correctly.",

            "solution":
            "Create the variable before using it or check spelling and capitalization.",

            "example":
            "Correct:\n\nprint(True)\n\nIncorrect:\n\nprint(true)"

        }


    # Zero Division Error
    elif "zerodivisionerror" in error_message:

        return {

            "issue": "Division by Zero",

            "explanation":
            "A number cannot be divided by zero in Python.",

            "reason":
            "Division by zero is mathematically undefined.",

            "solution":
            "Check the denominator before performing division.",

            "example":
            "if b != 0:\n    result = a / b"

        }


    # Type Error
    elif "typeerror" in error_message:

        return {

            "issue": "Invalid Data Type Operation",

            "explanation":
            "Python found an operation between incompatible data types.",

            "reason":
            "Different data types cannot always be combined directly.",

            "solution":
            "Convert the values into compatible data types.",

            "example":
            "Correct:\n\nint('10') + 5"

        }


    # Value Error
    elif "valueerror" in error_message:

        return {

            "issue": "Invalid Value",

            "explanation":
            "The value provided is not acceptable for that operation.",

            "reason":
            "The data type is correct but the value is not valid.",

            "solution":
            "Provide a valid value before performing the operation.",

            "example":
            "int('123')"

        }


    # Index Error
    elif "indexerror" in error_message:

        return {

            "issue": "Index Out of Range",

            "explanation":
            "You are trying to access a position that does not exist in the list.",

            "reason":
            "List indexing starts from 0 and must be within the available range.",

            "solution":
            "Check the list length before accessing the index.",

            "example":
            "numbers[0]"

        }


    else:

        return {

            "issue": "Runtime Error",

            "explanation":
            "Python encountered an error while executing the program.",

            "reason":
            "Review the error message and check the related code.",

            "solution":
            "Debug the program based on the error type.",

            "example":
            "Check Python documentation."

        }
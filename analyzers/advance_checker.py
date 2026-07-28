def advanced_review(code):

    suggestions = []

    lines = code.split("\n")


    # Variable naming check
    for index, line in enumerate(lines, start=1):

        if "=" in line:

            variable = line.split("=")[0].strip()

            if len(variable) == 1 and variable.isalpha():

                suggestions.append({

                    "line": index,

                    "issue":
                    "Single letter variable name",

                    "suggestion":
                    "Use meaningful variable names for better readability."

                })


    # Comment checking
    has_comment = False

    for line in lines:

        if "#" in line:
            has_comment = True


    if len(lines) > 5 and not has_comment:

        suggestions.append({

            "line": "-",

            "issue":
            "No comments found",

            "suggestion":
            "Add comments to explain important parts of your code."

        })


    # Duplicate line checking

    checked_lines = set()

    for index, line in enumerate(lines, start=1):

        line = line.strip()

        if line and line in checked_lines:

            suggestions.append({

                "line": index,

                "issue":
                "Duplicate code",

                "suggestion":
                "Avoid repeating the same code. Consider using a function."

            })

        checked_lines.add(line)


    return suggestions
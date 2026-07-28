import ast


def analyze_code_quality(code):

    suggestions = []

    lines = code.split("\n")

    # 1. Long lines
    for i, line in enumerate(lines):

        if len(line) > 80:
            suggestions.append({
                "line": i + 1,
                "message": "This line is longer than 80 characters."
            })

    # 2. Tabs instead of spaces
    for i, line in enumerate(lines):

        if "\t" in line:
            suggestions.append({
                "line": i + 1,
                "message": "Use spaces instead of tabs for indentation."
            })

    # 3. Missing comments
    if "#" not in code:
        suggestions.append({
            "line": "-",
            "message": "Consider adding comments to explain important parts of your code."
        })

    # 4. Single-letter variable names
    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.Name):

                if len(node.id) == 1 and node.id not in ["i", "j", "k"]:

                    suggestions.append({
                        "line": node.lineno,
                        "message": f"Variable '{node.id}' could have a more meaningful name."
                    })

    except:
        pass

    return suggestions
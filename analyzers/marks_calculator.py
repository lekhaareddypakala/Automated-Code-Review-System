def calculate_marks(result):

    marks = 100

    # Syntax Error
    if result["status"] == "error":
        return 0

    # Runtime Error
    if "runtime" in result:

        if result["runtime"]["status"] == "error":
            marks -= 30

    # Quality Suggestions
    if "quality" in result:

        marks -= len(result["quality"]) * 5

    if marks < 0:
        marks = 0

    return marks
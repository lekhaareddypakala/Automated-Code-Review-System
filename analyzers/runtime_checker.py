import subprocess
import tempfile
import sys


def check_runtime(code):

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False
        ) as file:

            file.write(code)

            file_path = file.name


        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=5
        )


        if result.returncode == 0:

            return {

                "status": "success",

                "output": result.stdout

            }


        else:

            return {

                "status": "error",

                "error": result.stderr

            }


    except subprocess.TimeoutExpired:

        return {

            "status": "error",

            "error": "Program execution timed out. Possible infinite loop."

        }

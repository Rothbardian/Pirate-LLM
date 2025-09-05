from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file
# from functions.run_calc_expression import run_calc_expression

function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
    # "run_calc_expression": run_calc_expression,
}

def call_function(function_call: types.FunctionCall, verbose=False):
    function_name = function_call.name
    args = function_call.args or {}

    # Inject working directory (security)
    args["working_directory"] = "./calculator"

    # Default empty args list for run_python_file if not provided
    if function_name == "run_python_file" and "args" not in args:
        args["args"] = []

    if verbose:
        print(f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}")

    func = function_map.get(function_name)
    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"}
                )
            ],
        )

    try:
        result = func(**args)
    except Exception as e:
        result = f"Function call failed: {e}"

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result}
            )
        ],
    )

from google.genai import types

from calculator.pkg.calculator import Calculator
from calculator.pkg.render import render

def run_calc_expression(working_directory, expression):
    """
    Directly instantiate and run the Calculator on the expression,
    then render the output as the calculator CLI would do.
    Arguments:
      - working_directory: str, not used here but for consistent API
      - expression: str, the arithmetic expression to calculate
    Returns:
      - str: the rendered output string
    """
    calculator = Calculator()
    try:
        result = calculator.evaluate(expression)
        output = render(expression, result)
        return output
    except Exception as e:
        return f"Error: {e}"

schema_run_calc_expression = types.FunctionDeclaration(
    name="run_calc_expression",
    description="Evaluate an arithmetic expression using the Calculator and render the output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "expression": types.Schema(type=types.Type.STRING, description="The arithmetic expression to evaluate"),
        },
        required=["expression"],
    ),
)
from api_wrapper.calculator.__api import ExternalCalculator


class Calculator:
    """
    Any solution can do the job, but this one is designed to be robust and handle edge cases.
    It wraps around an external calculator library to provide basic arithmetic operations
    """

    def __init__(self):
        self._calc = ExternalCalculator()

    def add(self, a, b):
        return self._safe_compute("add", a, b)

    def subtract(self, a, b):
        return self._safe_compute("subtract", a, b)

    def multiply(self, a, b):
        return self._safe_compute("multiply", a, b)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return self._safe_compute("divide", a, b)

    def _safe_compute(self, operation, a, b):
        try:
            # Validate inputs
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Arguments must be numbers")

            result = self._calc.compute(operation, a, b)
            return result

        except ValueError as e:
            raise ValueError(f"Calculation failed: {e}")

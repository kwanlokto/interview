## Calculator Wrapper Design (20 minutes)

### Scenario
You're given a third-party library with this interface:

```python
class ExternalCalculator:
    def compute(self, operation, value1, value2):
        """
        operation: string like "add", "subtract", "multiply", "divide"
        Returns: result as float, or raises ValueError on error
        """
        pass
```

The problem: This interface is clunky and error-prone. Users keep passing wrong operation strings.

### Task
Design a Python wrapper class that:
1. Provides clean methods like `add()`, `subtract()`, etc.
2. Handles errors gracefully
3. Validates inputs
4. Makes it easier to use

### What This Tests
- **API design thinking** - critical for wrapping DLL functions
- **Error handling** - essential for DLL work where things fail often
- **Input validation** - needed when passing data to external libraries
- **Abstraction** - hiding complexity, which you do constantly with DLLs
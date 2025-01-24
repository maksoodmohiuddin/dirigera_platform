# Python Testing Prompt Library

## Prompt:
Using the guidelines listed here, implement comprehensive tests for the [specific Python module, function, or class here].

### 1. Test Structure and Naming Conventions
- Use descriptive test names following the format `test_does_something_when_condition()`, clarifying the purpose of each test.
- Organize related tests in a dedicated test file (e.g., `test_module_name.py`), with helper functions or classes as needed.
- Use docstrings or comments to describe test purposes and group similar test cases for readability.

### 2. Essential Libraries
- **unittest**: Standard Python testing framework for creating test cases and suites.
- **pytest**: Enhanced testing framework supporting fixtures, parameterization, and concise assertions.
- **unittest.mock**: For mocking dependencies, functions, or classes.
- **pytest-mock**: A pytest plugin to simplify mocking with pytest.

### 3. Types of Tests
- **Unit Tests**: Test individual functions or methods, isolating any dependencies with mocks.
- **Integration Tests**: Verify interactions between components, optionally using in-memory databases or temporary files.
- **Parameterized Tests**: Test multiple inputs and scenarios using `@pytest.mark.parametrize` for concise coverage of edge cases.

### 4. Mocking and Test Data
- Use `unittest.mock.patch` or `pytest-mock` to mock dependencies, such as external services or complex functions.
- Use `Mock` or `MagicMock` to control behavior and verify interactions with mocks.
- Define reusable test data in fixtures or helper functions for consistent and maintainable testing.

### 5. Writing Effective Tests
- Follow the Arrange-Act-Assert (AAA) pattern to set up conditions, execute actions, and validate outcomes.
- Cover positive outcomes as well as edge cases and error handling, ensuring robustness.
- Use assertions to check return values, side effects, and exceptions; leverage assert statements in pytest for readability.

### 6. Test Coverage
- Aim for comprehensive coverage focusing on critical functionality and edge cases rather than aiming for 100%.
- Use tools like `pytest-cov` to generate coverage reports, identifying any untested code paths.
- Prioritize testing core logic and error-prone areas over simple getter and setter methods.
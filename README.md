# Calculator Demo Package

A simple calculator package demonstrating a complete CI/CD pipeline with GitHub Actions.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide).
- Full test coverage
- Automated release process
- Security scanning
- Code quality checks

## Installation

```bash
pip install calculator-demo
```

## Usage

```python
from calculator import add, subtract, multiply, divide

# Basic operations
result = add(5, 3)      # 8
result = subtract(5, 3)  # 2
result = multiply(5, 3)  # 15
result = divide(6, 2)    # 3.0
```

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/calculator-demo.git
   cd calculator-demo
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Run tests:
   ```bash
   pytest
   ```

## Release Process

See [RELEASE.md](RELEASE.md) for detailed information about the release process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
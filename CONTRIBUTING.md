# Contributing to AI Observability Python SDK

Thanks for your interest in contributing! Whether fixing a bug, adding a feature, or improving docs, your help is welcome.

## Getting Started

1. **Fork** the repository
2. **Clone** your fork

   `bash
   git clone https://github.com/YOUR_USERNAME/aiobservability-python.git
   cd aiobservability-python
   `

3. **Create a branch**

   `bash
   git checkout -b feature/your-feature-name
   `

4. **Install in development mode**

   `bash
   pip install -e .
   `

## Development

- The main SDK code is in `aiobservability/aiobservability.py`
- Public exports are in `aiobservability/__init__.py`
- Run the test script to validate changes:

   `bash
   python test_sdk.py
   `

## Testing with the Live API

Use the demo key for testing:

`python
from aiobservability import AIObservability
client = AIObservability(api_key="ai_demo_key_12345")
`

## Pull Request Guidelines

- Keep changes focused on a single feature or fix
- Test your changes with `python test_sdk.py`
- Update the README if adding new public methods
- PRs should target the `main` branch

## Questions?

Open an issue or reach out at hello@usefreelanceflow.com

---

**Happy coding!** 🚀
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aiobservability",
    version="1.0.0",
    author="FreelanceFlow",
    author_email="hello@usefreelanceflow.com",
    description="Python SDK for AI Observability - Monitor LLM usage across 21+ models with smart routing, cost tracking, and budget management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/freelanceflow/aiobservability-python",
    project_urls={
        "Documentation": "https://ai-api.usefreelanceflow.com/docs",
        "Source": "https://github.com/freelanceflow/aiobservability-python",
        "Tracker": "https://github.com/freelanceflow/aiobservability-python/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "aiohttp>=3.8.0",
    ],
    keywords="ai, llm, observability, cost-tracking, model-routing, openai, groq, google-gemini",
)

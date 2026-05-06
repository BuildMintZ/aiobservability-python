# AI Observability Python SDK

[![PyPI version](https://badge.fury.io/py/aiobservability.svg)](https://badge.fury.io/py/aiobservability)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Monitor, track, and optimize your LLM usage across 21+ AI models with one SDK.

## ✨ Features

- 🚀 **Smart Routing** - Route prompts by cost, speed, or quality
- 📊 **Cost Tracking** - Track usage and costs across all models
- 💰 **Budget Management** - Set budgets and get alerts
- 🔍 **Model Comparison** - Compare 21+ models side-by-side
- 📚 **RAG Knowledge Base** - Search your documents
- 🖼️ **Image Generation** - Generate images from text
- ⚡ **Async Support** - High-throughput async operations

## ✅ Confirmed Working Models

| Provider | Model | Latency | Cost |
|----------|-------|---------|------|
| Groq | llama-3.1-8b-instant | 58ms | ~$0.00003 |
| Groq | llama-3.3-70b-versatile | 386ms | ~$0.00003 |
| Groq | gpt-oss-120b | 308ms | ~$0.00014 |
| Google | gemma-3-27b-it | 773ms | FREE |
| Google | gemma-3-1b-it | 694ms | FREE |
| Google | gemini-2.5-flash | 1640ms | ~$0.000002 |

## 📦 Installation

```bash
pip install freelanceflow
🚀 Quick Start
python
from aiobservability import AIObservability

# Initialize client
client = AIObservability(api_key="your_api_key")

# Route a prompt (automatically picks best model)
response = client.route("What is machine learning?", preference="speed")
print(f"Response: {response['response']}")
print(f"Cost: ${response['cost']}")
print(f"Latency: {response['latencyMs']}ms")

📊 Usage Examples

Track LLM Usage

python
from aiobservability import LLMUsage

usage = LLMUsage(
    tenant_id="my-company",
    user_id="user-123",
    provider="groq",
    model="llama-3.1-8b-instant",
    prompt="What is AI?",
    completion="AI is artificial intelligence...",
    prompt_tokens=10,
    completion_tokens=50,
    duration_ms=150
)
client.track(usage)
Get Usage History
python

# Get history (uses default tenant)
history = client.get_usage_history(limit=10)
print(f"Found {len(history)} records")

# Or specify a different tenant
history = client.get_usage_history(tenant_id="other-tenant", limit=10)

# Compare Models

python
# Compare models side-by-side
comparison = client.compare_models("What is Python?")
for model in comparison['results']:
    print(f"{model['model']}: ${model['cost']} - {model['latencyMs']}ms")
Clean Up
python

# Close the client connection
client.close()

📖 API Reference
Full documentation: https://ai-api.usefreelanceflow.com/docs

🔑 Authentication
Get your API key from the AI Observability Dashboard.
https://observability.usefreelanceflow.com/app/dashboard

Demo key for testing: ai_demo_key_12345

🧪 Testing Your Installation
After installing, verify it works:

bash
python -c "from aiobservability import AIObservability; print('SDK works!')"
🤝 Contributing
Contributions welcome! Please see CONTRIBUTING.md.

📄 License
MIT License - see LICENSE file for details.

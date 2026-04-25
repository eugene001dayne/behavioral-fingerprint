# behavioralfingerprint

Capture how your AI agent behaves at deployment. Monitor how that behavior changes over time.

Part of the [Thread Suite](https://github.com/eugene001dayne) — AI agent reliability infrastructure.

## Install

```bash
pip install behavioralfingerprint
```

## Quick Start

```python
from behavioralfingerprint import BehavioralFingerprint

bf = BehavioralFingerprint()  # defaults to https://behavioral-fingerprint.onrender.com

# Register your agent
bf.register_agent(
    agent_id="my-agent-v1",
    endpoint_url="https://your-agent.com/run",
    name="My Production Agent"
)

# Capture a behavioral fingerprint
result = bf.capture_fingerprint("my-agent-v1")
print(result["scores"])
# {
#   "verbosity_score": 0.42,
#   "hedging_rate": 0.18,
#   "refusal_rate": 0.0,
#   "confidence_score": 0.71,
#   "consistency_score": 0.63,
#   "adherence_score": 0.90
# }

# Get latest fingerprint
latest = bf.get_latest_fingerprint("my-agent-v1")

# View fingerprint history
history = bf.list_fingerprints("my-agent-v1")
```

## Agent Endpoint Contract

Your agent endpoint must accept POST requests with:
```json
{"input": "probe text here"}
```

And return JSON with an `output`, `response`, `result`, or `content` field:
```json
{"output": "the agent's response"}
```

## Six Behavioral Dimensions

| Dimension | What it measures |
|-----------|-----------------|
| verbosity_score | How much the agent says (0 = concise, 1 = verbose) |
| hedging_rate | How often the agent qualifies its answers |
| refusal_rate | How often the agent declines requests |
| confidence_score | Ratio of confident to uncertain language |
| consistency_score | Similarity across semantically equivalent inputs |
| adherence_score | Compliance with explicit formatting/length instructions |

## Thread Suite

Iron-Thread · TestThread · PromptThread · ChainThread · PolicyThread · ThreadWatch · Behavioral Fingerprint

"Built for the age of AI agents."
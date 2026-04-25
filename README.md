# Behavioral Fingerprint

**Capture how your AI agent behaves at deployment. Monitor how that behavior changes over time. Know when the agent you deployed is no longer the agent you have.**

[![PyPI](https://img.shields.io/pypi/v/behavioralfingerprint)](https://pypi.org/project/behavioralfingerprint/)
[![npm](https://img.shields.io/npm/v/behavioralfingerprint)](https://www.npmjs.com/package/behavioralfingerprint)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)

Part of the [Thread Suite](https://github.com/eugene001dayne) — AI agent reliability infrastructure.

---

## The Problem

AI model providers push silent updates constantly. Claude, GPT-4o, Gemini — they all update without notice. When they do, the behavioral style of the model changes: verbosity shifts, hedging increases, refusals change, confidence patterns alter.

Developers find out when a downstream pipeline breaks or a user complains. There is no system that captures a behavioral baseline and monitors drift against it.

This is that system.

---

## How It Works

**Probe Battery** — a standardized set of 30 inputs across six behavioral dimensions, designed to elicit behavioral tendencies rather than test specific knowledge. Fixed prompts. Reproducible. Versioned.

**Behavioral Fingerprint** — a vector profile across all six dimensions captured at a specific moment.

**Delta** — the computed difference between two fingerprints. When drift exceeds a configured threshold, you get an alert.

### Six Behavioral Dimensions

| Dimension | What it measures |
|-----------|-----------------|
| `verbosity_score` | How much the agent says — token count distributions (0 = concise, 1 = verbose) |
| `hedging_rate` | Frequency of qualifying language ("it depends," "typically," "one could argue") |
| `refusal_rate` | How often and on what inputs the agent declines |
| `confidence_score` | Ratio of high-certainty to uncertain language |
| `consistency_score` | Similarity across semantically equivalent inputs |
| `adherence_score` | Compliance with explicit formatting and length constraints |

---

## Quick Start

### Python

```bash
pip install behavioralfingerprint
```

```python
from behavioralfingerprint import BehavioralFingerprint

bf = BehavioralFingerprint()

# Register your agent
bf.register_agent(
    agent_id="my-agent-v1",
    endpoint_url="https://your-agent.com/run",
    name="My Production Agent"
)

# Capture a behavioral fingerprint at deployment
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

# One week later — capture again and compare
result2 = bf.capture_fingerprint("my-agent-v1")

# View full fingerprint history
history = bf.list_fingerprints("my-agent-v1")
```

### JavaScript

```bash
npm install behavioralfingerprint
```

```javascript
const BehavioralFingerprint = require("behavioralfingerprint");
const bf = new BehavioralFingerprint();

await bf.registerAgent("my-agent-v1", "https://your-agent.com/run", "My Production Agent");
const result = await bf.captureFingerprint("my-agent-v1");
console.log(result.scores);
```

---

## Agent Endpoint Contract

Your agent endpoint must accept POST requests:

```json
{"input": "probe text here"}
```

And return JSON with an `output`, `response`, `result`, or `content` field:

```json
{"output": "the agent's response"}
```

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Status + version |
| GET | `/health` | Health check |
| POST | `/agents` | Register an agent |
| GET | `/agents` | List all agents |
| GET | `/agents/{agent_id}` | Get agent by ID |
| PUT | `/agents/{agent_id}` | Update agent |
| GET | `/batteries` | List probe batteries |
| GET | `/batteries/default` | Get the default battery |
| GET | `/batteries/{battery_id}` | Get battery by ID |
| POST | `/fingerprint/{agent_id}` | Capture a fingerprint |
| GET | `/fingerprint/{agent_id}/latest` | Get latest fingerprint |
| GET | `/fingerprints/{agent_id}` | Full fingerprint history |
| GET | `/fingerprints/{agent_id}/{fingerprint_id}/raw` | Raw probe-by-probe results |
| GET | `/dashboard/stats` | Overview stats |

**Live API:** https://behavioral-fingerprint.onrender.com  
**API Docs:** https://behavioral-fingerprint.onrender.com/docs

---

## Thread Suite

Behavioral Fingerprint is one layer in a complete AI agent reliability pipeline:

```
Iron-Thread      → Did the AI return the right structure?
TestThread       → Did the agent do the right thing?
PromptThread     → Is my prompt the best version of itself?
ChainThread      → Did the handoff between agents succeed?
PolicyThread     → Is the AI staying within our rules in production?
ThreadWatch      → Is the entire pipeline healthy right now?
Behavioral FP    → Has the way this agent responds to the world changed?
```

---

## License

Apache 2.0 — open source, free to use, attribution appreciated.

Built by [Eugene Dayne Mawuli](https://github.com/eugene001dayne) · Accra, Ghana  
*"Built for the age of AI agents."*
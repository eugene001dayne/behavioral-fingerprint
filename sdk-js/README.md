# behavioralfingerprint

Capture how your AI agent behaves at deployment. Monitor how that behavior changes over time. Know when the agent you deployed is no longer the agent you have.

Part of the [Thread Suite](https://github.com/eugene001dayne) — AI agent reliability infrastructure.

---

## Install

```bash
npm install behavioralfingerprint
```

## Quick Start

```javascript
const BehavioralFingerprint = require("behavioralfingerprint");

const bf = new BehavioralFingerprint();

// Register your agent
await bf.registerAgent(
  "my-agent-v1",
  "https://your-agent.com/run",
  "My Production Agent"
);

// Capture a behavioral fingerprint at deployment
const result = await bf.captureFingerprint("my-agent-v1");
console.log(result.scores);
// {
//   verbosity_score: 0.42,
//   hedging_rate: 0.18,
//   refusal_rate: 0.0,
//   confidence_score: 0.71,
//   consistency_score: 0.63,
//   adherence_score: 0.90
// }

// Later — capture again and compare to detect drift
const result2 = await bf.captureFingerprint("my-agent-v1");

// Full fingerprint history
const history = await bf.listFingerprints("my-agent-v1");
```

## Agent Endpoint Contract

Your agent must accept POST requests with:
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
| `verbosity_score` | How much the agent says — 0 = concise, 1 = verbose |
| `hedging_rate` | Frequency of qualifying language |
| `refusal_rate` | How often the agent declines requests |
| `confidence_score` | Ratio of confident to uncertain language |
| `consistency_score` | Similarity across semantically equivalent inputs |
| `adherence_score` | Compliance with formatting and length instructions |

## Methods

```javascript
bf.registerAgent(agentId, endpointUrl, name, description)
bf.listAgents()
bf.getAgent(agentId)
bf.captureFingerprint(agentId)
bf.getLatestFingerprint(agentId)
bf.listFingerprints(agentId)
bf.getFingerprintRaw(agentId, fingerprintId)
bf.getDefaultBattery()
bf.stats()
bf.health()
```

## Live API
https://behavioral-fingerprint.onrender.com
https://behavioral-fingerprint.onrender.com/docs

## Thread Suite
Iron-Thread      → Did the AI return the right structure?
TestThread       → Did the agent do the right thing?
PromptThread     → Is my prompt the best version of itself?
ChainThread      → Did the handoff between agents succeed?
PolicyThread     → Is the AI staying within our rules in production?
ThreadWatch      → Is the entire pipeline healthy right now?
Behavioral FP    → Has the way this agent responds to the world changed?

Built by [Eugene Dayne Mawuli](https://github.com/eugene001dayne) · Accra, Ghana
*"Built for the age of AI agents."*
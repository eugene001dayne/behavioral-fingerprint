const fetch = require("node-fetch");

class BehavioralFingerprint {
  constructor(baseUrl = "https://behavioral-fingerprint.onrender.com") {
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  async _req(method, path, body = null) {
    const options = { method, headers: { "Content-Type": "application/json" } };
    if (body) options.body = JSON.stringify(body);
    const res = await fetch(`${this.baseUrl}${path}`, options);
    if (!res.ok) throw new Error(`BehavioralFingerprint error: ${res.status} ${await res.text()}`);
    return res.json();
  }

  // Agents
  registerAgent(agentId, endpointUrl, name, description = null) {
    return this._req("POST", "/agents", { agent_id: agentId, endpoint_url: endpointUrl, name, description });
  }
  listAgents() { return this._req("GET", "/agents"); }
  getAgent(agentId) { return this._req("GET", `/agents/${agentId}`); }
  updateAgent(agentId, fields) { return this._req("PUT", `/agents/${agentId}`, fields); }

  // Batteries
  listBatteries() { return this._req("GET", "/batteries"); }
  getDefaultBattery() { return this._req("GET", "/batteries/default"); }
  getBattery(batteryId) { return this._req("GET", `/batteries/${batteryId}`); }

  // Fingerprinting
  captureFingerprint(agentId) { return this._req("POST", `/fingerprint/${agentId}`); }
  getLatestFingerprint(agentId) { return this._req("GET", `/fingerprint/${agentId}/latest`); }
  listFingerprints(agentId) { return this._req("GET", `/fingerprints/${agentId}`); }
  getFingerprintRaw(agentId, fingerprintId) { return this._req("GET", `/fingerprints/${agentId}/${fingerprintId}/raw`); }

  // Dashboard
  stats() { return this._req("GET", "/dashboard/stats"); }
  health() { return this._req("GET", "/health"); }
}

module.exports = BehavioralFingerprint;
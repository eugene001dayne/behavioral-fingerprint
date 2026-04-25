import httpx
from typing import Optional


class BehavioralFingerprint:
    def __init__(self, base_url: str = "https://behavioral-fingerprint.onrender.com"):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(base_url=self.base_url, timeout=60.0)

    def _req(self, method: str, path: str, json=None):
        r = self.client.request(method, path, json=json)
        r.raise_for_status()
        return r.json()

    # Agents
    def register_agent(self, agent_id: str, endpoint_url: str, name: str, description: str = None):
        return self._req("POST", "/agents", json={
            "agent_id": agent_id,
            "endpoint_url": endpoint_url,
            "name": name,
            "description": description,
        })

    def list_agents(self):
        return self._req("GET", "/agents")

    def get_agent(self, agent_id: str):
        return self._req("GET", f"/agents/{agent_id}")

    def update_agent(self, agent_id: str, endpoint_url: str = None, name: str = None, description: str = None):
        payload = {k: v for k, v in {
            "endpoint_url": endpoint_url, "name": name, "description": description
        }.items() if v is not None}
        return self._req("PUT", f"/agents/{agent_id}", json=payload)

    # Batteries
    def list_batteries(self):
        return self._req("GET", "/batteries")

    def get_default_battery(self):
        return self._req("GET", "/batteries/default")

    def get_battery(self, battery_id: str):
        return self._req("GET", f"/batteries/{battery_id}")

    # Fingerprinting
    def capture_fingerprint(self, agent_id: str):
        """Runs probe battery against the agent and stores the fingerprint."""
        return self._req("POST", f"/fingerprint/{agent_id}")

    def get_latest_fingerprint(self, agent_id: str):
        return self._req("GET", f"/fingerprint/{agent_id}/latest")

    def list_fingerprints(self, agent_id: str):
        return self._req("GET", f"/fingerprints/{agent_id}")

    def get_fingerprint_raw(self, agent_id: str, fingerprint_id: str):
        """Returns the full probe-by-probe raw results."""
        return self._req("GET", f"/fingerprints/{agent_id}/{fingerprint_id}/raw")

    # Dashboard
    def stats(self):
        return self._req("GET", "/dashboard/stats")

    def health(self):
        return self._req("GET", "/health")
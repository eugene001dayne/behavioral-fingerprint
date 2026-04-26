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

# Drift comparison
    def compare_fingerprints(self, agent_id: str, fingerprint_a_id: str, fingerprint_b_id: str):
        return self._req("POST", f"/fingerprint/{agent_id}/compare", json={
            "fingerprint_a_id": fingerprint_a_id,
            "fingerprint_b_id": fingerprint_b_id,
        })

    def list_drift_records(self, agent_id: str):
        return self._req("GET", f"/drift/{agent_id}")

    # Webhooks
    def create_webhook(self, name: str, url: str, min_severity: str = "low"):
        return self._req("POST", "/webhooks", json={
            "name": name, "url": url, "min_severity": min_severity
        })

    def list_webhooks(self):
        return self._req("GET", "/webhooks")

    def delete_webhook(self, webhook_id: str):
        return self._req("DELETE", f"/webhooks/{webhook_id}")

    # Alerts
    def list_alerts(self, agent_id: str):
        return self._req("GET", f"/alerts/{agent_id}")

    def acknowledge_alert(self, alert_id: str):
        return self._req("PATCH", f"/alerts/{alert_id}/acknowledge")

# Scheduling
    def set_schedule(self, agent_id: str, schedule: str, schedule_enabled: bool = True):
        return self._req("POST", f"/agents/{agent_id}/schedule", json={
            "schedule": schedule,
            "schedule_enabled": schedule_enabled,
        })

    def get_schedule(self, agent_id: str):
        return self._req("GET", f"/agents/{agent_id}/schedule")
import requests


class YougileAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title=None):
        payload = {}
        if title is not None:
            payload["title"] = title
        return requests.post(f"{self.base_url}/api-v2/projects", json=payload,
                             headers=self.headers)

    def update_project(self, project_id, title=None, users=None):
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        return requests.put(f"{self.base_url}/api-v2/projects/{project_id}",
                            json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.base_url}/api-v2/projects/{project_id}",
                            headers=self.headers)

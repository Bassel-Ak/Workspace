import requests

url = "https://edu-bassel-abdelhamid.odoo.com"
db = "edu-bassel-abdelhamid"
username = "bassel.akram09@gmail.com"
password = "BassAK@odoo98"

login_payload = {
    "jsonrpc": "2.0",
    "params": {
        "db": db,
        "login": username,
        "password": password
    }
}

response = requests.post(f"{url}/web/session/authenticate", json=login_payload)
data = response.json()

if response.ok and data.get("result"):
    uid = data["result"]["uid"]
    print(f"✅ JSON-RPC Login successful. UID: {uid}")
else:
    print("❌ JSON-RPC login failed.")
    print(data)

from core.odoo_connector import OdooConnector

def test_auth():
    # Replace with your actual details or load from .env
    url = "https://edu-bassel-abdelhamid.odoo.com"
    db = "edu-bassel-abdelhamid"
    username = "bassel.akram09@gmail.com"
    password = "BassAK@odoo98"

    connector = OdooConnector(url, db, username, password)
    connector.authenticate()
    assert connector.uid is not None
    print("Authentication successful!")

if __name__ == "__main__":
    test_auth()

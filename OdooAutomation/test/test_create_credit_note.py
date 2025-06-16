import os
from dotenv import load_dotenv
from core.odoo_connector import OdooConnector
from odoo_models.credit_note import CreditNote

load_dotenv()

def test_create_credit_note():
    # Load environment variables
    url = os.getenv("ODOO_URL")
    db = os.getenv("ODOO_DB")
    username = os.getenv("ODOO_USERNAME")
    password = os.getenv("ODOO_PASSWORD")

    assert all([url, db, username, password]), "Missing Odoo credentials in .env file"

    # Authenticate
    connector = OdooConnector(url, db, username, password)
    connector.authenticate()

    # Create a sample CreditNote instance
    credit_note = CreditNote(
        customer="Platinum House",
        product="Acoustic Bloc Screens",
        quantity=1,
        credit_notes_account="201003",
        price=1000.0,
        vat=14,
        wht=1
    )

    # Convert to dict and send to Odoo
    credit_note_id = connector.create_credit_note(credit_note.to_dict())
    assert credit_note_id is not None, "Failed to create credit note"
    print(f"✅ Credit note created successfully! ID: {credit_note_id}")

if __name__ == "__main__":
    test_create_credit_note()

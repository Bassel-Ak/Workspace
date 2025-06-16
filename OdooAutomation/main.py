import os
from dotenv import load_dotenv
from core.odoo_connector import OdooConnector
from excel_io.excel_reader import ExcelReader
from odoo_models.credit_note import CreditNote
from utils.validators import validate_credit_note_data
from utils.logger import setup_logger

# Load environment variables from .env file
load_dotenv()

# Initialize logger
Logger = setup_logger()

# Initialize Odoo credentials from environment
url = os.getenv("ODOO_URL")
db = os.getenv("ODOO_DB")
username = os.getenv("ODOO_USERNAME")
password = os.getenv("ODOO_PASSWORD")

# Authenticate with Odoo
connector = OdooConnector(url, db, username, password)
connector.authenticate()
Logger.info("✅ Authenticated with Odoo.")

# Load Excel credit notes
reader = ExcelReader("data/credit_notes.xlsx")
reader.load()
rows = reader.get_credit_notes()
Logger.info(f"📥 Loaded {len(rows)} credit notes from Excel.\n")

# Mapping from Excel headers to CreditNote constructor fields
FIELD_MAPPING = {
    "customer": "customer",
    "product": "product",
    "quantity": "quantity",
    "account": "credit_notes_account",
    "unit_price": "price",
    "vat": "vat",
    "wht": "wht"
}

success_count = 0
fail_count = 0

# Process each row
for idx, raw_row in enumerate(rows, start=1):
    try:
        Logger.debug(f"➡️  Processing row {idx}: {raw_row}")

        # Map Excel keys to model field names
        mapped_row = {
            new_key: raw_row[old_key] for old_key, new_key in FIELD_MAPPING.items()
        }

        # Set default values if missing
        mapped_row["vat"] = mapped_row.get("vat", 0)
        mapped_row["wht"] = mapped_row.get("wht", 0)

        # Validate credit note
        validate_credit_note_data(mapped_row)

        # Create credit note instance and push to Odoo
        credit_note = CreditNote(**mapped_row)
        credit_note_id = connector.create_credit_note(credit_note.to_dict())
        Logger.info(f"✅ Successfully created credit note with ID: {credit_note_id}\n")
        success_count += 1

    except Exception as e:
        import traceback
        fail_count += 1
        Logger.error(f"❌ Failed to process row {idx}: {e}")
        Logger.debug(traceback.format_exc())

Logger.info("\n📊 Summary Report")
Logger.info(f"   ✅ Success: {success_count}")
Logger.info(f"   ❌ Failed: {fail_count}\n")

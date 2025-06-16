OdooAutomation/
├── core/
│   └── odoo_connector.py
├── odoo_models/
│   └── credit.py            ← Contains the CreditNote class
├── excel_io/
│   ├── __init__.py
│   └── excel_reader.py      ← Handles loading/parsing Excel files
├── test/
│   ├── test_excel_reader.py ← Validated Excel reading
│   ├── test_odoo_connector.py ← Authenticated to Odoo
│   └── test_create_credit_note.py ← We're working on this one now
├── data/
│   └── credit_notes.xlsx          ← Your Excel sheet(s) go here
│   └── credit_notes_invalid_test.xlsx          ← Your Excel sheet(s) go here
│   └── credit_notes_test.xlsx          ← Your Excel sheet(s) go here
├── .env                     ← Stores ODOO_URL, ODOO_DB, etc.
├── main.py                  ← Entry point (not fully wired yet)
└── requirements.txt

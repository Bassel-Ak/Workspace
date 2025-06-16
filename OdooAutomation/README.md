# Odoo Credit Note Automation

## 📌 Overview

This project automates the process of creating credit notes in **Odoo 18 Enterprise** using data from an Excel sheet. It connects to Odoo via XML-RPC and processes each entry as a draft credit note.

---

## 📁 Project Structure

```
OdooAutomation/
├── core/
│   └── odoo_connector.py        # Handles Odoo XML-RPC connection and creation logic
├── odoo_models/
│   └── credit_note.py          # CreditNote data class
├── io/
│   └── excel_reader.py         # Reads and parses Excel sheet
├── data/
│   └── credit_notes.xlsx       # Source Excel file with credit note data
├── test/
│   └── test_create_credit_note.py  # Test script for creating a sample credit note
├── .env                        # Environment variables for Odoo credentials
├── main.py                     # Main script to run the automation
└── README.md                   # This file
```

---

## ✅ Features

- Reads credit note data from Excel
- Flexible column header handling (case-insensitive)
- Authenticates with Odoo via XML-RPC
- Maps names to Odoo IDs (customer, product, account, taxes)
- Creates draft credit notes (`out_refund`)
- Supports VAT and WHT tax linking
- Clear terminal logs for success/failure

---

## ⚙️ Setup

1. **Clone the repo:**

```bash
git clone <your_repo_url>
cd OdooAutomation
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create ****\`\`**** file**:

```ini
ODOO_URL=http://localhost:8069
ODOO_DB=my_database
ODOO_USERNAME=admin
ODOO_PASSWORD=admin
```

4. **Prepare Excel file:** Put `credit_notes.xlsx` inside the `data/` folder with the following headers:

- Customer
- Product
- Quantity
- Credit Notes Account
- Price
- VAT
- WHT

---

## 🚀 Running the Script

```bash
python3 main.py
```

You will see output logs per row. Draft credit notes will be created in Odoo.

---

## 🧪 Testing

To run the sample test:

```bash
python3 -m test.test_create_credit_note
```

---

## 🔄 Optional Enhancements

- Post/confirm the created credit notes automatically
- Attach original files or metadata
- GUI or `.exe` wrapper for end users
- Send email notification after each run
- Log errors to a file

---

## 📞 Contact

Built by Bassel Akram and ChatGPT for Odoo automation.


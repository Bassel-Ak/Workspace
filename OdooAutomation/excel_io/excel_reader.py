import pandas as pd

class ExcelReader:
    # Required columns all lowercase and stripped
    REQUIRED_COLUMNS = {
        "customer", "product", "quantity", "credit notes account", "price", "vat", "wht"
    }

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load(self):
        # Read Excel file
        self.df = pd.read_excel(self.file_path)

        # Normalize columns: lowercase + strip whitespace
        self.df.columns = [col.strip().lower() for col in self.df.columns]

        self._validate_headers()

    def _validate_headers(self):
        # Check if all required columns are present in normalized form
        missing = self.REQUIRED_COLUMNS - set(self.df.columns)
        if missing:
            raise ValueError(f"Missing required columns in Excel: {missing}")

    def get_credit_notes(self):
        credit_notes = []
        for idx, row in self.df.iterrows():
            # Skip empty rows where customer or product is missing
            customer = row.get("customer")
            product = row.get("product")
            if pd.isna(customer) or pd.isna(product):
                continue

            # Validate required fields presence and types
            account = row.get("credit notes account")
            price = row.get("price")

            if pd.isna(account):
                raise ValueError(f"Row {idx+2}: 'credit notes account' is missing")

            if pd.isna(price) or not isinstance(price, (int, float)) or price <= 0:
                raise ValueError(f"Row {idx+2}: 'price' must be a positive number")

            credit_note = {
                "customer": customer,
                "product": product,
                "quantity": int(row.get("quantity", 0)),
                "account": account,
                "unit_price": float(price),
                "vat": float(row.get("vat", 0)),
                "wht": float(row.get("wht", 0)),
            }
            credit_notes.append(credit_note)
        return credit_notes

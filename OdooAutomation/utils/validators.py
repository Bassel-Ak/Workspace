import xmlrpc.client

def validate_credit_note_data(data):
    required_fields = ["customer", "product", "quantity", "account", "unit_price"]
    errors = []

    for field in required_fields:
        if field not in data or data[field] in (None, ""):
            errors.append(f"Missing required field: {field}")

    # Numeric checks
    if "quantity" in data:
        try:
            quantity = float(data["quantity"])
            if quantity <= 0:
                errors.append("Quantity must be greater than 0")
        except ValueError:
            errors.append("Quantity must be a number")

    if "unit_price" in data:
        try:
            price = float(data["unit_price"])
            if price < 0:
                errors.append("Price cannot be negative")
        except ValueError:
            errors.append("Price must be a number")

    if "vat" in data:
        try:
            vat = float(data["vat"])
            if vat < 0 or vat > 100:
                errors.append("VAT must be between 0 and 100")
        except ValueError:
            errors.append("VAT must be a number")

    if "wht" in data:
        try:
            wht = float(data["wht"])
            if wht < 0 or wht > 100:
                errors.append("WHT must be between 0 and 100")
        except ValueError:
            errors.append("WHT must be a number")

    return errors

def validate_odoo_instance(url):
    try:
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        _ = common.version()
        return True
    except Exception as e:
        print(f"🌐 Failed to reach Odoo instance: {e}")
        return False


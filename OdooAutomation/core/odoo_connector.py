import xmlrpc.client
from utils.logger import setup_logger

Logger = setup_logger()

class OdooConnector:
    def __init__(self, url, db, username, password):
        self.url = url.rstrip('/')
        self.db = db
        self.username = username
        self.password = password
        self.uid = None
        self.models = None

    def authenticate(self):
        common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        if not self.uid:
            raise Exception("Authentication failed")
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")

    def search_id(self, model, name, name_field="name"):
        # Search for a record by its name
        ids = self.models.execute_kw(
            self.db, self.uid, self.password,
            model, 'search',
            [[(name_field, '=', name)]],
            {'limit': 1}
        )
        return ids[0] if ids else None

    def create_credit_note(self, credit_note):
        Logger.debug(f"Searching for customer: {credit_note['customer']}")
        partner_id = self.search_id("res.partner", credit_note["customer"])
        Logger.debug(f"Partner ID: {partner_id}")
        Logger.debug(f"Searching for product: {credit_note['product']}")
        product_id = self.search_id("product.product", credit_note["product"])
        Logger.debug(f"Product ID: {product_id}")
        Logger.debug(f"Searching for account: {credit_note['credit_notes_account']}")
        account_id = self.search_id("account.account", credit_note["credit_notes_account"], name_field="code")
        Logger.debug(f"Account ID: {account_id}")

        vat_tax_id = self.search_id("account.tax", f"{credit_note['vat']}%") if credit_note["vat"] > 0 else None
        wht_tax_id = self.search_id("account.tax", f"{credit_note['wht']}%") if credit_note["wht"] > 0 else None
        tax_ids = list(filter(None, [vat_tax_id, wht_tax_id]))

        if not partner_id or not product_id or not account_id:
            raise Exception("Missing required external references (customer, product, or account)")

        line = {
            'product_id': product_id,
            'quantity': credit_note['quantity'],
            'price_unit': credit_note['price'],
            'account_id': account_id,
        }

        if tax_ids:
            line['tax_ids'] = [(6, 0, tax_ids)]

        move_data = {
            'partner_id': partner_id,
            'move_type': 'out_refund',
            'invoice_line_ids': [(0, 0, line)],
        }
        
        credit_note_id = self.models.execute_kw(
            self.db, self.uid, self.password,
            'account.move', 'create', [move_data]
        )

        # Optional: Post the credit note to confirm it
        self.models.execute_kw(
            self.db, self.uid, self.password,
            'account.move', 'action_post', [[credit_note_id]]
        )

        return credit_note_id

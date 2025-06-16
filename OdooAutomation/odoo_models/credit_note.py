class CreditNote:
    def __init__(self, customer, product, quantity, credit_notes_account, price, vat=0, wht=0):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.credit_notes_account = credit_notes_account
        self.price = price
        self.vat = vat
        self.wht = wht

    def to_dict(self):
        return {
            "customer": self.customer,
            "product": self.product,
            "quantity": self.quantity,
            "credit_notes_account": self.credit_notes_account,
            "price": self.price,
            "vat": self.vat,
            "wht": self.wht
        }

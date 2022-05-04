class PaymentMethod():
	pass
class CreditCard(PaymentMethod):
	def __init__(self, card_number, expiration, security_code, zip_code):
		self.card_number = card_number
		self.expiration = expiration
		self.security_code = security_code
		self.zip_code = zip_code

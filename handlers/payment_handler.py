import stripe

# Set your secret key. Remember to switch to your live secret key in production!
# You can find your secret key here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'your_secret_key'

class PaymentHandler:
    def __init__(self, amount, currency='usd'):
        self.amount = amount
        self.currency = currency

    def create_payment_intent(self):
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=self.amount,
                currency=self.currency,
            )
            return payment_intent
        except Exception as e:
            return str(e)

    def confirm_payment(self, payment_intent_id):
        try:
            payment_intent = stripe.PaymentIntent.confirm(payment_intent_id)
            return payment_intent
        except Exception as e:
            return str(e)
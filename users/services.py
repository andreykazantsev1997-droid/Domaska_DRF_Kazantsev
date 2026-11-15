import stripe
from django.conf import settings

stripe.api_key = settings.DASH_KEY

def create_product(course):
    name_course = stripe.Product.create(name=course.title)
    return name_course.id

def create_price(product_id, payment_amount):
    price = stripe.Price.create(product=product_id, unit_amount=int(payment_amount * 100), currency='rub')
    return price.id

def create_session(price_id):
    session = stripe.checkout.Session.create(
        success_url='https://127.0.0.1:8000/',
        line_items=[{'price': price_id, 'quantity': 1}],
        mode='payment',
    )
    return session.id, session.url
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'name': product.name, 'quantity': 1, 'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

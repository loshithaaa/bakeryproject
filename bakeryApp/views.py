from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product  # Import your Product model
from .cart import Cart  # Import your Cart class

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
    
def products(request):
    #return HttpResponse("Welcome to the products page")
    products = Product.objects.all()
    return render(request,'products.html', {'products': products})


@require_POST
def add_to_cart(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')

    try:
        product = Product.objects.get(id=product_id)
        cart.add(product)
        messages.success(request, f'Added {product.name} to the cart!')
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')

    return redirect('cart')



def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact object and save it
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contactus.html')



def cart(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart.cart})


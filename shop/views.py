from django.shortcuts import render, redirect ,get_object_or_404
from .models import Product, Cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def cart_view(request):
    cart = Cart.objects.first()  # for simplicity, using first cart
    return render(request, 'shop/cart.html', {'cart': cart})

'''def add_to_cart(request, product_id):
    cart = Cart.objects.first()  # for simplicity, using first cart
    product = Product.objects.get(id=product_id)
    cart.products.add(product)
    return redirect('cart')'''

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get the cart ID from session
    cart_id = request.session.get('cart_id', None)

    if cart_id is None:
        # Create a new cart if one doesn't exist
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id  # Store the cart ID in the session
    else:
        # Retrieve the existing cart
        cart = get_object_or_404(Cart, id=cart_id)

    # Add the product to the cart
    cart.products.add(product)  # Assuming products is a ManyToMany field
    cart.save()  # Save the cart

    return redirect('cart')  # Redirect to the cart view or another view
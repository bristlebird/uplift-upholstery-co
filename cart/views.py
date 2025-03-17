"""
Views for the Shoppping Cart page
"""
from django.shortcuts import render, redirect, \
    reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to render contents of the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if (product.track_quantity
                and quantity > (product.quantity_available - cart[item_id])):
            messages.error(
                request, f'Not enough of this item available. Please choose \
                    {(product.quantity_available - cart[item_id])} or less.'
            )
            return redirect(redirect_url)

        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
        )
    else:
        if product.track_quantity and quantity > product.quantity_available:
            messages.error(
                request, f'Not enough available. Please choose \
                    {product.quantity_available} or less.'
            )
            return redirect(redirect_url)

        cart[item_id] = quantity
        messages.success(
            request, f'Added {product.name} to your cart'
        )

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
        )
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

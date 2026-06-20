from carts.models import Cart


def get_user_carts_context(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user).select_related('product')
    else:
        if not request.session.session_key:
            request.session.create()
        carts = Cart.objects.filter(
            session_key=request.session.session_key
        ).select_related('product')

    cart_count = sum(item.quantity for item in carts)
    cart_total = sum(item.products_price() for item in carts)

    return {
        'carts': carts,
        'cart_count': cart_count,
        'cart_total_price': cart_total,
    }

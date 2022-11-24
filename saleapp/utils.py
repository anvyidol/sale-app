def cart_stats(cart):
    total, total_quantity = 0, 0

    if cart:
        for p in cart.values():
            total += p['price'] * p['quantity']
            total_quantity += p['quantity']

    return {
        "total": total,
        "total_quantity": total_quantity
    }




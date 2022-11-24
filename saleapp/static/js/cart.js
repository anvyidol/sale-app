const addToCart = (id, name, price) => {
    fetch('api/cart', {
        method: 'post',
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(res => res.json())
    .then(data => {
        const cartCounts = document.querySelectorAll('.cart_count')
        cartCounts.forEach(cc => {
            cc.innerHTML = data.total_quantity
        })
    })
}
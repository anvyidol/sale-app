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

const updateCart = (pId, _this) => {
    fetch('api/cart/' + pId, {
        method: 'put',
        body: JSON.stringify({
            "quantity": _this.value
        }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(res => res.json())
    .then(data => {
        const cartCounts = document.querySelectorAll('.cart_count')
        const cartTotals = document.querySelectorAll('.cart_total')
        cartCounts.forEach(cc => {
            cc.innerHTML = data.total_quantity
        })
        cartTotals.forEach(ct => {
            ct.innerHTML = data.total.toLocaleString('en-US')
        })
    })
}

const deleteProduct = (pId) => {
    const del = confirm("Hành động này không thể hoàn tác! Bạn chắc chắn muốn xóa?")
    if (del) {
        fetch('api/cart/' + pId, {
            method: 'delete',
        })
        .then(res => res.json())
        .then(data => {
            const cartCounts = document.querySelectorAll('.cart_count')
            const cartTotals = document.querySelectorAll('.cart_total')
            cartCounts.forEach(cc => {
                cc.innerHTML = data.total_quantity
            })
            cartTotals.forEach(ct => {
                ct.innerHTML = data.total.toLocaleString('en-US')
            })

            document.querySelector('#cart-' + pId).style.display = 'none'
        })
    }

}
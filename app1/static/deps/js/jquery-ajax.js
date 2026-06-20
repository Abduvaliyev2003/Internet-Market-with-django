$(document).ready(function () {
    var successMessage = $("#jq-notification");

    // Add to cart AJAX
    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#goods-in-cart-count");
        var goodsInCartCountMobile = $("#goods-in-cart-count-mobile");
        
        var product_id = $(this).data("product-id");
        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Show custom toast notification
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 4000);

                // Update cart content
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

                // Recalculate totals and counts from updated markup or parameters
                var newCount = cartItemsContainer.find(".cart-card").length;
                goodsInCartCount.text(newCount);
                if (goodsInCartCountMobile.length > 0) {
                    goodsInCartCountMobile.text(newCount);
                }
            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });

    // Remove from cart AJAX
    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#goods-in-cart-count");
        var goodsInCartCountMobile = $("#goods-in-cart-count-mobile");
        
        var cart_id = $(this).data("cart-id");
        var remove_from_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: remove_from_cart_url,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 4000);

                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

                var newCount = cartItemsContainer.find(".cart-card").length;
                goodsInCartCount.text(newCount);
                if (goodsInCartCountMobile.length > 0) {
                    goodsInCartCountMobile.text(newCount);
                }
            },
            error: function (data) {
                console.log("Ошибка при удалении товара из корзины");
            },
        });
    });

    // Decrement item quantity AJAX
    $(document).on("click", ".decrement", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.input-group').find('.number');
        var currentValue = parseInt($input.val());
        
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // Increment item quantity AJAX
    $(document).on("click", ".increment", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.input-group').find('.number');
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);
        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 4000);

                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Ошибка при обновлении количества товара");
            },
        });
    }
});
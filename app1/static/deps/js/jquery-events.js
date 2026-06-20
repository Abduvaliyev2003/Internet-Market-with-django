$(document).ready(function () {
    // Hide notification alert after 7 seconds
    var notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // Modal Cart open / close handlers
    function openCartModal() {
        $('#exampleModal').appendTo('body');
        $('#exampleModal').modal('show');
    }

    $('#modalButton').click(function () {
        openCartModal();
    });

    $('#modalButtonMobile').click(function () {
        openCartModal();
    });

    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Toggle delivery address field based on selected shipping type
    function toggleDeliveryAddress() {
        var selectedValue = $("input[name='requires_delivery']:checked").val();
        if (selectedValue === "1") {
            $("#deliveryAddressField").slideDown(300);
        } else {
            $("#deliveryAddressField").slideUp(300);
        }
    }

    // Initial check on page load
    if ($("input[name='requires_delivery']").length > 0) {
        toggleDeliveryAddress();
    }

    // On change event
    $(document).on("change", "input[name='requires_delivery']", function () {
        toggleDeliveryAddress();
    });
});
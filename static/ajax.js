document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelectorAll('.add-to-cart-form');
    form.forEach(function(form) {
        
        form.addEventListener('submit', function(event) {
            event.preventDefault();
    
            var xhr = new XMLHttpRequest();
            xhr.open('POST', form.action, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    
            xhr.onload = function() {
                if (xhr.status >= 200 && xhr.status < 400) {
                    var response = JSON.parse(xhr.responseText);
    
                    alert(response.message); // Handle success (you can show a message or update the cart count, etc.)
                } else {
                    alert('There was an error adding the product to the cart.'); // Handle error
                }
            };
    
            var encodedData = new URLSearchParams(new FormData(form)).toString();
            xhr.send(encodedData);
        });
    });

    });


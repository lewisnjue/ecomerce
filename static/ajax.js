document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('subscribe-email').addEventListener('submit', function(event) {
        event.preventDefault();

        var xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onerror = function() {

            if (!document.querySelector(".div-add-to-cart")) {
                // Create container if needed for errors
                var messageContainer = document.createElement('div');
                messageContainer.classList.add('div-add-to-cart');
                document.body.appendChild(messageContainer);
            }

            var message = document.createElement('p');
            message.innerHTML = 'something went wrong, please try again later.';
            message.classList.add('error');

            var messagediv = document.querySelector(".div-add-to-cart");
            messagediv.appendChild(message);

            setTimeout(() => {
                message.remove();
            }, 2000);


        }

    

        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 400) {
                var response = JSON.parse(xhr.responseText);

                // Check for container, create if needed
                if (!document.querySelector(".div-add-to-cart")) {
                    var messageContainer = document.createElement('div');
                    messageContainer.classList.add('div-add-to-cart');
                    document.body.appendChild(messageContainer);
                }

                var message = document.createElement('p');
                message.innerHTML = response.message;
                message.classList.add('success');

                var messagediv = document.querySelector(".div-add-to-cart");
                messagediv.appendChild(message);

                setTimeout(() => {
                    message.remove();
                }, 2000);


            } else {
                // Error handling logic (similar to success)
                if (!document.querySelector(".div-add-to-cart")) {
                    // Create container if needed for errors
                    var messageContainer = document.createElement('div');
                    messageContainer.classList.add('div-add-to-cart');
                    document.body.appendChild(messageContainer);
                }

                var message = document.createElement('p');
                message.innerHTML = 'their was an error while registerling your email address. Please try again later.';
                message.classList.add('error');

                var messagediv = document.querySelector(".div-add-to-cart");
                messagediv.appendChild(message);

                setTimeout(() => {
                    message.remove();
                }, 2000);
            }
        };

        var encodedData = new URLSearchParams(new FormData(form)).toString();
        xhr.send(encodedData);
    });
});





    // Add to cart functionality
    var forms = document.querySelectorAll('.add-to-cart-form');
    forms.forEach(function(form) {

        form.addEventListener('submit', function(event) {
            event.preventDefault();

            var xhr = new XMLHttpRequest(); // creating new XMLHttpRequest object 
            xhr.open('POST', form.action, true); // true here is optional
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onerror = function() {

                if (!document.querySelector(".div-add-to-cart")) {
                    // Create container if needed for errors
                    var messageContainer = document.createElement('div');
                    messageContainer.classList.add('div-add-to-cart');
                    document.body.appendChild(messageContainer);
                }

                var message = document.createElement('p');
                message.innerHTML = 'something went wrong, please try again later.';
                message.classList.add('error');

                var messagediv = document.querySelector(".div-add-to-cart");
                messagediv.appendChild(message);

                setTimeout(() => {
                    message.remove();
                }, 2000);


            }

        

            xhr.onload = function() {
                if (xhr.status >= 200 && xhr.status < 400) {
                    var response = JSON.parse(xhr.responseText);

                    // Check for container, create if needed
                    if (!document.querySelector(".div-add-to-cart")) {
                        var messageContainer = document.createElement('div');
                        messageContainer.classList.add('div-add-to-cart');
                        document.body.appendChild(messageContainer);
                    }

                    var message = document.createElement('p');
                    message.innerHTML = response.message;
                    message.classList.add('success');

                    var messagediv = document.querySelector(".div-add-to-cart");
                    messagediv.appendChild(message);

                    setTimeout(() => {
                        message.remove();
                    }, 2000);
    

                } else {
                    // Error handling logic (similar to success)
                    if (!document.querySelector(".div-add-to-cart")) {
                        // Create container if needed for errors
                        var messageContainer = document.createElement('div');
                        messageContainer.classList.add('div-add-to-cart');
                        document.body.appendChild(messageContainer);
                    }

                    var message = document.createElement('p');
                    message.innerHTML = 'There was an error adding the product to the cart.';
                    message.classList.add('error');

                    var messagediv = document.querySelector(".div-add-to-cart");
                    messagediv.appendChild(message);

                    setTimeout(() => {
                        message.remove();
                    }, 2000);
                }
            };

            var encodedData = new URLSearchParams(new FormData(form)).toString();
            xhr.send(encodedData);
        });
    });




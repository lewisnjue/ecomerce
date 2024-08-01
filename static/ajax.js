document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('subscribe-email').addEventListener('submit', function(event) {
        event.preventDefault();
        var form = event.target;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onerror = function() {
            handleError('Something went wrong, please try again later.');
        };

        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 400) {
                var response = JSON.parse(xhr.responseText);
                handleSuccess(response.message);
            } else {
                handleError('There was an error while registering your email address. Please try again later.');
            }
        };

        var encodedData = new URLSearchParams(new FormData(form)).toString();
        xhr.send(encodedData);
    });

    var forms = document.querySelectorAll('.add-to-cart-form');
    forms.forEach(function(form) {

        form.addEventListener('submit', function(event) {
            event.preventDefault();

            var xhr = new XMLHttpRequest();
            xhr.open('POST', form.action, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onerror = function() {
                handleError('Something went wrong, please try again later.');
            };

            xhr.onload = function() {
                if (xhr.status > 300 && xhr.status < 400) {
                    showLoginPopup();
                } else if (xhr.status >= 200 && xhr.status < 300) {
                    var response = JSON.parse(xhr.responseText);
                    handleSuccess(response.message);
              
                } else {
                    handleError('There was an error adding the product to the cart.');
                   
                }
            };

            var encodedData = new URLSearchParams(new FormData(form)).toString();
            xhr.send(encodedData);
        });
    });

    function handleSuccess(messageText) {
        var messageContainer = getMessageContainer();
        var message = document.createElement('p');
        message.innerHTML = messageText;
        message.classList.add('success');
        messageContainer.appendChild(message);
        setTimeout(() => {
            message.remove();
        }, 2000);
    }

    function handleError(messageText) {
        var messageContainer = getMessageContainer();
        var message = document.createElement('p');
        message.innerHTML = messageText;
        message.classList.add('error');
        messageContainer.appendChild(message);
        setTimeout(() => {
            message.remove();
        }, 2000);
    }

    function getMessageContainer() {
        var messageContainer = document.querySelector('.div-add-to-cart');
        if (!messageContainer) {
            messageContainer = document.createElement('div');
            messageContainer.classList.add('div-add-to-cart');
            document.body.appendChild(messageContainer);
        }
        return messageContainer;
    }

    function showLoginPopup() {
        var modal = document.createElement('div');
        modal.classList.add('login-modal');
        modal.innerHTML = `
            <div class="login-modal-content">
                <span class="close-button">&times;</span>
                <p>Please login first to add items to the cart.</p>
                <a href="/login" class="login-link">Login</a>
            </div>
        `;
        document.body.appendChild(modal);

        var closeButton = modal.querySelector('.close-button');
        closeButton.addEventListener('click', function() {
            modal.remove();
        });

        // Optional: close the modal when clicking outside of the content
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.remove();
            }
        });
    }

});

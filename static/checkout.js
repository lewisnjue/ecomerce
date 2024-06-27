// This is your test secret API key.
const stripe = Stripe("pk_test_51PWBWMDyeSzoV8OmrOMm8Da4PHHPZ47IpTU8MqvrsROhfooiwoSGxQkUDbzsHruPjzt7CWA9elHfWNRvCoGwCVUH00FicCwlo9");

initialize();

// Create a Checkout Session
async function initialize() {
    const csrfToken = document.getElementById('csrfToken').value; // Get token from hidden field


  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken, // Include CSRF token in header
      },
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  const checkout = await stripe.initEmbeddedCheckout({
    fetchClientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}
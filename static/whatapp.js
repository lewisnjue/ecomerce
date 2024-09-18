function openWhatsApp() {
    var phoneNumber = "254740771735"; // Replace with the desired Kenyan phone number
    var whatsappUrl = "https://api.whatsapp.com/send?phone=" + phoneNumber;
    window.open(whatsappUrl, '_blank');
}
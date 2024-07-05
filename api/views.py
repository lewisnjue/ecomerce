from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from main.models  import Cart,CartItem  # Assuming your Cart model is in the same app

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkorder(request, username):
    if request.user.is_staff or request.user.groups.filter(name='manager').exists():
            user = get_user_model().objects.get(username=username)
            cart = Cart.objects.get(user=user)
            items = CartItem.objects.filter(cart=cart)

            subtotal = sum(item.total for item in items)  # Concise subtotal calculation

            itemslist = [{'product': item.product, 'quantity': item.quantity} for item in items]

            returnitems = []
            for item in itemslist:
                quantity = item['quantity']
                product = item['product']
                price = product.price
                name = product.name
                returnitems.append({'quantity': quantity, 'price': price, 'name': name})

            return Response({'items': returnitems,'subtotal':subtotal})

    else:
        return Response({'error': 'You are not authorized to view this data'}, status=status.HTTP_403_FORBIDDEN)

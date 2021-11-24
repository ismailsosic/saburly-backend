from .models import Card
from .serializers import CardSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CardList(APIView):
    """
    List all cards, or create a new Card.
    """

    def get(self, request, format=None):
        cards = Card.objects.all().filter(user_id = request.user.id)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        userData = request.data
        userData["user"] = request.user.id
        serializer = CardSerializer(data=userData)
        if serializer.is_valid():
            if Card.objects.filter(date_from=userData["date_from"], date_to=userData["date_to"], user_id=request.user.id).exists():
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class CardDetail(APIView):
    """
    Retrieve, update or delete a Card instance.
    """
    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        card = self.get_object(pk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
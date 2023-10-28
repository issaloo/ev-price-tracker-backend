from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView


class GetEvPriceMain(APIView):
    def get(self, request, format=None):
        ev_price_count = cache["ev_price_count"]
        # ev_price_count = 1
        if ev_price_count is not None:
            return Response(ev_price_count)
        else:
            return Response({"message": "Key not found in Redis"})

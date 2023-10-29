from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView


class GetEvPriceMain(APIView):
    def get(self, request, format=None):
        ev_price_count = cache.get(key="ev_price_count")
        print(cache.keys("*"))

        if ev_price_count is not None:
            return Response(ev_price_count)
        else:
            return Response({"message": "Key not found in Redis"})
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


class GetEvPriceMain(APIView):

    """Get EV Prices from all vehicles in database.

    Args:
    ----
        APIView (class): DRF API View
    """

    permission_classes = [HasAPIKey]
    authentication_classes = []

    def get(self, request):
        """Get request for data.

        Raises
        ------
            Http404: 404 Error

        Returns
        -------
            dict: EV price data in json form
        """
        ev_price_json = cache.get(key="ev_price_json")
        if ev_price_json:
            return Response(ev_price_json, status=status.HTTP_200_OK)
        else:
            raise Response(status=status.HTTP_400_BAD_REQUEST)


GetEvPriceMainView = GetEvPriceMain.as_view()


class GetGraphModelDetail(APIView):

    """Get graph data for specified EV make and model.

    Args:
    ----
        APIView (class): DRF API View
    """

    permission_classes = [HasAPIKey]
    authentication_classes = []

    def get(self, request, pk):
        """Get request for data.

        Args:
        ----
            pk (str): primary key for database

        Raises:
        ------
            Http404: 404 Error

        Returns:
        -------
            dict: graph data in json form
        """
        ev_graph_data = cache.get(key=f"graph_{pk}")
        if ev_graph_data:
            return Response(ev_graph_data, status=status.HTTP_200_OK)
        else:
            raise Response(status=status.HTTP_400_BAD_REQUEST)


GetGraphModelDetailView = GetGraphModelDetail.as_view()

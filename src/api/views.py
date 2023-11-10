from django.core.cache import cache
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


# TODO: add authorization that frontend sends along (maybe from header?)
class GetEvPriceMain(APIView):

    """Get EV Prices from all vehicles in database.

    Args:
    ----
        APIView (class): DRF API View
    """

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
        if ev_price_json is not None:
            return Response(ev_price_json)
        else:
            raise Http404


GetEvPriceMainView = GetEvPriceMain.as_view()


class GetGraphModelDetail(APIView):

    """Get graph data for specified EV make and model.

    Args:
    ----
        APIView (class): DRF API View
    """

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
        if ev_graph_data is not None:
            return Response(ev_graph_data)
        else:
            raise Http404


GetGraphModelDetailView = GetGraphModelDetail.as_view()

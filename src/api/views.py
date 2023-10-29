from django.core.cache import cache
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


# TODO: add authorization that frontend sends along (maybe from header?)
class GetEvPriceMain(APIView):

    """_summary_.

    Args:
    ----
        APIView (_type_): _description_
    """

    def get(self, request):  # , format=None what is this format for?
        """_summary_.

        Args:
        ----
            request (_type_): _description_

        Raises:
        ------
            Http404: _description_

        Returns:
        -------
            _type_: _description_
        """
        ev_price_json = cache.get(key="ev_price_json")
        if ev_price_json is not None:
            return Response(ev_price_json)
        else:
            raise Http404


GetEvPriceMainView = GetEvPriceMain.as_view()


class GetGraphModelDetail(APIView):

    """_summary_.

    Args:
    ----
        APIView (_type_): _description_
    """

    def get(self, request, pk):
        """_summary_.

        Args:
        ----
            request (_type_): _description_
            pk (_type_): _description_

        Raises:
        ------
            Http404: _description_

        Returns:
        -------
            _type_: _description_
        """
        ev_graph_data = cache.get(key=f"graph_{pk}")
        if ev_graph_data is not None:
            return Response(ev_graph_data)
        else:
            raise Http404


GetGraphModelDetailView = GetGraphModelDetail.as_view()

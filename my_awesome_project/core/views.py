from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TestCreateSerializer, TestListSerializer
from .services.create_orders import save_orders
from .services.get_users_list import get_users


@extend_schema(responses={status.HTTP_200_OK: TestListSerializer})
@cache_page(60 * 60 * 24)
@api_view(["GET"])
def get_list_api_view(request: Request) -> Response:
    result = get_users()
    return Response(result)


@extend_schema(request=TestCreateSerializer)
@api_view(["POST"])
def create_orders_api_view(request: Request) -> Response:
    file = request.FILES["deals"]
    try:
        result = save_orders(file)
    except Exception:
        result = {"Status": "Error", "Desc": "в процессе обработки файла произошла ошибка"}
    return Response(result)

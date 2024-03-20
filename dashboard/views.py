from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import CreateUserSerializer
from utils.response import CustomResponse


class CreateUserAPI(APIView):
    def post(self, request):

        serializer = CreateUserSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(general_message="user create successfully").get_success_response()
        return CustomResponse(response=serializer.errors).get_failure_response()

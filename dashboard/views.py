from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
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


class UserLoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return CustomResponse(
                general_message='email and password is required'
            ).get_failure_response()

        user = authenticate(request, email=email, password=password)

        if user:
            return CustomResponse(
                general_message="successfully login",
            ).get_success_response()
        else:
            return CustomResponse(
                general_message="login failed"
            ).get_failure_response()


from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializer import CreateUserSerializer, UserEditSerializer
from utils.response import CustomResponse
from utils.permissions import TokenGenerate, CustomizePermission
from utils.apis import Apis
from .models import User


class CreateUserAPI(APIView):
    def post(self, request):

        serializer = CreateUserSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return CustomResponse(
                general_message="user create successfully"
            ).get_success_response()

        return CustomResponse(
            response=serializer.errors
        ).get_failure_response()


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
        auth = TokenGenerate().generate(user)

        if user:
            return CustomResponse(
                general_message="successfully login",
                response=auth
            ).get_success_response()
        else:
            return CustomResponse(
                general_message="login failed"
            ).get_failure_response()


class UserEditApi(APIView):
    authentication_classes = [CustomizePermission]

    def put(self, request):
        user_id = request.user.id

        user = User.objects.filter(id=user_id).first()

        serializer = UserEditSerializer(
            user,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()

            return CustomResponse(
                general_message="user edit successfully"
            ).get_success_response()

        return CustomResponse(
            response=serializer.errors
        ).get_failure_response()


class UserSuggestionAPI(APIView):
    authentication_classes = [CustomizePermission]

    def get(self, request):
        user_location = request.data.get('location')
        user_suggestion = request.data.get('suggestion')

        user_id = request.user.id
        if user_suggestion is None:
            user_suggestion = User.objects.filter(id=user_id).first().priority_locations

        weather_data = Apis().weather_api(user_location, user_suggestion)
        return CustomResponse(
            response=weather_data
        ).get_success_response()

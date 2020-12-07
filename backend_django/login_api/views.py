# 2020-04-20 minseung seon modified.
# generic 기반 클래스 뷰: 기본적인 기능을 모두 포함하는 뷰

from knox.models import AuthToken
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, ProfileSerializer


@api_view(['GET'])  # 해당 함수 view에서 처리할 http 메소드
def TestAPI(request):  # GET 127.0.0.1:8000/login_api/test/ 로 요청을 보내어 테스트용으로 This is API Test를 출력하는 api 를 만듦
    return Response("This is API Test")


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "길이가 짧습니다."}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],  # 1의 의미는 무엇일까..
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileUpdateAPI(generics.UpdateAPIView):
    lookup_field = "user_pk"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

from .models import User 
from .tokens import get_tokens_for_user
from utils.response.response import CustomResponse as cr 
from utils.exception.exception import CustomException as ce
from .serializers import (
    UserRegistrationSerailizer,
    UserLoginSerailizer,
    UserChangePasswordSerailizer,
    UserPasswordResetSerailizer,
    SendPasswordResetEmailSerailizer
)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)


from django.contrib.auth import authenticate



# ! User Registration View
class UserRegistrationView(APIView):
    serializer_class=UserRegistrationSerailizer
    permission_classes=[AllowAny]


    def post(self,request):
        """
        Registering User Account
        """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return cr.success(
                message="Your account has been successfully registered",
                status=HTTP_201_CREATED
            )
        return cr.error(
            message="Form Validation Error",
            errors=serializer.errors
            )
    



# ! User Login View
class UserLoginView(APIView):
    serializer_class=UserLoginSerailizer
    permission_classes=[AllowAny]


    def post(self,request):
        """
        Logging User and generating tokens
        """
        serializer=self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return cr.error(
            message="Form Validation Error",
            errors=serializer.errors
            )


        # ! Gets the validated data from the serializer 
        email=serializer.data.get('email')
        password=serializer.validated_data.get('password')

        # ! Checks if the user exists with the given credentials or not
        user=authenticate(email=email,password=password)

        # ! If a User exists  then generate Token for that user
        if user is not None:
            token=get_tokens_for_user(user)
            return cr.success(
                data=token,
                message="You have been successfully logged in",
            )
        
        # ! If User Doesn't exists or Invalid Credintials 
        return cr.error(
            message="Invalid Credential provided",
            status=HTTP_401_UNAUTHORIZED
        )
    



# ! User Change Password View
class UserChangePasswordView(APIView):
        serializer_class=UserChangePasswordSerailizer
        permission_classes=[IsAuthenticated]


        def post(self,request):
            """
            Changing Authenticated User Password 
            """
            user=request.user
            serializer=self.serializer_class(
                data=request.data,
                context={'user':user}
            )
            if not serializer.is_valid():
                return cr.error(
                message="Form Validation Error",
                errors=serializer.errors
                )
            return cr.success(
                message="Your password has been successfully changed"
            )
        



# !Send Password Reset Email View
class SendPasswordResetEamilView(APIView):
    serializer_class=SendPasswordResetEmailSerailizer


    def post(self,request):
        """
        Method for sending email for resetting users password
        """
        serializer=self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return cr.error(
            message="Form Validation Error",
            errors=serializer.errors
            )

        return cr.success(
            message="Link for resetting your password has been sent to your email"
        )
    



# ! User Password Reset View 
class UserPasswordResetView(APIView):
    serializer_class=UserPasswordResetSerailizer
    permission_classes=[AllowAny]


    def post(self,request,uid,token):
        """
        Method For Resetting User Password
        """
        serializer=self.serializer_class(
            data=request.data,
            context={'uid':uid,'token':token}
        )
        if not serializer.is_valid():
            return cr.error(
            message="Form Validation Error",
            errors=serializer.errors
            )

        return cr.success(
            message="Your password has been successfully changed"
        )
        

     
             








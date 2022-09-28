from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import views 
from rest_framework import status
from core import serializers as core_serializer
from core import models as core_models
from core.utils import create_response

from core.tasks import *

# Create your views here.
class SendEmail(views.APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            register = core_models.Test.objects.get(id=id)
            serializer = core_serializer.TestSerializer(register)
            return Response(serializer.data)

        send_mail_on_get.delay()
        register = core_models.Test.objects.all()
        serializer = core_serializer.TestSerializer(register, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer_instance = core_serializer.TestSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return create_response("Enter valid Data",400)
        else:
            send_mail_on_post.delay()
            core_models.Test.objects.create(
                first_name = request.data.get("first_name"),
                last_name = request.data.get("last_name"),
                email = request.data.get("email"),
                phone_no = request.data.get("phone_no"),
                address = request.data.get("address")

            )
            return create_response("Data Added Successfully",200)

    def put(self,request,pk=None):
        send_mail_on_put.delay(pk)
        register_data = core_models.Test.objects.filter(id=pk).last()
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        phone_no = request.data.get("phone_no")
        email = request.data.get("email")
        address = request.data.get("address")

        register_data.first_name = first_name
        register_data.last_name = last_name
        register_data.phone_no = phone_no
        register_data.email = email
        register_data.address = address
        if register_data:
            register_data.save()
            return create_response("Data Updated Successfully",200)
        else:
            return create_response("Please enter valid id",400)




from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from sale.serializer.action_ser import Action, ActionSerializer
# Create your views here.


class GetCapitalInfoView(APIView):
    def get(self, request):
        print('hello')
        action = Action(id=5, title='dsfsadfd')
        action_ser = ActionSerializer(instance=action)
        print(action_ser.data)
        
        return Response(data=action_ser.data)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import Sale, UserIICO
from sale.serializer.action_ser import SaleSerializer, SalesSerializer, Sales
from datetime import datetime
# Create your views here.


def is_date_in_range(start_date, end_date, current_date):
    
    return start_date<= current_date <= end_date

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


class GetCapitalInfoView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        user = UserIICO.objects.get(pk=user_id)
        user_age = calculate_age(user.date_of_birth)
        actions = Sale.objects.all()
        avilible_actions = []
        for action in actions:
            if (action.users_filter.user_id==user.pk):
                avilible_actions.append(action)
                continue
            if ((action.users_filter.sex=='all')or(action.users_filter.sex==user.sex))and(user_age>=action.users_filter.start_age)and(user_age<=action.users_filter.end_age)and(is_date_in_range(action.start_date, action.end_date, datetime.now().date())):
                avilible_actions.append(action)

     
        data = [SaleSerializer(action).data for action in avilible_actions]
       
        return Response(data={'avalible_actions':data})
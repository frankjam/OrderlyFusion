from rest_framework import serializers
from CustomersApp.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','name','code','phone','email')
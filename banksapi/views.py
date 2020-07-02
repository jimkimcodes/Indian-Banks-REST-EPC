from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BanksList(APIView):
    def get(self, request, format=None):
        banks = Banks.objects.all()
        serializer = BanksSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BanksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchesList(APIView):
    def get(self, request, format=None):
        banks = Branches.objects.all()
        serializer = BranchesSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BranchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BanksDetail(APIView):
    def get_object(self, id):
        try:
            return Banks.objects.get(id=id)
        except Banks.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bank = self.get_object(id)
        serializer = BanksSerializer(bank)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        bank = self.get_object(id)
        serializer = BanksSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        bank = self.get_object(id)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class BranchesIFSCDetail(APIView):
    def get_object(self, id):
        try:
            return Branches.objects.get(ifsc=id)
        except Branches.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bank = self.get_object(id)
        serializer = BranchesSerializer(bank)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        bank = self.get_object(id)
        serializer = BranchesSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        bank = self.get_object(id)
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class BranchesFilter(APIView):
    def get_object(self, name, city):
        print(name, city)
        try:
            return Branches.objects.filter(bank__name=name, city=city)
        except Branches.DoesNotExist:
            raise Http404

    def get(self, request, name, city, format=None):
        bank = self.get_object(name, city)
        serializer = BranchesSerializer(bank, many=True)
        return Response(serializer.data)



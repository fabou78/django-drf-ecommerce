from rest_framework import serializers
from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model: Category
        fields = '__all__'

    # def __str__(self):
    #     return

    # def __unicode__(self):
    #     return


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model: Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: Product
        fields = '__all__'

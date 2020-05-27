from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source = 'author.username')

    class Meta: #"모델 메타데이터"란 앞서 보았던 필드 단위의 옵션들과 달리 모델 단위의 옵션이라고 볼 수 있습니다. 
                #예를들면, 정렬 옵션(ordering), 데이터베이스 테이블 이름(db_table), 또는 읽기 좋은 이름이나 복수(plural) 
                # 이름을 지정해 줄 수 있습니다(verbose_name, verbose_name_plural). 
                # 모델클래스에 Meta 클래스를 반드시 선언해야 하는 것은 아니며, 모든 옵션을 모두 설정해야 하는 것도 아닙니다.
        model = Post
        fields=('pk','title','content','image','filename','author_name')

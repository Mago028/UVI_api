# api/views.py
# api/views.py
import requests
from django.http import Http404
from rest_framework import status
from .models import UVI
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .serializers import UVISerializer
import json

def search_UVI_by_area(areaNo):
    try:
        uvi_instance = UVI.objects.get(areaNo=areaNo)
        return uvi_instance
    except UVI.DoesNotExist:
        return None

@api_view(['GET'])
def get_UVI(request, areaNo):
    service_key = "인증키(decoding)"
    time = timezone.now().strftime("%Y%m%d%H")
    
    params = {
        "serviceKey": service_key,
        "dataType": "JSON",
        "areaNo": areaNo,
        "time": time 
    }
    
    url = f"http://apis.data.go.kr/1360000/LivingWthrIdxServiceV4/getUVIdxV4"
    # 공공데이터/기상청_생활기상지수 조회서비스(3.0)/자외선지수
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'header' in data['response']:
                header = data['response']['header']
                if header['resultCode'] == '00':
                    if 'body' in data['response'] and 'items' in data['response']['body']:
                        items = data['response']['body']['items']['item']
                        uvi_list = [item['h12'] for item in items] # 오늘의 자외선 지수 추출
                        uvi_data = {"uvi_list":uvi_list, "areaNo": areaNo}
                        
                        serializer = UVISerializer(data=uvi_data)
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                        
                        return Response(uvi_data)
                else:
                    return Response({"error": header['resultMsg']}, status=400)
            else:
                return Response({"error": "API 응답에 'response', 'header' 키가 없습니다."}, status=400)
    except json.JSONDecodeError as e:
        return Response({"error": "JSON 디코드 오류: " + str(e)}, status=400)

    uvi_instance = search_UVI_by_area(areaNo)  # 검색값 연결
    if uvi_instance is not None:
        # 검색 결과 사용
        serializer = UVISerializer(uvi_instance)


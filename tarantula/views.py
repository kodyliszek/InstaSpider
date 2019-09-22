from django.http import HttpResponse
from django.views import View


class TarantulaView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
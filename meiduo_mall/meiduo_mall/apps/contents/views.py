from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View


class IndexView(View):
    """首页广告"""

    def get(self, request):
        """提供首页广告界面"""
        return render(request, 'index.html')

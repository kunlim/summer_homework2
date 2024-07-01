# views.py

import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse


def chart_view(request):
    
    x = [0, 0.5, 1, 1.5, 2,2.5,3]
    y = [0, 0.5, 1, 1.5, 2,2.5,3]

    plt.figure()
    plt.plot(x, y)
    plt.title('Chart Test')
    #plt.xlabel('X-axis')
    #plt.ylabel('Y-axis')

    # 将图表转换为图像数据并以 base64 编码的形式传递给模板
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return render(request, 'charts/chart.html', {'graphic': graphic})
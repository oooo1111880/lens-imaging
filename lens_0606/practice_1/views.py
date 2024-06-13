from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def hitime(request):
    return render(request,'hiworld.html',{
        'current_time':str(datetime.now()), 
    })


def test(request,pn):
    print(f'User input:{pn}')
    return render(request, 'test.html',{
        'user_input':pn,
    })

from django.shortcuts import render

def lens(request):
    Image = ''
    Focal = ''
    Object = ''
    if request.method == 'POST':
        try:
            Focal = request.POST['Focal']
            Object = request.POST['Object']
            Focal_value = float(Focal)
            Object_value = float(Object)

            if(Focal_value == 0 or Object_value == 0) :
                Image = "無法計算"
            elif(Focal_value == Object_value):
                Image = "無窮遠處，無法成像"
            else:
                Image = round(1 / ((1 / Focal_value) - (1 / Object_value)), 3)
                ImageStr = str(Image) + 'cm'
                return render(request, "lensimaging.html", {'Image': ImageStr, 'Focal': Focal, 'Object': Object})
            
        except (ValueError):
            Image = "無法計算 請重新輸入"
            return render(request, "lensimaging.html", {'Image': Image, 'Focal': Focal, 'Object': Object})
        
    return render(request, "lensimaging.html", {'Image': Image, 'Focal': Focal, 'Object': Object})
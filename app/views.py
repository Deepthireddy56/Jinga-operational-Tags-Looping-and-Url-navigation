from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'Name':'DEEPTHI REDDY','Course':['PYTHON','DJANGO','SQL','WEB TECHNOLOGY']}
    return render(request,'loop.html',context=d)
def Url(request):
    d={'A':[1,2,3,4,5,6,7,8],'B':'FRAMEWORK'}
    return render(request,'Url.html',context=d)



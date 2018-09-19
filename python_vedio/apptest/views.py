from django.shortcuts import render,HttpResponse

# Create your views here.
def test_view(req):
    # return HttpResponse('hello world')
    print(req.content_type)
    print(req.
    return render(req,'test.html')


def artical(req,aa,bb):
    print(req.scheme)
    # return render(req,'test.html')
    return HttpResponse('artical %s %s'%(aa,bb))
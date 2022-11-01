from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse("Yooohooo Family!! Welcome to our page!")

def aboutPageView(request):
    return HttpResponse('Our company is famous from being in Frozen and we are having a big summer blowout!')

def contactPageView(request, contact_name, contact_email):
    return HttpResponse("Welcome " + contact_name + " we will send an email to " + contact_email)
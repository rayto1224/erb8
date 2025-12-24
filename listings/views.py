from django.shortcuts import render

# Create your views here.
def listings(request):
    print(request,request.path)
    return render(request,'listings/listings.html')

def listing(request,listing_id):
    print(request,request.path)
    return render(request,'listings/listing.html')

def search(request):
    print(request,request.path)
    return render(request,'listings/search.html')

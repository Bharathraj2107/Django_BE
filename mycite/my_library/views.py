from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.http import HttpResponseNotFound
from .import models
from .import views

# Create your views here.
# def demo(request):#it is a page
#     return HttpResponse("welcome to my first project")
# articles={
#     'Stories':'My stories Page',
#     'Novels': 'My Novels Page',
#     'Poet': 'My Poet Page',
#     'politics': 'My politics Page'
# }

# def lib_news(request,topic):
#     return HttpResponse(articles[topic])

#raising the 404 error
# def lib_news(request,topic):
#     try:
#         res=articles[topic]
#         return  HttpResponse(articles[topic])
#     except:
#         res='No Page exist for that topic'
#         return HttpResponseNotFound(res)
# def add_views(request,n1,n2):
#     add_num=n1+n2
#     res=f'{n1}+{n2} ={add_num}'
#     return HttpResponse(str(res))#convert number to string to display
#
# def page_num_view(request,num_page):
#     topic_list=list(articles.keys())
#     topic=topic_list[num_page]
#     return HttpResponseRedirect(topic)
# def oprtns_view(request):
#     my_var={
#         'first_name':'Prajwal', 'last_name':'Kumar',
#         'my_lst':[2,4,6,8,10],
#         'user_logged_in': True,
#         # 'user_logged_in':False
#     }
#     return render(request,"my_library/lib_optrns.html",context=my_var)#we are sending the request to the html and my var is send as paramtere to the html
# def add(request):
#     add=Number1+Number2
#     sub = Number1 - Number2
#     mul = Number1 * Number2
#     div = Number1 / Number2
#     return render(request,"my_library/calculator.html")
# calc/views.py

#cd .. if we go into the application twice

# def add_numbers(request):
#     return render(request,"my_library/calculator.html")
#interview-questions
#migration
#it will check the authentication  changes and steps taken
def list_customers(request):
    all_customers=models.Lib_Customers.objects.all()#all_customers is object
    context_list={'Lib_Customers':all_customers}#'Lib_Customers' it is the table name
    return render(request,'my_library/cust_details.html',context=context_list)#for ref in html we use context

# def add(request):
#     if request.POST:
#         first_name=request.POST['First_Name']
#         last_name=request.POST['Last_Name']
#         age=request.POST['Age']
#         models.Lib_Customers.objects.create(first_name=first_name, last_name=last_name, age=age)
#         return redirect(reverse('my_library:list_customers'))
#     else:
#         return render(request,'my_library/add.html')
def delete(request):
    if request.POST:
        pk=request.POST['pk']
        try:
            models.Lib_Customers.objects.get(pk=pk).delete()
            return redirect(reverse('my_library:list_customers'))
        except:
            print("pk is not found")
            return redirect(reverse('my_library:list_customers'))
    else:
        return render(request,'my_library/delete.html')
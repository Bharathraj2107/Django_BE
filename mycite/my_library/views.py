from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.http import HttpResponseNotFound
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

def add_numbers(request):
    return render(request,"my_library/calculator.html")
#interview-questions
#migration
#it will check the authentication  changes and steps taken
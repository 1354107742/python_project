from django.shortcuts import HttpResponse, render, redirect
from app01.models import User
from app01.models import Publisher
from app01.models import Author

error_msg = ""


def login(request):
    #需要判断
    if request.method == "GET":
        #如果是第一次来，是跟我要一个登陆页面来添数据 --》get
        return render(request, 'login.html')
    else:
        login_tr(request)


def index(request):
    return render(request, 'index.html')


def login_tr(request):
    request.POST.get('email')
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    print(email, pwd)
    ret = User.objects.filter(email=email, pwd=pwd)
    if ret:
        #登陆成功
        #跳转到进入页面
        return render(request,'index.html')
    else:
        error_msg = "你的账号和密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})

def list_book(request):
    #第一步：去数据库查所有的出版社
    ret = Publisher.objects.all().order_by('id')
    print(ret)
    #第二步：将其在网页上表达出来
    return render(request, 'list_book2.html', {'ret': ret})

def list_add(request):
    #返回一个添加页面，让用户在上面添加出版社的信息
    #因为之前已经让id变为自增
    #所以在新增上，只需要添加书名即可
    if request.method  == 'POST':
        #此时已经填写完数据，给我发数据
        #首先取得用户数据
        add_name = request.POST.get('name')
        #将数据添加到数据库
        Publisher.objects.create(name = add_name )
        #跳转回初始书架列表
        return redirect("/list_book/")

    return render(request, 'list_add2.html')


def list_del(request):
    #获取删除出版社的id
    del_id = request.GET.get('id')
    print(del_id)
    #根据id数据库删除对应数据
    Publisher.objects.filter(id = del_id).delete()
    #让用户返回到书架列表
    return redirect('/list_book/')

def list_edit(request):
    #获取编辑出版社的id（为了操作）
    edit_id  = request.GET.get('id')
    if request.method == 'POST':
        #取出用户编辑之后的数据
        new_name = request.POST.get('name')
        #对数据进行修改
        #寻找要修改的id
        edit_id = Publisher.objects.get(id = edit_id)
        #对id中名字进行更改
        edit_id.name = new_name
        #对数据进行保存操作
        edit_id.save()
        #返回到书架列表
        return redirect('/list_book/')
    #根据id数据库修改对应数据
    ret = Publisher.objects.get(id=edit_id)
    #进入到编辑页面表单
    print(ret)
    return render(request,'list_edit2.html',{'edit_name': ret})

def book_view(request):
    #1.查询所有图书数据库中的信息
    book = Author.objects.all()
    #2.将循环得到的数据回传到当前目录
    return render(request,"book_view.html",{"book": book})

def book_add(request):
    #首先要判断是为GET还是POST（跟前面一个道理）
    if request.method == "POST":
        #1.首先得到用户数据
        add_name = request.POST.get("book_title")
        add_publisher  = request.POST.get("publisher_id")
        #2.向图书数据库中添加数据
        Author.objects.create(title=add_name, publisher_id=add_publisher)
        return redirect('/book_view/')
    #返回原主页
    press_data = Publisher.objects.all()
    return render(request,"book_add.html",{'press_list': press_data})


def book_del(request):
    #基本功能与出版社功能实现方法是相同的
    #获取要删除的id
    del_id = request.GET.get('id')
    #在数据库对获取参数进行删除
    Author.objects.filter(id = del_id).delete()
    #直接刷新当前界面
    # return redirect('/book_view/')
    #跳转到删除反馈
    return render(request,"delete_success.html")

def book_edit(request):
    #获取编辑图书的id
    edit_id = request.GET.get("id")
    #在数据库中查找到该书
    edit_id_obj = Author.objects.get(id = edit_id)
    #对提交的新数据进行修改
    if request.method == "POST":
        edit_title = request.POST.get("book_title")
        edit_pub = request.POST.get("publisher_id")
        #修改图书名字
        edit_id_obj.title = edit_title
        #修改出版社名
        edit_id_obj.publisher_id = edit_pub
        #保存当前修改
        edit_id_obj.save()
        return redirect("/book_view/")
    press_data = Publisher.objects.all()
    return render(request, "book_edit.html", {
        'book_id_obj': edit_id_obj,
        "press_data": press_data
    })


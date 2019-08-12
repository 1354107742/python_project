from django.shortcuts import HttpResponse, render, redirect
from app01.models import User
from app01.models import Publisher

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

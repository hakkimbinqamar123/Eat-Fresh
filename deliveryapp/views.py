from django.shortcuts import render, redirect
from deliveryapp.models import *
from django.views.generic import CreateView,ListView,DeleteView
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")



def signup(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('password')

        # Hash the password
        hashed_password = make_password(d)

        if User_details.objects.filter(email=b):
            msg = {'msg1': 'Username already exists'}
            return render(request, './already.html', msg)
        else:
            ab = User_details(username=a, email=b, phone=c, password=hashed_password)
            ab.save()
            return render(request, "login.html")
    else:
        return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = Staff.objects.filter(username=username, password=password)
        obj2 = User_details.objects.filter(username=username, password=password)

        if obj.filter(username=username, password=password).exists():
            for i in obj:
                y = i.staff_id
                x = i.usertype
                z = i.username
                request.session['shop_id'] = z
                request.session['username'] = username
                request.session['password'] = password
                request.session['staff_id'] = y
                request.session['usertype'] = x

                if x == 'AP':
                    if Staff.objects.filter(username=username, password=password, shop_id=1).exists():
                        return render(request, "staff_home1.html")
                    elif Staff.objects.filter(username=username, password=password, shop_id=2).exists():
                        return render(request, "staff_home2.html")


                elif x == 'R':
                    return render(request, "rejected.html")
                elif x == 'w':
                    return render(request, "process.html")
                else:
                    return render(request, "home.html")

        elif obj2.filter(username=username, password=password,).exists():
            for i in obj2:
                y = i.user_id
                x = i.usertype
                z = i.username

                request.session['username'] = username
                request.session['password'] = password
                request.session['user_id'] = y
                request.session['usertype'] = x
                request.session['username'] = z

                if x == 'A':
                    return render(request, "adminhome.html")
                elif x == "u":
                    return render(request, "customerhome.html")
        else:
            return render(request, "invalid.html")
    return render(request,"login.html")

def staff_registration(request):
    return render(request,"staff_registration.html")

def staff_registration(request):
    if request.method=="POST":
        a = request.POST.get('username')
        b = request.POST.get('phoneno')
        c = request.POST.get('state')
        d = request.POST.get('district')
        e = request.POST.get('address')
        g = request.POST.get('email')
        h = request.POST.get('password')
        i = request.POST.get('shop_id')
        k = request.FILES.get("verification")
        j = request.POST.get("gender")
        f = request.FILES.get("photo")
        if Staff.objects.filter(email=g):
            msg = {'msg1': 'username already exists'}
            return render(request, './already.html', msg)
        else:
            ab = Staff(username=a, phoneno=b, state=c, district=d, address=e, email=g, password=h, shop_id=i, photo=f, gender=j, verification=k)
            ab.save()
            return render(request,"home.html")
    else:
        return render(request, "staff_registration.html")

def staff_home1(request):
    return render(request,"staff_home1.html")

def staff_home2(request):
    return render(request,"staff_home2.html")

def adminhome(request):
    return render(request,"adminhome.html")

def customerhome(request):
    return render(request,"customerhome.html")


def ch(request):
    a = Staff.objects.filter(usertype='w')
    return render(request, "staff_details.html",{"a":a})

def updatestatus(request,staff_id):
    Staff.objects.filter(staff_id=staff_id).update(usertype='AP')
    return render(request,"staff_details.html")


def agentreject(request,staff_id):
    Staff.objects.filter(staff_id=staff_id).update(usertype='R')
    return render(request, "staff_details.html")

class Listuser(ListView):
    template_name ="listofusers.html"
    model = User_details
    context_object_name = "a"

def deleteuser(request,user_id):
    a = User_details.objects.get(user_id=user_id)
    a.delete()
    return redirect("/listofusers")

class Liststaff(ListView):
    template_name ="listofstaffs.html"
    model = Staff
    context_object_name = "a"

def deletestaff(request,staff_id):
    a = Staff.objects.get(staff_id=staff_id)
    a.delete()
    return redirect("/listofstaffs")


def customerprofile(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = User_details.objects.get(user_id=int(user_id))

        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')


        up.username = username
        up.phone = phone
        up.email = email
        up.password = password
        up.save()
        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'customerprofile.html',context)

    else:
        user_id = request.session['user_id']
        up = User_details.objects.get(user_id=int(user_id))
        context={'up':up}
        return render(request, 'customerprofile.html',context)



def staffprofile1(request):
    if request.method == 'POST':
        staff_id = request.session['staff_id']
        up = Staff.objects.get(staff_id=int(staff_id))

        username = request.POST.get('username')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')


        up.username = username
        up.phoneno = phoneno
        up.email = email
        up.password = password
        up.address = address
        up.save()
        context = {'msg': 'Staff Details Updated','up':up}
        return render(request, 'staffprofile1.html',context)

    else:
        staff_id = request.session['staff_id']
        up = Staff.objects.get(staff_id=int(staff_id))
        context={'up':up}
        return render(request, 'staffprofile1.html',context)



def staffprofile2(request):
    if request.method == 'POST':
        staff_id = request.session['staff_id']
        up = Staff.objects.get(staff_id=int(staff_id))

        username = request.POST.get('username')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')


        up.username = username
        up.phoneno = phoneno
        up.email = email
        up.password = password
        up.address = address
        up.save()
        context = {'msg': 'Staff Details Updated','up':up}
        return render(request, 'staffprofile2.html',context)

    else:
        staff_id = request.session['staff_id']
        up = Staff.objects.get(staff_id=int(staff_id))
        context={'up':up}
        return render(request, 'staffprofile2.html',context)

def productadd1(request):
    if request.method=="POST":
        a = request.POST.get('productname')
        b = request.POST.get('quantity')
        c = request.POST.get('price')
        d = request.FILES.get("photo")
        e= request.POST.get('shop_id')
        if Products.objects.filter(productname=a):
            msg = {'msg1': 'product already exists'}
            return render(request, './already.html', msg)
        else:
            ab = Products(productname=a, quantity=b, price=c, photo=d ,shop_id =1)
            ab.save()
            return render(request,"staff_home1.html")
    else:
        return render(request, "productadd.html")


def productadd2(request):
    if request.method=="POST":
        a = request.POST.get('productname')
        b = request.POST.get('quantity')
        c = request.POST.get('price')
        d = request.FILES.get("photo")
        e= request.POST.get('shop_id')
        if Products.objects.filter(productname=a):
            msg = {'msg1': 'product already exists'}
            return render(request, './already.html', msg)
        else:
            ab = Products(productname=a, quantity=b, price=c, photo=d ,shop_id =2)
            ab.save()
            return render(request,"staff_home2.html")
    else:
        return render(request, "productadd.html")

def customerview1(request):
    a = Products.objects.filter(shop_id=1)
    return render(request, "sample.html", {"a": a})

def customerview2(request):
    a = Products.objects.filter(shop_id=2)
    return render(request, "sample.html", {"a": a})
def customerview3(request):
    a = Products.objects.filter(shop_id=1)
    return render(request, "sample3.html", {"a": a})
def customerview4(request):
    a = Products.objects.filter(shop_id=2)
    return render(request, "sample3.html", {"a": a})

def sample1(request):
    a = Products.objects.filter(shop_id=1)
    return render(request, "sample.html", {"a": a})

def sample2(request):
    a = Products.objects.filter(shop_id=2)
    return render(request, "sample.html", {"a": a})



def shop1product(request):
    a = Products.objects.filter(shop_id=1)

    return render(request, "staffproductview.html",{"a":a})

def shop2product(request):
    a = Products.objects.filter(shop_id=2)
    return render(request, "staffproductview2.html",{"a":a})


def deleteproduct(request, product_id):
    details = Products.objects.get(product_id=product_id)
    details.delete()
    return redirect("/staffproductview")


def product_edit(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        t = Products.objects.get(product_id=int(product_id))


        r_n = request.POST.get('productname')
        r_d = request.POST.get('quantity')
        r_a= request.POST.get('price')
        r_b = request.POST.get('name')
        t.productname  = r_n
        t.quantity = r_d
        t.price= r_a
        t.name = r_b
        t.save()
        msg = 'updated'
        n_all = Products.objects.all()
        context = {'details': n_all, 'msg': msg}
        return redirect('/staffproductview')
    else:
        product_id = request.GET.get('id')
        t = Products.objects.get(product_id=int(product_id))
        context = {'t': t}
        return render(request, 'staffproductedit.html',context)

def product_edit2(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        t = Products.objects.get(product_id=int(product_id))


        r_n = request.POST.get('productname')
        r_d = request.POST.get('quantity')
        r_a= request.POST.get('price')
        r_b = request.POST.get('name')
        t.productname  = r_n
        t.quantity = r_d
        t.price= r_a
        t.name = r_b
        t.save()
        msg = 'updated'
        n_all = Products.objects.all()
        context = {'details': n_all, 'msg': msg}
        return redirect('/staffproductview2')
    else:
        product_id = request.GET.get('id')
        t = Products.objects.get(product_id=int(product_id))
        context = {'t': t}
        return render(request, 'staffproductedit.html',context)

def purchase(request):
    if request.method == "POST":
        a = request.POST.get('card')
        b = request.POST.get('number')
        c = request.POST.get('cvv')
        e = request.POST.get('qty')

        ab = purchase(card=a, number=b, cvv=c,qty=e)
        ab.save()
        return render(request, "customerhome.html")

    else:

        return render(request, "purchase.html")



from django.shortcuts import render, redirect
from .models import Products, User_details, Cart


def product_detail(request, product_id):
    product = Products.objects.get(product_id=product_id)
    return render(request, 'product_detail.html', {'product': product})



def add_to_cart(request, product_id):
    if request.method == 'POST':
        user_id = request.user.id  # Assuming you have user authentication

        product = Products.objects.get(id=product_id)
        no_of_items = int(request.POST.get('quantity', 1))

        cart_item, created = Cart.objects.get_or_create(user_id_id=user_id, product_id_id=product_id)

        if not created:
            cart_item.no_of_items += no_of_items
        else:
            cart_item.no_of_items = no_of_items

        cart_item.total_price = product.price * cart_item.no_of_items
        cart_item.save()

        messages.success(request, f'{product.productname} added to your cart successfully.')
        
        return redirect('cart_page')  # Redirect to the cart page after adding to cart
    else:
        return render(request, 'error.html', {'message': 'Invalid request method.'})



def cart_page(request):
    user_id = request.user.id
    cart_items = Cart.objects.filter(user_id_id=user_id)

    return render(request, 'cart_page.html', {'cart_items': cart_items})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    cart_item.delete()

    messages.success(request, f'{cart_item.product_id.productname} removed from your cart.')

    return redirect('cart_page')






























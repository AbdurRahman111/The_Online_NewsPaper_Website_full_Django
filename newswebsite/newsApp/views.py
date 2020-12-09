from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import catagory_of_news, add_news_new,News_Comment, like
from django.contrib.auth.models import User
from django.contrib import messages
from .templatetags import get_dict
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


def index(request):
    # this is for sorting our categories
    prods = None
    prodcat = catagory_of_news.get_all_category()
    categoryid = request.GET.get('category')
    print(categoryid)
    if categoryid:
        prods = add_news_new.get_all_product_by_categoryID(categoryid)
    else:
        prods = add_news_new.get_all_product()

    # this is for show posts and news to index page
    allPosts = add_news_new.objects.all()
    params = {'prod': prods, 'prodcats': prodcat, 'allPosts': allPosts}
    return render(request, 'index.html', params)


def login_finc(request):
    if request.method == 'POST':
        username_log = request.POST['username_log']
        user_log_password = request.POST['user_log_password']
        # this is for authenticate username and password for login
        user = authenticate(username=username_log, password=user_log_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In !!")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again !!")
            return redirect('login')

    else:
        return render(request, 'login.html')


def signup(request):
    if request.method=='POST':
        #check the post peramiters
        user_name=request.POST['user_name']
        user_phone=request.POST['user_phone']
        user_email=request.POST['user_email']
        User_Date=request.POST['User_Date']
        user_password12=request.POST['user_password']
        user_password_confirm=request.POST['user_password_confirm']


        #chech the error inputs
        if user_password12 != user_password_confirm:
            messages.error(request, "Passwords are not match")

            return redirect('signup')

        if len(user_phone)<4:
            messages.error(request, "Phone Number Al least 4 Digits")
            return redirect('signup')

        if len(user_password12)<8:
            messages.error(request, "Passwords Must be Al least 8 Digits")
            return redirect('signup')


        # create user

        myuser = User.objects.create_user(user_name, user_email, user_password_confirm)
        myuser.user_phone=user_phone
        myuser.User_Date=User_Date
        myuser.save()

        sub_of_email="Congrates, You Have Successfully Create an account in The Online Newspaper"
        mes_of_email="Congrates, You Have Successfully Create an account in Our Online Newspaper. You Now can Read our posts, news and see pictures. You can Like and comments our news and share your Opinion here. You can Know update news of Sports, World, Finance etc. Thank You"

        send_mail(
            sub_of_email, # Subject of message
            mes_of_email, # Message
            'md0099ahsohel@gmail.com', # From Email
            [user_email], # To Email

        fail_silently=False
        )


        messages.success(request, "you have successfully create your Account !!")

        return render(request, 'index.html')

    else:
        return render(request, 'signup.html')


def logout_func(request):
    # this is for logout from user id
    logout(request)
    messages.success(request, "Successfully logout !!")
    return redirect('index')


# make APIs for comments in news
def postComments(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postId = request.POST.get("postId")
        post = add_news_new.objects.get(id=postId)
        serial_no= request.POST.get('serial_no')

        if serial_no == "":
            News_Comment_data = News_Comment(comment=comment, user=user, postID=postId, post=post)
            News_Comment_data.save()

            messages.success(request, "Your Reply is Successfully Posted !!")

        else:
            parent = News_Comment.objects.get(serial_no=serial_no)
            News_Comment_data = News_Comment(comment=comment, user=user, postID=postId, post=post, parent=parent)
            News_Comment_data.save()

            messages.success(request, "Your Reply is Successfully Posted !!")

    return redirect(f'/{post.slug}')


# this is for personal information
def settings(request):
    if request.method=="POST":
        return render(request, 'account_settings.html')
    else:
        return render(request, 'account_settings.html')



# this is for details page of news, and also used for comment transfer
def blogPost(request, slug):
    post=add_news_new.objects.filter(slug=slug).first()
    comments = News_Comment.objects.filter(post=post, parent=None)
    replies = News_Comment.objects.filter(post=post).exclude(parent=None)

    repDict = {}
    for reply in replies:
        if reply.parent.serial_no not in repDict.keys():
            repDict[reply.parent.serial_no] = [reply]

        else:
            repDict[reply.parent.serial_no].append(reply)

    context={"post":post, 'comments': comments, 'repDict':repDict }
    return render(request, "news_post.html", context)


# this is for getting likes and likes counting
def LikeView(request):
    if request.method=="POST":
        post_id = request.POST.get('post_id')
        post_obj = add_news_new.objects.get(id=post_id)
        user=request.user

        if user in post_obj.likes.all():
            print(user)
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        Like, created = like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if Like.value == 'Like':
                Like.value='Unlike'
            else:
                Like.value = 'Like'

        Like.save()


    return redirect('index')

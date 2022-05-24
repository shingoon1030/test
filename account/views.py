from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import User
#from .timetableClean import timetableCleaning
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages


def login(request) :                                    # 로그인 처리
    if request.method == 'POST' :
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username = userid, password = pwd)
        print(userid, pwd, user )
        if user is not None :
            auth.login(request, user)
            return redirect('home')
        else :
            messages.add_message(request, messages.WARNING, '유저 정보가 없습니다. 아이디와 비밀번호를 확인해주세요')
            return render(request, 'login.html')
    else :
        return render(request, 'login.html')

def signup(request) :                                   # 회원가입 처리
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        res_data = {} 

        if not (username and password and repassword and email) :
            messages.info(request, '모든 항목을 채워주세요.')
        elif password != repassword :
            messages.add_message(request, messages.WARNING, '입력한 비밀번호가 서로 다릅니다.')
        elif not("hana.hs.kr" in str(email)) :
            messages.add_message(request, messages.WARNING, '하나고등학교 이메일이 아닙니다.')
        elif len(str(password)) < 8 :
            messages.add_message(request, messages.WARNING, '비밀번호가 너무 짧습니다. 8자 이상으로 입력해주세요.')
        else :
            flag = True
            try :
                trash = User.objects.get(username=username)
                messages.add_message(request, messages.WARNING, '이미 존재하는 아이디입니다.')
                flag = False
            except :
                pass
            try :
                trash = User.objects.get(email=email)
                messages.add_message(request, messages.WARNING, '이미 가입된 이메일입니다.')
                Flag = False
            except :
                pass

            if flag :
                user = User(username=username, password=make_password(password), email=email)
                user.time_table = 'notAuth'
                user.save()
                user = auth.authenticate(request, username = username, password = password)
                auth.login(request, user)

                current_site = get_current_site(request) 
                message = render_to_string('activate_email.html',                         
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = "[HasTime] 하나고 에브리타임 인증 메일입니다."
                email = EmailMessage(mail_subject, message,'has_everytime@naver.com', to=[email])
                email.send()
                return redirect('mustAuth')
        return render(request, 'signup.html') 
    
    else :
        return render(request, 'signup.html')

def logout(request) :                                       # 로그아웃
    auth.logout(request)
    return redirect('home')

def activate(request, uid64, token):                        # 메일 인증
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.time_table="Auth"
        user.save()
        auth.login(request, user)
        return redirect('home')
    else:
        return None

def mustAuth(request) :                                     # 미인증 유저에 대해 인증요구 페이지로 이동시키기
    return render(request, 'mustAuth.html')

def resendMail(request) :                                     # 인증 메일 재전송
    current_site = get_current_site(request) 
    message = render_to_string('activate_email.html',                         
    {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
        'token': account_activation_token.make_token(user),
    })
    mail_subject = "[HasTime] 하나고 에브리타임 인증 메일입니다."
    email = EmailMessage(mail_subject, message,'has_everytime@naver.com', to=[email])
    email.send()
    return render(request, 'mustAuth.html')

def timetableShow(request) :                                # 시간표 입력 페이지로 이동
    return render(request, 'timetableManage.html', {'current' : str(request.user.time_table)})

    
def timetableUpdate(request) :                                 # 시간표 업데이트
    request.user.time_table = request.POST['timetableField']
    request.user.save()
    print(request.user.time_table)
    #timetableCleaning()

    return redirect('timetable')
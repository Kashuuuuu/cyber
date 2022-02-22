from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.models import User
from course.models import course_detail
from shop.models import *
from user_profile.models import instructor, student

from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def private_message(request,msg):
    
    instruct=instructor.objects.filter(slug=msg)
    res={'instruct':instruct}

    return  render(request,'priveate-message.html',res)

def profile_certificates(request,certificate):
    li=[]
    instruct=instructor.objects.filter(slug=certificate)
    stud=student.objects.filter(slug=certificate)
    
    if len(instruct)>0:
        res={'instruct':instruct}
    elif len(stud)>0:
        res={'instruct':stud}
    if len(instruct)>0:
        usr=instructor.objects.get(user=User.objects.get(id=request.user.id))
        cr=course_detail.objects.filter(course_instructor=usr)
        for c in cr:
            if c.course_certificate!= '':
                li.append(c)
        res['crtfct']=li
    return  render(request,'profile-certificates.html',res)

def setting_genralinfo(request,genralinfo):
    if request.user.is_authenticated:
        nxt=request.get_full_path()
        instruct=instructor.objects.filter(slug=genralinfo)
        stud=student.objects.filter(slug=genralinfo)

        if request.method=='POST':
                fname = request.POST.get('fname')
                lname = request.POST.get('lname')
                # name = request.POST.get('name')
                email = request.POST.get('email')
                about=request.POST.get('about')
                img = request.FILES.get('img')
                fb_social=request.POST.get('fb_social')
                tw_social=request.POST.get('tw_social')
                li_social=request.POST.get('li_social')
                yt_social=request.POST.get('yt_social')   
                user=User.objects.get(id=request.user.id)
                if len(fname)!=0:
                    user.first_name = fname
                if len(lname)!=0:
                    user.last_name = lname
                user.save()
                print(fname,lname,img,email,about,fb_social,tw_social,yt_social,li_social,'pppp')
                print(len(fname),'fnm',len(lname))
                if len(instruct)>0: 
                    inst=instruct[0]
                    inst.user=user
                    if len(fname)!=0 :
                        inst.name=fname+' '+lname
                    if img!=None:
                        inst.img=img
                    if len(email)!=0:
                        inst.email=email
                    if len(about)!=0:
                        inst.about=about
                    if len(fb_social)!=0:
                        inst.facebook=fb_social
                    if len(tw_social)!=0:
                        inst.twitter=tw_social
                    if len(yt_social)!=0:
                        inst.youtube=yt_social
                    if len(li_social)!=0:
                        inst.linkedin=li_social
                    inst.save()
                    messages.success(request,'Profile Updated.')
                    return redirect(request.get_full_path())
                elif len(stud)>0: 
                        st=stud[0]
                        st.user=user
                        if len(fname)!=0:
                            st.name=fname+' '+lname
                        if img!=None:
                          st.img=img
                        if len(email)!=0:
                            st.email=email
                        if len(about)!=0:
                            st.about=about
                        if len(fb_social)!=0:
                            st.facebook=fb_social
                        if len(tw_social)!=0:
                            st.twitter=tw_social
                        if len(yt_social)!=0:
                            st.youtube=yt_social
                        if len(li_social)!=0:
                            st.linkedin=li_social
                        st.save()
                        messages.success(request,'Profile Updated.')
                        return redirect(request.get_full_path())
                else:
                    return redirect(nxt)
        if len(instruct)>0:
            res={'instruct':instruct}
        elif len(stud)>0:
            res={'instruct':stud}
    
        return  render(request,'setting-genralinfo.html',res)
    else:
        return redirect('error')


def settings_avatar(request,avatar):
    
    if request.user.is_authenticated:
        instruct=instructor.objects.filter(slug=avatar)
        stud=student.objects.filter(slug=avatar)

        # if request.method=='POST':
        #     img = request.FILES['img'] 
        #     if len(instruct)>0: 
        #         inst=instruct[0]
        #         inst.img=img
        #         inst.save()
        #     elif len(stud)>0: 
        #         st=stud[0]
        #         st.img=img
        #         st.save()
        # if len(instruct)>0:
        #     res={'instruct':instruct}
        # elif len(stud)>0:
        #     res={'instruct':stud}
        
        
        return  render(request,'settings-avatar.html')
    else:
        return redirect('error')

    
def settings_privacy(request,privacy):
    
    if request.user.is_authenticated:    
        # instruct=instructor.objects.filter(slug=privacy)
        # stud=student.objects.filter(slug=privacy)
        # if len(instruct)>0:
        #     res={'instruct':instruct}
        # elif len(stud)>0:
        #     res={'instruct':stud}

        

        return  render(request,'settings-privacy.html')
    else:
        return redirect('error')

  
def change_pwd(request,pwd):
    
    if request.user.is_authenticated:    
        instruct=instructor.objects.filter(slug=pwd)
        stud=student.objects.filter(slug=pwd)
        if len(instruct)>0:
            slg=instructor.objects.get(slug=pwd)
            res={'instruct':instruct}
        elif len(stud)>0:
            slg=student.objects.get(slug=pwd)
            res={'instruct':stud}

        if request.method == "POST":
            old = request.POST['old']
            new = request.POST['new']
            confirm = request.POST['confrm']
            user = User.objects.get(id=request.user.id)
            mail=user.email
            check=user.check_password(old)
            if confirm==new:
                if check==True:
                    user.set_password(new)
                    user.save()
                    user=User.objects.get(email=mail)
                    login(request,user)
                    messages.error(request, "Password Updated")
                    return redirect(f'/change-password/{slg.slug}')
                else:
                    messages.error(request, "Incorrect Old Password")
                    return redirect(f'/change-password/{slg.slug}')
            else:
                messages.error(request,'New And Confirm Password Not Match.')
        
        # if len(instruct)>0:
        #     res={'instruct':instruct}
        # elif len(stud)>0:
        #     res={'instruct':stud}

        return  render(request,'change-password.html',res)
    else:
        return redirect('error')
        

def profile(request,profile):
    
        instruct=instructor.objects.filter(slug=profile)
        stud=student.objects.filter(slug=profile)
        if len(instruct)>0:
            res={'instruct':instruct}
        elif len(stud)>0:
            res={'instruct':stud}
        if request.user.is_authenticated:
            if request.user.userType.type=='1':
                cr=course_detail.objects.filter(course_instructor=instructor.objects.get(slug=profile))
                totl=0
                for c in cr:
                    crs=courses_purchase_order.objects.filter(course=c).count()
                    totl+=crs
                res['stud']=totl
            elif request.user.userType.type=='2':
                totl=0
                us=User.objects.get(id=request.user.id)
                crs=courses_purchase_order.objects.filter(user=us).count()
                totl+=crs
                res['corse_prchase']=totl
            # else:
            #     res={'instruct':stud}
       
            
               
        return  render(request,'profile.html',res)
   
def success_story(request):
    return  render(request,'success-story.html')


def instructors(request):
    inst=instructor.objects.all()
    res={'instructor':inst}
    return  render(request,'instructor.html',res)


def orders(request,order):
     
    instruct=instructor.objects.filter(slug=order)
    stud=student.objects.filter(slug=order)
    if len(instruct)>0:
        res={'instruct':instruct}
    elif len(stud)>0:
        res={'instruct':stud}
    if request.user.is_authenticated:   
        c=User.objects.get(id=request.user.id)
        res['crs_oder']=courses_purchase_order.objects.filter(user=c)
        res['prod_oder']=products_purchase_order.objects.filter(user=c)
    return  render(request,'orders.html',res)


def quzess(request,quize):
    
    
    instruct=instructor.objects.filter(slug=quize)
    stud=student.objects.filter(slug=quize)
    
    if len(instruct)>0:
        res={'instruct':instruct}
    elif len(stud)>0:
        res={'instruct':stud}

    return  render(request,'quzess.html',res)

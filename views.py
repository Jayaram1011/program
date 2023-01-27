
import datetime

from django.shortcuts import redirect, render
from stestapp.models import Details, History


def base(request):
    return render(request,'base.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        print(type(username),type(password))
        try:
            user_dataname = Details.objects.get(username=username,password=password)
            print(user_dataname)
            print("username and password exists in database")
            current_time = datetime.datetime.now()
            History.objects.create(user_id=user_dataname,timestamp=current_time)
            request.session['name'] = username
            request.session['password'] = password
            print('sankar')
            return redirect('details')
        except:
            print('reddy')
            print("Enter correct username and password")
    return render(request,'login.html')
                   
def details(request):
    try:
        username_data = request.session['name']
        userid = Details.objects.values().filter(username=username_data)
        user_id = (list(userid)[0]['id'])
        details = History.objects.all().filter(user_id = user_id)
        print('ron')
        print()
        return render(request,'details.html',{'message':details,'username_data':username_data,'userid':user_id})
    
    except Exception as e:
        print(e)
        print('xyz')
        return render(request,'login.html')
    
def logout(request):
    print('logout here')
    try:
        del request.session['name']
        del request.session['password']
        request.session.flush()
        request.session.modified = True
    except:
        pass
    return render(request,'login.html')
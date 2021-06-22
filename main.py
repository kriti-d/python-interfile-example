import  execer

def get_name(request):
    name = request.POST.get('first_name') 
    execer(name)

get_name()

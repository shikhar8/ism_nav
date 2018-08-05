from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
import json
def home_page(request):
    return render(request,'places/home_page.html',{})
def getx(request):
    start= request.GET['start']
    end= request.GET['end']
    #return HttpResponse(start)
    a = {0: 'rd', 1: 'amul', 2: 'main canteen', 3: 'nlhc', 4: 'sac'}
    b = {0: [1, 1, 2, 3, 4], 1: [5, 1, 2, 13, 4], 2: [21, 3, 1, 4, 4], 3: [21, 2, 9, 1, 1], 4: [1, 2, 3, 4, 1]}
    #c = start
    #ax=Place.object.filter(Placename=start).number
    #print(ax)
    #d = end
    flag = 0
    #b={}
    #try:
     #with open("abc.json","w") as abc:
     #   json.dump(bx,abc)
    #except error:
    #   pass

    #try:
    #  with open("abc.json", "r") as abcd:
    #    shr = abcd.read()
    #    return HttpResponse(type(shr))
    #  #shr=json.loads(shr1)
       #return HttpResponse(shr1)
    #except :
        #return HttpResponse(shr1)

        #pass
    #for i in shr.keys():
     #   b[int(i)] = shr[i]
     #   return HttpResponse(b)

    from .models import Place
    abc = Place.objects.filter(Placename=start)
    for i in abc:
        c= str(i)

    from itertools import combinations
    from itertools import permutations
    for i in a.keys():
        if c == a[i]:
            e= i
            flag = 1
            break
    #if flag == 0:
        #print("place not found")
    #flag = 0
    abc = Place.objects.filter(Placename=end)
    for i in abc:
        d = str(i)
    for i in a.keys():
        if d == a[i]:
            f = i
            flag = 1
            break
    #return HttpResponse(e)
    #if flag == 0:
        #print("place not found")
    # print(e,f)
    list = [0, 1, 2, 3, 4]
    list.remove(e)
    list.remove(f)
    # print(list)
    tmp = [e]
    final = []
    for i in range(4):
        for j in permutations(list, i):
            # print(j)
            for k in j:
                # print(k)

                tmp.append(k)
            tmp.append(f)
            final.append(tmp)
            tmp = [e]
    print(final)
    fmul = []
    # help(permutations)
    for i in final:
        mul = 1
        l = len(i)
        for j in range(l - 1):
            mul *= b[i[j]][i[j + 1]]
        fmul.append(mul)
        mul = 0
    print(fmul)
    total = {}
    n = len(fmul)
    final1 = final
    #print(final1)
    # for i in range(n):
    #    print(final[i],"->",fmul[i])
    for i in range(len(final)):
        x = final[i]
        for j in range(len(x)):
            y = x[j]
            final1[i][j] = a[y]
    #print(final1)
    #print(fmul)
    sum=0
    for i in fmul:
        sum+=i
    xy=sorted(range(n))
    for i in range(n):
        final1[i].append('-->')
        final1[i].append((fmul[i]))
    return  render(request,'places/num.html',{'final1':final1,'start':start,'end':end,'sum':sum})



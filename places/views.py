from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request,'places/home_page.html',{})
def getx(request):
    start= request.GET['start']
    end= request.GET['end']
    #return HttpResponse(start)
    a = {0: 'rd', 1: 'amul', 2: 'main canteen', 3: 'nlhc', 4: 'sac'}
    b = {0: [1, 1, 2, 3, 4], 1: [5, 1, 2, 13, 4], 2: [21, 3, 1, 4, 4], 3: [21, 2, 9, 1, 1], 4: [1, 2, 3, 4, 1]}
    c = start
    #ax=Place.object.filter(Placename=start).number
    #print(ax)
    d = end
    flag = 0
    from itertools import combinations
    from itertools import permutations
    for i in a.keys():
        if c == a[i]:
            e = i;
            flag = 1;
            break;
    #if flag == 0:
        #print("place not found")
    #flag = 0
    for i in a.keys():
        if d == a[i]:
            f = i;
            flag = 1;
            break;
    #if flag == 0:
        #print("place not found")
    # print(e,f)
    list = [0, 1, 2, 3, 4]
    list.remove(e)
    list.remove(f)
    # print(list)
    tmp = [e]
    final = []
    for i in range(3):
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





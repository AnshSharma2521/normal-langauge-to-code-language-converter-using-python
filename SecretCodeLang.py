import random as r
alpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = ""
for i in range(0,100):
    c = int(input("Enter 1 for code and Enter 0 for decode"))
    ab = r.choice(alpha)
    cd = r.choice(alpha)
    de = r.choice(alpha)
    bc = r.choice(alpha)
    fh = r.choice(alpha)
    bn = r.choice(alpha)
    if c==1:
      a = input("Enter what you want to say")
      b = len(a)
      if len(a)>2:
         c = a[1:len(a)]
         d = ab+cd+de+c+bc+fh+bn
         print(d)
         n +=d
         c = int(input())
         if c==0:
            break
      else:
         e = a[0:1]
         f = alpha[1:2]
         print(f)
         g = int(input())
         if g==0:
            break
    elif c==0:
        q = input("Enter word for decode")
        if len(q)<5:
            var2 = q[3:len(q)]
            j = var2[0:1]
            l = j + var2[0]
            l = int(input())
            if l == 0:
                break
        else:
            if len(q) > 5:
                var1 = q[3:len(q)]
                h = var1[0:(len(var1) - 1)]
                s = q[(len(q) - 1):len(q)] + h
                print(s)
                m = int(input())
                if m == 0:
                    break
print(n)

















































""""n = int(input())
List = [ list(input().strip()) for _ in range(n)]
s1 = input().strip()
s2 = input().strip()

st_co, sl_co = 0 , 0
x , y = -1 , -1


count = 0 

for items in List :
    if '*' in items :
        st_co += 1 
        if x == -1 and y ==-1 :
            x , y =  count , items.index('*')
    count += 1 

if len(s1) == st_co :
    a , b = s1, s2
else :
    a, b = s2,s1 

        
for let_ind in range(len(a)) :
    List[x+let_ind][y] = a[let_ind]

x , y = -1 , -1


count = 0 

for items in List :
    if '*' in items :
        st_co += 1 
        if x == -1 and y ==-1 :
            x , y =  count , items.index('*')
    count += 1 

if List[x][y-1] == b[0] and b[0] not in a  :
    for let_ind in range(len(b)) :
        List[x][y+let_ind] = b[let_ind]
else:
    for let_ind in range(1 ,len(b)) :
        List[x][y+let_ind-1] = b[let_ind]
    

for ind in List :
    print(*ind)


'''
10
++++++++++
++++++++++
+++*++++++
+++*++++++
+++***++++
+++*++++++
+++*++++++
+++*++++++
++++++++++
++++++++++
MANAGE
NEW

6
++++++
++*+++
++****
++*+++
++*+++
++++++
LION
IRON

'''"""











s = input().strip().upper()
if 'A' in s: 
    a,b = s.split('A')
    print(int(a) + int(b))
elif 'S' in s :
    a,b = s.split('S')
    print(int(a) - int(b))
elif 'M' in s :
    a,b = s.split('M')
    print(int(a) * int(b))
elif 'D' in s :
    a,b = s.split('D')
    print(int(a) / int(b))
    










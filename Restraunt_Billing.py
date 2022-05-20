menu={'chilli potato':{'honey chilli potato':99,'spicy chilli potato':149},'noodles':{'hakka noodles':99,'veggie noodles':129},'burger':{'1 patty':59,'2 patty':99},'momos':{'tandoori momos':79,'steam momos':69},'pizza':{'cheeze pizza':99,'veggie pizza':149},'shakes':{'oreo shake':199,'kitkat shake':99},'coffee':{'cold coffee':149,'latte':199},'mojito':{'alchoholic':299,'non-alchoholic':199}}

from datetime import datetime #date time module me se submodule/class datetime aayega and in 
#datetime class we have function now() 
'''
print(menu['chilli potato'])
print(menu['chilli potato']['honey chilli potato'])
print(menu['chilli potato']['spicy chilli potato'])
'''

a='chilli potato'
a1='honey chilli potato'
a2='spicy chilli potato'

b='noodles'
b1='hakka noodles'
b2='veggie noodles'

c='burger'
c1='1 patty'
c2='2 patty'

d='momos'
d1='tandoori momos'
d2='steam momos'

e='pizza'
e1='cheeze pizza'
e2='veggie pizza'

f='shakes'
f1='orea shake'
f2='kitkat shake'

g='coffee'
g1='cold coffee'
g2='latte'

h='mojito'

for val in menu.items():
    print(val[0],":")
    for eat in val[1].items():
        print(eat[0],end="\t")
        print(eat[1])
        
        
name=input("please enter your name: ") 

f=open(name,"a")
f.write(str(datetime.now()))
date=input("please enter today's date: ")
f.write(date)
f.write("order:")

f.close()



 
sum1=0     
while(True): 
    con=input("do you want to order yes or no: ")
    if(con=="no"):
        break
    
    f=open(name,"a")
    
    
    order=input("please enter your order (all small letter please): ")
    f.write("\n")
    f.write(order)
    f.write(":")
    f.write("\n")
    choice=input("please place the choice from the order: ")
    f.write(choice)
    f.write("\t")
    price=menu[order][choice]
    f.write("Price: ")
    f.write(str(price))
    print("price: ",menu[order][choice])
    
    
    sum1=sum1+menu[order][choice]
    
    
    
print("your total bill is: ",sum1,"\n Thank You,Please revisit")    
f.write("\nTotal Bill: ")
f.write(str(sum1))
f.close() 
# list=[12,10,90,10,9,2,11]
#
# for i in list:
#     if(i>9):
#         print(i)
#
from dict_a1 import value

# list=['hello','tushar','vinod','naik']
# a=int(input("enter the number: "))
# for i in list:
#     if(len(i)>a):
#         print(i)

# a=[]
# for i in range(1,6):
#     b=int(input("enter the number: "))
#     a.append(b)
# b=[10,20,30,40,20]
# print(a)
# print(max(b))
# print(max(a))


# list=['abc', 'xyz', 'aba', '1221']
# for i in list:
#     if(len(i)>2) and i[0]==i[-1]:
#         print(i)
#

# list1=[1,4,3,5,6,8]
# mul=1
# for i in list1:
#     mul=mul*i
# print(mul)

# lis=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# lis.pop(5)
# lis.pop(4)
# lis.pop(0)
# print(lis)


# lis=[10,34,2,4,5,7,2]
# li=[i for i in lis if i%2!=0]
# print(li)

# lis=[10,34,2,4,5,7,2]
# for i in lis:
#     print(i,'\t',lis.index(i))
#


# lis=[10,34,2,4,5,7,2]
# if len(lis)!=0:
#     print("list not is empty")
# else:
#     print("list is empty")

#
# lis=[10,34,2,4,5,7,2]
# li=lis.copy()
# print(li)

# lis=[10,34,2,4,5,7,2]
# print(lis)
# a=int(input("enter the indx: "))
# print(lis.index(a))


# s='emp'
# list = [1,2,3,4]
# ch=[]
#
# for i in list:
#     ch.append(s+str(i))
# print(ch)

# list = [1,2,3,4]
# lis=[10,34,2,4]
# for x,y in zip(list,lis):
#     print(x,y)

# list1=[1, 3, 5, 7, 9, 10]
# list2=[2, 4, 6, 8]
# list1[-1:]=list2
# print(list1)

# a=["Black", "Red", "Maroon", "Yellow"]
# b=["#000000", "#FF0000", "#800000", "#FFFF00"]
# c=list()
#
# for i in range(len(a)):
#     dict={'color_name':a[i],'color_code':b[i]}
#     c.append(dict)
# print(c)

#
# a=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("Enter the indec"))
#
# if n>0 and n>len(a):
#     print("exist")
# else:
#     print("not exist")

# a=["Black", "Red", "Maroon", "Yellow"]
# b=["#000000", "#FF0000", "#800000", "#FFFF00"]
# lis=[]
# for i in range(len(a)):
#     dict={'color_name':a[i],'color_code':b[i]}
#     lis.append(dict)
#
# print(lis)



# dict1={'a':1,'b':2,'c':3}
#
# dict1={v:k for k,v in dict1.items()}
#
# print(dict1)

mystring1 = "vidyanidhi"
print(mystring1[:3])  # or mystring[0:3]

# items start through 6-1
# print(mystring1[2:6])
#
# # items start from 3 through the rest of the array
# print(mystring1[3:])
#
# # items from the beginning through 6-1
# print(mystring1[:6])
#
# # start from 2 till 7-1 not past stop, by step 2
# print(mystring1[2:7:2])

# from last (-1)  to (-5) by step 2
# print(mystring1[-1:-6:-2])

# print(mystring1[2:-5])














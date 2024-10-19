# 1)
# def sqr(num):
#     return num**2
# print(sqr(5))
#
# print("using lambda")
# print((lambda x:x*x)(6))

# 2)
# def pr():
#     print("hello")
# pr()
# print("using lambda")
# (lambda :print("hello"))()


# 3)
# def fun(num1,num2=10):
#     print(num1 , num2)

# fun(20)
# print("using lambda")
# b=lambda x,y=30:print(x,y)
# b(25)

# 4)
# def myfun(*arg):
#     for i in arg:
#         print(i)
# myfun(10,20,30)
#
# print("using lambda")
#
# (lambda *args:[print(i) for i in args])(10,20,30,40)

# (lambda x:print("is evan")if x%2==0 else print("odd"))(9)
#
# (lambda *args:[print(i) for i in args])(10,20,30,40,)


# def specil(fun):
#     def spec():
#         print("Special")
#         fun()
#     return spec
#
# @specil
# def a():
#     print("a")
# @specil
# def b():
#     print("b")
# @specil
# def c():
#     print("c")
#
# a()
# b()
# c()

(lambda **args: [print(x,y) for x,y in args.items()])(name='tushar',age=21)










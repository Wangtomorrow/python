#coding=utf-8

#===============================================================================
# #简单的输入输出
# name = input()  #input接收，并存入name。
# print(name);print('adfasf');...   #输出name,没f没f没f。同一行使用多条语句用分号分开
#===============================================================================

#===============================================================================
# #""--''的应用，还有转义字符，字符串的一堆乱七八糟的东西,打印let's go.没啥区别，就是套用的事.
# print('let\'s go')
# print("let's go")     #双套单，单套双，自己套自己加\转义字符吧
# print('let'+"'"+'s go')
# s = 'C:\now'    #MDZZ  给\n当成回车的转义字符
# s1 = 'C:\\now'  #\转义\
# s3 = r'C:\now\a\c\d\f'  #r 原始字符串，全部都给加一个\转义字符,结尾不能是\，看下面
# #s4 = r'C:\now\a\c\d\f\'   #报错，解决办法再看下面
# s5 = r'C:\now\a\c\d\f''\\'
# s6 = """456465,      #这块不能换行-----多行字符串这样存，妈的这不是注释么
# 4654654,
# 46546546,
# 6546546,
# """
#===============================================================================

#===============================================================================
# #数据类型的巴拉巴拉
# print(1+2)         #字符串的拼接
# print('1'+'2')
# #整形（长整型跟整形结合了，长度不受限制，大数运算），浮点型（有小数点的），布尔型，e记法（科学计数法，特别大/小的数）
# a = 0.0000000000000000000000000000000045   #4.5e-33
# b = 1.5e11   #150000000000.0
# print(True + True)  #Ture + False
# print(a)
# #类型转换    int()  str()  float()  字符串类型强制转换成整型啥的，报错。   int（）直接砍掉小数点后面的东西，不四舍五入。惨
# #                               整形转换成浮点型没啥问题
# #这块注意的地方就是  str ，以后定义的时候能不用就不用
# #type() 获得关于变量类型的信息   isinstance(变量/常量，类型)返回True或者False
#===============================================================================

#===============================================================================
# 简单的测试小程序，算是熟悉输入输出吧
# #print("---------------hello,world----------------")
# import random
# secret = random.randint(1,10)
# num = input("请输入:")
# guess = int(num)    #强制类型转换为int型，注意括号位置，直接砍掉小数点后面的东西，不四舍五入。惨。
# if guess == secret:
#     print("正确！")
# else:
#     if guess > secret:
#         print("大了！*3")
#     else:
#         print("小了！")
# while guess != secret:
#     num = input("错误，请重新输入数字:")
#     guess = int(num)
#     if guess == secret:
#         print("正确！")
#     else:
#         if guess > secret:
#             print("大了！")
#         else:
#             print("小了！")
#
# print("结束。")
#
#===============================================================================

#===============================================================================
# #x if 条件 else y
# #assert 条件   后面条件为假时，程序崩溃，抛出AssertionError异常，用来置入检查点
# while 1:
#     score = int (input("please input:"))
#     if 90 <= score <= 100:
#         print('A')
#     elif 80 <= score < 90:   #elif == else if
#         print('B')
#     elif 70 <= score < 80:
#         print('C')
#     elif 0 <= score < 70:
#         print('D')
#     else:
#         print("error!")
#===============================================================================

#===============================================================================
#
# #for 目标 in 表达式：
# #    循环体
# name = 'wangzongyi'
# for i in name:
#     print(i,end=' ')   #打印name里的每一个值，i是啥都行
# for i in range(len(name)):        #range(m,n) 从m到n下标
#     print(name[i],end='')
#===============================================================================

#===============================================================================
# member = ['A','AB','ABC','ABCD']  #定义一个列表，类似于c数组，但是比那个叼
# for i in member:
#     print(i , len(i))    #打印member里的每一个成员及他们的长度
#===============================================================================

#===============================================================================
# #range([start,] stop[,step=1])  #"[]"括号括起来的表示可选参数，生成一个star--stop的数字序列
# #print(list(range(5)))    #list打印列表
# for i in range(2,6,2):
#     print(i)
#===============================================================================

#break与continue用法跟c相同，恩，一如既往的没有分号。注意引号引号引号
#===============================================================================
# #break
# name = 'wangzongyi'
# answer = input('Please input:')
# while 1:
#     if name == answer:
#         break
#     answer = input('Wrong!Please try again!')
# print('Right!')
#===============================================================================
#===============================================================================
# #continue
# for i in range(1,12):
#     if i % 2 == 0:
#         continue
#     print(i)
#===============================================================================

#===============================================================================
# #列表 == 贼特么叼的数组（啥玩意都能存） list  a[0]第一  a[-1]倒数第一
# member = ['A','AB','ABC','ABCD','ABCDE']
# number = [1,2,3,4,5]
# mix = [1,'abc','王宗仪','1.234',[1,2,3,4]]  #混合列表。确实叼
# empty = []   #空列表
#
#添加
# member.append('QWER')   #append() 向列表末添加元素，骚，只能传一个元素
# member.extend(['QQQQQ','WWWWW'])   #extend([...]) 引用一个列表来扩建列表
# member.insert(0,'zxc')    #insert(位置，元素) 在特定位置加入元素。数数，0,1,2,3,4,5,6...，对，很对
#删除
# member.remove('AB')
# del member[2]
# member.pop()    #arr.pop()从列表中取出最后一个元素,扔了不要了。可以赋值：name = member.pop()
# member.pop(1)   #抛出第n个
#
# 列表分片（slice）
# member[1:3]   #输出 ['AB', 'ABC'] 1,2
# member[n:] / member[:n] / member[:]  #列表的复制.为复制，指向不同空间。若要指向同一空间，list1 = list2

# #列表的balabala
# list1 = [1,6]
# list2 = [3,0]
# print(list1 > list2)  #从第0个元素开始比较，遇到不同，直接退出
# list3 = [1,6]
# print((list1 < list2) and (list1 == list3))   #1 and 1
# list4 = list1 + list2
# print(list4)    #拼接。不要用"+",用添加的方法。"+"两边数据类型必须相同。
# list3 *= 3;
# print(list3)
# print(1 in list1)
# print(10 not in list1)
#
# print(3 in mix)     #False  3在列表mix里的一个列表里，只能影响一层
# print(3 in mix[4])  #Ture
# print(mix[4][2])    #访问列表里的列表中的元素类似于二维数组
#
#其他方法
# num = member.count('A')         #arr.count() 计算参数在列表中出现的次数
# num1 = member.index('A')        #arr.intdex() 返回参数在列表中的位置
# num3 = member.index('ABC',1,3)  #1,3范围的起始位置  输出2，依然采用原列表的角标
# number.reverse()                #没有参数，列表倒置 *******
#
#倒置和排序
# number1 = [1,5,3,5,9]
# number2 = [1,5,3,5,9]
# number1.sort()                  #sort用指定的方法对列表进行排序，没有参数，默认从小到大  ***********************
# number1.reverse()               #sort + reverse 实现从大到小排序
# number2.sort(reverse = True)    #sort(func,key,reverse)   func方法，默认归并排序，key预算法搭配的关键字。reverse默认 = False
#===============================================================================

#===============================================================================
#元组：列表+限制    不可改变类型。  tuple 一旦初始化，不能修改
#——创建和访问元组  大部分情况下，小括号      逗号的决定性作用****逗号隔开的一组元素的数据默认建立一个元组
#tuple1 = (1,2,3,4,5,6,7)           #创建
#tuple1[2] #/ tuple[4:] / ...       #访问
#tuple1[2] = 66                    #报错。无法更改*********

#tuple2 = (1)                       #输出 1 ，没括号。type(tuple2)--<class 'int'>,后面加 , 就可以，即tuple2 = (1,)
#tuple3 = 1,1,2,3                   #type(tuple3)--<class 'tuple'>
#tuple4 = ()                        #空元组
#8 * (8) / 8 * (8,)                 #64/8个8

#更新和删除元组
#member = ('A','AB','ABC','ABCD','ABCDE')
#利用切片来添加删除
#member = member[:2] + ('zxc',) + member[2:]      #先切片。然后给zxc加进去，重新拼接，让member指向他。原来的member指向的还有，等回收。此方法可以间接删除元素
#del member    删除。一般不用，有类似于JAVA的回收机制
#print(member)

#元组的操作符
#拼接    "+"左右两边必须都是元组
#重复    8 * (8,)
#关系    ><=
#成员     in / not in
#逻辑     and / or
#=====================================================================================

#=====================================================================================
#字典     是映射，不是存储表  工厂函数（类型）
# a = ['qwe','asd','zxc']
# b = ['123','456','789']
# print(b[a.index('qwe')])
#
# dict_1 = {'qwe':'123', 'asd':'456', 'zxc':'789'}
# print(dict_1['qwe'])
#
# dict_2 = dict((('A',12),('B',4456)))
# print(dict_2)
#
# dict_3 = dict(wewe = 'wwww',sdsds = 'eeeee')  #索引不能加引号
# print(dict_3)
#
# dict_3['wewe'] = '1231321321321'
# print(dict_3)
#
# dict_3['qwwqwq'] = '12sf3esfa'
# print(dict_3)
#
# dict_4 = {}
# #print(dict_4.fromkeys((1,2,3)))
# print(dict_4.fromkeys((1,2,3),'asfasfasfasfa'))  #只能穿一个参数
# #if  print(dict_4.fromkeys((1,3),'safasfas'))   重新建立一个新的字典，而不是更换此字典的值
#
# #访问
# dict_4 = dict_4.fromkeys(range(10),'z')
# print(dict_4)
# for eachKey in dict_4.keys():   #同 values items
#     print(eachKey)
#
# print(dict_4.get(123))   #get方法  用来访问 不知道有没有的时候
# print(123 in dict_4)
#
# #清空
# print(dict_4.clear())

# #浅拷贝
# aa = {1:'dd',2:'ee'}
# bb = aa.copy()
# cc = aa
# print(bb)
# print(cc)
# print(id(aa))
# print(id(bb))
# print(id(cc))
#
# print(aa.pop(2))
# print(aa.popitem())  #随机弹

# aa = {1:'dd',2:'ee'}
# aa.setdefault('q7q7q7q7q')
# print(aa)
# aa.setdefault(3,'4e65w46w5e')
# print(aa)
#
# bb = {'ppp':'pqdvmv'}
# aa.update(bb)
# print(aa)
#=====================================================================================

#=====================================================================================
#集合  集合里面所有元素是唯一的，去重，无序
#1.一堆元素用{}   2.set（）
# set_1 = set([1,2,3,4,5,5,5])
# print(set_1)

#去重
#列表
# num1 = [1,2,3,4,5,5,5,0]
# temp = []
# for each  in num1:
#     if each not in temp:
#         temp.append(each)
# print(temp)
#集合方法    得到无序
# num1 = [1,2,3,4,5,5,5,0]
# num1 = list(set(num1))
# print(num1)

#add  remove

#frozenset 不可变集合
# num3 = frozenset([1,2,3,6,5,4])
# num3.add(8)  #报错

#=====================================================================================

#=====================================================================================
#字符串     #http://bbs.fishc.com/thread-38992-1-1.html//查看帮助文档
# str1 = 'wang zong yi'
# str1 = str1[:3]+'sssss'+str1[3:]   #不是修改。是改变指向
# print(str1)
#
# str2 = 'AAAaa'
#print(str2.capitalize())        #capitalize首字母大写
#print(str2.casefold())          #casefold全变小写
#print(str2.center(12))          #center(width)  width宽度的缩进
#print(str1.count('zong',0,10))  #count(sub,[,start[,end]]) 统计sub在start到end中出现的次数
#endswith(sub,[,start[,end]])     expandtabs([tabsize = 8])
#区分 find(sub,[,start[,end]])/index(sub,[,start[,end]])
#isalnum()   isdigit()   isdecimal()    isalpha()   islower()/isupper()  isnumeric()  isspace()  istitle()
#join(sub)  ljust(width)/lstrip()/rstrip()   lower()  partition(sub)  replace(old,new[,count])  rfind(sub,[,start[,end]])
#print(str1.translate(str.maketrans('g','p')))   #str.maketrans('g','p')  输出{asiic:asiic}


# #字符串的格式化  format   其他各种各样的操作符去论坛或者网上找
# print("{0} love {1} {2}".format('I','www','aaa'))   #{n} 位置参数
# print("{a} love {b} {c}".format(a = 'I',b = 'www',c = 'aaa'))    #{a}关键字参数   俩可以一起使用，位置参数必须在关键字参数前
# print("{{0}}".format("asdfasf"))     #同理  \   不打印后面的参数，被注释掉了
# print('{0:.1f}{1}'.format(27.658,'GB'))     #0后面的: 格式化符号

# print('%c' % 97)
# print('%c %c %c' % (97, 98, 99))   #必须写成有括号的元组
# print('%s' % 'sfdf fsdfs sfsfsdfs')
# print('%d + %d = %d' % (1 , 2 , 1+2))
# print('%o' % 10)     #格式化无符号八进制   %x/%X  十六进制（区分大小写）
# print('%f' % 22.23232)    #默认精确到小数点后六位   %e/%E    %g/%G 灵活决定使用%f还是%e
#
# print('%3.2f' % 22.23232)
# print('%10d' % 5)
# print('%-10d' % 5)
# print('%+d' % 5)
# print('%+d' % -5)
# print('%#o' % 10)   #八进制
# print('%#X' % 10)   #十六进制
# print('%010d' % 5 )
# print('%-010d' % 5 )   #- 左对齐,右边加000000
#\各种转义字符
#=====================================================================================

#=====================================================================================
#列表，元组，字符串  //序列
# #list()   #转成列表 有参/无参
# a = list()
# print(a)
# b = 'wangzongyi'
# b = list(b)
# print(b)
# c = (1,2,3,4,5)
# c = list(c)
# print(c)

#turple()   #转成元组

#str(obj)     #转成字符串

#len()

# #max()   min()   数据类型一定要统一
# chars = '1234567980'
# print(min(chars))

#sum(iterable[,start = 0])   数据类型还要统一，整形，浮点型

#sorted()  默认小到大

#reversed()
# numbers = [1,-55,99,6,3,5,3]
# print(list(reversed(numbers)))

#enumerate()   返回一个索引值跟列表元素对应的
#numbers = [1,-55,99,6,3,5,3]
#print(list(enumerate(numbers)))     #[(0, 1), (1, -55), (2, 99), (3, 6), (4, 3), (5, 5), (6, 3)]

#zip()   #下标匹配
# a = [1,2,3,4,5]
# b = [11,22,33,44,55,66,77]
# print(list(zip(a,b)))       #[(1, 11), (2, 22), (3, 33), (4, 44), (5, 55)]
#=====================================================================================

#=====================================================================================
#函数
# def function_1():
#     print('abc')
#     print('sdddafasf')
# def function_2(name, id):
#     print(name + id + 'asdsdfs')
# def function_3(num1, num2):
#     result = num1 + num2
#     print(num1,'+',num2 ,'=',num1+ num2)
# def function_4(num1, num2):
#     return num1 + num2
# function_1()
# function_2('wang', '123')
# function_3(1,2)
# print(function_4(2,3))

#函数的参数  形/实

#函数文档
# def function_123():
#     """
#     123132132132123
#     """    #函数文档
#     #asfasfasfasfasfasdfasfa   #注释
#     print('asfasfasfasdfsa')
# #function_123()
# print(function_123.__doc__)

#关键字参数   参数多的时候实用,通过参数名来定位参数
# def function_21321(name, id):
#     print(name , '154sfda' , id)
# function_21321(id = 'wang' , name = 'sfsf')

#默认参数 定义默认值的参数
# def function_21321(name = '123', id = '333333'):
#     print(name , '154sfda' , id)
# #function_21321(id = 'wang' , name = 'sfsf')
# function_21321()

#收集参数/可变参数   用元组给打包起来   print本身就有一个收集参数，自己去看帮助文档
# def function_456456(*name,id = 222):
#     print('length = ',len(name))
#     print('a = ',name[1])
#     print('id = ',id)
# function_456456('www','ewewew','4w56ef',id = '165165')

#返回值  动态确定类型，不固定     无变量，只有名字
# def backmore():
#     """返回多个值（列表，同理可返回元组）"""
#     return [1,'asdfa',2.1611]
# print(backmore())

#变量的作用域*****（可见性）
# def product(a , b):
#     c = a * b
#    #print('函数内打印全局变量ppp的值：',ppp)
#     ppp = 465465
#     print('修改后ppp为',ppp)         #函数内试图修改全局变量。py会新建一个名字一样的局部变量(shadowing屏蔽)。尽量访问，不要修改
#     return c
# ppp = 123
# d = product(2 , 3)
# print('product = ',d)
# #print('打印局部变量c的值：',c)  跟别的一样，栈存储
# print('打印全局变量ppp的值：',ppp)

#global关键字
# a = 10
# def pp():
#     global a
#     a = 5
#     print(a)
# pp()
# print(a)

#内嵌函数
 #内部函数整个作用域都在外部函数内 ， 只能在此外部函数内调用
# def fun1():
#     print('fffff11111')
#     def fun2():
#         print('222222')
#     fun2()
# fun1()

#闭包
# def fun_1(x):
#     def fun_2(y):
#         return x * y
#     return fun_2    # 没括号
#
# #1 i = fun_1(8)
# #  i(5)
# print(fun_1(8)(5))
#外部无法直接调用内部函数

# def a():
#     x = 5;
#     def b():
#         x *= x
#         return x
#     return b()
# print(a())   #报错，两种解决办法
#这种情况存放到容器中，因为容器不存储在栈中
# def a():
#     x = [5];
#     def b():
#         x[0] *= x[0]
#         return x[0]
#     return b()
# print(a())
#nonlocal 强制转换成不是局部变量
# def a():
#     x = 5;
#     def b():
#         nonlocal x
#         x *= x
#         return x
#     return b()
# print(a())

#lambda表达式   省去定义函数的过程。不需要考虑命名问题。简化代码可读性
# def fun(x,y):
#     return y * x
# #使用lambda表达式如下
# a = lambda x,y : y * x
# print(a(5,4))

#filter  过滤器    help(filter)
# print(list(filter(None,[1,0,False,True])))   #过滤掉非true

# def odd(x):
#     return x % 2
# temp = range(10)
# show = filter(odd, temp)       #函数名，可迭代序列
# print(list(show))

#print(list(filter(lambda x : x % 2, range(10))))   #套套套

#map(函数，可迭代序列)
#print(list(map(lambda x : x * 2, range(10))))
#=====================================================================================

#=====================================================================================
#递归
#设置递归深度的方法
# import sys
# sys.setrecursionlimit(1000000)
#非递归写法
# def fun(n):
#     c  = n
#     for i in range(1,n):
#         c  *= i
#         print(c,i)
# fun(5)
#递归写法
# def fun_1(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fun_1(n-1)
# print(fun_1(5))
#危险性

#斐波那契数列 递归实现
#迭代
# def fun_1(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#     while n < 1:
#         print('wrong')
#         return -1
#     while (n - 2) > 0:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
# print(fun_1(12))
#递归
# def fun(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return fun(n - 1) + fun(n - 2)
# print(fun(12))
#分治  递归慢，迭代快

#汉诺塔
# def hannoi(n, x, y, z):
#     if n == 1:
#         print(x,'-->',z)
#     else:
#         hannoi(n-1, x, y, z)#将前n-1个盘子从x移动到y上
#         print(x, '-->',z) #将最底下的最后一个盘子从x到z
#         hannoi(n-1, y, x, z)#将y上的n-1个盘子到z
# n = int(input('请输入汉诺塔层数：'))
# hannoi(n, 'X', 'Y', 'Z')
#=====================================================================================

#=====================================================================================
#文件  文件对象方法 close()    read()
# help(open)
# f = open('F:\\a1.txt')
# f.read()
# f.tell()   #指针位置
# f.readline()
# f.seek(0,0)   #设置指针位置
#
# for eachline in f:
#     print(eachline)
#
# list(f)
# #f.write('aaaaaaaaaa')  #报错，不能写入
#
# f.close()
#
#=====================================================================================

#=====================================================================================
#os模块
#import os
#help(os)
#os.path

#pickle模块  amazing 几乎所有的py对象转成二进制
# import pickle
# a = [123,55,'wzy',['ewwew']]
# pickle_file = open('a.pkl','wb')   #wb格式
# pickle.dump(a,pickle_file)
# pickle_file.close()
# #读取
# pickle_file = open('a.pkl','rb')
# b = pickle.load(pickle_file)
# print(b)
#=====================================================================================

#=====================================================================================
#异常处理
#自己查吧

#try-except
# try:
#     检测范围
# except Exception[as reason]:
#     出现异常（Exception）后的处理代码   print(''+str(reason))
#如果多个异常可以写多个except或者用元组括起来except（a，b）：，如果不知道要显示哪个，就可以直接except：
#同时处理多个异常，则可以遇到第一个异常直接跳出执行相应的except，别的不执行

#try-finally
# try:
#     检测范围
# except Exception[as reason]:
#     出现异常（Exception）后的处理代码
# finally:
#     无论如何都会被执行的代码

#raise语句
#自己引出一个异常

#else
#在try-except 后加else
#with  自动判断文件不需要，自动关闭
# try :
#     with open('abc.txt','w') as f:
#         for each_line in f:
#             print(each_line)
# except OSError as reason:
#     print('wrong!'+str(reason))
#=====================================================================================

#=====================================================================================
#EasyGui 图形化界面
# import easygui
# easygui.msgbox('fdfdf')
#import easygui as g
#g.msgbox('ddd')
#http://bbs.fishc.com/thread-46069-1-1.html
#=====================================================================================

#=====================================================================================
#面向对象
#class Turtle:     #python中类名约定以大写字母开头
#class A(B)      #定义一个继承B 的 A
    #属性
    #lenth = 10
    #方法
    #def fun(self):
    #   print(lenth)
#t = Turtle()    #创建对象
#调用方法跟java差不多

#self
#相当于this指针
#def fun(self)

#__init__(self)   #构造方法
# class Ball:
#     def __init__(self,name):
#         self.name = name
#     def kick(self):
#         print(self.name)
# b = Ball('wang')
# b.kick()

#公有/私有   #默认公有，前面加__改为私有 namemangling
# class Ball:
#     __name = 'wzy'
#     def getName(self):
#         return self.__name
# b = Ball()
# #b.__name()   #报错.name也报错
# print(b.getName())

#继承
# class B:
#     def fun_b(self):
#         print('B')
# class A(B):     #A继承B
#     def fun_b(self):
#         print('A')
# b = B()
# b.fun_b()
# a = A()
# a.fun_b()     #子类中定义与父类方法重名，会覆盖

#super
# class Fish():
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#     def move(self):
#         self.x -= 1
#         self.y += 1
#         print(self.x, self.y)
# class Goldfish(Fish):
#     pass
# class Shark(Fish):
#     def __init__(self):     #重写init方法
#         #Fish.__init__(self)   #1.调用未绑定的父类方法
#         super().__init__()     #2.使用super，自动查找基类中对应的方法。以后修改父类的时候省事
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print('hungry')
#         else:
#             print('ok')
# f = Fish()
# f.move()
# s = Shark()
# s.eat()
# s.move()

#多重继承   尽量少用，容易产生不可预见的bug
# class Person():
#     def __init__(self):
#         self.name = 'www'
#     def speak(self):
#         print(self.name)
# class Student():
#     def study(self):
#         print('study')
# class Wzy(Person,Student):
#     pass
# wzy = Wzy()
# wzy.speak()
# wzy.study()

#组合
# class Date:
#     def __init__(self,year,mon,day):
#         self.year=year
#         self.mon=mon
#         self.day=day
#
#     def birth_info(self):
#         print("The birth is %s-%s-%s"%(self.year,self.mon,self.day))
# class People:
#     def __init__(self,name,age,year,mon,day):
#         self.name=name
#         self.age=age
#         self.birth=Date(year,mon,day)
#     def walk(self):
#         print("%s is walking"%self.name)
# class Teacher(People):
#     def __init__(self,name,age,year,mon,day,course):
#         People.__init__(self,name,age,year,mon,day)
#         self.course=course
#     def teach(self):
#         print("%s is teaching"%self.name)
# class Student(People):
#     def __init__(self,name,age,year,mon,day,group):
#         People.__init__(self,name,age,year,mon,day)
#         self.group=group
#     def study(self):
#         print("%s is studying"%self.name)
# t1=Teacher("alex",28,1989,9,2,"python")
# s1=Student("jack",22,1995,2,8,"group2")
# t1.teach()
# t1.walk()
# print(t1.name)
# t1.birth.birth_info()

#mixin

#类，类对象，实例对象
# class C:
#     count = 0
# a = C()
# b = C()
#
# print(a.count)
# print(b.count)
# a.count += 10
# C.count += 100

#issubclass(class,classinfo) 检查class是不是classinfo的子类，classinfo可以是元组和本身
#isinstance(object,classinfo) 检查对象object是不是classinfo的对象，。。。
#hasattr(object,'name') 测试对象里是否有指定的属性，注意‘’
#getattr(object,'name'[,default])  返回对象指定的属性值，如果不存在返回指定的default
#setattr(objext,'name',value)  设定指定属性的值，若不存在，则新建
#delattr(object,’name‘) 删除指定属性的值
#property(fget = None, fset = None, fdel = None, doc = None)  通过属性设置属性

#=====================================================================================

#=====================================================================================
#魔法方法
#__new__(cla[,.....])  实例化对象第一个执行的魔法方法。一般不会修改，当继承不可变类型需要修改时
# class CapStr(str):     #继承string类
#     def __new__(cls, string):   #需要在调用之前先修改new
#         string = string.upper()
#         return str.__new__(cls,string)   #返回基类的方法
# a = CapStr('fsfsfsdf')
# print(a)

#__init__(self[,...])  相当于构造方法  只能返回None

#__def__(self)   辣鸡回收机制   不是发生del的时候调用，而是指向这个对象的引用都释放了，就调用

#各种算数运算  q

#简单定制  计时器
#time模块详解
#time.localtime返回struct_time的时间格式
#重写__str__he 和 __repr__

# import time as t
# class MyTimer():
#     def __init__(self):
#         self.unit = ['年', '月', '天', '小时',  '分钟', '秒']
#         self.prompt = '未开始计时！'
#         self.begin = 0
#         self.end = 0
#         self.lasted = []
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#     def __add__(self, other):
#         prompt = '总共运行了'
#         result = []
#         for index in range(6):
#             result.append(self.lasted[index] + other.lasted[index])
#             if result[index]:
#                 prompt += (str(result[index]) + self.unit[index])
#         return prompt
#     #开始计时
#     def start(self):
#         self.begin = t.localtime()
#         self.prompt = "请先停止计时!"
#         print('开始计时。。。')
#     #停止计时
#     def stop(self):
#         if not self.begin:
#             print('请开始计时!')
#         else:
#             self.end = t.localtime()
#             self._calc()
#             print('计时结束。。。')
#     #内部方法计算运行时间
#     def _calc(self):
#         self.lasted = []
#         self.prompt = "总共运行了"
#         for index in range(6):
#             self.lasted.append(self.end[index] - self.begin[index])
#             if self.lasted[index]:
#                 self.prompt += (str(self.lasted[index]) + self.unit[index])
#         #print(self.prompt)
#         self.begin = 0
#         self.end = 0
# t1 = MyTimer()
# t1.start()
# t1.stop()
# print(t1)

#属性访问
#1.对象名.方法名
#2.property   #property(fget = None, fset = None, fdel = None, doc = None)  通过属性设置属性
#__getattribute__  __getattr__   __setattr__   __delattr__   按调用顺序排序   注意避免死循环
# class Retangle:
#     def __init__(self, width = 0, height = 0):
#         self.width = width
#         self.height = height
#     def __setattr__(self, name, value):   #赋值触发
#         if name == 'square':
#             self.width = value
#             self.height = value
#         else:
#             super().__setattr__(name, value)   #self.__dict__[name] = value
#     def getArea(self):
#         return self.width * self.height
# r1 = Retangle(4,5)
# print(r1.getArea())
# r1.square = 10
# print(r1.getArea())
# print(r1.__dict__)    #将对象的属性以字典序的形式输出


#描述符  将某种特殊类型的类的实例指派给另一个类的属性
#特殊类型  __get__  __set__  __delete__
# class MyDecriptor:
#     #def 各种方法
# class Test:
#     x = MyDecriptor()
# test = Test()
# test.x

#定制容器
#协议  大概相当于接口  要求没那么严格
#定制容器类型的协议
    #定制的容器不可变  __len()__  __getitem()__
    #可变 除了__len()__  __getitem()__  还要__setitem()__   __delitem()__
# class CountList:
#     def __init__(self, *args):   #*args 传入的参数是可变数量的
#         self.values = [x for x in args]   #列表推导式
#         self.count = {}.fromkeys(range(len(self.values)),0)
#     def __len__(self):
#         return len(self.values)
#     def __getitem__(self, key):
#         self.count[key] += 1
#         return self.values[key]
# c = CountList(1,3,5,7,9)
# c1 = CountList(2,4,6,8,10)
# print(c[1])
# print(c1[2])
# print(c.count)
# print(c1.count)

#迭代器
#iter()
#next()
# string = 'wang'
# it = iter(string)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# #print(next(it))   #报错StopIteration
# # for each in string
# #     print(each)
# __iter()__
# __next()__

#生成器 yield
# def myGen():
#     print('12')
#     yield 1
#     yield 2
# m = myGen()
# print(next(m))
# print(next(m))
# #print(next(m))  #StopIteration

#列表推导式  字典推导式  集合推导式   生成器推导式

#if __name__ == '__main__'

#=====================================================================================






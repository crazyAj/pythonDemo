# Python 基础

[TOC]

## 一、简介特点
### 1、简介

    Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
    
    Python 是交互式语言： 这意味着，您可以在一个 Python 提示符 >>> 后直接执行代码。
    
    Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
    
    Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

### 2、特点

    1）易于学习：Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。

    2）易于阅读：Python代码定义的更清晰。
    
    3）易于维护：Python的成功在于它的源代码是相当容易维护的。
    
    4）一个广泛的标准库：Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和Macintosh兼容很好。
    
    5）互动模式：互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。
    
    6）可移植：基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。
    
    7）可扩展：如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。
    
    8）数据库：Python提供所有主要的商业数据库的接口。
    
    9）GUI编程：Python支持GUI可以创建和移植到许多系统调用。
    
    10）可嵌入: 你可以将Python嵌入到C/C++程序，让你的程序的用户获得"脚本化"的能力。
    

## 二、环境搭建

### 1、下载

    Python官网：https://www.python.org/
    Python文档下载地址：https://www.python.org/doc/

### 2、安装
#### 1）Unix & Linux  

	打开 WEB 浏览器访问 https://www.python.org/downloads/source/ 选择适用于Unix/Linux 的源码压缩包。
	下载及解压压缩包。
	如果你需要自定义一些选项修改Modules/Setup
	执行 ./configure 脚本
	make
	make install

#### 2）Window  

	打开 WEB 浏览器访问 https://www.python.org/downloads/windows/ 在下载列表中选择Window平台安装包，包格式为：python-XYZ.msi 文件 ， XYZ 为你要安装的版本号。
	下载后，双击下载包，进入 Python 安装向导，安装非常简单，你只需要使用默认的设置一直点击"下一步"直到安装完成即可。

#### 3）MAC

	MAC 系统一般都自带有 Python2.x版本 的环境，你也可以在链接 https://www.python.org/downloads/mac-osx/ 下载最新版安装。

### 3、环境变量配置

#### 1）Unix & Linux 

	在 csh shell: 输入
	setenv PATH "$PATH:/usr/local/bin/python", 按下      "Enter"。

	在 bash shell (Linux): 输入
	export PATH="$PATH:/usr/local/bin/python" ，按下      "Enter"。

	在 sh 或者 ksh shell: 输入
	PATH="$PATH:/usr/local/bin/python" , 按下"Enter"。
	注意: /usr/local/bin/python 是 Python 的安装目录。

#### 2）Windows

	在命令提示框中(cmd) : 输入
	path=%path%;C:\Python , 按下"Enter"。
	注意: C:\Python 是Python的安装目录。

	在"Path"行，添加python安装路径即可(我的  D:\Python32)

### 4、运行

	python Xxx
		   Python命令行参数：
		   -d			在解析时显示调试信息
		   -O			生成优化代码 ( .pyo 文件 )
		   -S			启动时不引入查找Python路径的位置
		   -V			输出Python版本号
		   -X			从 1.6版本之后基于内建的异常（仅仅用于字符串）已过时。
		   -c cmd		执行 Python 脚本，并将运行结果作为 cmd 字符串。
		   file			在给定的python文件执行python脚本。


## 三、基础知识

### 1、编码

	如果你输出中文字符 "你好，世界" 就有可能会碰到中文编码问题。
	解决方法:
	1)在文件开头加入 # -*- coding: UTF-8 -*-
	2)在文件开头加入 # coding=utf-8
	注意：# coding=utf-8 的 = 号两边不要空格。

### 2、语法

#### 1）交互式编程

    Window/linux 在命令行中输入 Python 命令即可启动交互式编程

#### 2）脚本式编程

    Python 文件将以 .py 为扩展名
    
    设置了 Python 解释器 PATH 变量。使用 python test.py
    
    Python 解释器在/usr/bin目录中，使用以下命令执行脚本：
    # 脚本文件添加可执行权限
    chmod +x test.py
    ./test.py

### 3、标识符

#### 1）在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。

#### 2）Python 中的标识符是区分大小写的。

#### 3）以下划线开头的标识符是有特殊意义的。

    以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。

#### 4）以双下划线开头的 __foo 代表类的私有成员

    以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。

#### 5）Python 可以同一行显示多条语句，方法是用分号 ; 分开

### 4、保留字

```python
保留字不能用作常数或变数，或任何其他标识符名称。
and			exec			not
assert			finally			or
break			for			pass
class			from			print
continue		global			raise
def			if			return
del			import			try
elif			in			while
else			is			with
except			lambda			yield
```

### 5、行和缩进

	Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。
	python 最具特色的就是用缩进来写模块。
	缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

### 6、多行语句

	Python语句中一般以新行作为语句的结束符。
	使用斜杠（ \）将一行的语句分为多行显示

	s = 'a' + \
		'b'

	语句中包含 [], {} 或 () 括号就不需要使用多行连接符
	days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

### 7、引号

	Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的

	word = 'word'
	sentence = "这是一个句子。"
	paragraph = """这是一个段落。
	包含了多个语句"""

### 8、注释

```python
python中单行注释采用 # 开头。
python 中多行注释使用三个单引号(''')或三个双引号(""")。

# 第一个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```

### 9、空行

	函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

	空行与代码缩进不同，空行并不是Python语法的一部分。

	书写时不插入空行，Python解释器运行也不会出错。
	但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

	记住：空行也是程序代码的一部分。

### 10、等待用户输入

```python
input("按下 enter 键退出，其他任意键显示")
```

### 11、同一行显示多条语句

```python
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

### 12、print 输出

```python
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,

t = '1'; t2 = '2'; print(t, t2)
```

### 13、命令行参数

	执行一些操作来查看一些基本信息，Python 可以使用 -h 参数查看各参数帮助信息
	python -h

### 14、变量类型

#### 1）变量赋值

    等号（=）用来给变量赋值

#### 2）多个变量赋值

```python
Python允许你同时为多个变量赋值
a = b = c = 1

也可以为多个对象指定多个变量
a, b, c = 1, 2, "john"
```
#### 3）标准数据类型
    
Python有五个标准的数据类型
> Numbers（数字）  
> String（字符串）  
> List（列表）  
> Tuple（元组）  
> Dictionary（字典）

##### a）Numbers（数字）

```python
Number对象创建
var1 = 1

del语句删除对象的引用
del var1[,var2[,var3[....,varN]]]]

Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数 a + bj,或者 complex(a,b)）
```

##### b）String（字符串）

> 字符串或串(String)是由数字、字母、下划线组成的一串字符  
> s="a1a2···an"(n>=0)

```python
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头

截取字符串 [头下标:尾下标]
s = 'abcdef'
s[1:5]
'bcde'

加号（+）是字符串连接运算符，星号（*）是重复操作
str = 'Hello World!'
print str   			# 输出完整字符串
print str[0]			# 输出字符串中的第一个字符
print str[2:5]  		# 输出字符串中第三个至第六个之间的字符串
print str[2:]   		# 输出从第三个字符开始的字符串
print str * 2   		# 输出字符串两次
print str + "TEST"  		# 输出连接的字符串
>>> Hello World!
>>> H
>>> llo
>>> llo World!
>>> Hello World!Hello World!
>>> Hello World!TEST

列表截取可以接收第三个参数，参数作用是截取的步长（间隔一个位置）来截取字符串
letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
print(letters[1:4:2])
>>> ['h', 'c']
```    

##### c）List（列表）

> 列表用 [ ] 标识，是 python 最通用的复合数据类型。  
> 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，下标可以为空表示取到头或尾。

```python
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list   			# 输出完整列表
print list[0]			# 输出列表的第一个元素
print list[1:3]  		# 输出第二个至第三个元素
print list[2:]   		# 输出从第三个开始至列表末尾的所有元素
print tinylist * 2   		# 输出列表两次
print list + tinylist		# 打印组合的列表
>>> ['runoob', 786, 2.23, 'john', 70.2]
>>> runoob
>>> [786, 2.23]
>>> [2.23, 'john', 70.2]
>>> [123, 'john', 123, 'john']
>>> ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
```

##### d）Tuple（元组）

> 似于 List（列表）。  
> 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

```python
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组
>>> ('runoob', 786, 2.23, 'john', 70.2)
>>> runoob
>>> (786, 2.23)
>>> (2.23, 'john', 70.2)
>>> (123, 'john', 123, 'john')
>>> ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')  
```

##### e）Dictionary（字典）

> 列表是有序的对象集合，字典是无序的对象集合。  
> 字典当中的元素是通过键来存取的，而不是通过偏移存取。  
> 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

```python
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
>>> This is one
>>> This is two
>>> {'dept': 'sales', 'code': 6734, 'name': 'runoob'}
>>> ['dept', 'code', 'name']
>>> ['sales', 6734, 'runoob']

t = {'a': {'b': 2}}
print(t['a']['b']) >>> 2
```

#### 3）数据类型转换

```python
以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
int(x [,base]) 					将x转换为一个整数
long(x [,base] ) 				将x转换为一个长整数
float(x) 					将x转换到一个浮点数
complex(real [,imag]) 				创建一个复数
str(x) 						将对象 x 转换为字符串
repr(x) 					将对象 x 转换为表达式字符串
eval(str) 					用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s) 					将序列 s 转换为一个元组
list(s) 					将序列 s 转换为一个列表
set(s) 						转换为可变集合，无序不重复元素集
dict(d) 					创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) 					转换为不可变集合
chr(x) 						将一个整数转换为一个字符
unichr(x) 					将一个整数转换为Unicode字符
ord(x) 						将一个字符转换为它的整数值
hex(x) 						将一个整数转换为一个十六进制字符串
oct(x) 						将一个整数转换为一个八进制字符串

--- repr / eval ----
a = 20
b = a * 4 / 2
print(eval(repr(b)))

c = "a * 4 / 2"
print(eval(str(c)))

--- set ------------
x = set('runoob')
y = set('google')
print(x, y)
# 交集
print(x & y)
# 并集
print(x | y)
# 差集
print(x - y)
>>> {'r', 'u', 'o', 'n', 'b'} {'g', 'e', 'l', 'o'}
>>> {'o'}
>>> {'r', 'u', 'o', 'n', 'b', 'l', 'g', 'e'}
>>> {'n', 'r', 'b', 'u'}

--- dict -----------
# 传入关键字
print(dict(a='11', b=2))
# 可迭代对象方式来构造字典
print(dict([('a', '11'), ('b', 2)]))
# 映射函数方式来构造字典
print(dict(zip(['a', 'b'], ['11', 2])))
```

### 15、运算符

#### 1）算术运算符

```python
+		加 - 两个对象相加			a + b 输出结果 30
-		减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
*		乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
/		除 - x除以y				b / a 输出结果 2
%		取模 - 返回除法的余数			b % a 输出结果 0
**		幂 - 返回x的y次幂
//		取整除 - 返回商的整数部分（向下取整）	9//2 >>> 4	-9//2 >>> -5
```

#### 2）比较运算符

```python
==		等于 - 比较对象是否相等
!=		不等于 - 比较两个对象是否不相等
<>		不等于 - 比较两个对象是否不相等。python3 已废弃。这个运算符类似 !=
>		大于 - 返回x是否大于y
<		小于 - 返回x是否小于y
>=		大于等于 - 返回x是否大于等于y
<=		小于等于 - 返回x是否小于等于y

比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价
```

#### 3）赋值运算符

```python
=		简单的赋值运算符		c = a + b 将 a + b 的运算结果赋值为 c
+=		加法赋值运算符		c += a 等效于 c = c + a
-=		减法赋值运算符		c -= a 等效于 c = c - a
*=		乘法赋值运算符		c *= a 等效于 c = c * a
/=		除法赋值运算符		c /= a 等效于 c = c / a
%=		取模赋值运算符		c %= a 等效于 c = c % a
**=		幂赋值运算符		c **= a 等效于 c = c ** a
//=		取整除赋值运算符		c //= a 等效于 c = c // a
```

#### 4）位运算符

```python
&		按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|		按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
^		按位异或运算符：当两对应的二进位相异时
~		按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
<<		左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
>>		右移动运算符：把">>"左边的运算数的各二进位全部右移若干位
```

#### 5）逻辑运算符

```python
and		x and y，布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
or		x or y，布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值
not		not x，布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True
```

#### 6）成员运算符

```python
in		如果在指定的序列中找到值返回 True，否则返回 False
not in		如果在指定的序列中没有找到值返回 True，否则返回 False
```

#### 7）身份运算符

```python
is		is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

is not		is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
注： id() 函数用于获取对象内存地址。
```

#### 8）运算符优先级
	
```python
**						指数 (最高优先级)
~ + -						按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //					乘，除，取模和取整除
+ -						加法减法
>> <<						右移，左移运算符
&						位 'AND'
^ |						位运算符
<= < > >=					比较运算符
<> == !=					等于运算符
= %= /= //= -= += *= **=			赋值运算符
is is not					身份运算符
in not in					成员运算符
not and or					逻辑运算符
```

### 16、逻辑语句

#### 1）条件语句 - if 语句

```python
语法：
if 判断条件：
	执行语句……
elif 判断条件2:
	执行语句2……
else：
	执行语句……
```

#### 2）循环语句

##### a）while 循环语句

```python
语法：
while 判断条件(condition)：
	执行语句(statements)……

循环使用 else 语句
在 python 中，while … else 在循环条件为 false 时执行 else 语句块

count = 0
while count < 5:
	print count, " is  less than 5"
	count = count + 1
else:
	print count, " is not less than 5"
```

##### b）for 循环语句

```python
语法：
for iterating_var in sequence:
	statements(s)

for letter in 'Python':     # 第一个实例，打印每个字母
	print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例，遍历列表
	print '当前水果 :', fruit


通过序列索引迭代
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
	print '当前水果 :', fruits[index]


步长
for i in range(1, 10, 2):
	print i


循环使用 else 语句
在 python 中，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
```

##### c）break 语句

```python
Python break语句，就像在C语言中，打破了最小封闭for或while循环。
```

##### d）continue 语句

```python
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
```

##### e）pass 语句

```python
Python pass 是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
```

### 17、Number(数字)

```python
Python Number 数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。


Number 对象将被创建：
var1 = 1

del语句删除单个或多个对象:
del var
del var_a, var_b
```

#### 1）math 模块、cmath 模块

```python
Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。

cmath 模块运算的是复数，math 模块运算的是数学运算。

要使用 math 或 cmath 函数必须先导入：
import math
import cmath

# 查看方法
>> dir(math)
>> dir(cmath)
```

#### 2）数学函数

```python
fabs(x)				返回数字的绝对值，如abs(-10) 返回 10
ceil(x)				返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)			如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)				返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)				返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)			返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)				如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)			返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)			返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)			返回给定参数的最小值，参数可以为序列。
modf(x)				返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)			x**y 运算后的值。
round(x [,n])			返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)				返回数字x的平方根
```

#### 3）随机数函数

```python
导包 import random

choice(seq)				从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()				随机生成下一个实数，它在[0,1)范围内。
seed([x])				改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)				将序列的所有元素随机排序
uniform(x, y)				随机生成下一个实数，它在[x,y]范围内。
```

#### 4）三角函数

```python
acos(x)			返回x的反余弦弧度值。
asin(x)			返回x的反正弦弧度值。
atan(x)			返回x的反正切弧度值。
atan2(y, x)		返回给定的 X 及 Y 坐标值的反正切值。
cos(x)			返回x的弧度的余弦值。
hypot(x, y)		返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)			返回的x弧度的正弦值。
tan(x)			返回x弧度的正切值。
degrees(x)		将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)		将角度转换为弧度
```

#### 5）数学常量

```python
pi			数学常量 pi（圆周率，一般以π来表示）
e			数学常量 e，e即自然常数（自然常数）。
```

### 18、字符串

#### 1）字符串运算符

```python
+			字符串连接
*			重复输出字符串
[]			通过索引获取字符串中字符
[ : ]			截取字符串中的一部分
in			成员运算符 - 如果字符串中包含给定的字符返回 True
not in			成员运算符 - 如果字符串中不包含给定的字符返回 True
r / R			原始字符串 - 所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。print r'\n'   >>> \n
%			格式字符串
```

#### 2）转义字符

```python
\			(在行尾时)	续行符
\\			反斜杠符号
\'			单引号
\"			双引号
\a			响铃
\b			退格(Backspace)
\e			转义
\000		空
\n			换行
\v			纵向制表符
\t			横向制表符
\r			回车
\f			换页
\oyy		八进制数，yy代表的字符，例如：\o12代表换行
\xyy		十六进制数，yy代表的字符，例如：\x0a代表换行
\other		其它的字符以普通格式输出
```

#### 3）字符串格式化

```python
将一个值插入到一个有字符串格式符 %s 的字符串中

print("My name is %s and weight is %d kg!" % ('Zara', 21))
>>>  print "My name is %s and weight is %d kg!" % ('Zara', 21)

字符串格式化符号:
%c			格式化字符及其ASCII码
%s			格式化字符串
%d			格式化整数
%u			格式化无符号整型
%o			格式化无符号八进制数
%x			格式化无符号十六进制数
%X			格式化无符号十六进制数（大写）
%f			格式化浮点数字，可指定小数点后的精度
%e			用科学计数法格式化浮点数
%E			作用同%e，用科学计数法格式化浮点数
%g			%f和%e的简写
%G			%F 和 %E 的简写
%p			用十六进制数格式化变量的地址

格式化操作符辅助指令:
*			定义宽度或者小数点精度
-			用做左对齐
+			在正数前面显示加号( + )
<sp>			在正数前面显示空格
#			在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0			显示的数字前面填充'0'而不是默认的空格
%			'%%'输出一个单一的'%'
(var)			映射变量(字典参数)
m.n.			m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
```

#### 4）Unicode 字符串

```python
u'Hello World !'
>>> u'Hello World !'

引号前小写的"u"表示这里创建的是一个 Unicode 字符串。
如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：

u'Hello\u0020World !'
>>> u'Hello World !'
```

#### 5）字符串内建函数

```python
string.capitalize()                                  把字符串的第一个字符大写
string.center(width)                                 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
string.count(str, beg=0, end=len(string))            返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.decode(encoding='UTF-8', errors='strict')     以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
string.encode(encoding='UTF-8', errors='strict')     以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
string.endswith(obj, beg=0, end=len(string))         检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.expandtabs(tabsize=8)                         把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
string.find(str, beg=0, end=len(string))             检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.format()                                      格式化字符串
string.index(str, beg=0, end=len(string))            跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.isalnum()                                     如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
string.isalpha()                                     如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
string.isdecimal()                                   如果 string 只包含十进制数字则返回 True 否则返回 False.
string.isdigit()                                     如果 string 只包含数字则返回 True 否则返回 False.
string.islower()                                     如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
string.isnumeric()                                   如果 string 中只包含数字字符，则返回 True，否则返回 False
string.isspace()                                     如果 string 中只包含空格，则返回 True，否则返回 False.
string.istitle()                                     如果 string 是标题化的(见 title())则返回 True，否则返回 False
string.isupper()                                     如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
string.join(seq)                                     以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
string.ljust(width)                                  返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.lower()                                       转换 string 中所有大写字符为小写.
string.lstrip()                                      截掉 string 左边的空格
string.maketrans(intab, outtab])                     maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)                                             返回字符串 str 中最大的字母。
min(str)                                             返回字符串 str 中最小的字母。
string.partition(str)                                有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string
string.replace(str1, str2,  num=string.count(str1))  把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
string.rfind(str, beg=0,end=len(string) )            类似于 find()函数，不过是从右边开始查找.
string.rindex( str, beg=0,end=len(string))           类似于 index()，不过是从右边开始.
string.rjust(width)                                  返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
string.rpartition(str)                               类似于 partition()函数,不过是从右边开始查找
string.rstrip()                                      删除 string 字符串末尾的空格.
string.split(str="", num=string.count(str))          以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串
string.splitlines([keepends])                        按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
string.startswith(obj, beg=0,end=len(string))        检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.strip([obj])                                  在 string 上执行 lstrip()和 rstrip()
string.swapcase()                                    翻转 string 中的大小写
string.title()                                       返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
string.translate(str, del="")                        根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
string.upper()                                       转换 string 中的小写字母为大写
string.zfill(width)                                  返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
```

### 19、列表(List)

#### 1）更新列表

```python
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print list

>>> ['Google', 'Runoob']
```

#### 2）删除列表元素

```python
list1 = ['physics', 'chemistry', 1997, 2000]
del list1[2]
print list1

>>> ['physics', 'chemistry', 2000]
```

#### 3）列表脚本操作符

```python
len([1, 2, 3])				3					长度
[1, 2, 3] + [4, 5, 6]			[1, 2, 3, 4, 5, 6]			组合
['Hi!'] * 4				['Hi!', 'Hi!', 'Hi!', 'Hi!']		重复
3 in [1, 2, 3]				True					元素是否存在于列表中
for x in [1, 2, 3]: print x,		1 2 3					迭代
```

#### 4）列表截取

```python
L = ['Google', 'Runoob', 'Taobao']
L[2]
>>> 'Taobao'
L[-2]
>>> 'Runoob'
L[1:]
>>> ['Runoob', 'Taobao']

L[2]	'Taobao'			读取列表中第三个元素
L[-2]	'Runoob'			读取列表中倒数第二个元素
L[1:]	['Runoob', 'Taobao']		从第二个元素开始截取列表
```

#### 5）列表函数

```python
cmp(list1, list2)			比较两个列表的元素
len(list)				列表元素个数
max(list)				返回列表元素最大值
min(list)				返回列表元素最小值
list(seq)				将元组转换为列表
```

#### 6）列表方法

```python
list.append(obj)				在列表末尾添加新的对象
list.count(obj)					统计某个元素在列表中出现的次数
list.extend(seq) 				在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj) 				从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 			将对象插入列表
list.pop([index=-1]) 				移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj) 				移除列表中某个值的第一个匹配项
list.reverse() 					反向列表中元素
list.sort(cmp=None, key=None, reverse=False) 	对原列表进行排序
```

### 20、元组

> 元组中只包含一个元素时，需要在元素后面添加逗号  
> tup1 = (50,)

#### 1）修改元组

```python
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print tup3
```

#### 2）修改元组

```python
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

tup = ('physics', 'chemistry', 1997, 2000)
print tup
del tup
print "After deleting tup : "
print tup

元组被删除后，输出变量会有异常信息，输出如下所示：

('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
	File "test.py", line 9, in <module>
	print tup
NameError: name 'tup' is not defined
```

#### 3）元组运算符

```python
len((1, 2, 3))				3				计算元素个数
(1, 2, 3) + (4, 5, 6)			(1, 2, 3, 4, 5, 6)		连接
('Hi!',) * 4				('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)				True				元素是否存在
for x in (1, 2, 3): print x,		1 2 3				迭代
```

#### 4）元组索引，截取

```python
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素

L = ('spam', 'Spam', 'SPAM!')
L[2]		'SPAM!'				读取第三个元素
L[-2]		'Spam'				反向读取，读取倒数第二个元素
L[1:]		('Spam', 'SPAM!')		截取元素
```

#### 5）无关闭分隔符

```python
任意无符号的对象，以逗号隔开，默认为元组

print 'abc', -4.24e93, 18+6.6j, 'xyz'
x, y = 1, 2
print "Value of x , y : ", x,y

>>> abc -4.24e+93 (18+6.6j) xyz
>>> Value of x , y : 1 2
```

#### 6）元组内置函数

```python
len(tuple) 			计算元组元素个数
max(tuple) 			返回元组中元素最大值
min(tuple) 			返回元组中元素最小值
tuple(seq) 			将列表转换为元组

cmp(tuple1, tuple2) 		比较两个元组元素,3.62废弃
3.62废弃 cmp 改为：

import operator

a = (1, 2)
b = (1, 2)
print(operator.eq(a, b))
```

### 21、字典(Dictionary)

> 如果用字典里没有的键访问数据，会输出错误  
> 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住  
> 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

#### 1） 删除字典元素

```python
能删单一的元素也能清空字典

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键是'Name'的条目
dict.clear()      # 清空字典所有条目
del dict          # 删除字典
```

#### 2）内置函数

```python
cmp(dict1, dict2) 		比较两个字典元素。
len(dict) 			计算字典元素个数，即键的总数。
str(dict) 			输出字典可打印的字符串表示。
type(variable) 			返回输入的变量类型，如果变量是字典就返回字典类型。

cmp(dict1, dict2) 		比较两个字典元素,3.62废弃
3.62废弃 cmp 改为：

import operator

a = {1, 2}
b = {1, 2}
print(operator.eq(a, b))
```

#### 3）内置方法

```python
dict.clear() 				删除字典内所有元素
dict.copy() 				返回一个字典的浅复制
dict.fromkeys(seq[, val]) 		创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
dict.get(key, default=None) 		返回指定键的值，如果值不在字典中返回default值
dict.has_key(key) 			如果键在字典dict里返回true，否则返回false
dict.items() 				以列表返回可遍历的(键, 值) 元组数组
dict.keys() 				以列表返回一个字典所有的键
dict.setdefault(key, default=None) 	和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict.update(dict2) 			把字典dict2的键/值对更新到dict里
dict.values() 				以列表返回字典中的所有值
pop(key[,default]) 			删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem() 				返回并删除字典中的最后一对键和值。
```

### 22、日期和时间

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。  
时间间隔是以秒为单位的浮点小数。  
> time.perf_counter()  
> 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。  
> time.clock在Python3.3废弃，在Python3.8中将被移除  
> 导包：  
> import time

#### 1）时间元组(struct_time元组)

```python
用一个元组装起来的9组数字处理时间
0		4位数年			2008
1		月			1 到 12
2		日			1到31
3		小时			0到23
4		分钟			0到59
5		秒			0到61 (60或61 是闰秒)
6		一周的第几日		0到6 (0是周一)
7		一年的第几日		1到366 (儒略历)
8		夏令时			-1, 0, 1, -1是决定是否为夏令时的旗帜

struct_time元组具有如下属性：
0		tm_year			2008
1		tm_mon			1 到 12
2		tm_mday			1 到 31
3		tm_hour			0 到 23
4		tm_min			0 到 59
5		tm_sec			0 到 61 (60或61 是闰秒)
6		tm_wday			0到6 (0是周一)
7		tm_yday			1 到 366(儒略历)
8		tm_isdst		-1, 0, 1, -1是决定是否为夏令时的旗帜
```

#### 2）获取当前时间

```python
从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

time.time()
浮点数的时间戳

localtime = time.localtime(time.time())
时间元组
```

#### 3）格式化的时间
```python
最简单的获取可读的时间模式的函数是asctime():

time.asctime(time.localtime())
>>> Thu Apr  7 10:05:21 2016

time.strftime(format[, t])
格式化日期

python中时间日期格式化符号：
%y	两位数的年份表示（00-99）
%Y	四位数的年份表示（000-9999）
%m	月份（01-12）
%d	月内中的一天（0-31）
%H	24小时制小时数（0-23）
%I	12小时制小时数（01-12）
%M	分钟数（00-59）
%S	秒（00-59）
%a	本地简化星期名称
%A	本地完整星期名称
%b	本地简化的月份名称
%B	本地完整的月份名称
%c	本地相应的日期表示和时间表示
%j	年内的一天（001-366）
%p	本地A.M.或P.M.的等价符
%U	一年中的星期数（00-53）星期天为星期的开始
%w	星期（0-6），星期天为星期的开始
%W	一年中的星期数（00-53）星期一为星期的开始
%x	本地相应的日期表示
%X	本地相应的时间表示
%Z	当前时区的名称
%%	%号本身
```
#### 4）解析时间

```python
time.strptime(t, format)
```

#### 5）Time 模块
```python
time.altzone 					返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
time.asctime([tupletime]) 			接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
time.perf_counter() 				用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
time.ctime([secs]) 				作用相当于asctime(localtime(secs))，未给参数相当于asctime()
time.gmtime([secs]) 				接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
time.localtime([secs]) 				接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
time.mktime(tupletime) 				接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
time.sleep(secs) 				推迟调用线程的运行，secs指秒数。
time.strftime(fmt[,tupletime]) 			接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
time.strptime(str,fmt='%a %b %d %H:%M:%S %Y') 	根据fmt的格式把一个时间字符串解析为时间元组。
time.time() 					返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
time.tzset() 					根据环境变量TZ重新初始化时间相关设置。
```

#### 6）日历（Calendar）模块
```python
导包：
import calendar

calendar.calendar(year,w=2,l=1,c=6) 		返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
calendar.firstweekday() 					返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。
calendar.isleap(year) 						是闰年返回 True，否则为 False。
calendar.leapdays(y1,y2) 					返回在Y1，Y2两年之间的闰年总数。
calendar.month(year,month,w=2,l=1) 			返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
calendar.monthcalendar(year,month) 			返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
calendar.monthrange(year,month) 			返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
calendar.prcal(year,w=2,l=1,c=6) 			相当于 print calendar.calendar(year,w=2,l=1,c=6)。
calendar.prmonth(year,month,w=2,l=1) 		相当于 print calendar.month(year,month,w=2,l=1) 。
calendar.setfirstweekday(weekday) 			设置每周的起始日期码。0（星期一）到6（星期日）。
calendar.timegm(tupletime) 					和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
calendar.weekday(year,month,day) 			返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
```

#### 7）实例
```python
import time
import calendar

t = time.perf_counter()
print(dir(time.struct_time.tm_hour))
# 时间戳
print(time.time())
# 时间元组
print(time.localtime())
print(time.localtime(time.time()))
# 时间元组 ASC显示
print(time.asctime(time.localtime()))
# 时间元组 --> 时间戳
print(time.mktime(time.localtime()))
# 格林威治(GMT)时间
print(time.gmtime())
# 时间元组 --> 字符串
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 字符串 --> 时间元组
print(time.strptime('2020-08-13 10:58:12', '%Y-%m-%d %H:%M:%S'))
print(calendar.month(2020, 8))
print(calendar.firstweekday())
t2 = time.perf_counter()
print("耗时 --> %f" % (t2 - t))
```

### 23、函数

#### 1）定义一个函数
```python
a）函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
b）任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
c）函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
d）函数内容以冒号起始，并且缩进。
e）return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
```

#### 2）函数调用

	直接方法名 + 参数，进行调用

#### 3）参数传递

##### a）可更改(mutable)与不可更改(immutable)对象

```python
不可更改的对象：strings, tuples, 和 numbers
可修改对象：list,dict


不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
```

##### b）python 函数的参数传递：
```python
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
```

#### 4）参数

	参数类型：必备参数、关键字参数、默认参数、不定长参数

##### a）必备参数

```python
必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

def printme( str ):
	"打印任何传入的字符串"
	print str
	return

#调用printme函数
printme('test')
```

##### b）关键字参数

```python
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

def printme( str ):
	"打印任何传入的字符串"
	print str
	return

#调用printme函数
printme( str = "My string")
```

##### c）默认参数

```python
调用函数时，默认参数的值如果没有传入，则被认为是默认值。

def printinfo( name, age = 35 ):
	"打印任何传入的字符串"
	print "Name: ", name
	print "Age ", age
	return

#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )
```

##### d）不定长参数

```python
一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

def printinfo( arg1, *vartuple ):
	"打印任何传入的参数"
	print "输出: "
	print arg1
	for var in vartuple:
		print var
	return

# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
```

#### 5）匿名函数

```python
使用 lambda 来创建匿名函数。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

语法：lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )

filter(lambda t: t % 2 == 0, [1, 2, 3, 4, 5])
>>> [2, 4]

map(lambda t: t ** 2, [1, 2, 3])
>>> [1, 4, 9]

# map 处理按照个数最少的来
map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
>>> [5, 7, 9]


from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
>>> 15


arr = ["54", "7365462", "8723", "9", "3"]
arr.sort(key=lambda t: len(t))
print(arr)
>>> ['9', '3', '54', '8723', '7365462']
```

#### 6）return 语句

```python
return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
```

#### 7）变量作用域

	两种最基本的变量作用域：全局变量、局部变量
	定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域

	局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

#### 8）几个内置函数或方法

##### a）列表推导式

```python
list = [item (if...else...item2) for item in iterable (if)]
if...else... 和 if 只能有一个

print([i for i in range(5)])
>>> [0, 1, 2, 3, 4]
# 输入0-5

print([i for i in range(5) if i % 2 == 0])
>>> [0, 2, 4]
# 输出偶数

print([0 if i == 0 else -1 if i % 2 == 0 else 1 for i in range(5)])
>>> [0, 1, -1, 1, -1]
# 输出：0 - 0，偶数 - -1， 奇数 - 1

print({x: y for x, y in zip(('a', 'b', 'c'), range(3)) if y % 2 == 0})
>>> {'a': 0, 'c': 2}
# 与zip的连用,注意x与y之间的逗号,和字典x与y之间的冒号
```

##### b）zip() 函数

```python
将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
利用 * 号操作符，可以将元组解压为列表。

语法：
zip([iterable, ...])


x = ['a', 'b', 'c']
y = [1, 2, 3]
z = ['a', 'b']
t = (('a', 1), ('b', 2), ('c', 3))
print(tuple(zip(x, y)))
print(tuple(zip(z, y)))
print(tuple(zip(*t)))

>>> (('a', 1), ('b', 2), ('c', 3))
>>> (('a', 1), ('b', 2))
>>> (('a', 'b', 'c'), (1, 2, 3))
```

##### c）iter() 和 next() 函数

```python
b = [1,2,3,4]
a = iter(b)
>>> next(a)会依次返回1,2,3,4，StopIteration，StopIteration...
a = iter(b,19)
>>> next(a)会依次返回1,2,3,4，19,19,19...
```

### 24、模块

> Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

#### 1）模块的引入

```python
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
```

##### a）import 语句

```python
使用 import 语句来引入模块：import module1[, module2[,... moduleN]]

模块函数调用：模块名.函数名
```

##### b）from … import 语句

```python
from 语句让你从模块中导入一个指定的部分到当前命名空间中

语法：from modname import name1[, name2[, ... nameN]]

from math import fabs
print(fabs(-0.21))
```

##### c）from … import * 语句

```python
导入一个模块中的所有项目。然而这种声明不该被过多地使用。

from math import *
```

#### 2）模块的搜索路径

```python
当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
```

#### 3）PYTHONPATH 变量

```batch
在 Windows 系统，典型的 PYTHONPATH 如下：
set PYTHONPATH=c:\python27\lib;

在 UNIX 系统，典型的 PYTHONPATH 如下：
set PYTHONPATH=/usr/local/lib/python
```

#### 4）命名空间和作用域

```python
如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。

如果要给函数内的全局变量赋值，必须使用 global 语句。

Money = 2000
def AddMoney():
	global Money
	Money = Money + 1
```

#### 5）dir()函数

```python
dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
```

#### 6）globals() 和 locals() 函数

```python
如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

def test():
	v = 2
	print(locals())
	print(globals())

k = 1
test()

>>> {'v': 2}
	{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00BE8E20>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/lenovo/Desktop/test.py', '__cached__': None, 'test': <function test at 0x00F8A388>, 'k': 1}
```

#### 7）reload() 函数

```python
当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。

语法：reload(module_name)
```

#### 8）Python中的包

```python
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

***包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包***

实例：
run.py
myPackage(包)
	|-- __init__.py
	|-- module1.py
	|-- module2.py

[ run.py ]
# from myPackage import module1, module2
# module1.test1()
# module2.test2()

from myPackage.module1 import test1
from myPackage.module2 import test2
test1()
test2()

[ __init__.py ]
if __name__ == '__main__':
	print('main program')
else:
	print('init module')

[ module1.py ]
def test1():
	print('module1.test1')

[ module2.py ]
def test2():
	print('module2.test2')


运行 run.py
>>> init module
	module1.test1
	module2.test2
```

### 25、文件I/O

#### 1）打印到屏幕 print

```python
print([object, ...], *, sep=' ', end='\n', file=sys.stdout，flush=FALSE)

print之后是默认换行的，是因为其默认属性 end 默认值为"\n"（\n为换行符）
```

#### 2）读取键盘输入 input

```python
input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）

普通输入：
	str = input("请输入：")
	print("你输入的内容是: ", str)


表达式输入：
	str = input('请输入：')
	print("内容：", eval(str))

	>>> 请输入：[x*5 for x in range(2,10,2)]
		内容： [10, 20, 30, 40]
```

#### 3）打开和关闭文件

```python
用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。

语法：
	file object = open(file_name [, access_mode][, buffering])

完整的语法格式为：
	open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

各个参数的细节如下：
	file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
	access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
	buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

参数说明:
	file: 必需，文件路径（相对或者绝对路径）。
	mode: 可选，文件打开模式
	buffering: 设置缓冲
	encoding: 一般使用utf8
	errors: 报错级别
	newline: 区分换行符
	closefd: 传入的file参数类型
	opener:


不同模式打开文件的完全列表：
	t			文本模式 (默认)。
	x			写模式，新建一个文件，如果该文件已存在则会报错。
	b			二进制模式。
	+			打开一个文件进行更新(可读可写)。
	U			通用换行模式（不推荐）。
	r			以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
	rb			以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
	r+			打开一个文件用于读写。文件指针将会放在文件的开头。
	rb+			以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
	w			打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	wb			以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
	w+			打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	wb+			以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
	a			打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	ab			以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	a+			打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
	ab+			以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
```

```flow
Opening=>start: Opening Files

RWJuggle=>condition: Read&Write
RWTJuggle=>condition: Truncate
RWTRes=>operation: w+
[Initial Position Begin]
RWPBJuggle=>condition: Begin
RWPBRes=>operation: r+
[Initial Position Begin]
RWPERes=>operation: a+
[Initial Position End]

RJuggle=>condition: Read
RRes=>operation: r
[Initial Position Begin]

WTJuggle=>condition: Truncate
WTRes=>operation: w
[Initial Position Begin]
WNTRes=>operation: a 
[Initial Position End]

Opening->RWJuggle
RWJuggle(yes)->RWTJuggle
RWTJuggle(yes)->RWTRes
RWTJuggle(no)->RWPBJuggle
RWPBJuggle(yes)->RWPBRes
RWPBJuggle(no)->RWPERes

RWJuggle(no)->RJuggle
RJuggle(yes)->RRes
RJuggle(no)->WTJuggle
WTJuggle(yes)->WTRes
WTJuggle(no)->WNTRes
```

| 模式       | r   | r+  | w   | w+  | a   | a+  |
| ---------- | --- | --- | --- | --- | --- | --- |
| 读         | +   | +   |     | +   |     | +   |
| 写         |     | +   | +   | +   | +   | +   |
| 创建       |     |     | +   | +   | +   | +   |
| 覆盖       |     |     | +   | +   |     |     |
| 指针在开始 | +   | +   | +   | +   |     |     |
| 指针在结尾 |     |     |     |     | +   | +   |

#### 4）File对象的属性

```python
file对象相关的所有属性的列表：
	file.closed			返回true如果文件已被关闭，否则返回false。
	file.mode			返回被打开文件的访问模式。
	file.name			返回文件的名称。
	file.softspace			如果用print输出后，必须跟一个空格符，则返回false。否则返回true。


file = open("./myPackage/module1.py", "r")
print("名称：%s" % file.name)
print("编码：%s" % file.encoding)
print("模式：%s" % file.mode)
print("文件关闭：%s" % file.closed)

buf = 20
res = ""
s = file.read(buf)
while s != '':
	print("指针:%s" % file.tell(), end=" ")
	res += s
	s = file.read(buf)
print("\n结果：\n%s" % res)
file.close()
print("文件关闭：%s" % file.closed)

>>> 名称：./myPackage/module1.py
>>> 编码：cp936
>>> 模式：r
>>> 文件关闭：False
>>> 指针:21 指针:40
>>> 结果：
>>> def test1():
		print('module1.test1')
>>> 文件关闭：True
```

##### a) close()

```python
File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。

语法：
	fileObject.close()
```

##### b) write()

```python
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

write()方法不会在字符串的结尾添加换行符('\n')：

语法：
	fileObject.write(string)
```

##### c) read()

```python
read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

语法：
	fileObject.read([count])
```

##### d)  file 对象常用的函数

```python
file.close() 				关闭文件。关闭后文件不能再进行读写操作。
file.flush() 				刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
file.fileno() 				返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
file.isatty() 				如果文件连接到一个终端设备返回 True，否则返回 False。
file.next() 				返回文件下一行。
file.read([size]) 			从文件读取指定的字节数，如果未给定或为负则读取所有。
file.readline([size]) 			读取整行，包括 "\n" 字符。
file.readlines([sizeint])  		读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
file.seek(offset[, whence]) 		设置文件当前位置
file.tell() 				返回文件当前位置。
file.truncate([size]) 			截取文件，截取的字节通过size指定，默认为当前文件位置。
file.write(str) 			将字符串写入文件，返回的是写入的字符长度。
file.writelines(sequence) 		向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
```

#### 5）文件定位

```python
tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。

seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
```

#### 6）重命名和删除文件

```python
导包：import os
```

##### a）重命名 rename()

```python
语法：
os.rename(current_file_name, new_file_name)
```

##### b）删除文件 remove()

```python
语法：
os.remove(file_name)
```

#### 7）Python里的目录

```python
os模块有许多方法能帮你创建，删除和更改目录。
```

##### a）创建目录 mkdir()

```python
当前目录下创建新的目录

语法：
os.mkdir("newdir")
```

##### b）切换目录 chdir()

```python
改变当前的目录

语法：
os.chdir("newdir")
```

##### c）获取目录 getcwd()

```python
显示当前的工作目录

语法：
os.getcwd()
```

##### d）删除目录 rmdir(), 删除文件 remove()/unlink()

```python
rmdir()方法删除目录，目录名称以参数传递。
在删除这个目录之前，它的所有内容应该先被清除。

remove()/unlink()方法用于删除指定路径的文件。
如果指定的路径是一个目录，将抛出OSError。

语法：
os.rmdir('dirname')
```

##### e）文件和目录遍历器 walk()

```python
语法：
os.walk(top[, topdown=True[,onerror=None[,followlinks=False]]])

参数：
top				要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)
root				当前正在遍历的这个文件夹本身的地址
dirs				返回list，内容是该文件夹中所有的目录的名字(不包括子目录)
files 				返回list，内容是改文件夹中所有的文件(不包括子目录)
topdown 			可选，为True，则优先遍历top目录，否则优先遍历top的子目录(默认为开启)
onrror 				可选，需要一个callable对象，当walk异常时，会调用
followlinks 			可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。

实例1：
import  os
for p, dirs, files in os.walk(root):
	print("\n" + p)
	print(dirs)
	print(files)
	print()


实例2：
import  os
#os.walk遍历目录后，删除文件和目录
def rmDirAndFile(path):
	#先把各个目录的文件删除完
	for root, dirs, files  in os.walk(path):
		for file in files:
			filepath = os.path.join(root, file)
			try:
				os.remove(filepath)
				print("删除文件%s成功" % file)
			except:
				print("删除文件%s异常" % file)

	#再去删除空目录
	for root, dirs, files in os.walk(path):
		for dir in dirs:
			dirpath = os.path.join(root,dir)
			try:
				os.rmdir(dirpath)
				print("删除文件夹%s成功" % dirpath)
			except:
				print("删除文件夹%s异常" % dirpath)
				import  traceback
				print(traceback.format_exc())

rmDirAndFile(r"D:\rpa_learn\good98\good99")
```

#### 8）shutil文件操作模块

```python
shutil是一种高层次的文件操作工具
类似于高级API，而且主要强大之处在于其对文件的复制与删除操作更是比较支持好。
```

##### a）使用方法

```python
复制：
	copyfile(src, dst) 			从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
	copymode(src, dst) 			只是会复制其权限其他的东西是不会被复制的
	copystat(src, dst) 			复制权限、最后访问时间、最后修改时间
	copy(src, dst) 				复制一个文件到一个文件或一个目录
	copy2(src, dst) 			在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
	move(src, dst)				如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
	copytree(olddir,newdir,True/Flase) 	把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
	copyfileobj(fsrc, fdst[, length])	将文件内容拷贝到另一个文件中

强制删除文件夹：
	shutil.rmtree('要清空的文件夹名')

移动/重命名：
	shutil.move('原文件夹/原文件名','目标文件夹/目标文件名')
```

##### b）案例

```python
import shutil

# 将文件内容拷贝到另一个文件中
shutil.copyfileobj(open('old.txt', 'r'), open('new.txt', 'w'))
# 拷贝文件
shutil.copyfile('old.txt', 'old1.txt')
# 仅拷贝权限。内容、组、用户均不变
shutil.copymode('old.txt', 'old1.txt')
# 复制权限、最后访问时间、最后修改时间
shutil.copystat('old.txt', 'old1.txt')
# 复制一个文件到一个文件或一个目录
shutil.copy('old.txt', 'old2.txt')
# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了
shutil.copy2('old.txt', 'old2.txt')
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.copytree('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb')
# 移动目录或文件
shutil.move('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb') # 把aaa目录移动到bbb目录下
# 删除一个目录
shutil.rmtree('C:/Users/xiaoxinsoso/Desktop/bbb') # 删除bbb目录
```

### 26、异常处理

```python
python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。
异常处理 / 断言(Assertions)
```

#### 1）标准异常

```python
BaseException			所有异常的基类
SystemExit			解释器请求退出
KeyboardInterrupt		用户中断执行(通常是输入^C)
Exception			常规错误的基类
StopIteration			迭代器没有更多的值
GeneratorExit			生成器(generator)发生异常来通知退出
StandardError			所有的内建标准异常的基类
ArithmeticError			所有数值计算错误的基类
FloatingPointError		浮点计算错误
OverflowError			数值运算超出最大限制
ZeroDivisionError		除(或取模)零 (所有数据类型)
AssertionError			断言语句失败
AttributeError			对象没有这个属性
EOFError			没有内建输入,到达EOF 标记
EnvironmentError		操作系统错误的基类
IOError				输入/输出操作失败
OSError				操作系统错误
WindowsError			系统调用失败
ImportError			导入模块/对象失败
LookupError			无效数据查询的基类
IndexError			序列中没有此索引(index)
KeyError			映射中没有这个键
MemoryError			内存溢出错误(对于Python 解释器不是致命的
NameError			未声明/初始化对象 (没有属性)
UnboundLocalError		访问未初始化的本地变量
ReferenceError			弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError			一般的运行时错误
NotImplementedError		尚未实现的方法
SyntaxError			Python 语法错误
IndentationError		缩进错误
TabError			Tab 和空格混用
SystemError			一般的解释器系统错误
TypeError			对类型无效的操作
ValueError			传入无效的参数
UnicodeError			Unicode 相关的错误
UnicodeDecodeError		Unicode 解码时的错误
UnicodeEncodeError		Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning				警告的基类
DeprecationWarning		关于被弃用的特征的警告
FutureWarning			关于构造将来语义会有改变的警告
OverflowWarning			旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning			可疑的运行时行为(runtime behavior)的警告
SyntaxWarning			可疑的语法的警告
UserWarning			用户代码生成的警告
```

#### 2）异常处理

##### a）try....except...else

```python
语法：
try:
	<语句>        #运行别的代码
except <名字>：
	<语句>        #如果在try部份引发了'name'异常
except <名字>  as <参数>:
	<语句>        #如果引发了'name'异常，获得附加的数据
else:
	<语句>        #如果没有异常发生
```

##### b）不带任何异常类型使用except， 发生异常执行

##### c）使用相同的except语句来处理多个异常信息：

```python
try:
	正常的操作
	......................
except(Exception1[, Exception2[,...ExceptionN]]]):
	发生以上多个异常中的一个，执行这块代码
	......................
else:
	如果没有异常执行这块代码
```

##### d）案例

```python
try:
	with open(r"b", "r") as fi:
		fi.write("aaa")
except ZeroDivisionError as e:
	print("除0异常")
	print(e)
except IOError as e:
	print("文件不存在")
	print(e)
except Exception as e:  # 等价于 except:
	print("通用异常")
	print(e)
else:
	print("无异常")
finally:
	print("最后执行")


等价于：
try:
	with open(r"b", "r") as fi:
		fi.write("aaa")
except (ZeroDivisionError, IOError, Exception) as e:
	print("文件不存在")
	print(e)
else:
	print("无异常")
finally:
	print("最后执行")
```

##### e）预定义的清理行为

```python
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

资源清理：
with open(r"b","r") as fi:
		fi.write("aaa")


操作多个文件:
__encoding = "utf-8"
path = "D:\\python-project\\"
with open(path + "2.txt", "a", encoding=__encoding) as w, open(path + "1.txt", "r", encoding=__encoding) as r:
	for line in r:
		w.write(line)
```


#### 3）触发异常

```python
使用raise语句自己触发异常

语法：
	raise [Exception [, args [, traceback]]]

参数：
	语句中 Exception 是异常的类型（例如，NameError）参数标准异常中任一种，args 是自已提供的异常参数。
	最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。


案例：
	try:
		raise (Exception("截断异常"))
	except:
		print("通用异常")
	else:
		print("无异常")
	finally:
		print("最后执行")
```

#### 4）用户自定义异常

```python
通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。


与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。
在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例。

class MyError(RuntimeError):
	def __init___(self, message):
		self.message = message


try:
	raise MyError("Test def-Exception")
except MyError as e:
	print(e)
```

### 27、OS 文件/目录方法

```python
os 模块提供了非常丰富的方法用来处理文件和目录。

os.access(path, mode)				检验权限模式
os.chdir(path)					改变当前工作目录
os.chflags(path, flags)				设置路径的标记为数字标记。
os.chmod(path, mode)				更改权限
os.chown(path, uid, gid)			更改文件所有者
os.chroot(path)					改变当前进程的根目录
os.close(fd)					关闭文件描述符 fd
os.closerange(fd_low, fd_high)			关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
os.dup(fd)					复制文件描述符 fd
os.dup2(fd, fd2)				将一个文件描述符 fd 复制到另一个 fd2
os.fchdir(fd)					通过文件描述符改变当前工作目录
os.fchmod(fd, mode)				改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
os.fchown(fd, uid, gid)				修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
os.fdatasync(fd)				强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
os.fdopen(fd[, mode[, bufsize]])		通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
os.fpathconf(fd, name)				返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
os.fstat(fd)					返回文件描述符fd的状态，像stat()。
os.fstatvfs(fd)					返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
os.fsync(fd)					强制将文件描述符为fd的文件写入硬盘。
os.ftruncate(fd, length)			裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
os.getcwd()					返回当前工作目录
os.getcwdu()					返回一个当前工作目录的Unicode对象
os.isatty(fd)					如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
os.lchflags(path, flags)			设置路径的标记为数字标记，类似 chflags()，但是没有软链接
os.lchmod(path, mode)				修改连接文件权限
os.lchown(path, uid, gid)			更改文件所有者，类似 chown，但是不追踪链接。
os.link(src, dst)				创建硬链接，名为参数 dst，指向参数 src
os.listdir(path)				返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.lseek(fd, pos, how)				设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
os.lstat(path)					像stat(),但是没有软链接
os.major(device)				从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
os.makedev(major, minor)			以major和minor设备号组成一个原始设备号
os.makedirs(path[, mode])			递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
os.minor(device)				从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
os.mkdir(path[, mode])				以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
os.mkfifo(path[, mode])				创建命名管道，mode 为数字，默认为 0666 (八进制)
os.mknod(filename[, mode=0600, device])		创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
os.open(file, flags[, mode])			打开一个文件，并且设置需要的打开选项，mode参数是可选的
os.openpty()					打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
os.pathconf(path, name)				返回相关文件的系统配置信息。
os.pipe()					创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
os.popen(command[, mode[, bufsize]])		从一个 command 打开一个管道
os.read(fd, n)					从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
os.readlink(path)				返回软链接所指向的文件
os.remove(path)					删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
os.removedirs(path)				递归删除目录。
os.rename(src, dst)				重命名文件或目录，从 src 到 dst
os.renames(old, new)				递归地对目录进行更名，也可以对文件进行更名。
os.rmdir(path)					删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
os.stat(path)					获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
os.stat_float_times([newvalue])			决定stat_result是否以float对象显示时间戳
os.statvfs(path)				获取指定路径的文件系统统计信息
os.symlink(src, dst)				创建一个软链接
os.tcgetpgrp(fd)				返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
os.tcsetpgrp(fd, pg)				设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
os.tempnam([dir[, prefix]])			返回唯一的路径名用于创建临时文件。
os.tmpfile()					返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
os.tmpnam()					为创建一个临时文件返回一个唯一的路径
os.ttyname(fd)					返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
os.unlink(path)					删除文件路径
os.utime(path, times)				返回指定的path文件的访问和修改的时间。
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])	输出在文件夹中的文件名通过在树中游走，向上或者向下。
os.write(fd, str)				写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
os.path 模块					获取文件的属性信息。
```

### 28、内置函数

```python
abs()			divmod()		input()			open()			staticmethod()
all()			enumerate()		int()			ord()			str()
any()			eval()			isinstance()		pow()			sum()
basestring()		execfile()		issubclass()		print()			super()
bin()			file()			iter()			property()		tuple()
bool()			filter()		len()			range()			type()
bytearray()		float()			list()			raw_input()		unichr()
callable()		format()		locals()		unicode()		vars()
chr()			frozenset()		long()			reload()		xrange()
classmethod()		getattr()		map()			repr()			zip()
cmp()			globals()		max()			reverse()		__import__()
compile()		hasattr()		memoryview()		round()
complex()		hash()			min()			set()
delattr()		help()			next()			setattr()
dict()			hex()			object()		slice()
dir()			id()			oct()			sorted()		exec 内置表达式

打印 ASCII
print(ord('a'))		>>> 97
print(ord('0'))		>>> 48
print(ord('A'))		>>> 65

isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。

exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
```

## 四、高级教程

### 1、面向对象

```python
类(Class)		用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量			类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员			类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写			如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量			定义在方法中的变量，只作用于当前实例的类。
实例变量			在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承			即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化			创建一个类的实例，类的具体对象。
方法			类中定义的函数。
对象
通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
```
#### 1）案例

```python
class Parant:
	"""Parant 类"""

	var = 1

	def __init__(self):
		"""初始化"""
		print("--- %s 初始化 ---" % self.__class__.__name__)

	def __del__(self):
		"""销毁"""
		print("--- %s 已销毁 ---" % self.__class__.__name__)

	def call(self, param):
		print("%s 类，var = %d" % (self.__class__.__name__, self.var))
		print("%s 类，param = %s" % (self.__class__.__name__, param))

	def callParant(self, param):
		print("%s 类，param = %s" % (self.__class__.__name__, param))


# 可以多继承， Child(Parant, Parant2)
class Child(Parant):
	"""Child 类"""

	var2 = 2

	def __init__(self):
		"""初始化"""
		print("--- %s 初始化 ---" % self.__class__.__name__)

	def __del__(self):
		"""销毁"""
		print("--- %s 已销毁 ---" % self.__class__.__name__)

	def call(self, param):
		print("%s 类，var = %d" % (self.__class__.__name__, self.var))
		print("%s 类，var2 = %d" % (self.__class__.__name__, self.var2))
		print("%s 类，param = %s" % (self.__class__.__name__, param))

	def callChild(self, param):
		print("%s 类，param = %s" % (self.__class__.__name__, param))


obj = Child()
print("%s 类 = %s " % (obj.__class__.__name__, obj.__getattribute__('var')))
print("%s 类 = %s " % (obj.__class__.__name__, obj.__getattribute__('var2')))
obj.call("call")
obj.callParant("callParant")
obj.callChild("callChild")
print("__dict__ = %s" % obj.__dict__)
print("__module__ = %s" % obj.__module__)
print("__doc__ = %s" % obj.__doc__)
print("__class__.__name__ = %s" % obj.__class__.__name__)
print("__class__.__bases__ = %s" % obj.__class__.__bases__)
print("__hash__() = %d" % obj.__hash__())
obj.__setattr__("var", -1)
print(obj.__getattribute__("var"))
obj.__delattr__("var")
print(obj.__getattribute__("var"))


>>> --- Child 初始化 ---
>>> Child 类 = 1
>>> Child 类 = 2
>>> Child 类，var = 1
>>> Child 类，var2 = 2
>>> Child 类，param = call
>>> Child 类，param = callParant
>>> Child 类，param = callChild
>>> __dict__ = {}
>>> __module__ = __main__
>>> __doc__ = Child 类
>>> __name__ = Child
>>> __bases__ = <class '__main__.Parant'>
>>> __hash__() = -2146852128
>>> -1
>>> 1
>>> --- Child 已销毁 ---
```

#### 2）单下划线、双下划线、头尾双下划线

```python
__foo__		定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

_foo		以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

__foo		双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
```

#### 3）创建实例对象

```python
实例化类似函数调用方式，并通过 __init__ 方法接收参数。

obj = Child()
```

#### 4）访问属性

```python
使用点号 . 来访问对象的属性。

obj.var
obj.var2
obj.call("call")
```

#### 5）内置类属性

```python
__dict__		类的属性（包含一个字典，由类的数据属性组成）
__doc__			类的文档字符串
__name__		类名
__module__		类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ 		类的所有父类构成元素（包含了一个由所有父类组成的元组）
__getattribute__	访问对象的属性。
__setattr__		设置一个属性。如果属性不存在，会创建一个新属性。
__delattr__		删除属性。
```

#### 6）对象销毁(垃圾回收)

```python
析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
```


#### 7）类的继承

```python
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。

通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。

语法：
	class 派生类名(基类名)

特点：
	a) 如果在子类中需要父类的构造方法就需要显式的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看： python 子类继承父类构造函数说明。
	b) 在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
	c) Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
	如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。

语法：
	class SubClassName (ParentClass1[, ParentClass2, ...])
```

#### 8）基础重载方法

```python
__init__ ( self [,args...] ) 		构造函数，简单的调用方法: obj = className(args)
__del__( self ) 			析构方法, 删除一个对象，简单的调用方法 : del obj
__repr__( self ) 			转化为供解释器读取的形式，简单的调用方法 : repr(obj)
__str__( self ) 			用于将值转化为适于人阅读的形式，简单的调用方法 : str(obj)
__cmp__ ( self, x ) 			对象比较，简单的调用方法 : cmp(obj, x)
```

### 2、正则表达式

```python
re 模块使 Python 语言拥有全部的正则表达式功能。

import re

str = "1、哈喽;123、aj;\n22、哈哈;\nasdf"

# 方法1
arr = re.split(r"\n", str, re.I | re.S)
pre = []
content = []
for ary in arr:
	line = re.findall(r"\d+、.*?;", ary, re.I | re.S)
	for res in line:
		ma = re.match(r"(\d+)、(.*);", res, re.I | re.S)
		pre.append(ma.group(1))
		content.append(ma.group(2))
print(list(zip(pre, content)))

# 方法2
print(re.findall(r"(\d+)、(.*?);", str, re.I | re.S))
```

#### 1）正则表达式修饰符 - 可选标志:

```python
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志

re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
```

#### 2）re.match 函数

```python
从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none

语法：
	re.match(pattern, string, flags=0)

参数：
	pattern		匹配的正则表达式
	string		要匹配的字符串
	flags		标志位，用于控制正则表达式的匹配方式

匹配对象方法：
	group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
	groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
```

#### 3）re.search 函数

```python
re.search 扫描整个字符串并返回第一个成功的匹配。其他同上。

语法：
	re.search(pattern, string, flags=0)
```

#### 4）re.sub 函数

```python
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。

语法：
	re.sub(pattern, repl, string, count=0, flags=0)

参数：
	pattern : 正则中的模式字符串。
	repl : 替换的字符串，也可为一个函数。
	string : 要被查找替换的原始字符串。
	count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

示例：
	import re

	# 将匹配的数字乘以 2
	def double(matched):
		value = int(matched.group('value'))
		return str(value * 2)

	s = 'A23G4HFD567'
	print(re.sub('(?P<value>\d+)', double, s))

	>>> A46G8HFD1134
```

#### 5）re.compile 函数

```python
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。当匹配成功时返回一个 Match 对象。

语法：
	re.compile(pattern[, flags])

Match 对象：
	group([group1, …]) 	获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
	start([group]) 		获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
	end([group]) 		获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
	span([group]) 		方法返回 (start(group), end(group))。
```

#### 6）re.findall 函数

```python
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

注意： match 和 search 是匹配一次 findall 匹配所有。

语法：
	findall(string[, pos[, endpos]])

参数：
	string : 待匹配的字符串。
	pos : 可选参数，指定字符串的起始位置，默认为 0。
	endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
```

#### 7）re.finditer 函数

```python
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

语法：
	re.finditer(pattern, string, flags=0)
```

#### 8）re.split 函数
 
```python
按照能够匹配的子串将字符串分割后返回列表。

语法：
	re.split(pattern, string[, maxsplit=0, flags=0])

参数：
	pattern	匹配的正则表达式
	string	要匹配的字符串。
	maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
	flags	标志位，用于控制正则表达式的匹配方式
```

#### 9）python3正则表达式的几个高级用法（分组）

##### a）自定义命名分组

```python
定义：
	(?P<自定义分组名称>正则字符串)

使用：
	group("自定义分组名称")

示例：
	str = "a11b22"
	match = re.search(r'(?P<part1>\w+\d+)(?P<part2>\w+\d+)', str, re.I | re.S)
	print(match.group("part2"))
	>>> b22

扩展：
	可以引用前面定义的内容：
	使用：
		(?P<自定义分组名称>正则字符串)(?P=自定义分组名称)

	示例：
		str = "a11b22ab"
		match = re.search(r'(?P<part1>\w+)\d+(?P<part2>\w+)\d+(?P=part1)(?P=part2)', str, re.I | re.S)
		print(match.group("part2"))
```

##### b）数字分组

```python
定义：
	(正则1)…(正则2)…(正则3)......\1…\2…\3…

示例：
	str = "a11b22ab"
	match = re.search(r'(?P<part1>\w+)\d+(?P<part2>\w+)\d+\1\2', str, re.I | re.S)
	print(match.group("part2"))
```

##### c）前置肯定分组

```python
不消耗匹配内容，而是加入后面正则表达式中，所以也称为前置不消耗分组
定义：
	(?=pattern)(?Ppattern123) 等效于 (?Ppattern1pattern123)

示例：
	#查询url是否以http://www.开头
	re.findall(r'(?=http:\/\/www\.)(?P<name>.*)','http://www.baidu.com')
	>>> ['http://www.baidu.com']
```

##### d）前置否定分组

```python
不包含开头的其余部分
定义：
	(?!pattern1)(?Ppattern123) 等效于 (?P!pattern1pattern123)

示例：
	#查询url不包含http://开头以外的其余部分
	re.findall(r'(?!http:\/\/)(?P<name>www.*)', 'http://www.baidu.com')
	>>> ['www.baidu.com']
```

##### e）后置肯定分组

```python
包含结尾的所有部分，不消耗匹配内容，而是加入前面分组中
定义：
	(?Ppattern123)(?<=pattern1) 等效于 (?Ppattern123pattern1)

示例：
	s = re.findall(r'(?P<name>\d+)(?<=\d)', '987java678abc')
	>>> ['987', '678', '891', '2345', '2454']

	s = re.findall(r'(?P<name>\D+)(?<=\D)', 'java678abc')
	>>> ['java', 'abc', 'abe', 'stu', 'dy']
```

##### f）消耗—不捕获

```python
参与匹配，不捕获，即不返回结果，不将匹配结果送给后面

定义：
	(?:pattern)

示例：
	str = '''
		s=http://www-1.baidu.com
		s=https://www-2.baidu.com
		s=ftp://www-3.baidu.com
	'''
	# 注意，下面的str后面，没有re.S，否则操作有错，对每一行进行正则匹配捕获
	re.findall(r'(?:http|https|ftp):\/\/(?P<name>.*)', str)
	>>> ['www-1.baidu.com', 'www-2.baidu.com', 'www-3.baidu.com']
```

##### g）前置—后置位置颠倒

```python
str = r'<div class="test1"><h1><span>学习大数据bigData</span></h1></div>'

# 前置肯定与后置肯定颠倒颠颠位置后，则匹配、不捕获、消耗
s1 = re.findall(r"(?<=<h1>).+?(?=</h1>)",str)
>>> ['<span>学习大数据bigData</span>']

# (?:pattern)不参与分组，但后面有分组时，则不参与消耗
s1 = re.findall(r"(?:<h1>).+?(?=</h1>)",str)
s1 = re.findall(r"(?:<h1>)(?P<id123>.+?)(?=</h1>)",str)
>>> ['<span>学习大数据bigData</span>']

# (?:pattern)不参与分组，前后有分组时，则不参与消耗
s1 = re.findall(r"(?:<h1>)(?P<id123>.+?)(?:</h1>)",str)
>>> ['<span>学习大数据bigData</span>']

# 前置发挥正常作用，前置放在后面时，匹配，不对前面消耗
s1 = re.findall(r"(?=<h1>).+?(?=</h1>)",str)
>>> ['<h1><span>学习大数据bigData</span>']

# (?:pattern)对后面无分组时，参与捕获、消耗
s1 = re.findall(r"(?:<h1>).+?(?=</h1>)",str)
>>> ['<h1><span>学习大数据bigData</span>']

# (?:pattern)对后面有分组时，消耗、但不参与捕获
s1 = re.findall(r"(?:<h1>)(.+?)(?=</h1>)",str)
>>> ['<span>学习大数据bigData</span>']
```

### 3、网络编程

#### CGI

```python
CGI(Common Gateway Interface)，通用网关接口，它是一段程序，运行在服务器上如：HTTP 服务器，提供同客户端 HTML 页面的接口。
```

#### HTTP

```python
标准库：urllib
第三方：requests

常见的媒体格式类型如下：content-type: text/html;charset:utf-8;

text/html                   HTML格式
text/plain                  纯文本格式
text/xml                    XML格式
image/gif                   gif图片格式
image/jpeg                  jpg图片格式
image/png                   png图片格式

application/xhtml+xml       XHTML格式
application/xml             XML数据格式
application/atom+xml        Atom XML聚合格式
application/json            JSON数据格式
application/pdf             pdf格式
application/msword          Word文档格式
application/octet-stream    二进制流数据（如常见的文件下载）
application/x-www-form-urlencoded   <form encType=””>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）
multipart/form-data         需要在表单中进行文件上传时，就需要使用该格式
```

#### 1）urllib

```python
urllib 是请求url连接的官方标准库，在Python2中主要为urllib和urllib2，在Python3中整合成了urllib。

共有四个模块：
1、request：主要负责构造和发起网络请求,定义了适用于在各种复杂情况下打开 URL (主要为 HTTP) 的函数和类
2、error：处理异常
3、parse：解析各种数据格式
4、robotparser：解析robot.txt文件
```
```python
导包：
	from urllib import request, parse

ps：如果导入 from urllib 没有代码提示，需要导入独立的模块。
```
```python
模块中最常用的函数：
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

请求参数：
1、url:  请求的网址
2、data：要发送到服务器的数据
3、timeout：设置网站的访问超时时间

响应参数：
1、对 HTTPResponse 类型数据进行操作
   read()，readline()，readlines()，fileno()，close() 
2、info()	返回HTTPMessage对象，表示远程服务器返回的头信息
3、getcode()	返回Http状态码。如果是http请求，200请求成功完成 ; 404网址未找到
4、geturl()	返回请求的url
```

##### a）quote()、unquote()、urlencode()

```python
quote 			将整个字符串编码
unquote 		将整个字符串解码
urlencode		将参数(key-value)编码


from urllib import quote
quote('http://www.baidu.com')
>>> 'http%3A//www.baidu.com'

from urllib import unquote
unquote('http%3A//www.baidu.com')
>>> 'http://www.baidu.com'

import urllib
urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
>>> 'eggs=2&bacon=0&spam=1'
```

##### b）urllib.request

```python
data 默认是 key=val 形式
```

###### Ⅰ）GET 请求（data不带参数）

```python
response = urllib.request.urlopen(url,data=None, [timeout, ]*)

响应参数：
1、response.info() 	查看响应对象的头信息，返回 http.client.HTTPMessage object
2、getheaders() 	返回一个list列表头信息
3、response		通过read(), readline(), readlines() 读取，但是获得的数据是二进制的所以还需要decode将其转化为字符串格式
4、getCode() 		查看请求状态码
5、geturl() 		获得请求的url
```

###### Ⅱ）POST 请求（data带参数）

```python
同 GET 请求
response = urllib.request.urlopen(url,data=data, [timeout, ]*)
```

###### Ⅲ）设置 headers 和 proxy

```python
proxy_hander = request.ProxyHandler(proxies)
opener = request.build_opener(proxy_hander)
req = request.Request(encodeUrl, headers=headers, data=bytes(json.dumps(data), __charset))
res = opener.open(req, timeout=10)
```

#### 2）requests

```python
导包：
	import requests
```
```python
各种方法：

1、GET 请求
requests.get(‘https://github.com/timeline.json’)

2、POST 请求
requests.post(“http://httpbin.org/post”)

3、PUT 请求
requests.put(“http://httpbin.org/put”)

4、DELETE 请求
requests.delete(“http://httpbin.org/delete”)

5、HEAD 请求
requests.head(“http://httpbin.org/get”)

6、OPTIONS 请求
requests.options(“http://httpbin.org/get” )
```
```python
响应的内容：
r.encoding                       #获取当前的编码
r.encoding = 'utf-8'             #设置编码
r.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
r.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。

r.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None

r.status_code                     #响应状态码
r.raw                             #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()
r.ok                              # 查看r.ok的布尔值便可以知道是否登陆成功

#*特殊方法*#
r.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
r.raise_for_status()             #失败请求(非200响应)抛出异常
```

###### a）GET 请求

```python
Ⅰ) param 参数
url = r"http://192.168.11.164:8888/spring-boot/rest/testGet"
params = {'a': '啊', 'b': '2'}
res = requests.get(url, params=params, timeout=5)
print(res.headers)
print(res.content.decode(__charset))

Ⅱ) 手动拼接 url
url = r"http://192.168.11.164:8888/spring-boot/rest/testGet"
params = {'a': '啊', 'b': '2'}
encodeParam = parse.urlencode(params)
encodeUrl = '?'.join([url, encodeParam])
res = requests.get(encodeUrl, timeout=5)
```

###### b）POST 请求

```python
url = r"http://192.168.11.164:8888/spring-boot/rest/testPost"
data = {
	'a': '嗷嗷嗷',
	'b': 'haha'
}
res = requests.post(encodeUrl, json=data, timeout=10)
```

###### c）设置 headers 和 proxy

```python
params = {'a': '啊', 'b': '2'}
encodeParam = parse.urlencode(params)
encodeUrl = '?'.join([url, encodeParam])
data = {
	'a': '嗷嗷嗷',
	'b': 'haha'
}
headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
					"AppleWebKit/537.36 (KHTML, like Gecko) "
					"Chrome/68.0.3440.106 Safari/537.36",
	"content-type": "application/json; charset=UTF-8"
}
cookies = {
	"cookieKey": "cookieVal"
}
ip_port = "192.168.84.151:8890"
proxies = {
	"http": "http://" + ip_port,
	"https": "https://" + ip_port
}
res = requests.post(encodeUrl, headers=headers, proxies=proxies, cookies=cookies, json=data, timeout=10)
print(res.headers)
print(res.content.decode(__charset))
```

#### 3）urllibe3

```python
http 连接池

导包：
	import urllib3

忽略日志忽略 python3 https 请求警告：
	在使用文件调用前，添加 urllib3.disable_warnings()
```
```python
> 使用示例

url = r"https://www.baidu.com"
try:
	# 创建一个连接池的实例
	# 1. retry: 重试重定向次数, 默认次数为3次, 如果想要关闭重定向, 但是不想关闭重试只需redirect = Flase, 如果重定向重试都关闭, retries = False
	# 2. timeout: 超时, 可以设置链接超时和读超时  timeout = urllib3.Timeout(connect=1, read=2)
	# 3. numpools: 池子的数量, 假如有10个池子, 当你访问第11个ip的时候第一个池子会被干掉, 然后建一个新的供第11个使用.一个池子是作用于同一个ip下的,
	#    即：http: // aaa.com / a 和http: // aaa.com / b是会共用一个池子的
	# 4. maxsize: 一个池子缓存的最大连接数量.没有超过最大链接数量的链接都会被保存下来.在block为false的情况下,
	#    添加的额外的链接不会被保存一般多用于多线程之下, 一般情况是设置为和线程数相等的数量, 保证每个线程都能访问一个链接.
	# 5. 还有一个参数是block, 默认为False, 如果线程数量大于池子最大链接数量.这时设置block为true, 则会阻塞线程, 因为线程会等其他线程使用完链接,
	#    如果设置为False, 则不会阻塞线程, 但是会新开一个链接.有一个弊端是, 使用完之后这个链接会关闭, 所以如果 多线程经常建立链接会影响性能, 多占用多余的资源
	timeout = urllib3.Timeout(connect=5, read=5)  # 也可以设置 timeout=10 连接和读写都是10s
	http = urllib3.PoolManager(retries=2, timeout=timeout, num_pools=20, maxsize=20, block=False)
	for i in range(1, 3):
		print("\n--- 第 " + str(i) + " 次 请求 ---")
		res = http.request(method='GET',
							url=url,
							headers={'Content-Type': 'application/json'},
							# GET 参数 (POST 无效， 需要拼接 url 参数转义)
							fields={"key": "value"},
							# POST 内容
							body=None)
		# 状态码
		print("status = ", res.status)
		# 数据
		print("data = ", res.data.decode(__charset)[0:15])
		# 响应头
		print("headers = ", json.dumps(dict(res.headers)))
except Exception as e:
	print("Urllib3 http 连接池 请求异常")
	traceback.print_exc()
```

### 4、MySQL

#### 1）mysql-connector

##### a）安装

```python
使用 pip 命令来安装 mysql-connector：
python -m pip install mysql-connector

导包
import mysql.connector
```

##### b）操作

```python
import traceback
# 导包
import mysql.connector

# 创建表
def create():
    try:
        mydb = mysql.connector.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 数据库用户名
            passwd="root",  # 数据库密码
            database="demo"
        )
        mycursor = mydb.cursor()
        mycursor.execute('''
        create table example (
        	id varchar(64) not null primary key,
        	emp_key varchar(64) null,
        	emp_val varchar(64) null
        )
        ''')
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x)
    except:
        print(traceback.format_exc())


# 查询
def selectAll():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM example")
        # fetchall() 获取所有记录
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except:
        print(traceback.format_exc())


# 插入
def insert(id, emp_key, emp_val):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        sql = "insert into example value('%s', '%s', '%s')" % (id, emp_key, emp_val)
        mycursor.execute(sql)
        mydb.commit()
    except:
        print(traceback.format_exc())


# 更新
def update(emp_key, emp_val):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        sql = "update example set emp_val = '%s' where emp_key = '%s'" % (emp_val, emp_key)
        mycursor.execute(sql)
        mydb.commit()
    except:
        print(traceback.format_exc())


# 删除
def delete(id):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        sql = "delete from example where id = '%s'" % id
        mycursor.execute(sql)
        mydb.commit()
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    create()
    insert('1', '11', '111')
    update('11', '1')
    delete('1')
    selectAll()
```

#### 2）PyMySQL

##### a）安装

```python
pip3 install PyMySQL
```

##### b）操作

```python
import traceback
# 导包
import pymysql


# 查询所有
def selectAll():
    try:
        # ip, user, password, database
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        cursor.execute("select * from example")
        index = cursor.rowcount
        print("影响数 - %s" % index)
        res = cursor.fetchall()
        print("id - emp_key - emp_val")
        for i in range(len(res)):
            print("[%s] %s - %s - %s" % (i + 1, res[i][0], res[i][1], res[i][2]))
    except:
        print(traceback.format_exc())
    finally:
        db.close()


# 查询单个
def selectOne():
    try:
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        cursor.execute("select * from example")
        res = cursor.fetchone()
        print("%s - %s - %s" % (res[0], res[1], res[2]))
    except:
        print(traceback.format_exc())
    finally:
        db.close()


# 更新
def update(emp_key, emp_val):
    if emp_key.strip() == '' or emp_val.strip() == '':
        print("参数错误")
        return

    try:
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        sql = "update example set emp_val = '%s' where emp_key = '%s'" % (emp_val, emp_key)
        print("sql = %s" % sql)
        cursor.execute(sql)
        index = cursor.rowcount
        print("影响数 - %s" % index)
        # 提交
        db.commit()
    except:
        # 回滚
        db.rollback()
        print(traceback.format_exc())
    finally:
        db.close()


# 删除
def delete(emp_key):
    if emp_key.strip() == '':
        print("参数错误")
        return

    try:
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        sql = "delete from example where emp_key = '%s'" % emp_key
        print("sql = %s" % sql)
        cursor.execute(sql)
        index = cursor.rowcount
        print("影响数 - %s" % index)
        # 提交
        db.commit()
    except:
        # 回滚
        db.rollback()
        print(traceback.format_exc())
    finally:
        db.close()


if __name__ == '__main__':
    selectOne()
    update('1', '111')
    delete('1')
    selectAll()
```


### 5、网络编程

#### 1）网络编程的一些重要模块


| 协议   | 功能用处 | 端口号 | Python 模块                |
| ------ | -------- | ------ | -------------------------- |
| HTTP   | 网页访问 | 80     | httplib, urllib, xmlrpclib |
| NNTP   | 帖子     | 119    | nntplib                    |
| FTP    | 文件传输 | 20     | ftplib, urllib             |
| SMTP   | 发送邮件 | 25     | smtplib                    |
| POP3   | 接收邮件 | 110    | poplib                     |
| IMAP4  | 获取邮件 | 143    | imaplib                    |
| Telnet | 命令行   | 23     | telnetlib                  |
| Gopher | 信息查找 | 70     | gopherlib, urllib          |

#### 2）Socket、SocketServer

##### a）简介

Python 提供了两个级别访问的网络服务：
- 低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
- 高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。
- 

##### b）使用

使用 socket() 函数来创建套接字
```python
socket.socket([family[, type[, proto]]])

参数
- family: 套接字家族可以是 AF_UNIX 或者 AF_INET
- type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
- protocol: 一般不填默认为0.
```

<h5>Socket 对象(内建)方法</h5>
<table class="reference"><thead>
<tr>
<th>函数</th>
<th>描述</th>
</tr>
</thead><tbody>
<tr>
<td colspan="2"><b>服务器端套接字</b></td>
</tr>
<tr>
<td>s.bind()</td>
<td>绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。</td>
</tr>
<tr>
<td>s.listen()</td>
<td>开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。</td>
</tr>
<tr>
<td>s.accept()</td>
<td>被动接受TCP客户端连接,(阻塞式)等待连接的到来</td>
</tr>
<tr>
<td colspan="2"><b>客户端套接字</b></td>
</tr>
<tr>
<td>s.connect()</td>
<td>主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。</td>
</tr>
<tr>
<td>s.connect_ex()</td>
<td>connect()函数的扩展版本,出错时返回出错码,而不是抛出异常</td>
</tr>
<tr>
<td colspan="2"><b>公共用途的套接字函数</b></td>
</tr>
<tr>
<td>s.recv()</td>
<td>接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。</td>
</tr>
<tr>
<td>s.send()</td>
<td>发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。</td>
</tr>
<tr>
<td>s.sendall()</td>
<td>完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。</td>
</tr>
<tr>
<td>s.recvfrom()</td>
<td>接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。</td>
</tr>
<tr>
<td>s.sendto()</td>
<td>发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。</td>
</tr>
<tr>
<td>s.close()</td>
<td>关闭套接字</td>
</tr>
<tr>
<td>s.getpeername()</td>
<td>返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。</td>
</tr>
<tr>
<td>s.getsockname()</td>
<td>返回套接字自己的地址。通常是一个元组(ipaddr,port)</td>
</tr>
<tr>
<td>s.setsockopt(level,optname,value)</td>
<td>设置给定套接字选项的值。</td>
</tr>
<tr>
<td>s.getsockopt(level,optname[.buflen])</td>
<td>返回套接字选项的值。</td>
</tr>
<tr>
<td>s.settimeout(timeout)</td>
<td>设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）</td>
</tr>
<tr>
<td>s.gettimeout()</td>
<td>返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。</td>
</tr>
<tr>
<td>s.fileno()</td>
<td>返回套接字的文件描述符。</td>
</tr>
<tr>
<td>s.setblocking(flag)</td>
<td>如果 flag 为 False，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用 recv() 没有发现任何数据，或 send() 调用无法立即发送数据，那么将引起 socket.error 异常。</td>
</tr>
<tr>
<td>s.makefile()</td>
<td>创建一个与该套接字相关连的文件</td>
</tr>
</tbody></table>

##### c）实例

服务端
```python
import socket
import time
import _thread
import traceback

dic = {}


# 建立客户端连接
def run():
    print('--- ServerSocket Start ---')
    # 创建 socket 对象
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定 ip、port
    serverSocket.bind(('192.168.11.164', 9999))
    # 设置最大连接数，超过后排队
    serverSocket.listen(5)
    while True:
        # 建立客户端连接
        conn, address = serverSocket.accept()
        # 缓存连接
        dic[address] = conn


def send():
    while True:
        print(dic)
        temp = dic.copy()
        for key in temp.keys():
            try:
                msg = "[%s] hello %s" % (time.ctime(time.time()), key)
                temp[key].send(msg.encode('utf-8'))
            except:
                dic.pop(key)
                print(traceback.format_exc())
        time.sleep(5)


# 服务端
if __name__ == '__main__':
    t1 = _thread.start_new_thread(run, ())
    t2 = _thread.start_new_thread(send, ())
    while True:
        time.sleep(10)
```

客户端
```python
import socket
import time
import traceback

# 客户端
if __name__ == '__main__':
    while True:
        try:
            print('--- ClientSocket Start ---')
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(('192.168.11.164', 9999))
            while True:
                time.sleep(1)
                # 接收小于 1024 字节的数据
                msg = clientSocket.recv(1024)
                if msg is None:
                    continue
                print('recive - %s' % msg.decode("utf-8"))
        except:
            print(traceback.format_exc())
        finally:
            clientSocket.close()
            time.sleep(5)
```


### 6、SMTP发送邮件

#### 1）简介

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

#### 2）语法

Python创建 SMTP 对象语法如下：
```python
import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

参数说明：
- host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:runoob.com，这个是可选参数。
- port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
- local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。
```

Python SMTP对象使用sendmail方法发送邮件，语法如下：
```python
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]

参数说明：
- from_addr: 邮件发送者地址。
- to_addrs: 字符串列表，邮件发送地址。
- msg: 发送消息
```

#### 3）实例

##### a）发送文本邮件

```python
import smtplib
import traceback
from email.header import Header
from email.mime.text import MIMEText

# 授权码
auth = "xxx"
sender = "yangwenjiemail@163.com"
receiver = "389130663@qq.com"


def send():
    message = MIMEText('Python 测试邮件！', 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header('Python 测试邮件！', 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.163.com', 25)
        smtpObj.login(sender, auth)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print('邮件已发送')
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    send()
```

##### b）发送HTML邮件

```python
import smtplib
import traceback
from email.header import Header
from email.mime.text import MIMEText

# 授权码
auth = "xxx"
sender = "yangwenjiemail@163.com"
receiver = "389130663@qq.com"


def send():
    html = """
        <p>测试 HTML 邮件内容</p>
        <a>https://www.baidu.com</a>
    """
    message = MIMEText(html, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header('Python 测试 HTML 邮件！', 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.163.com', 25)
        smtpObj.login(sender, auth)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print('邮件已发送')
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    send()
```

##### c）发送邮件携带附件

```python
import smtplib
import traceback
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# 授权码
auth = "xxx"
sender = "yangwenjiemail@163.com"
receiver = "389130663@qq.com"


def send():
    try:
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = Header('Python 测试附件上传！', 'utf-8')
        # 邮件正文内容
        html = """
            <p>Python 邮件发送测试...</p>
            <p><a href="http://www.baidu.com">百度</a></p>
            <p>图片演示：</p>
            <p><img src="cid:imgId"></p>
        """
        message.attach(MIMEText(html, 'html', 'utf-8'))

        # HTML 指定图片
        pic =  open(r'D:\aj\soft\wallpager\刺客丶伍陆柒.jpg', 'rb')
        attch = MIMEImage(pic.read())
        pic.close()
        # 定义图片 ID，在 HTML 文本中引用
        attch.add_header('Content-ID', '<imgId>')
        message.attach(attch)

        # 构造附件1 文本
        f1 = open(r'C:\Users\lenovo\Desktop\temp.txt', 'rb')
        att1 = MIMEApplication(f1.read())
        f1.close()
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="temp.txt"'
        att1.set_charset('utf-8')
        message.attach(att1)

        # 构造附件2 图片
        f2 = open(r'D:\aj\soft\wallpager\刺客丶伍陆柒.jpg', 'rb')
        att2 = MIMEApplication(f2.read())
        f2.close()
        att2.add_header('Content-Type', 'application/octet-stream')
        att2.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', '刺客丶伍陆柒.jpg'))
        att2.set_charset('utf-8')
        message.attach(att2)

        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.163.com', 25)
        smtpObj.login(sender, auth)
        smtpObj.sendmail(sender, receiver, message.as_string())
        smtpObj.quit()
        print('邮件已发送')
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    send()
```


### 7、多线程

#### 1）简介

Python3 线程中常用的两个模块为：
- _thread
- threading(推荐使用)
注：thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。

#### 2）线程

##### a）_thread 模块

语法:
```python
_thread.start_new_thread ( function, args[, kwargs] )

参数说明:
- function - 线程函数。
- args - 传递给线程函数的参数,他必须是个tuple类型。
- kwargs - 可选参数。
```

使用实例：
```python
import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
```

结果：
```python
Thread-1: Wed Apr  6 11:36:31 2016
Thread-1: Wed Apr  6 11:36:33 2016
Thread-2: Wed Apr  6 11:36:33 2016
Thread-1: Wed Apr  6 11:36:35 2016
Thread-1: Wed Apr  6 11:36:37 2016
Thread-2: Wed Apr  6 11:36:37 2016
Thread-1: Wed Apr  6 11:36:39 2016
Thread-2: Wed Apr  6 11:36:41 2016
Thread-2: Wed Apr  6 11:36:45 2016
Thread-2: Wed Apr  6 11:36:49 2016
```

##### b）threading  模块

```python
threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
- threading.currentThread(): 返回当前的线程变量。
- threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
- threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
- run(): 用以表示线程活动的方法。
- start():启动线程活动。
- join([time]): 等待至线程中止。这阻塞调用线程直至线程的- join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
- isAlive(): 返回线程是否活动的。
- getName(): 返回线程名。
- setName(): 设置线程名。
```

使用实例：
```python
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")
```

结果：
```python
开始线程：Thread-1
开始线程：Thread-2
Thread-1: Wed Apr  6 11:46:46 2016
Thread-1: Wed Apr  6 11:46:47 2016
Thread-2: Wed Apr  6 11:46:47 2016
Thread-1: Wed Apr  6 11:46:48 2016
Thread-1: Wed Apr  6 11:46:49 2016
Thread-2: Wed Apr  6 11:46:49 2016
Thread-1: Wed Apr  6 11:46:50 2016
退出线程：Thread-1
Thread-2: Wed Apr  6 11:46:51 2016
Thread-2: Wed Apr  6 11:46:53 2016
Thread-2: Wed Apr  6 11:46:55 2016
退出线程：Thread-2
退出主线程
```

##### c）线程同步

使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间

```python
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```

结果：
```python
开启线程： Thread-1
开启线程： Thread-2
Thread-1: Wed Apr  6 11:52:57 2016
Thread-1: Wed Apr  6 11:52:58 2016
Thread-1: Wed Apr  6 11:52:59 2016
Thread-2: Wed Apr  6 11:53:01 2016
Thread-2: Wed Apr  6 11:53:03 2016
Thread-2: Wed Apr  6 11:53:05 2016
退出主线程
```

##### d）线程优先级队列（ Queue）

Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

```python
Queue 模块中的常用方法:
- Queue.qsize() 返回队列的大小
- Queue.empty() 如果队列为空，返回True,反之False
- Queue.full() 如果队列满了，返回True,反之False
- Queue.full 与 maxsize 大小对应
- Queue.get([block[, timeout]])获取队列，timeout等待时间
- Queue.get_nowait() 相当Queue.get(False)
- Queue.put(item) 写入队列，timeout等待时间
- Queue.put_nowait(item) 相当Queue.put(item, False)
- Queue.task_done() 在完成一项工作之后，Queue.task_done() 函数向任务已经完成的队列发送一个信号
- Queue.join() 实际上意味着等到队列为空，再执行别的操作
```

使用实例：
```python
import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```

结果：
```python
开启线程：Thread-1
开启线程：Thread-2
开启线程：Thread-3
Thread-3 processing One
Thread-1 processing Two
Thread-2 processing Three
Thread-3 processing Four
Thread-1 processing Five
退出线程：Thread-3
退出线程：Thread-2
退出线程：Thread-1
退出主线程
```


### 8、XML 解析

#### 1）简介

XML数据处理最广泛使用的API主要有SAX和DOM接口。
- Simple API For XML(SAX)：注册感兴趣事件的回调函数，然后让解析器遍历文档。当你的文档较大或者内存受限时，这种方法是有用的，解析器一边从硬盘读取数据，一边解析文件，这样整个文件无需保存在内存。
- Document Object Model(DOM) API：DOM是WWW联盟推荐的API，这要求整个文件被读取到内存，按照层次形式表示XML文档的所有特征。

#### 2）使用

##### a） SAX 解析

SAX 是一种基于事件驱动的API。
利用 SAX 解析 XML 文档牵涉到两个部分: 解析器和事件处理器。
解析器负责读取 XML 文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
而事件处理器则负责对事件作出响应，对传递的 XML 数据进行处理。
1、对大型文件进行处理；
2、只需要文件的部分内容，或者只需从文件中得到特定信息。
3、想建立自己的对象模型的时候。
在 Python 中使用 sax 方式处理 xml 要先引入 xml.sax 中的 parse 函数，还有 xml.sax.handler 中的 ContentHandler。

<b>ContentHandler 类方法介绍</b>
```python
characters(content) 方法
调用时机：
- 从行开始，遇到标签之前，存在字符，content 的值为这些字符串。
- 从一个标签，遇到下一个标签之前， 存在字符，content 的值为这些字符串。
- 从一个标签，遇到行结束符之前，存在字符，content 的值为这些字符串。
- 标签可以是开始标签，也可以是结束标签。

startDocument() 方法
- 文档启动的时候调用。

endDocument() 方法
- 解析器到达文档结尾时调用。

startElement(name, attrs) 方法
- 遇到XML开始标签时调用，name 是标签的名字，attrs 是标签的属性值字典。

endElement(name) 方法
- 遇到XML结束标签时调用。
```

<b>make_parser 方法</b>
```python
创建一个新的解析器对象并返回。
xml.sax.make_parser( [parser_list] )

参数说明:
- parser_list - 可选参数，解析器列表
```

<b>parser 方法</b>
```python
创建一个 SAX 解析器并解析xml文档：
xml.sax.parse( xmlfile, contenthandler[, errorhandler])

参数说明:
- xmlfile - xml文件名
- contenthandler - 必须是一个 ContentHandler 的对象
- errorhandler - 如果指定该参数，errorhandler 必须是一个 SAX - ErrorHandler 对象
- parseString 方法
- parseString 方法创建一个 XML 解析器并解析 xml 字符串：
```

<b>parseString 方法</b>
```python
xml.sax.parseString(xmlstring, contenthandler[, errorhandler])

参数说明:
- xmlstring - xml字符串
- contenthandler - 必须是一个 ContentHandler 的对象
- errorhandler - 如果指定该参数，errorhandler 必须是一个 SAX - ErrorHandler对象
```

<b>实例：</b>
```xml
<collection shelf="New Arrivals">
<movie title="Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title="Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar">
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>
```

代码：
```python
import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # 元素开始调用
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         title = attributes["title"]
         print ("Title:", title)

   # 元素结束调用
   def endElement(self, tag):
      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "format":
         print ("Format:", self.format)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # 读取字符时调用
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader
   parser = xml.sax.make_parser()
   # 关闭命名空间
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # 重写 ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("movies.xml")
```

结果：
```python
*****Movie*****
Title: Enemy Behind
Type: War, Thriller
Format: DVD
Year: 2003
Rating: PG
Stars: 10
Description: Talk about a US-Japan war
*****Movie*****
Title: Transformers
Type: Anime, Science Fiction
Format: DVD
Year: 1989
Rating: R
Stars: 8
Description: A schientific fiction
*****Movie*****
Title: Trigun
Type: Anime, Action
Format: DVD
Rating: PG
Stars: 10
Description: Vash the Stampede!
*****Movie*****
Title: Ishtar
Type: Comedy
Format: VHS
Rating: PG
Stars: 2
Description: Viewable boredom
```

##### b） xml.dom 解析

<b>实例</b>
```python
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)
```

结果：
```python
Root element : New Arrivals
*****Movie*****
Title: Enemy Behind
Type: War, Thriller
Format: DVD
Rating: PG
Description: Talk about a US-Japan war
*****Movie*****
Title: Transformers
Type: Anime, Science Fiction
Format: DVD
Rating: R
Description: A schientific fiction
*****Movie*****
Title: Trigun
Type: Anime, Action
Format: DVD
Rating: PG
Description: Vash the Stampede!
*****Movie*****
Title: Ishtar
Type: Comedy
Format: VHS
Rating: PG
Description: Viewable boredom
```


### 9、JSON 数据解析

```python
json 模块：
- json.dumps(): 对数据进行编码。
- json.loads(): 对数据进行解码。
```

<br/>
<b>Python 编码为 JSON 类型转换对应表：</b>
<table>
<colgroup>
<col width="73%">
<col width="27%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Python</th>
<th class="head">JSON</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>dict</td>
<td>object</td>
</tr>
<tr class="row-odd"><td>list, tuple</td>
<td>array</td>
</tr>
<tr class="row-even"><td>str</td>
<td>string</td>
</tr>
<tr class="row-odd"><td>int, float, int- &amp; float-derived Enums</td>
<td>number</td>
</tr>
<tr class="row-even"><td>True</td>
<td>true</td>
</tr>
<tr class="row-odd"><td>False</td>
<td>false</td>
</tr>
<tr class="row-even"><td>None</td>
<td>null</td>
</tr>
</tbody>
</table>

<br/>
<b>JSON 解码为 Python 类型转换对应表：</b>
<table>
<colgroup>
<col width="44%">
<col width="56%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">JSON</th>
<th class="head">Python</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>object</td>
<td>dict</td>
</tr>
<tr class="row-odd"><td>array</td>
<td>list</td>
</tr>
<tr class="row-even"><td>string</td>
<td>str</td>
</tr>
<tr class="row-odd"><td>number (int)</td>
<td>int</td>
</tr>
<tr class="row-even"><td>number (real)</td>
<td>float</td>
</tr>
<tr class="row-odd"><td>true</td>
<td>True</td>
</tr>
<tr class="row-even"><td>false</td>
<td>False</td>
</tr>
<tr class="row-odd"><td>null</td>
<td>None</td>
</tr>
</tbody>
</table>

<br/>

<b>实例：</b>

```python
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

--> 结果：Python 原始数据： {'name': 'Runoob', 'no': 1, 'url': 'http://www.runoob.com'}
JSON 对象： {"name": "Runoob", "no": 1, "url": "http://www.runoob.com"}
data2['name']:  Runoob
data2['url']:  http://www.runoob.com

# 格式化 json sort_keys排序 indent缩进 separators分隔符
json.dumps(dict, sort_keys=True, indent=2, separators=(',', ':'))

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)
 
# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
```


### 10、MongoDB

#### 1）安装

```python
- 安装
python3 -m pip3 install pymongo

- 指定版本
python3 -m pip3 install pymongo==3.5.1

- 更新
python3 -m pip3 install --upgrade pymongo
```

#### 2）使用

```python
import json
from bson import ObjectId
import pymongo


# 数据库列表
def listDB(mgClient):
    print('listDB ------------')
    dbList = mgClient.list_database_names()
    for db in dbList:
        print(db)


# 创建数据库，并插入数据
def createDB(mgClient):
    print('createDB ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    dic = {"a": "2", "b": "22"}
    mycol.insert_one(dic)


# 创建数据库，并插入数据(数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建)
def findAllCollection(mgClient):
    print('findCollection ------------')
    myDB = mgClient["demo"]
    collections = myDB.list_collection_names()
    for col in collections:
        print(col)


# 查询单个
def find(mgClient):
    print('find ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    doc = mycol.find_one()
    print(doc)


# 查询 demo 库下面所有 collection a字段倒序(1 为升序，-1 为降序，默认为升序)
def findAll(mgClient):
    print('findAll ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    for doc in mycol.find().sort("a", -1):
        print(doc)


# 查询指定条件，显示特定字段
def findBy(mgClient):
    print('findBy ------------')
    myDB = mgClient["demo"]
    mycol = myDB["sites"]
    # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1（默认是1）
    # 查询结果 _id不显示 a显示 b显示
    for doc in mycol.find({}, {"_id": "0", "a": 1, "b": 1}):
        print(doc)
    # 查询结果 a不显示 其余都显示
    for doc in mycol.find({}, {"a": 0}):
        print(doc)
    # 查询结果 都显示 查询条件a=1
    for doc in mycol.find({"a": "1"}, {"a": 1, "b": 1}):
        print(doc)
    else:
        print("未找到")
    # 高级查询，查询结果 _id不显示 查询条件a>1 json格式化输出
    for doc in mycol.find({"a": {"$gt": "1"}}, {"_id": 0}):
        print(json.dumps(dict(doc), sort_keys=True, indent=2, separators=(',', ':')))
    print('------------')
    # 高级查询，查询结果 _id不显示 查询条件匹配2个长度正则 json格式化输出
    for doc in mycol.find({"b": {"$regex": "^.{2}$"}}, {"_id": 0}):
        print(json.dumps(dict(doc), sort_keys=True, indent=2, separators=(',', ':')))


# 更新
def update(mgClient):
    print('update ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.update_many({"a": "2"}, {"$set": {"b": "345"}})
    print(doc.modified_count)


# 更新 模糊查找
def updateLike(mgClient):
    print('updateLike ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.update_many({"b": {"$regex": "^.{1}$"}}, {"$set": {"b": "345"}})
    print(doc.modified_count)


# 删除
def delete(mgClient):
    print('delete ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.delete_many({"_id": ObjectId('60069fac7e7a96e21e5d7181')})
    print(doc.deleted_count)


# 删除所有
def deleteAll(mgClient):
    print('deleteAll ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    doc = mycol.delete_many({})
    print(doc.deleted_count)


# 删除 collection
def deleteCollection(mgClient):
    print('deleteCollection ------------')
    myDb = mgClient["demo"]
    mycol = myDb["sites"]
    mycol.drop()


# 删除 db
def deletDB(mgClient):
    print('deletDB ------------')
    myDb = mgClient["demo"]
    myDb.command("dropDatabase")


if __name__ == '__main__':
    mgClient = pymongo.MongoClient('mongodb://192.168.13.220:27017')
    # createDB(mgClient)
    # find(mgClient)
    # findBy(mgClient)
    # update(mgClient)
    # updateLike(mgClient)
    # delete(mgClient)
    # deleteAll(mgClient)
    # findAll(mgClient)
    # deleteCollection(mgClient)
    # findAllCollection(mgClient)
    # deletDB(mgClient)
    # listDB(mgClient)
```
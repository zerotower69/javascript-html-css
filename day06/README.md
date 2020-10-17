# day06说明

学习了差不多一个星期，发现深入下去难度越来越大，而其中一部分原因在于其它的基础还不够扎实，为了更好地学习，我不想但也不得不更改原来地计划，插入一些其它模块地内容，这些内容有：
>1.网络协议部分
>>1.1 TCP/IP协议 \
>>1.2 HTTP/HTTPS协议 \
>>1.3 邮件协议
>2.XML

---

## 1.xml说明

XML(Extensible Markup Language)

XML看起来很像HTML，但这并不是HTML,主要有以下不同：
1.xml的标签是自己定义的
2.xml用来传输数据而不是像HTML那样显示数据，渲染数据。
3.XML具有自我描述性，而HTML没有。

XML的作用有哪些？

>1.从HTML中分离数据。\
>2.不同系统之间的兼容性可能不太一样，而XML降低了这种不兼容带来的复杂性。 \
>3.

## 2.术语和英文释义

|英文简写|英文全称|汉语术语|解释|
|:----:|:----|:----:|:----:|
|DTD|Document Type Defination|文档类型定义|
|XML|Extensible Markup Language|可扩展性标记语言|

## 3.XML的结构和语法

先来看一个简单的XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<email>
<to>Lucy</to>
<from>David</from>
<heading>Birthday party</heading>
<body>I want to invite you.</body>
</email>
```

对于一个xml文件来说，其声明部分：
|属性|解释|取值|
|:----:|:----:|:----:|
|version|说明xml遵循的版本|1.0 \ 1.1|
|encoding|解析器文档采用的unicode编码|UTF-8 \ UTF-16|
|standalone|独立文档声明|yes \ no|

关于注释：
>1.注释不能在声明之前 \

```xml
<!-- this is the comments of xml -->
<?xml version="1.0" encoding="UTF-8"?>
```

>2.注释不能放在标记里
>3.注释可以包围和隐藏标记
>4.两个连字符"--"不能出现在除了注释标记以外的任何地方。
>5.注释不能以"--->"的方式结尾。

## 4.XML处理指令

> \<?target instrucions ?>

```xml
<?xml version="1.0"?>
<name nickname="Tony Bill">
    <firstname>Tony</firstname>
    <!-- Tony lost his middle name in a fire -->
    <middlename/>
    <?nameprocessor PRINT nickname?>
    <lastname>Bill</lastname>
</name>
```

## 5.标记

标记三种意义：
结构、语义和样式
>结构将文档分为结构树
>将单个的元素和外部的实际事物联系起来
>指定如何显示元素

标记分为<kbd>空标记</kbd> 和<kbd>非空标记</kbd>

\<cccc/>是`空标记`,而\<xxx>\</xxx>是`非空标记`。

## 6.元素的命名规范

在xml中，元素的命名是有要求的。

>a)元素的第一个字母必须是26个字母或者下划线"_"。
>b)其它字符可以是数字，连字符“-”和句点。
>c)名字里不能有空格。
>d)名字里不能有冒号，除非在文档中使用了命名空间。
>e)开始符号“<"后必须紧跟元素名，中间不能有空格，但是元素名和">"之间是允许的。
>f)名称大小写敏感，必须严格保证您的输入。
>g)元素名应该言简意赅。

## 7.元素的内容

1.混合内容   2.简单内容  3.空内容

## 8.字符和实体引用

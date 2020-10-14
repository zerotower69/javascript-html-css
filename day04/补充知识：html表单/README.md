# 前言

学习了js的表单验证，发现很多东西还是基于html表单上的，因此，又花了一点时间把html和html5有关的表单知识全部过了一遍。

---

## 1.html表单简要

html 表单主要是用来收集用户的输入信息，并发送到服务端。
通俗一点来说，就是我要你提交信息给我，我呢，事先规定好统一的要求，你按照要求给我信息。
实际中，每次登录、或者你学校管理系统的修改个人信息资料等等都是表单，而表单中输入的数据会有不同的类型和选型，同时，也伴随着数据格式的校验。

## 2.简单的表单展示

请参考`测试用例`的 `html表单.html`中的示例。

## 3.input标签的type属性

type属性|解释
|:-----:|:---:|
|text|文本|
|password|密码|
|radio|单选按钮|
|checkbox|复选框|
|submit|提交按钮|

具体的使用参考 `测试用例`的`type属性.html`。

## 4.一些使用的表单示例

在`测试用例`的`表单示例.html`中，你会看到：
1.带有边框的表单
2.模拟登录场景下的表单

## 5.form标签的属性

|form属性|解释|值|示例|
|:----:|:----:|:----:|:----|
|action|当提交数据时向何处传递数据|URL|\<form action="./submit.html">|
|accept|规定服务器接收的文件类型|MIME_type|
|accept-charset|规定表单处理表单数据的可用字符集|character_set|
|autocomplete|是否开启表单的自动完成功能|on<br> off|
|enctype|规定在向服务器发送表单数据之前如何对其进行编码。（适用于 method="post" 的情况）|application/x-www-form-urlencoded <br>  multipart/form-data  <br> text/plain||
|method|规定用于发送表单数据的 HTTP 方法|get<br>post||
|name|规定表单的名称|text||
|novalidate|提交表单时不进行验证|novalidate||
|target|规定在何处打开action URL|_blank<br>_self<br>_parent<br>_top||



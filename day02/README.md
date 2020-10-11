# day02 20201011

---

## 1.js的作用域

==什么是作用域？==

在js中，作用域是可访问变量、对象和函数的集合。
js的局部作用域：变量在函数内创建，变量就是局部作用域。函数外是不可以使用这个在函数内部定义的变量的，这也为不同函数有相同的变量名提供了可能。函数使用创建时变量会被创建，随着函数调用结束后而销毁。

js的全局作用域: 即变量实在函数外定义的，全局脚本可用，且一旦定义了，函数内定义新的变量时不可以再使用该名称，否则报错。

## 2.js字符串

### 2.1 字符串的引用格式

js的字符串前面已经提到，要么用单引号要么双引号，这点和python是一样的。
且和大多数语言一样的是，javascript的字符串每个字符可以被访问，使用索引的方式，索引从0开始。

```javascript
var aa="hello, javascript!";
//第一个字符从0开始
aa[0]==='h';   //注意，javascript使用的编码是unicode。
```

### 2.2 字符串的长度

你可以使用length查看字符串的长度。

```javascript
var aa="hello, world!";
va lengthOfaa= aa.length;
```

### 2.3 转义字符

为什么需要转义字符，一个简单的实例

```javascript
var aa="my name is "David"";
```

有时候字符串的内容里包含了引号，而引号本身又是字符串的定义。从示例的字母D开始，字符串已经结束了，这就破坏了我们的定义，怎么办？
转义字符。它告诉字符串执行相应的转义。

```javascript
var aa="my name is \"David\"";   //使用转义字符后，字符串才是我们需要的
//my name is "David"
```

==这里收集了一些常用的转义字符==

```javascript
\n  //换行符
\\  //输出反斜杠，因为斜杠已经用来定义转义字符。
\t //制表符
\'   '//单引号
\"   "//双引号
\b  //退格
\f  //换页符
```

### 2.4 把字符串视为对象

```javascript
var aa=new String("hello, world!");
```

一般情况下字符串创建直接给字面值，但也通过构建对象的方式。然而，官方不推荐这样做，因为这样运行的速度会比较慢。

### 2.5 字符串属性

1.constructor  返回创建字符串属性的函数
2.length 返回字符串长度。
3.prototype 允许你向字符串添加属性和方法。

### 2.6 字符串方法

## 3.js的运算符

### 3.1 算术运算符

```javascript
+ - * / %  ++ --
```

### 3.2 赋值运算符

```javascript
= += -= *= /= %=
```

### 3.3 字符串使用+号拼接

```javascript
var a1="hello, ";
var a2="world!";
var a3=a1+a2;  //a3="hello, world!";
```

### 3.4 数字和字符串混合相加

```javascript
var x=5+5;  //x=10
var y="hello"+"world!" //y="helloworld!"
var z="hello"+5;   //z="hello5"
```

### 3.5 比较运算符

```javascript
==  //等于
=== //绝对等于  绝对等于实说两个变量值和类型都相等，例如： var a="hello"; var b=new String("hello")  a===b 的结果是false，因为值一样，但a的类型是字符串，b的类型是对象。
!= //不等于
!== //绝对不等于 具体说明同绝对等于（===）
> //大于
< //小于
>=  //大于或者等于
<=  //小于或者等于
```

### 3.6 逻辑运算符

```javascript
&&  //and
|| //or
! //not
```

### 3.7 条件表达式

variableName=(condition)?value1:value2;
当condition为true时，取值value1，当condition为false时，取值value2.

```javascript
judge=(age<18)?"已成年":"未成年";
```

## 4.条件语句

和大多数语句一样：

1. if
2. if...else...
3. if...else if...else...
4. switch()

```javascript
//1.if语句只当表达式为true的时候执行代码块的内容
if(age>=18){
    console.log("我成年了");
}
//if...else...当表达式为真执行if后面的代码块，否则执行else后面的代码块。
if(age>=18){
    console.log("我成年了");
}
else{
    console.log("我是未成年人");
}
//if(condition1)... else if(condition2)... else... 当condition1为真执行 if后面的代码块，
//否则判断contition2的真假，当condition2为真执行else if后面的代码块，否则执行else后面的代码块。
if(age>18){
    console.log("我成年了");
}
else if(age<12){
    console.log("我还在读小学");
}
else{
    console.log("我已经上中学了");
}
//下面将用一个分数等级的例子展示switch的用法
var level;
switch(grade/10){
    case 10:level='A';
    break;
    case 9:level='A';
    break;
    case 8:level='B';
    break;
    case 7:level='C';
    break;
    case 6:level='D';
    break;
    default:level='E';
    break;
};
//注意每一个case后都有break,不然就到了其它的case或者default。
```

## 5.js的循环

### 5.1js的for循环

for(stament1;stament2;stament3){}

各个stament用;分隔,第一个stament为初始的量，循环开始的值，可以在此初始化循环变量,也可以在此省略初始化变量。

stament2为判断条件，不满足条件将退出循环。省略这里除非你在for循环中设置了break，否则循环就是个死循环。
stament3为每次循环后更改的变量，可以在此递增循环变量。也可以忽略这里。

```javascript
for(var i=1;i<=10;i++){
    console.log("i=",i);
}
```

### 5.2 for/in循环

for/in循环经常用来遍历对象的属性。

```javascript
var person={name:'David',age=21,country:'China'};
for (x in person){
    console.log(x);
}
```

### 5.3 while循环

while(condition){

}
while会在condition为真的时候，执行花括号内的代码块。

```javascript
while(true){
    console.log("hello");
}
```

记得在代码块中加入循环变量，否则你的循环将会是一个死循环。

### 5.4  do/while循环

do{

}
while(condition);

```javascript
var i=0;
do{
    console.log("hello");
    i++;
}
while(i<=5);
```

和上面的一样，不管条件是否成立，代码块都将被执行一次。

==总结：一般来说，for循环更好一些，因为你不太容易忘记设置循环变量==

## 6.js的continue和break

continue用于进入下一次的循环，而break得作用是跳出循环。

```javascript
for(var i=0,var sum=0;i<=20;i++){
    if(i%2==1) continue;
    sum+=i;
}  //对0--20内偶数求和,continue的作用是，数字是奇数跳过

///###############################//#endregion
for(var i=1;;){
    console.log('hello');
    if(i==12) break;
    i++;
}//执行12次后的输出退出循环
```

## 7.js的typeof、null和undefined

1.typeof检查变量的类型

```javascript
typeof "Hello, world!";  //String
typeof 12.34;    //Number
typeof true //boolean
typeof ["David","Susan","Lucy","Jack"];  //Object
typeof {name:"David",age:21,sex:"男"} //Object
```

在js中，null代表为空，是一个对象，只不过什么都没有，经常是在释放变量的时候使用。
而undefined代表值和类型都是undefined，表示变量声明了但是从来没有赋值。

```javascript
null==undefined //true  值相同
null === undefined //false 类型不同
```

## 8.js的数据类型转换

### 8.1 js的数据类型

6种基本类型： number\string\boolean\function\object\symbol

3种对象类型：Object\Array\Date

2种不含任何值得数据类型：null\undefined

### 8.2 js的constructor构造器

constructor构造器将返回所有js变量的构造函数

```javascript
"John".constructor //String()
(12.34).constructor  //Number()
false.constructor  //Boolean()
[1,2,3,4].constructor  //Array()
{name:'David',age:21}.constructor //Object()
new Date().constructor  //Date()
function() {}.constructor  //Function()  
```

### 8.3 数字转换为字符串

```javascript
var aa=12.34
String(aa);
String(34);
(12.34).toString()
```

# day01 20201010

基础的学习笔记

---

## 1.基本的引入方式

javascript的引入可以是在head、body或者js文件单独的方式，引入的次数不限，但随着代码量的增多，从js外部文件的引入的选择更好。
举例：

```js

```

## 2.js的输出

>js的输出.html

## 3.js的语法

### 3.1 js的字面量

固定的量

```javascript
3.14
100
34e6
//字符串可以是单引号也可以是双引号
'我是字符串'
"我是字符串"
```

### 3.2 变量和常量

```javascript

//变量可以修改，常量不可以修改，且与其它语言不同的是，
//你并不需要在定义的时候指定变量的值。
//等号的左边是变量，而右边是上文所说的字面量
//每一个变量刚开始的值都是一个undefined
var cc
//cc的值为 undefined  你可以在js中测试其正确性
var aa=11;
var aa="hello js";
var aa=["David","Susan","Lucy"];
//可以看到上述的变量可以任意修改，且不受字面量类型的束缚。
const bb=123;  //定义后不可以修改

```

### 3.3语句和注释

```javascript
//所有的语句用；分隔，但是没用也可以，就像python那样，但是;永远是一个好习惯。
//正如你所看到的, js注释依靠”//“来实现，当然了，还可以使用/**/
//我是注释
/*我是注释*/

```

### 3.4运算符

算术运算符：+-*/%  (优先级和大多数语言一致)
比较运算符：== != > < <= >=

### 3.5 关键字

```javascript
//javascript的关键字有：
abstract
if  else
instanceof
super
boolean
enum
int
byte
long
char
float
short
double
while
null
var
const
switch
for
continue
break
export
interface
synchronized
extends
let
this
case
true
false
throw
throws
try
catch
final
finally
native
new
transient
class
package
function
private
typeof
debugger
goto
protected
default
public
void
delete
implements
return
volatile
do
import
in
static
with
```

### 3.6js的字符集

javascript默认使用unicode字符集。

## 4.js的语句

```javascript
//1.每行代码以";"结尾
//2.多余的空格将被忽略
//3.代码块用{}(同大多数语言一样)
//4.当字符串过长你可以使用 \换行

document.write("我是测试\
内容")
//但下面的用法是错的
document.write \
("我是测试内容")
```

==语法标识符==

## 5.js的数据类型

js 的基本数据类型有字符串、数字、布尔、空、未定义和Symbol
引用类型有：对象、数组和函数。

### 5.1数字

```javascript
var a=123
var b=12.34
var c=34e4  //科学计数法
```

### 5.2字符串

```javascript
var a="hello world"; //双引号
var b='hello world'; //单引号
```

### 5.3布尔

布尔只有真（true)和假（false)

```javascript
var a=true;
var b=false;
```

### 5.4 数组

对比直接赋值和索引赋值。

```javascript
//索引赋值
var aa= new Array();
aa[0]="David";
aa[1]="Susan";
aa[2]="Lucy";
aa[3]="Jack";
//直接赋值
var bb=new Array("David","Susan","Lucy","Jack");
//数组的打印.html
```

### 5.5 对象

用花括号括起，然后用键值对的形式赋值
name:value 的形式

```javascript
var person={
    name:'David',
    sex:'男',
    age:21
}
//对象的打印.html
//深入对象，增加对象的方法
//在上面的定义中 增加一个控制台问候的方法
var person={
    name:'David',
    sex:'男',
    age:21,
    greeting:function(){
        console.log("hello",person.name,"!");
    }
}
```

### 5.6 undefined 和null

变量刚赋值时为undefined,表示未定义。清空赋值的内容用null清空变量的内容。

```javascript
var aa;  //此时的值为 undefined
aa=11;  //赋值11
...
aa=null;  //根据实际的需要需要清空，为null
```

## 6.js函数

javascript函数的格式是 
function functionName([args]){

}
function是关键字
functionName是函数名 后面是括号,括号里是一系列的参数，其后紧跟花括号{}.

就如之前测试用例的，我的每一个测试用例都是按钮点击事件，每次点击按钮后都会触发按钮事件，事件就会调用已经定义的函数。

几种不同的函数都在 函数.html可测试。

==变量的生存周期==
变量分为局部变量和全局变量。
局部变量指的是函数里定义的变量，只能是函数内部使用，外部无法使用，且函数运行时被创建，函数运行后被销毁。
全局变量在script全局的变量，在页面创建时创建，随着页面的销毁而销毁。

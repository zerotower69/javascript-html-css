# DAY03 20201012

## 1.js正则表达式

==这一块将是比较重要又较难的一部分==
==什么是正则表达式？==

### 1.1 正则表达式的基本定义

### 1.2 使用基本举例

### 1.3 正则表达式的语法格式

 var patt=new RegExp(pattern,modifiers);
 var patt=/pattern/modifiers   /匹配格式/修饰符

```javascript
1.修饰符：i g  m  //i 用来表示大小写不敏感    g 执行全局匹配   m 执行多行匹配

2. [] //[] 用来查找某个范围的字符
[0-9]  //查找数字0-9
[A-Z] //查找大小英文字母

3.元字符  //有特殊含义的字符
\w //查找字母数字以及下划线
\W //查找非单词字符
\d    //查找数字
\D   //查找非数字字符
\s    //查找空白字符
\S  //查找非空白字符
\b    //匹配单词边界
\B  //匹配非单词边界
\0 //find null character
\n //查找换行字符
\t //查找制表符
\xxx //查找八进制xxx的字符
\xdd //查找十六进制dd的字符
\uxxxx //查找以十六进制数xxxx规定的Unicode的字符

4.量词：
n+  //匹配至少包含一个n的字符串  如/e/ 匹配 "egg"的'e' ,匹配"peeeeeeeeeeeeeeeeear"所有的'e';
n*  //匹配任何包含0个或者多个n的字符串 /bo*/ 匹配 "A ghost booooed" 中的 "boooo"，"A bird warbled" 中的 "b"，但是不匹配 "A goat grunted"  从匹配项的第一个字母开始匹配，允许被匹配项中不存在除第一个字母不存在的其它字母
n? //匹配任何包含0个或者1个的字符串 /e?le?/ 匹配 "angel" 中的 "el"，"angle" 中的 "le"。
n{X}  //X是正整数，匹配包含 X 个 n 的序列的字符串。例如，/a{2}/ 不匹配 "candy," 中的 "a"，但是匹配 "caandy," 中的两个 "a"，且匹配 "caaandy." 中的前两个 "a"。
n{X,Y} //X 和 Y 为正整数。前面的模式 n 连续出现至少 X 次，至多 Y 次时匹配。例如，/a{1,3}/ 不匹配 "cndy"，匹配 "candy," 中的 "a"，"caandy," 中的两个 "a"，匹配 "caaaaaaandy" 中的前面三个 "a"。注意，当匹配 "caaaaaaandy" 时，即使原始字符串拥有更多的 "a"，匹配项也是 "aaa"。
n$ //匹配任何结尾为 n 的字符串。例如校验以0012结尾的字符串  /0012$/
^n //匹配任何以n开头的字符串  
?=n // 匹配任何其后紧接指定字符串 n 的字符串。
?!=n //匹配任何其后没有紧接指定字符串 n 的字符串。

5.RegExp方法
exec() //检索字符串中指定的值。返回找到的值，并确定其位置。
test() //检索字符串中指定的值。返回 true 或 false。
toString()//返回正则表达式的字符串。

6.支持正则表达式的String对象的方法
search()  //检索与正则表达式相匹配的值。
match()  //找到一个或多个正则表达式的匹配。
replace() //替换与正则表达式匹配的子串。
split()  //把字符串分割为字符串数组。

7.RegExp对象属性
constructor() //返回一个函数，该函数是一个创建 RegExp 对象的原型。
global() //判断是否设置了 "g" 修饰符
ignoreCase() //判断是否设置了 "i" 修饰符
lastIndex() //用于规定下次匹配的起始位置
multiline() //判断是否设置了 "m" 修饰符
source() //返回正则表达式的匹配模式
```

在1.4中将具体使用上述的正则表达式。

### 1.4 使用正则表达式进行校验或者匹配

1.使用test()方法检验某个字符串是否匹配某个模式。符合返回true,否则返回false
==测试用例请使用正则表达式2.html==

```javascript
//1.字符串中是否具有某个字符
var pre=/z/;
var str="I went to zoo yesterday.";
pre.test(str);  //true
var str2="I live in Beijing";
pre.test(str2);  //false
```

2.如果要校验中文字符，必须认识unicode编码格式，中文字符对应的unicode编码有两个字节，共4个十六进制数。
格式位\u0000格式 ，且基本的中文数字编码范围是：4E00-9FA5 基本汉字补充：9FA6-9FEF。所以校验范围从4E00-9FEF。

```javascript
var reg=/[\u4E00-\u9FEF]/;
var str="kill opple 我";
var re=reg.test(str);   //true
var str="kill one person";
var re=reg.test(str);  //false
```

### 1.5 常用的正则表达式场景

此部分的内容请参考：正则校验.html

### 1.6 持续深入正则表达式

## 总结

想不到一个正则表达式就去了一天，太难了，不过我已经做了尽可能的详尽说明，希望能让你少走一些弯路。

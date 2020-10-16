# mermaid

让我写点英文装装逼格。

在markdown中画出想要的流程图、时序图
You can draw all flowcharts and suquece diagrams you want in the markdown.

---

## 1.flowcharts

>demo1 simple flowchart

```mermaid
graph TD;
A-->B;
A-->C;
B-->D;
C-->D;
```

>demo2 different syntax

```mermaid
graph TD;
A[Double Eleven]-->|get money| B(go shopping)
B-->C{my list};
C-->|one| D[labtop];
C-->|two| E[ipad];
C-->|three| F[iPhone];
C-->|four| G[kindle];
```

Please observe the effect of different syntaxs.

>demo3

In this demo, you can see the difference of `TD`,`TB`,`BT`,`RL`,and `LR`.

```mermaid
graph TD;
start-->|TD|top
```

```mermaid
graph TB;
start-->|TB|top;
```

```mermaid
graph BT;
start-->|BT|top;
```

```mermaid
graph LR;
start-->|LR|top;
```

```mermaid
graph RL;
start-->|RL|top;
```

>demo4
In this demo, you will see the difference of nodes and shapes by difference syntax.

```mermaid
graph LR;
A[I am a graph];

B(I am a graph.);

C{I am a graph.};

D([I am a graph.]);

E[[I am a graph.]];

F[(I am a graph.)];

G((I am a graph.));

H>I am a graph.];

I{{I am a graph.}};

J[/I am a graph./];

K[\I am a graph.\];

L[/I am a graph\]

M[\I am a graph./]
```

the link between two elements.

```mermaid
graph LR;
A1-->B1;
A2---B2;
A3---|I am link line|B3;
A4-->|I am link line|B4;
A5-.-B5;
A6==>B6;
A7==>|text|B7;
```

It is possible declare many links in the same line as per below:

```mermaid
graph LR;
A-->B-->C;
```

It is also possible to declare multiple nodes links in the same line as per below:

```mermaid
graph LR;
A-->B & C-->D;
```

```mermaid
graph TB;
A & B-->C & D;
```

```mermaid
flowchart TB
    c1-->a2
    subgraph one
    a1-->a2
    end
    subgraph two
    b1-->b2
    end
    subgraph three
    c1-->c2
    end
    one --> two
    three --> two
    two --> c2
```


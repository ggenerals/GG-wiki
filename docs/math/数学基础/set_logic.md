# 集合与逻辑

## 集合

集合的定义为一些确定对象组成的总体。

性质：确定性、互异性、无序性。

集合可以用以下三种方法描述：

- 枚举法：$\set{1,2,3}$，要求是有限集合。
- 描述法：如 $\set{x|x>0}$。
- 区间法：如 $[x,y]$。

规定如下记号：

- $\varnothing$：空集，表示没有元素的集合；
- $\in$：属于，$x\in A$ 表示**元素** $x$ 在**集合** $A$ 中出现。
- $\notin$：不属于。

有如下五个特殊的集合：

$$\mathbb{N,Z,Q,R,C}$$

分别表示：

- $\mathbb N$：自然数集；
- $\mathbb Z$：整数集；
- $\mathbb Q$：有理数集；
- $\mathbb R$：实数集；
- $\mathbb C$：复数集。

集合运算有最基础的几种：

- 交：记作 $A\cap B$，表示 $\set{x|x\in A\texttt{ 或 }x\in B}$；
- 并：记作 $A\cup B$，表示 $\set{x|x\in A\texttt{ 且 }x\in B}$。
- 补：记作 $\complement_A B$，表示 $\set{x|x\in A\texttt{ 且 }x\notin B}$，需满足 $B\subseteq A$。

集合之间有如下关系：

- 包含：记作 $A\subseteq B$，表示 $A$ 中元素都在 $B$ 中出现，此时，称 $A$ 是 $B$ 的一个子集；
- 真包含：记作 $A\varsubsetneqq B$，表示 $A$ 中元素都在 $B$ 中出现，且 $A\ne B$，此时，称 $A$ 是 $B$ 的一个真子集。
- $\varnothing \subseteq A$，$\varnothing\varsubsetneqq A(A\ne \varnothing)$

考虑集合 $A=\{1,2,\cdots ,n\}$，它的子集数量为 $2^n$（每个元素在/不在）、真子集数量为 $2^n-1$。

记 $\Omega=\{1,2,\cdots ,n\}$，令 $S\subseteq \Omega,T\subseteq \Omega$，则 $T\subseteq S$ 的集合对 $(S,T)$ 数量为 $3^n$。

也就是常说的枚举子集，代码实现如下：
```cpp
for(int T=S;T;T=S&(T-1)) ;
```

## 命题

命题：能够判断真假的语句。

全称量词 $\forall$ 与存在量词 $\exists$。

命题间的关系：

- 原命题：$a\Rightarrow b$，即“若 $a$，则 $b$”；
- 逆命题：$b\Rightarrow a$；
- 否命题：$a\not\Rightarrow b$；
- 逆否命题：$b\not\Rightarrow a$。

艾弗森括号：表示命题的真假。用 $[a]$ 表示，若 $a$ 为真则 $[a]=1$，反之为 $0$。
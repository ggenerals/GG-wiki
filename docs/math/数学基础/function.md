# 函数入门
即映射关系。

定义函数 $f$：设集合 $A,B$，若按照关系 $f$，对于 $A$ 中的每一个元素，在集合 $B$ 中都有一个元素与之对应，则称：

$$f:A\to B$$

为一个函数。

通常使用数集，可以记为 $y=f(x)(x\in A,y\in B)$。

$f$ 的定义域为 $A$，值域为 $\set{y|y\in B,\exists x\in A,f(x)=y}$。
## 性质
有些函数可能有如下性质：

- 单调性：对于一段区间 $T\subset S$，$\forall x_1,x_2\in T,x_1<x_2,f(x_1)<f(x_2)$。
- 奇偶性：  
  - 偶性质：$f(x)=f(-x)$；
  - 奇性质：$f(x)=-f(-x)$。
- 周期性：如果存在 $T$，满足 $\forall x,f(x)=f(x+T)$（$x,x+T$ 都在定义域内），则称 $f$ 具有周期性，$T$ 是其周期。一般我们用的是最小的正整数 $T$。

可以用图像研究函数。
## 初等函数
- 一次函数：$kx+b$；
- 二次函数：$ax^2+bx+c$；
- 反比例函数：$\frac{k}{x}$；
- 幂函数：$x^a$；
- 指数函数：$a^x$；
- 对数函数：$\log_a x$。
- 三角函数：$\sin,\cos,\tan$。

还有分段函数。

关于三角函数，有如下性质：

- $\cos^2\theta+\sin^2\theta=1$；
- 关于 $\cos$ 和 $\sin$ 的诱导公式：奇变偶不变，符号看象限。
- 和差角公式：
  - $\cos(x+y)=\cos x\cos y-\sin x\sin y$；
  - $\sin(x+y)=\cos x\sin y+\sin x\cos y$。
- 旋转坐标轴：
  - 将 $(x,y)$ 所在的坐标轴旋转了 $\theta$ 后，坐标会变成 $(x\cos\theta-y\sin\theta,x\sin\theta+y\cos\theta)$。

## 导数
$f(x)$ 的导数等于 $\lim\limits_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$。

导数也可进行四则运算：

- 若 $h(x)=f(x)+g(x)$，则 $h'(x)=f'(x)+g'(x)$。
- 若 $h(x)=f(x)\cdot g(x)$，则 $h'(x)=f'(x)g(x)+f(x)g'(x)$。
- 若 $h(x)=f(g(x))$，则 $h'(x)=f'(g(x))\cdot g'(x)$。
- 若 $h(x)=\frac1{g(x)}$，则 $h'(x)=-\dfrac{g'(x)}{[g(x)]^2}$。

初等函数的导数：

- 若 $f(x)=kx$，则 $f'(x)=k$；
- 若 $f(x)=x^2$，则 $f'(x)=2x$；
- 若 $f(x)=x^n$，则 $f'(x)=nx^{n-1}$；
- 若 $f(x)=a^x$，则 $f'(x)=a^x\ln a$；
  - 证明：

    $$\begin{aligned}(a^x)'&=\lim\limits_{\Delta x\to 0}\frac{a^{x+\Delta x}-a^x}{\Delta x}\\&=a^x\lim\limits_{\Delta x\to 0}\frac{a^{\Delta x}-1}{\Delta x}\end{aligned}$$

    然后就是要求 $\lim\limits_{\Delta x\to 0}\frac{a^{\Delta x}-1}{\Delta x}$，不妨令 $t=a^{\Delta x}-1$，则 $\log_a(t+1)=\Delta x$，于是：

    $$\begin{aligned}\lim\limits_{\Delta x\to 0}\frac{a^{\Delta x}-1}{\Delta x}&=\lim\limits_{\Delta x\to 0} \frac{t}{\log_a(t+1)}\\&=\lim\limits_{\Delta x\to 0} \frac1{\frac1t\log_a(t+1)}\\&=\lim\limits_{\Delta x\to 0} \frac1{\log_a(t+1)^{\frac1t}}\\&=\frac1{\log_ae}=\ln a\end{aligned}$$

    不难发现，$a=e$ 时，$\ln e=1$，所以 $(e^x)'=e^x$。

- $f(x)=\log_ax$，则 $a^{f(x)}=x$，两边取导，则 $a^{f(x)}\cdot f'(x)\ln a=1$。所以 $f'(x)=\frac 1{x\ln a}$。  
  同理可得，$a=e$ 时，$\ln e=1$，所以 $(\ln x)'=\frac1x$。

- 三角函数：  
  $\sin'(x)=\cos x$；  
  $\cos'(x)=-\sin x$；  
  $\tan'(x)=1+\tan^2x$。

洛必达法则：如果在 $\lim\limits_{x\to a}\frac{f(x)}{g(x)}$ 中，$f(a)=g(a)=0$。那么：

$$\lim\limits_{x\to a}\frac{f(x)}{g(x)}=\lim\limits_{x\to a}\frac{f'(x)}{g'(x)}$$

利用导数，可以得到：

$$f(x)=\sum_{i=0}^{+\infty}c_ix^i$$

其中，$c_i=\dfrac{f^{(i)}(0)}{i!}$，$f^{(i)}$ 表示 $f$ 的 $i$ 阶导。

比如，$e^x=\sum\limits_{i=0}^{+\infty}\dfrac{x^i}{i!}$。特别的，$0^0=0$。

$e^{ix}=\cos x+i\sin x$。令 $x=\pi$，$e^{i\pi}=-1$。
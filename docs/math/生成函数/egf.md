# 指数型生成函数

这是一篇 Plonkit 风格的娱乐性质文章，欢迎大家指出问题，探讨交流！

[图寻文档](https://oi-wiki.org/math/poly/egf/)

这个是序列指数生成函数。

## Part I 基础识别

您可以根据形式特别像泰勒展开的式子定位 EGF。

$$F(x)=\sum_{n}a_nx^n(n!)^{-1}$$

它的加法和乘法也与 poly 相同，其中乘法隐含了特殊 meta：。

$$\begin{aligned}F(x)G(x)=\sum_{i\geq 0}a_ix^i(i!)^{-1}\sum_{j\geq 0}b_jx^j(j!)^{-1}\\=\sum_{n\geq 0}x^n(n!)^{-1}\sum_{i=0}^n{n\choose i}a_ib_{n-i}\end{aligned}$$

也就是 

$$\left\{\sum_{i=0}^n{n\choose i}a_nb_{n-i}\right\}$$

的 EGF。

EGF 的求导和积分也隐含了特殊的 meta：

求导相当于系数 $a$ 左移，即：$a_n=a_{n+1}$，而积分相当于系数 $a$ 向右移，即 $a_n=a_{n-1}$，可以利用这个性质建立递推式。

**注意：上述的左移/右移不会改变 $\mathbf{1/n!}$ 的系数!**。

## Part II 聚焦区域

一般来说，您可以适时地把 EGF 利用泰勒展开等技巧转化为封闭形式，找到更多的解题线索。

例如：序列 $\{1,1...\}$ 的 EGF 是 

$$\sum_{n\geq 0}\frac{x^n}{n!}=e^x$$

序列 $\{1,-1,1,-1,1...\}$ 的 EGF 是 

$$\sum_{i\geq 0}\frac{(-1)^ix^i}{i!}=e^{-x}$$

等比数列的 EGF 是：

$$\sum_{n\geq 0}\frac{p^nx^n}{n!}=e^{px}$$

### EGF 中多项式 exp 的组合意义
您先考虑多个 EGF 相乘的组合意义：

不难发现，设 $a_{j}$ 为从第 $i$ 种颜色中选择 $j$ 个元素的方案数，那么 EGF 乘完后：$[x^k]$ 系数的组合意义就是：长度为 $k$ 的本质不同颜色序列个数。

假如颜色之间不区分：我们再设 $F_k(n)$ 表示：长度为 $n$ 的本质不同颜色序列个数，容易得到：。

$$F_k(n)=\frac{n!}{k!}\sum_{\sum b_i=n}\prod_{j=1}^k \frac{a_{b_j}}{b_j!} $$

设 $a^n$ 的 EGF为 $\hat a$，而 $F_k(n)$ 的 EGF 为 $G_k(x)$，有定义式推出：

$$\begin{aligned}G_k(x)&=\sum_{n\geq 0}F_k(n)\frac{x^n}{n!}\\&=\frac{1}{k!}\sum_{n\geq 0}x^n\sum_{\sum b_i=n}\prod_{j=1}^k \frac{a_{b_j}}{b_j!}\end{aligned}$$

把 $x^n$ 拆进右边，就得到：

$$=\frac{1}{k!}\sum_{n\geq 0}\sum_{\sum b_i=n}\prod_{j=1}^k \frac{a_{b_j}x^{b_j}}{b_j!}$$

也就是 $\frac{1}{k!}(\hat a)^k$。

于是我们论证了：对于 $a$ 这样一个刻画 **从某种颜色中选择元素的方案数** 组合结构，它的 $\textrm{exp}$ 就是：**将一个定长序列染成任意种互不区分的颜色的方案数**，或者是 **图寻文档** 中的表述：**有标号元素构成的集合的生成集族有多少种情况**。

## Part III 特殊覆盖

沉浸式寻找 5k 点ing~
### P17285 不会说明你有鱼鱼蒸
这题关键有两个 EGF，它们分别是：$f_0(x)=\sum_{2i}x^{i}(2i)!^{-1},f_1(x)=\sum_{2i+1}x^{i}(2i+1)!^{-1}$。

推一下它们的 $\exp$：

$$2\exp f_0=e^x+e^{-x}，2\exp f_1=e^x-e^{-x}$$

具体地，就是利用 EGF 为 $e^{±x}$ 的序列的性质，进行对位相消，使得只保留奇数位或偶数位。

然后你暴力启动把原来的式子给展了：
![](https://cdn.luogu.com.cn/upload/image_hosting/tt95cinp.png)

然后我们发现 $[x^m]e^{xk}$ 这个东西是前面所提及的 $k$ 等比数列的 EGF，因此可以转化：$[x^m]m!e^{x(2i+2j-n)}=(2i+2j-n)^{m}$。

再把我们丢掉的 $1/2$ 系数和 ${n \choose k}$ 乘回来得到更舒服的式子：

$$ans=[x^m]\frac{1}{2^n}{n\choose k}\sum_{i=0}^{n-k}\sum_{j=0}^k(-1)^{1+j}{n-k\choose i}{k\choose j}(2i+2j-n)^m$$

考虑计算枚举 $i+j=t$ 统计答案，设：

$$h(t)=\sum_{j=0}^{t}(-1)^{j}{k\choose j}{n-k\choose t-j}$$

他的 OGF 是 $[x^t]H(x)=[x^t](1-x)^k(1+x)^{n-k}$。

先对 $H(x)$ 取 $\ln$：

$$\ln H(x)=(n-k)\ln(1+x)+k\ln(1-x)$$

因为

$$\ln H(x)
=k\ln(1-x)+(n-k)\ln(1+x),$$

所以

$$\frac{H'(x)}{H(x)}
=
-\frac{k}{1-x}+\frac{n-k}{1+x}
=
\frac{n-2k-nx}{1-x^2}.$$

于是

$$(1-x^2)H'(x)
=(n-2k-nx)H(x).$$

代入

$$H(x)=\sum_{t=0}^n a_tx^t$$

下面利用 EGF 求导的性质，注意我们要还原系数 $[x^t]$ 的 $a_t$ 再除以 $(t-1)!$：

$$[x^{t-1}]H'(x)=[x^{t}]H(x)\times t!\times(t-1)!^{-1}=h[x^t]t$$

于是上式子化为，$[x^t]$ 默认指求导前的系数：

$$\sum_{t} [x^{t+1}]\times {(t+1)}\times x^{t}-\sum_t [x^{t-1}]\times (t-2)\times x^{t}=\sum [x^t](n-2k)x^t-\sum_t [x^{t-1}]nx^t$$

比较 $x^t$ 的系数，就得到

$$(t+1)[x^{t+1}]-(t-1)[x^{t-1}]=(n-2k)[x^t]-n[x^{t-1}]$$

所以递推式为：

$$\boxed{
(t+1)a_{t+1}
=(n-2k)a_t-(n-t+1)a_{t-1}
}$$

也就是

$$\boxed{
a_{t+1}
=
\frac{(n-2k)a_t-(n-t+1)a_{t-1}}{t+1}
}$$

初始条件是

$$ a_0=1,\qquad a_1=n-2k.$$

## Part IV 地图资源

![](https://cdn.luogu.com.cn/upload/image_hosting/pso20q3t.png)
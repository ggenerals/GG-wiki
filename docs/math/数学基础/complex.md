# 复数
## 复数基础知识
虚数单位 $i$ 满足 $i^2=1$。

复数形如 $z=a+bi(a,b\in \mathbb R)$。

复数的模等于 $|z|=\sqrt{a^2+b^2}$。

复数 $z=a+bi$ 的共轭复数为 $\overline{z}=a-bi$。

定义 $z_1=a_1+b_1i,z_2=a_2+b_2i$。复数的四则运算如下：

- 加法：$z_1+z_2=(a_1+a_2)+(b_1+b_2)i$；
- 减法：$z_1-z_2=z_1+(-z_2)$；
- 乘法：$z_1\cdot z_2=(a_1+b_1i)(a_2+b_2i)=(a_1a_2-b_1b_2)+(a_1b_2+b_1a_2)i$；
- 除法：$z_1\div z_2=z_1\times \frac{1}{z_2}$；
- 倒数：$\frac1z=\frac1{a+bi}=\frac{a-bi}{(a+bi)(a-b_i)}=\frac{a-bi}{a^2+b^2}$。

在复平面上，所有复数 $z=a+bi$ 可以用坐标 $(a,b)$ 表示。

不难发现，在单位圆上，坐标 $(\cos\theta,\sin\theta)$ 对应复数 $\cos\theta+i\sin\theta$。

所以复数还有一种角度表示法：$z=|z|(\cos\theta+i\sin\theta)$。

棣莫弗定理：设 $z_1=|z_1|(\cos\theta_1+i\sin \theta_1)$，$z_2=|z_2|(\cos\theta_2+i\sin \theta_2)$。则 $z_1\cdot z_2=|z_1||z_2|(\cos\theta_1\cdot\cos\theta_2-\sin\theta_1\sin\theta_2)$。

欧拉定理：$e^{i\pi}=-1$。
## 单位根
先来解一个方程 $x^n=1$。

答案是

$$x_k=\cos\left(\frac{2\pi}nk\right)+i\sin\left(\frac{2\pi}nk\right)(0\le k<n)$$

这 $n$ 个解就是**单位根**，用 $\omega_n^k$ 表示。

$$\omega_n^k=\cos\left(\frac{2\pi}nk\right)+i\sin\left(\frac{2\pi}nk\right)$$

如果 $k\ge n$，则 $\omega_n^k=\omega_n^{k\bmod n}$。

单位根有如下性质：
- $|\omega|=1$；
- $\omega_n^x\cdot\omega_n^y=\omega_n^{x+y}$；
- $(\omega_n^x)^y=\omega_n^{xy}$。
- $\omega_n^{x+\frac n2}=-\omega_n^x$
- $w_n^0=1$。

单位根反演：

$$[n\mid k]=\frac1n\sum_{i=0}^{n-1}\omega_n^{ik}$$

证明：

- $n\nmid k$ 时，右边等于 $\dfrac 1n\cdot\dfrac{\omega_n^{kn}-1}{\omega_n^k-1}$，$w_n^{kn}=w_n^0=1$，所以右式等于 $0$。
- $n\mid k$ 时，右式等于 $\dfrac1n\cdot n=1$。

单位根反演可以计算对于任意多项式

$$f(x)=\sum_{i=0}^m c_ix^i$$

求：

$$\sum_{k=0}^m[n\mid k]c_k$$

可以得到，其值等于：

$$\frac1n\sum_{i=0}^{n-1}f(\omega_n^i)$$

证明方法就是直接带入：

$$\begin{aligned}
\sum_{k=0}^m[n\mid k]c_k&=
\sum_{k=0}^mc_k\cdot\frac1n\sum_{i=0}^{n-1}\omega_n^{ik}\\
&=\frac1n\sum_{i=0}^{n-1}\sum_{k=0}^mc_k(\omega_n^{i})^k\\
&=\frac1n\sum_{i=0}^{n-1}f(\omega_n^i)
\end{aligned}$$
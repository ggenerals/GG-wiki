# 中国剩余定理

## 适用范围
给定：

$$\begin{cases}
x\equiv a_1\pmod{m_1}\\
x\equiv a_2\pmod{m_2}\\
\cdots\\
x\equiv a_i\pmod{m_i}\\
\cdots\\
x\equiv a_n\pmod{m_n}
\end{cases}$$

求最小正整数 $x$。

## 中国剩余定理（CRT）

当 $m_1,m_2,\cdots,m_n$ 两两互质，且

$$\begin{cases}x\equiv a_1\pmod{m_1}\\x\equiv a_2\pmod{m_2}\\\cdots\\x\equiv a_i\pmod{m_i}\\\cdots\\x\equiv a_n\pmod{m_n}\end{cases}$$

令 $M=\operatorname{lcm}(a_1,\cdots,a_n)$，$m_i=\frac{M}{a_i}$，有特解 $x=(\sum\limits_{i=1}^n m_i\times m_i^{-1}\times a_i)\bmod M$。

## 扩展中国剩余定理（exCRT）

exCRT 的本质是合并形如

$$x\equiv a_i\pmod{m_i}$$

的式子。

考虑

$$\begin{cases}x\equiv a_1\pmod {m_1}\\x\equiv a_2\pmod {m_2}\end{cases}$$

这个式子可以合并，不妨令

$$x=km_1+a_1$$

所以

$$km_1+a_1\equiv a_2\pmod {m_2}$$

可以发现 $k$ 的解为：

$$k=(a_2-a_1)\cdot{m_1}^{-1}\bmod{m_2}$$

通过 exGCD，可以得到一个合法的 $k$，并得到一个在模 $m_1m_2$ 的意义下，$x$ 的一个值，合并完成。
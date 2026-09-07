# 数论基础
整个数论章节中，我们默认只讨论整数。
## 模运算
对于带余除法

$$p\div q=d\cdots r$$

我们定义：

$$\left\lfloor \frac pq\right\rfloor=d,p\bmod q=r$$

在 C++ 中两种运算分别为：

```cpp
d = floor(p * 1.0 / q);
r = p % q;
```
### 模运算的性质
模运算具有如下性质：

- $(a+b)\bmod p=(a\bmod p+b\bmod p)\bmod p$。
- $(-b)\bmod p=(-b\bmod p+p)\bmod p$。
- $(a\times b)\bmod p=(a\bmod p)\times (b\bmod p)\bmod p$。
### 乘法取模
在求两个极大的数乘积对 $p$ 取模的情况下，直接相乘可能爆 `long long` 甚至 `__int128`，这时候我们可以使用类似快速幂的方式进行龟速乘，代码如下：

```cpp
int qmul(int a,int b,int p)
{
    int ans=0;
    while(b)
    {
        if(b&1) ans=(ans+a)%p;
        a=(a+a)%p;
        b>>=1;
    }
    return ans;
}
```

不难发现，龟速乘的时间复杂度为 $O(\log b)$ 的。

同时我们也有快速乘，时间复杂度 $O(1)$：

??? note "快速乘的代码实现"

    ```cpp
    unsigned long long quick_mul(long long a, long long b, long long mod) 
    {
        unsigned long long c =(unsigned long long)a * b -(unsigned long long)((long double)a / mod * b + 0.5L) * mod;
        if (c < mod) return c;
        return c + mod;
    }
    ```

## 整除
定义 $a$ 整除 $b$ 当且仅当存在整数 $x$ 使得 $b=ax$，记作 $a\mid b$。也就是：

$$b\bmod a=0$$

不难发现整除的性质：

- $a\mid b,b\mid c\Rightarrow a\mid c$
- $a\mid b,a\mid c\Rightarrow \forall x,y\in\mathbb Z,a\mid (xb+yc)$
- $a\mid b,b\mid a\Rightarrow a=\pm b$
- $a\mid b\Rightarrow \forall m\ne 0,(ma)\mid(mb)$
## 约数和倍数
若 $a\mid b$，则称 $a$ 是 $b$ 因数，$b$ 是 $a$ 倍数。
### 公约数和公倍数
若 $g\mid a,g\mid b$，则称 $g$ 是 $a,b$ 的一个公约数。

若 $a\mid g,b\mid g$，则称 $g$ 是 $a,b$ 的一个公倍数。
#### 最大公约数
若 $g$ 是 $a,b$ 的公约数中最大的一个，则称 $g$ 为 $a,b$ 的最大公约数，记作：

$$g=\gcd(a,b)$$
#### 最小公倍数
若 $g$ 是 $a,b$ 的公倍数中最小的一个，则称 $g$ 为 $a,b$ 的最小公倍数，记作：

$$g=\operatorname{lcm}(a,b)$$
#### 多元情况
给定数列 $a=[a_1,a_2,\cdots,a_n]$，若 $\forall i\in\{1,2,\cdots,n\}，g\mid a_i$，则称 $g$ 是 $a$ 的一个公约数。

若 $g$ 是 $a$ 的公约数中最大的一个，则称 $g$ 为 $a$ 的最大公约数，记作：

$$g=\gcd(a_1,a_2,\cdots,a_n)$$

给定数列 $a=[a_1,a_2,\cdots,a_n]$，若 $\forall i\in\{1,2,\cdots,n\}，a_i\mid g$，则称 $g$ 是 $a$ 的一个公倍数。

若 $g$ 是 $a$ 的公倍数中最小的一个，则称 $g$ 为 $a$ 的最小公倍数，记作：

$$g=\operatorname{lcm}(a_1,a_2,\cdots,a_n)$$
## 质数
如果 $p$ 除了 $1,p$ 外不存在 $g|p$，则称 $p$ 为质数，否则为合数。
### 算数基本定理
也就是质因数分解：对于任意正整数 $n$，一定存在 $p_i\in prime$，满足：

$$n=p_1p_2\cdots p_s$$

不计次序，该表示方法唯一。通常我们写作：

$$n=\prod_{i=1}^n p_i^{e_i}$$
## 同余
如果 $a,b,p$ 满足：

$$a\bmod p=b\bmod p$$

则称 $a,b$ 在模 $p$ 意义下同余，记作：

$$a\equiv b\pmod p$$
### 同余的性质
- $a\equiv a\pmod p$；
- $a\equiv b\pmod p\Rightarrow b\equiv a\pmod p$；
- $a\equiv b\pmod p,b\equiv c\pmod p\Rightarrow a\equiv c\pmod p$
- $a\equiv b\pmod p,c\equiv d\pmod p\Rightarrow (a\pm c)\equiv (b\pm d)\pmod p,ac\equiv bd\pmod p$
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


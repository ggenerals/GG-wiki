# 模意义下的乘法逆元

## 逆元的概念

在[数论基础](https://wiki.gengen.qzz.io/math/数论/mod-prime/)章节中，我们提到加，减，乘法是可以取模的，但是除法不能取模。  

那在我们需要取模，但是又用到了除法的情况下我们该怎么办呢？  

由此，我们引入了模意义下的乘法逆元，事实上不止普通乘法有逆元，矩阵乘法、多项式乘法等也有，但本章我们只讨论模意义下的乘法逆元，后文简称为逆元。

逆元的定义是模意义下整数 $a$ 的倒数，记作 $a^{-1}$，需要注意的是，并不是所有的数的所有模数意义下都有逆元。

根据定义有，

$$a^{-1} \times a \equiv 1 (\bmod p)$$

其中 $p$ 为给定的模数。

## 单个逆元的求解方式

### exgcd 求逆元

根据同余定义式，转化可得：

$$kp+a^{-1}a=1$$

其中 $k$ 为未知数，  

那么我们得到了一个二元一次不定方程，其中 $p,a$ 已知，利用 $\text{exgcd}$ 可以求出 $a^{-1}$。

```cpp linenums="1"
int exgcd(int a,int b,int &x,int &y){
    if(!b){
        x=1,y=0;
        return a;
    }
    int d=exgcd(b,a%b,x,y),t=x;
    x=y,y=t-(a/b)*y;
    return d;
}
int inv(int a,int mod){
    int x,y;
    exgcd(a,mod,x,y);
    return (x%mod+mod)%mod;
}
```

此法对于任意模数均适用。

### 费马小定理/快速幂法求逆元

???+ note "费马小定理"

    设 $p$ 为质数，$a$ 为任意整数，有 $a^{p} \equiv a (\bmod p)$。

证明略，等待后人编写。
    
根据费马小定理，有推论：

$$a^{-1} \equiv a^{p-2} (\bmod p)$$

那么，我们可以通过快速幂的方式求出 $a$ 的逆元。

```cpp linenums="1"
int qpow(int x,int y,int mod){
    int res=1;
    while(y){
        if(y&1) res=res*x%mod;
        x=x*x%mod,y>>=1;
    }
    return res;
}
int inv(int x,int mod){
    return qpow(x,mod-2,mod);
}
```

此法只对于质数模数适用，但大多数时候模数确实为质数，所以这种方法较为常见。

## 多个逆元的求解方式


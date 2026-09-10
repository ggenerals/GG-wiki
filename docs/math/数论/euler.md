## 欧拉函数
## 欧拉函数
### 欧拉函数的定义
> （定义）欧拉函数：$\varphi(n)$ 表示 $n$ 以内的正整数与 $n$ 的互质的数的个数。
>
> $$\varphi(n)=|\{k|1\le k\le n,k\perp n\}|$$
### 欧拉函数的性质
> 性质 1：
>
> $$\forall p\in \text{prime},\varphi(p)=p-1$$
>
> 易证。

> 性质 2：
>
> $$\forall p\in \text{prime},\varphi(p^k)=p^k-p^{k-1}=p^{k-1}(p-1)$$
>
> 证明：不互质的数是 $p,2p,\cdots,p^k$，所以互质的数有 $p^k-p^{k-1}$。

> 性质 3：
>
> $$\varphi(mn)=\varphi(n)\varphi(m),n\perp m$$
>
> 证明：使用中国剩余定理。

> 性质 4：
>
> $$\forall a|x,\varphi(ax)=a\varphi(x)$$
>
> > 证明：
> > 设与 $x$ 互质的数分别为 $d_1,d_2,\cdots d_{\varphi(x)}$。  
> > 易证 $a\perp d_i(1\le i\le \varphi(x))$。  
> > 若 $a>1$，则 $d_1+x,d_2+x,\cdots,d_{\varphi(x)}+x$ 均和 $ax$ 互质。  
> > 同理 $d_i+tx(0\le t<a)$ 小于 $ax$ 且 $(d_i+tx)\perp ax$。  
> > 总计有大于等于 $a\varphi(x)$ 组互质。
> > 设与 $x$ 不互质的一个数为 $k$，记 $d=\gcd(n,k),p=\frac{k}{d},q=\frac{n}{d}$，那么 $d+tx=d(p+q)$ 必然和 $ax$ 有公因数 $d$，故上一段构造的集合充分，所以 $\forall a|x,\varphi(ax)=a\varphi(x)$。
## 欧拉函数的求法
### 求单个欧拉函数的值
> 性质 5：设 $n=\prod p_i^{e_i}$，则：
> 
> $$\varphi(n)=n\prod\frac{p_i-1}{p_i}$$
>
> > 证明：
> >
> > $$\begin{aligned}\varphi(n)&=\varphi\left(\prod p_i^{e_i}\right)\\&=\prod \varphi(p_i^{e_i})\\&=\prod [p_i^{e_i-1}(p_i-1)]\\&=\prod \left(p_i^{e_i}\cdot \frac{p_i-1}{p_i}\right)\\&=n\prod\frac{p_i-1}{p_i}\end{aligned}$$

故可以得到如下代码：

```cpp
int phi(int n)
{
	int ans=n;
	for(int i=2;i*i<=n;i++)
		if(n%i==0)
		{
			ans=ans*(i-1)/i;
			while(n%i==0) n/=i;
		}
	if(n>1) ans=ans*(n-1)/n;
	return ans;
}
```

时间复杂度 $O(\sqrt n)$。

> 性质 6：$\forall n>2$，$\varphi(n)$ 为偶数。
> 
> 证明：由于 $\varphi(n)=n\prod\frac{p_i-1}{p_i}$，所以如果 $\varphi(n)$ 含有积质因子，那么 $p_i-1$ 为偶数，不成立。
> 
> 那么 $n$ 只含有质因子 $2$，记 $n=2^k$，则 $\varphi(n)=2^{k-1}$，显然此时只有 $k=1$ 有贡献，即 $n=2$。
> 
> 还有一种情况，$n$ 不含质因子，故 $n=1$。所以性质成立。
## 欧拉定理
### 欧拉定理
> 欧拉定理：若 $a\perp n$，则：
> 
> $$a^{\varphi(n)}\equiv 1\pmod n$$
### 费马小定理
$n$ 为质数时，$\varphi(n)=n-1$，则：

$$a^{n-1}\equiv 1\pmod n$$
## 欧拉定理的应用
### 求乘法逆元
> 性质 7：若 $a\perp n$，则：
> 
> $$a^{-1}\equiv a^{\varphi(n)-1}\pmod n$$
### 指数降幂
> 推论 1：若 $a\perp n$，则：
> 
> $$a^b\equiv a^{b\bmod \varphi(n)}\bmod n$$
## 扩展欧拉定理
> 扩展欧拉定理：对于任意正整数 $a,n$ 和非负整数 $b$：
> 
> $$a^b\equiv\begin{cases}a^b\bmod n&b<\varphi(n)\\a^{b\bmod \varphi(n)+\varphi(n)}\bmod n&b\ge \varphi(n)\end{cases}$$
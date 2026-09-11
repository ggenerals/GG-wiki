---
authors:
   - name: Gcend
     github: Gcend-gen
---

本文作者： {{ page_creator(page.file.src_uri) }}

# 最大公因数
为什么要专门开一个子目讲这个啊？！

## 基础概念

首先，两个非负整数 $x,y$ 的公因数为 $k$，当且仅当，$k \mid x$ 且 $k \mid y$。

而最大公因数 $z$ 就是 $x,y$ 的所有公因数中最大的那一个。

记作，$\gcd(x,y)=z$。

与之对应的，我们有最小公倍数。  

两个非负整数 $x,y$ 的公倍数为 $k$，当且仅当，$x \mid k$ 且 $y \mid k$。

而最小公倍数 $z$ 就是 $x,y$ 的所有公倍数中最小的那一个。

记作，$\text{lcm}(x,y)=z$。

---

通过定义，我们可以得到：

$$\gcd(1,a)=1$$

$$\gcd(0,a)=a$$

特别的，$\gcd(0,0)$ 存在争议，一部分人认为其无意义，另一部分人认为其值为 $0$。

---

**性质 1：** $ab=\gcd(a,b) \text{lcm}(a,b)$。

??? note "证明"

    设 $a,b$ 的所有质因子组成集合 $P$，对于 $p \in P$，设

    $$v_p(a)=\alpha,v_p(b)=\beta$$

    其中 $v_p(x)$ 表示 $p$ 在 $x$ 的唯一分解中出现的次数。

    那么：

    $$v_p(ab)=\alpha + \beta$$  

    另一方面，根据最大公因数和最小公倍数的定义，

    $$v_p(\gcd(a,b))=\min(\alpha,\beta)$$

    $$v_p(\operatorname{lcm}(a,b)(a,b))=\max(\alpha,\beta)$$

    而显然有

    $$\min(\alpha,\beta)+\max(\alpha,\beta)=\alpha + \beta$$

    所以

    $$v_p(\gcd(a,b)\operatorname{lcm}(a,b)(a,b))=\alpha + \beta=v_p(ab)$$

    对于每一个质数 $p$，两边的质因数分解中 $p$ 的指数都相同。

    由唯一分解定理，两个正整数的质因数分解完全相同就说明它们相等，因此
    
    $$ab=\gcd(a,b)\operatorname{lcm}(a,b)$$


## 求解方式

**性质 2：** 当 $a>b$ 时，$\gcd(a,b)=\gcd(a-b,b)$。

??? note "证明"

    设 $k=\gcd(a,b)$，那么有 $k \mid a,k \mid b$。

    所以有 $k|a-b$ 又因为 $k|b$，所以 $k$ 为 $a-b$ 与 $b$ 的公因数。

    对于 $t \nmid a,t \mid b$ 或 $t \mid a,t \nmid b$。

    有 $t \nmid a-b$，所以不会产生新的公共因子。

    那么当 $a>b$ 时，$\gcd(a,b)=\gcd(a-b,b)$。 

通过这种方式求最大公因数的方法叫做**辗转相减法（更相减损术）**。

---

**性质 3：** 当 $a>b$ 时，$\gcd(a,b)=\gcd(a \mod b,b)$。

??? note "证明"

    一直使用 **性质 2**，直到 $a \le b$。

通过这种方法求最大公因数的方法叫做**辗转相除法**。

这种做法的时间复杂度是 $O(\log \max(a,b))$。

??? note "时间复杂度证明"

    不妨设 $a>b$。

    1. $b \ge \frac{a}{2}$，那么 $a-b \le \frac{a}{2}$。
    
    2. $b < \frac{a}{2}$，那么 $a \mod b < b < \frac{a}{2}$。

    那么每次 $a$ 或 $b$ 会减少至少一半，所以总共只会进行 $O(\log \max(a,b))$ 次。

over.
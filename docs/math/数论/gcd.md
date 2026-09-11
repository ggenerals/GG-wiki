---
authors:
   - name: Gcend
     github: Gcend-gen
---

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

通过这种方法，重复递归，直到其中一项为 $0$，另一项的值即为 $\gcd(a,b)$，这种求最大公因数的方法叫做**辗转相减法（更相减损术）**。

---

**性质 3：** 当 $a>b$ 时，$\gcd(a,b)=\gcd(a \bmod b,b)$。

??? note "证明"

    一直使用 **性质 2**，直到 $a < b$。

通过这种方法，重复递归，直到其中一项为 $0$，另一项的值即为 $\gcd(a,b)$，这种求最大公因数的方法叫做**欧几里德算法（辗转相除法）**。

这种做法的时间复杂度是 $O(\log \max(a,b))$。

??? note "时间复杂度证明"

    不妨设 $a>b$。

    1. $b \ge \frac{a}{2}$，那么 $a-b \le \frac{a}{2}$。
    
    2. $b < \frac{a}{2}$，那么 $a \bmod b < b < \frac{a}{2}$。 

    那么每次 $a$ 或 $b$ 会减少至少一半，所以总共只会进行 $O(\log \max(a,b))$ 次。

事实上，我们有一个函数 `__gcd(a,b)` 可以得到 $\gcd(a,b)$，但还是推荐自己写代码。

代码示例如下，

```cpp linenums="1"
int gcd(int x,int y){ // 传入的 x > y
    if(!y) return x;
    return gcd(y,x%y);
}
```

## 扩展欧几里德定理

扩展欧几里德定理用于求解二元一次不等式组的整数解问题，简称为 $\text{exgcd}$。

### 裴蜀定理

**定理 1：** 若 $a,b$ 是不全为 $0$ 的非负整数，那么对于任意整数 $x,y$，均有 $\gcd(x,y) \mid a x + b y$ 成立；而且，存在整数 $x,y$，使得 $a x + b y = \gcd(a,b)$。

??? note "证明"

    等待后人更新。

我们可以通过裴蜀定理判断二元一次不定方程是否存在整数解。

### 求解过程

若方程存在整数解，我们可以在与欧几里德算法相同复杂度的情况下求出该方程的一组整数解。

???+ question "例题"

    求出 $a x + b y = c$ 的一组整数解。

???+ note "求解过程"

    首先，利用裴蜀定理判断解的存在性。

    如果有解，那么 $a x + b y = c = k \times \gcd(a,b)$。

    那么我们先求出 $a x’ +b y‘=\gcd(a,b)$ 的解，然后扩大 $k$ 倍即为答案。

    设

    $$a x_1 + b y_1 = \gcd(a,b)$$

    $$b x_2 + (a \bmod b) y_2 = \gcd(b,a \bmod b)$$

    所以 

    $$a x_1 + b y_1 = b x_2 + (a \bmod b) y_2$$

    $$a x_1 + b y_1 = b x_2 + (a - (\lfloor \frac{a}{b} \rfloor) \times b) y_2$$

    $$a x_1 + b y_1 = a y_2 + b (x_2 - \lfloor \frac{a}{b} \rfloor y_2)$$

    因为 $a = a,b = b$，所以，

    $$x_1 = y_2,y_1 = x_2 - \lfloor \frac{a}{b} \rfloor y_2$$

    递归求解即可，直到 $b = 0$ 时，$x = 1,y = 0$。

---

代码示例如下，

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
```

函数的返回值为 $\gcd(a,b)$，$x,y$ 在递归中被求解。

---

Over.

感谢 Gcend 编写此页面。
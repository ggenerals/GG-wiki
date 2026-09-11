---
authors:
   - name: Gcend
     github: Gcend-gen
---

本文作者： {{ page_creator(page.file.src_uri) }}

# 最大公因数
为什么要专门开一个子目讲这个啊？！

首先，两个非负整数 $x,y$ 的公因数为 $k$，当且仅当，$k|x$ 且 $k|y$。

而最大公因数 $z$ 就是 $x,y$ 的所有公因数中最大的那一个。

记作，$\gcd(x,y)=z$。

与之对应的，我们有最小公倍数。  

两个非负整数 $x,y$ 的公倍数为 $k$，当且仅当，$x|k$ 且 $y|k$。

而最小公倍数 $z$ 就是 $x,y$ 的所有公倍数中最小的那一个。

记作，$\text{lcm}(x,y)=z$。

---

**定理：** $ab=\gcd(a,b) \text{lcm}(a,b)$。

!!! note 证明：

  设 $a,b$ 的所有质因子组成集合 $P$，对于 $p \in P$，设

  $$v_p{a}=\alpha,v_p(b)=\beta$$

  其中 $v_p(x)$ 表示 $p$ 在 $x$ 的唯一分解中出现的次数。

  那么：

  $$v_p(ab)=\alpha + \beta$$  

  另一方面，根据最大公因数和最小公倍数的定义，

  $$v_p(\gcd(a,b))=\min(\alpha,\beta)$$

  $$v_p(\text{lcm}(a,b))=\max(\alpha,\beta)$$

  而显然有

  $$\min(\alpha,\beta)+\max(\alpha,\beta)=\alpha + \beta$$

  所以

  $$v_p(\gcd(a,b)\text{lcm}(a,b))=\alpha + \beta=v_p(ab)$$

  对于每一个质数 $p$，两边的质因数分解中 $p$ 的指数都相同。

  由唯一分解定理，两个正整数的质因数分解完全相同就说明它们相等，因此

  $$ab=\gcd(a,b)\text{lcm}(a,b)$$
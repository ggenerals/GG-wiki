# 向量入门
## 向量
向量是既有大小，又有方向的量。

零向量记作 $\vec 0$。单位向量满足 $|\vec e|=1$。

向量加法：平行四边形法则。向量加法满足交换律和结合律。

向量减法：$\vec a-\vec b=\vec a+(-\vec b)$。

向量也可以用坐标表示。

向量乘法：记 $\vec a$ 和 $\vec b$ 形成夹角 $\theta$，则：

- 向量点乘：$\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta$。  
  其物理意义为 $\vec a$ 在 $\vec b$ 方向做的功。

$$(x_1,y_1)\cdot(x_2,y_2)=x_1x_2+y_1y_2$$
- 向量叉乘：$\vec a\times\vec b=|\vec a||\vec b|\sin\theta$。  
  其几何意义为 $\vec a$ 与 $\vec b$ 所夹的面积。
  
$$(x_1,y_1)\times(x_2,y_2)=x_1y_2-y_1x_2$$

向量叉乘没有交换律，但是点乘有。

通过点乘，我们可以发现 $\vec{v_1}=(x_1,y_1),\vec{v_2}=(x_2,y_2)$ 夹角为 $\cos\theta=\dfrac{\vec{v_1}\cdot \vec{v_2}}{|\vec{v_1}||\vec{v_2}|}=\dfrac{x_1x_2+y_1y_2}{\sqrt{x_1^2+y_1^2}\sqrt{x_2^2+y_2^2}}$.
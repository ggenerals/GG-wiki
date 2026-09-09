# 线段树基础
## 线段树
线段树，顾名思义就是存储线段的树。它适合用来处理区间修改与查询的问题。

一棵最普通的线段树的结构长什么样子呢，每个节点表示一段区间 $\left[l,r\right]$，并且有两个子区间，左区间是 $\left[l,mid\right]$，右区间是 $\left[mid+1,r\right]$。至于节点的编号，很简单，根节点编号是 $1$，对于一个点 $k$，它的左儿子的编号是 $2k$，右儿子的编号是 $2k+1$。

每一个节点存储你需要的信息，但这个信息必须满足可合并性。因为你需要先算出两个子区间的信息（叶子节点的信息已知，所以只能从下往上），再合并到当前的区间。这个操作叫做 `push_up`。对于查询和修改的区间，我们的处理是将这个区间分割为几个线段树上的区间，去修改或查询几个小区间的信息。这时，线段树特殊的结构就发挥作用了。

我们不难看出每个区间的长度都是 $2$ 的幂次级别的，所以这棵树只有 $\log$ 层。我们考虑一个修改或查询区间 $\left[L,R\right]$，对这个区间的长度进行二进制拆分，每一个 $2$ 的幂次，总能在线段树上找到一个长度和它一个级别的区间，所以只会修改 $\log$ 个区间，于是，我们美丽的线段树拥有一个美丽的时间复杂度：单 $\log$。

我们来看一个经典的题目：单点修改，查询区间和，$n\le 10^5$。显然不能 $O(n^2)$ 暴力，考虑线段树。为了方便，我们先 `define` 一下：

```cpp
#define ls k<<1
#define rs k<<1|1
```

先考虑信息可不可以合并，显然大区间的和等于等个子区间的和相加，于是我们可以写出 `push_up`：

```cpp
void push_up(int k){
    tree[k]=tree[ls]+tree[rs];
}
```

我们然后要建树：

```cpp
void build(int k,int l,int r){//编号k的节点表示[l,r]这个区间
    if(l==r){
        tree[k]=a[l];//叶子节点就是单个数值
        return ;
    }
    int mid=(l+r)/2;
    build(ls,l,mid);//递归左区间
    build(rs,mid+1,r);//递归右区间
    push_up(k);//记得合并
}
```

然后是单点修改：

```cpp
void update(int p,int x,int k,int l,int r){//将a[p]修改为x
    if(l==r){//此时叶子节点一定是p的位置
        tree[p]=x;
        return ;
    }
    int mid=(l+r)/2;
    if(p<=mid){//表示p在左区间
        update(p,x,ls,l,mid);
    }else{//否则在右区间
        update(p,x,rs,mid+1,r);
    }
    push_up(k);//千万千万记得合并
}
```

最后区间查询：

```cpp
int query(int L,int R,int k,int l,int r){//[L,R]是查询区间，[l,r]是线段树区间
    if(l>=L&&r<=R){//当前的线段树区间包含在查询区间内
        return tree[k];
    }
    int mid=(l+r)/2,ans=0;
    if(L<=mid){//如果左区间包含有查询区间
        ans=query(L,R,ls,l,mid);
    }
    if(R>mid){//如果右区间包含有查询区间
        ans+=query(L,R,rs,mid+1,r);
    }
    return ans;
}
```

或者给出 sLMxf 的写法：

```cpp
int query(int L,int R,int k,int l,int r){
    if(L<=l&&r<=R) return tree[k];
    if(r<L||R<l) return 0;//判断与查询区间没有交就变成 0
    int mid=(l+r)/2;
    return query(L,R,ls,l,mid)+query(L,R,rs,mid+1,r);
}
```
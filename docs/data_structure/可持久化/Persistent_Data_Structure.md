# 可持久化数据结构

## 主席树

简单来说，利用前缀和的思想以及动态开点的优势，主要处理区间第 $k$ 小问题。  
一般的，对于每个 $i$，维护区间 $[1,i]$ 的权值线段树。考虑从 $[1,i-1]$ 到 $[1,i]$ 只进行了一次单点修改，只会改变 $log(n)$ 个节点，记录下来，对每个 $i$ 就有了不同的根 `rt[i]`，称每一个 `rt[i]` 所对应的线段树为一个版本。(顺一张图片，[来源](https://www.luogu.com.cn/article/obv7afu2))
![](https://img2024.cnblogs.com/blog/3357233/202607/3357233-20260701144834742-1981901136.png)

然后是模板：
```cpp linenums="1"
struct node{
    int v,ls,rs;
}tr[N];//动态开点，存左右儿子
int rt[N],tot;//每个版本的根、节点个数
#define ls(A) tr[(A)].ls
#define rs(A) tr[(A)].rs
int nw(node x){
    return tr[++tot]=x,tot;
}//新建节点
void build(int &p,int l,int r){
    p=++tot;
    if(l==r)return cin>>tr[p].v,void();
    int mid=(l+r)>>1;
    build(ls(p),l,mid),build(rs(p),mid+1,r);
    return ;
}
void insert(int v,int &p,int l,int r,int pos,int x){
    p=nw(tr[v]);//原来的版本为v,新建的版本为p
    if(l==r)return tr[p].v=x,void();
    int mid=(l+r)>>1;
    if(pos<=mid)insert(ls(p),ls(p),l,mid,pos,x);
    else insert(rs(p),rs(p),mid+1,r,pos,x);
    return ;
}
int query(int p,int l,int r,int pos){
    if(l==r)return tr[p].v;
    int mid=(l+r)>>1;
    if(pos<=mid)return query(ls(p),l,mid,pos);
    else return query(rs(p),mid+1,r,pos);
}
```

### 习题

#### [P2633 Count on a tree](https://www.luogu.com.cn/problem/P2633)

一道主席树解决树上问题的板子，难度较低。考虑 $u,v$ 之间的信息可以用 $tr[u]+tr[v]-tr[lca(u,v)]-tr[fa[lca(u,v)]]$ 表示，这个是显然的，然后你发现离散化一下就做完了。

#### [P5283 [十二省联考 2019] 异或粽子](https://www.luogu.com.cn/problem/P5283)

先做一遍前缀异或和，考虑一个 $n*n$ 的矩阵，$A(i,j)=s_i\oplus s_j$，注意到这个矩阵会关于对角线对称，并且对角线上都是 $0$。对于每一个 $a_i$ 求出 $rk_{1,i}$，即所有 $a_i \oplus a_j,1\le j\le n$ 中异或值第 $1$ 大的 $j$，然后丢到堆里，每次取最大的一个，不妨设取出来的为 $(x,y)$，表示其为与 $a_i$ 的异或值中的 $y$ 大的。统计答案，然后将 $(x,y+1)$ 丢到堆中，这样做的正确性自证不难。~~所以这和可持久化有什么关系~~

[P4735 最大异或和](https://www.luogu.com.cn/problem/P4735)

可持久化 Trie 练习题.
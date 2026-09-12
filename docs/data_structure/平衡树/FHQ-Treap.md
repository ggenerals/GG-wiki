# FHQ Treap

$\text{FHQ Treap}$，也被称为无旋 $\text{Treap}$，是一种时间复杂度较好，且支持可持久化的平衡树。

不同于大部分平衡树通过旋转操作维护序列平衡，$\text{FHQ Treap}$ 通过分裂与合并操作维护平衡树。同时，$\text{FHQ Treap}$ 通过随机赋权（即优先级），并调整其结构使其优先级满足堆性质的方式维护树高为 $O(\log n)$。

简单来说就是：权值满足 $\text{BST}$ 性质，优先级满足堆性质。

一些变量和基础操作定义：

```cpp
mt19937 rnd(time(0));//随机数生成器
int tot,rt;//节点数，根节点
int val[N],w[N],siz[N],ls[N],rs[N];//权值，优先级（大根堆），子树大小，左/右儿子

int nw(int v){//创建权值为 v 的新节点
    tot++;
    val[tot]=v;w[tot]=rnd();siz[tot]=1;
    return tot;
}

void up(int x){//更新 siz
    siz[x]=siz[ls[x]]+siz[rs[x]]]+1;
}
```


接下来讲解 $\text{FHQ-Treap}$ 的基础操作：**split** 和 **merge**。

**split**：将一棵平衡树按特定权值分为两棵。

```cpp
void split(int p,int &x,int &y,int v){//需要分裂的节点，分裂后 <=v 的部分和 >v 的部分
    if(p==0)return x=y=0,void();
    if(val[p]<=v){//若 val[p]<=v，则 p 及 ls[p] 都为 x 的一部分，在 rs[p] 继续分裂
        x=p;
        split(rs[p],rs[x],y,v);//递归处理 rs[x] 和 y
        up(x);
    }else{//反之，则 p 及 rs[p] 都为 y 的一部分，在 ls[p] 继续分裂
        y=p;
        split(ls[p],x,ls[y],v);//递归处理 x 和 ls[y]
        up(y);
    }
}
```

**merge**：合并两棵平衡树。由于我们在用到合并操作时，一棵树的所有节点的权值必定会小于等于另一棵树，所以合并操作是简单的。

```cpp
int merge(int x,int y){//左树，右树
    if(!x||!y)return x+y;//若其中一个节点为空，则返回另一个节点
    //让优先级较大的节点作为父亲以满足堆性质
    if(w[x]>w[y]){//x 作为父亲，y 接在 x 的右儿子，与 rs[x] 合并
        rs[x]=merge(rs[x],y);
        return up(x),x;
    }else{//同理
        ls[y]=merge(x,ls[y]);
        return up(y),y;
    }
}
```

非常简单对吧？那么其他操作你也可以轻松实现了。

**插入**：把权值 `<=v` 的树分裂出来，再和 `v` 合并。

```cpp
void insert(int v){
    int x,y;
    split(rt,x,y);
    rt=merge(merge(x,nw(v)),y);
}
```

**删除**：把权值只有 `v` 的树分裂出来，合并它的左右儿子（删掉根），再合并回去。

```cpp
void erase(int v){
    int w,x,y,z;
    split(rt,w,z,v);//w 为权值 <=v 的树
    split(w,x,y,v-1);//x 为权值 <v 的树，那么 y 就是只有 v 的树了
    rt=merge(merge(x,merge(ls[y],rs[y])),z);
}
```

**查询 v 的排名**：把权值 `<v` 的树分裂出来，得到其 `siz`。

```cpp
int getRank(int v){
    int x,y,res;
    split(x,y,v-1);
    res=siz[x]+1;
    return rt=merge(x,y),res;
}
```

**查询排名为 k 的数**：递归往下找。

```cpp
int getKth(int k,int x=rt){
    int lsiz=siz[ls[x]];
    if(k<=lsiz)return getKth(k,ls[x]);//此时排名 k 所在的位置被 ls[x] 包含
    if(k==lsiz+1)return val[x];//当前子树的第 (lsiz+1) 位就是 x
    return getKth(k-lsiz-1,ls[x]);//在 rs[x] 找，x 的第 k 位，相当于 rs[x] 的第 (k-lsiz-1) 位
}
```

**查询 v 的前驱**：把权值 `<v` 的树分裂出来，得到前驱的排名。

```cpp
int getPre(int v){
    int x,y,rk;
    split(x,y,v-1);
    rk=siz[x];
    return rt=merge(x,y),getKth(rk);
}
```

**查询 v 的后继**：同理。

```cpp
int getNxt(int v){
    int x,y,rk;
    split(x,y,v);
    rk=siz[x]+1;
    return rt=merge(x,y),getKth(rk);
}
```

好的，你已经学会 $\text{FHQ Treap}$ 了（也许吧）。
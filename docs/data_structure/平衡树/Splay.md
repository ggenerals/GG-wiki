# Splay

>参考：<https://www.cnblogs.com/ying-xue/p/17122409.html>

$\text{Splay}$ 的核心是通过对一些节点进行旋转，改变这棵树的结构，让它趋于平衡。

![img](https://img2024.cnblogs.com/blog/3357233/202607/3357233-20260701141933024-686809448.png)  
: 这张图上的数字为编号不是权值...

**rotate:** 本质上是将一个节点上移。比如上图右旋的过程相当于将节点 2 上移。

```cpp
void rotate(int x){//旋转操作
    int y = fa[x],z = fa[y],chk = get(x);//爹，爹的爹，是爹的哪个儿子
    ch[y][chk] = ch[x][chk^1];//如果我是爹的左儿子，把我的右儿子给爹的左儿子//如果是右儿子，把我的左儿子给爹的右儿子
    if(ch[x][chk^1])fa[ch[x][chk^1]] = y;//把这个儿子的爹改成我的爹
    ch[x][chk^1] = y;//父子关系换了，哈哈！
    fa[y] = x;fa[x] = z;//哈哈！哈哈！
    if(z)ch[z][y == ch[z][1]] = x;//如果爹的爹存在，更新儿子，你滴儿子是我辣！
    maintain(x);maintain(y);//pushup pushup
}
```

**splay:** 将一个节点通过不断的旋转转到根的位置。

```cpp
void splay(int x){
    for(int f;f = fa[x];rotate(x))//我还有爹吗，有就旋
    if(fa[f])rotate(get(x) == get(f) ? f : x);//如果有爹，相同的话要先旋爹
    root = x;//我是根辣！
}
```

一些辅助函数
```cpp
inline int nw(int key){
    return tr[++idx].key=key,tr[idx].siz=1,idx;
}
inline void push_up(int x){
    tr[x].siz=tr[ls(x)].siz+tr[rs(x)].siz+1;
}
inline void clear(int x){
    ls(x)=rs(x)=fa(x)=tr[x].siz=tr[x].key=0;
}
inline int get(int x){
    return x==rs(fa(x));
}
```

**插入**
```cpp
void ins(int key){
    int now=rt,f=0;
    while(now)f=now,now=tr[now].s[key>tr[now].key];
    now=nw(key),fa(now)=f,tr[f].s[key>tr[f].key]=now,splay(now);
    return ;
}
```

**删除**
```cpp
void del(int key){
    int now=rt,p=0;
    while(now&&tr[now].key!=key)
        p=now,now=tr[now].s[tr[now].key<key];
    if(!now)return splay(p),void();
    splay(now);
    int cur=ls(now);
    if(!cur)
        return rt=rs(now),fa(rs(now))=0,clear(now),void();
    while(rs(cur))cur=rs(cur);
    rs(cur)=rs(now),fa(rs(now))=cur,fa(ls(now))=0,clear(now);
    push_up(cur),splay(cur);
    return ;
}
```

**查询数x的前驱**
```cpp
int pre(int key){
    int now=rt,ans=0,f=0;
    while(now){
        f=now;
        if(tr[now].key>=key)now=ls(now);
        else ans=tr[now].key,now=rs(now);
    }
    return splay(f),ans;
}
```

**查询数x的后继**
```cpp
int nxt(int key){
    int now=rt,ans=0,f=0;
    while(now){
        f=now;
        if(tr[now].key<=key)now=rs(now);
        else ans=tr[now].key,now=ls(now);
    }
    return splay(f),ans;
}
```

**数x是第几大的（比x小的数的个数+1）**
```cpp
int rnk(int key){
    int now=rt,ans=1,f=0;
    while(now){
        f=now;
        if(tr[now].key<key)ans+=tr[ls(now)].siz+1,now=rs(now);
        else now=ls(now);
    }
    return splay(f),ans;
}
```

**查询第x大的数**
```cpp
int kth(int rk){
    int now=rt;
    while(now){
        int sz=tr[ls(now)].siz+1;
        if(sz>rk)now=ls(now);
        else if(sz==rk)break;
        else rk-=sz,now=rs(now);
    }
    return splay(now),tr[now].key;
}
```

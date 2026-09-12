# Welcome to GenGen wiki

这里是 GenGen-wiki，一个由 GGenerals 维护的 wiki。

<div style="text-align: center; margin: 20px 0;">
    <button id="openModalBtn" style="padding: 10px 20px; font-size: 16px; color: #fff; background-color: #ff4d4f; border: none; border-radius: 4px; cursor: pointer; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
        ❤ 赞赏支持
    </button>
</div>

<div id="rewardModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.6); z-index: 9999; justify-content: center; align-items: center;">
    <div style="position: relative; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); text-align: center; max-width: 90%; width: 520px;">
        <span id="closeModalBtn" style="position: absolute; top: 5px; right: 15px; font-size: 28px; cursor: pointer; color: #999; line-height: 1;">&times;</span>
        <img src="https://cdn.luogu.com.cn/upload/image_hosting/7uzglkak.png" alt="赞赏吗" style="display: block; max-width: 100%; height: auto; border-radius: 4px; margin-top: 10px;">
    </div>
</div>
<script>
    (function(){
        const modal=document.getElementById('rewardModal');
        const openBtn=document.getElementById('openModalBtn');
        const closeBtn=document.getElementById('closeModalBtn');
        openBtn.onclick=function(){
            modal.style.display='flex';
        }
        closeBtn.onclick=function(){
            modal.style.display='none';
        }
        modal.onclick=function(event){
            if(event.target===modal){
                modal.style.display='none';
            }
        }
    })();
</script>

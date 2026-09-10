import subprocess
from pathlib import Path

def define_env(env):
    @env.macro
    def page_creator(page_file_path):
        """
        传入当前页面的相对路径（如 'docs/index.md'），
        返回该文件在 Git 仓库中的首次提交作者（创建者）。
        """
        repo_root = Path(env.project_dir)
        # 构建文件的绝对路径
        file_path = repo_root / page_file_path

        if not file_path.exists():
            return "Unknown Creator"

        try:
            # git log --follow --diff-filter=A 获取首次创建该文件的提交
            # --format=%an 只取作者名字，%ae 可加邮箱，此处只取名字
            cmd = [
                'git', 'log', '--follow', '--diff-filter=A',
                '--format=%an', '--', str(file_path)
            ]
            result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            
            # git log 默认最新的提交在前（倒序），因此最后一行是初始提交
            if lines and lines[0]:
                # 注意：若文件从未提交过，lines 为空
                return lines[-1]  # 取最后一行，即创建者
            else:
                return "Uncommitted File"
        except Exception as e:
            return f"Error: {str(e)}"
import subprocess
from pathlib import Path


def define_env(env):
    @env.macro
    def page_creator(page_file_path):
        """
        传入 page.file.src_uri（相对于 docs 目录的路径），
        返回该文件在 Git 仓库中的首次提交作者。
        """
        repo_root = Path(env.project_dir).resolve()

        # docs_dir 可能配置为 "docs"，也可能是别的名字
        docs_dir = env.conf.get("docs_dir", "docs")
        docs_dir_path = (repo_root / docs_dir).resolve()

        # 拼接出文件的真实绝对路径
        file_abs = (docs_dir_path / page_file_path).resolve()

        if not file_abs.exists():
            return f"Unknown Creator (path: {file_abs})"

        # git 需要相对仓库根目录的路径
        try:
            rel_path = file_abs.relative_to(repo_root)
        except ValueError:
            return "Unknown Creator (outside repo)"

        try:
            cmd = [
                "git", "log", "--follow", "--diff-filter=A",
                "--format=%an", "--", str(rel_path)
            ]
            result = subprocess.run(
                cmd, cwd=str(repo_root),
                capture_output=True, text=True
            )

            if result.returncode != 0:
                return f"Git error: {result.stderr.strip()}"

            # git log 默认最新在前，最后一行才是最初的创建提交
            lines = [l for l in result.stdout.strip().split("\n") if l]
            if lines:
                return lines[-1]
            else:
                return "Uncommitted File"
        except Exception as e:
            return f"Error: {e}"
import subprocess
from pathlib import Path


def define_env(env):
    @env.macro
    def page_creator(page_file_path):
        """
        返回该文件最早一次提交的作者（= 创建者）。
        传入的是 page.file.src_uri（相对 docs 目录的路径）。
        """
        repo_root = Path(env.project_dir).resolve()
        docs_dir = env.conf.get("docs_dir", "docs")
        file_abs = (repo_root / docs_dir / page_file_path).resolve()

        if not file_abs.exists():
            return "Unknown Creator"

        try:
            rel_path = file_abs.relative_to(repo_root)
        except ValueError:
            return "Unknown Creator"

        try:
            # --reverse：最旧的提交排在最前
            # 不用 --follow / --diff-filter，避免两者互相干扰
            cmd = [
                "git", "log", "--reverse",
                "--format=%an", "--", str(rel_path)
            ]
            result = subprocess.run(
                cmd, cwd=str(repo_root),
                capture_output=True, text=True
            )

            if result.returncode != 0:
                return "Unknown Creator"

            lines = [l for l in result.stdout.strip().split("\n") if l]
            if lines:
                return lines[0]   # 第一条 = 最旧 = 创建者
            return "Uncommitted File"
        except Exception:
            return "Unknown Creator"
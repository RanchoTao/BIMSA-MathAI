from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

import mkdocs_gen_files


ROOT = Path(__file__).resolve().parent

COURSES = [('程序设计', '2025秋/Python', 'courses/2025-fall/programming.md'), ('个人自选', '2025秋/个人自选', 'courses/2025-fall/personal-electives.md'), ('数学分析', '2025秋/数学分析', 'courses/2025-fall/mathematical-analysis.md'), ('机器学习', '2025秋/机器学习', 'courses/2025-fall/machine-learning.md'), ('毛泽东思想和中国特色社会主义理论体系概论', '2025秋/毛泽东思想和中国特色社会主义理论体系概论', 'courses/2025-fall/mao-zedong-thought.md'), ('物理', '2025秋/物理', 'courses/2025-fall/physics.md'), ('羽毛球', '2025秋/羽毛球', 'courses/2025-fall/badminton.md'), ('英语演讲', '2025秋/英语演讲', 'courses/2025-fall/english-speech.md'), ('马克思主义基本原理', '2025秋/马克思主义基本原理', 'courses/2025-fall/marxism.md'), ('大学体育', '2026春/大学体育', 'courses/2026-spring/physical-education.md'), ('大学物理', '2026春/大学物理', 'courses/2026-spring/college-physics.md'), ('应用概率与数理统计', '2026春/应用概率与数理统计', 'courses/2026-spring/probability-statistics.md'), ('数学分析', '2026春/数学分析', 'courses/2026-spring/mathematical-analysis.md'), ('数学建模', '2026春/数学建模', 'courses/2026-spring/mathematical-modeling.md'), ('数据挖掘', '2026春/数据挖掘', 'courses/2026-spring/data-mining.md'), ('数据结构与算法分析', '2026春/数据结构与算法分析', 'courses/2026-spring/data-structures-algorithms.md'), ('机器学习', '2026春/机器学习', 'courses/2026-spring/machine-learning.md'), ('离散数学', '2026春/离散数学', 'courses/2026-spring/discrete-mathematics.md'), ('复变函数', '2026秋/复变函数', 'courses/2026-fall/complex-analysis.md'), ('实变函数', '2026秋/实变函数', 'courses/2026-fall/real-analysis.md'), ('数字信号处理', '2026秋/数字信号处理', 'courses/2026-fall/digital-signal-processing.md'), ('数据库原理与应用', '2026秋/数据库原理与应用', 'courses/2026-fall/database-systems.md'), ('时间序列模型', '2026秋/时间序列模型', 'courses/2026-fall/time-series.md'), ('深度学习', '2026秋/深度学习', 'courses/2026-fall/deep-learning.md'), ('计算机组成原理', '2026秋/计算机组成原理', 'courses/2026-fall/computer-organization.md'), ('随机过程', '2026秋/随机过程', 'courses/2026-fall/stochastic-processes.md'), ('高等代数', '2026秋/高等代数', 'courses/2026-fall/advanced-algebra.md'), ('图像处理与计算机视觉', '2027春/图像处理与计算机视觉', 'courses/2027-spring/image-processing-computer-vision.md'), ('图论', '2027春/图论', 'courses/2027-spring/graph-theory.md'), ('多元统计分析', '2027春/多元统计分析', 'courses/2027-spring/multivariate-statistics.md'), ('拓扑学与应用', '2027春/拓扑学与应用', 'courses/2027-spring/topology.md'), ('操作系统', '2027春/操作系统', 'courses/2027-spring/operating-systems.md'), ('数字通信和计算机网络', '2027春/数字通信和计算机网络', 'courses/2027-spring/communications-networks.md'), ('泛函分析', '2027春/泛函分析', 'courses/2027-spring/functional-analysis.md'), ('现代人工智能系统', '2027春/现代人工智能系统', 'courses/2027-spring/modern-ai-systems.md'), ('自动控制原理', '2027春/自动控制原理', 'courses/2027-spring/automatic-control.md'), ('自然语言处理', '2027春/自然语言处理', 'courses/2027-spring/natural-language-processing.md'), ('计算机图形学', '2027春/计算机图形学', 'courses/2027-spring/computer-graphics.md'), ('人工智能创业：从想法到产品', '2027秋/人工智能创业：从想法到产品', 'courses/2027-fall/ai-entrepreneurship.md'), ('博弈论', '2027秋/博弈论', 'courses/2027-fall/game-theory.md'), ('机器学习中的优化算法', '2027秋/机器学习中的优化算法', 'courses/2027-fall/optimization-for-machine-learning.md'), ('科学素养与伦理', '2027秋/科学素养与伦理', 'courses/2027-fall/scientific-literacy-ethics.md'), ('高等概率论', '2027秋/高等概率论', 'courses/2027-fall/advanced-probability.md'), ('创新创业讲座', '2028春/创新创业讲座', 'courses/2028-spring/innovation-entrepreneurship.md'), ('密码学', '2028春/密码学', 'courses/2028-spring/cryptography.md'), ('科技创业融资与股权设计', '2028春/科技创业融资与股权设计', 'courses/2028-spring/startup-finance-equity.md'), ('量子力学', '2028春/量子力学', 'courses/2028-spring/quantum-mechanics.md'), ('高等数值分析', '2028春/高等数值分析', 'courses/2028-spring/advanced-numerical-analysis.md'), ('高等数理统计', '2028春/高等数理统计', 'courses/2028-spring/advanced-mathematical-statistics.md')]


def read_course_readme(source_dir: str) -> str:
    directory = ROOT / source_dir
    for filename in ("README.md", "README"):
        path = directory / filename
        if path.is_file():
            return path.read_text(encoding="utf-8").strip()
    return ""


for title, source_dir, output_path in COURSES:
    readme = read_course_readme(source_dir)
    source_url = (
        "https://github.com/RanchoTao/BIMSA-MathAI/tree/main/"
        + quote(source_dir, safe="/")
    )

    with mkdocs_gen_files.open(output_path, "w") as page:
        page.write("---\n")
        page.write("hide:\n")
        page.write("  - edit\n")
        page.write("---\n\n")
        page.write(f"# {title}\n\n")

        if readme:
            page.write(readme)
            page.write("\n\n")
        else:
            page.write(
                "该课程页面已经接入 Wiki，课程说明与学习资料正在继续整理。\n\n"
            )

        page.write("## 课程资料\n\n")
        page.write(
            f"课程文件、讲义与历史附件保留在"
            f"[原始资料目录]({source_url})中。\n"
        )

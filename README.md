# BIMSA MathAI Wiki

面向 BIMSA 数学与人工智能项目学习者的非官方开放知识库，以 MkDocs Material 将 Markdown 内容构建为可搜索的网页书。历史课程附件继续保留在原有学期目录中，网站通过索引渐进整理，不做破坏性迁移。

> **非官方声明：**本项目由社区维护，与 BIMSA 官方无隶属或授权关系。培养方案、课程安排与考核要求请以官方信息为准。

## 网站

- GitHub Pages：<https://ranchotao.github.io/BIMSA-MathAI/>
- 源代码与反馈：<https://github.com/RanchoTao/BIMSA-MathAI>

未来绑定自定义域名时，只需在 Pages 中配置域名，并同步修改 `mkdocs.yml` 的 `site_url`（以及按需添加 `docs/CNAME`）。

## 本地运行

需要 Python 3.10 或更高版本：

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

浏览器访问终端显示的本地地址。提交前请严格构建：

```bash
mkdocs build --strict
```

## 内容结构

- `docs/`：网页正文，包括新生、生存、课程、科研、工具、生活和关于板块。
- `docs/courses/resources.md`：历史课程附件的网页索引。
- `2025秋/` 至 `2028春/`：原始学期资料，暂不批量移动或直接纳入网站导航。
- `templates/`：新增结构化内容时使用的模板。
- `mkdocs.yml`：主题、插件和站点导航配置。

## 贡献

欢迎补充经过整理的课程笔记、学习经验、研究流程与工具教程。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，使用课程模板，并确保来源、隐私、版权和课程规则允许公开。修改后通过 Pull Request 提交。

本仓库代码与原创文档按 [MIT License](LICENSE) 提供；已有第三方附件仍遵循各自权利人的许可，MIT 许可不自动覆盖这些材料。

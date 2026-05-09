# Grok + Pillow 图示生成计划

这个仓库专门解决 Grok（或其他 AI）生成图片时**中文乱码、字体变形**的问题。

**工作流程**：
1. 用 Grok 生成**无中文**的干净底图（提示词里写 `no Chinese text, use placeholder boxes`）
2. 用本仓库的 Python 脚本**本地精准叠加中文文字**

---

## 快速开始（Windows）

### 1. 安装依赖
```bash
pip install -r requirements.txt

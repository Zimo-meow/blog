import os
import yaml

# docs 目录路径（相对于当前脚本所在位置）
DOCS_DIR = "docs"

# MkDocs 基础配置
config = {
    "site_name": "My Study Blog",
    "theme": {
        "name": "material",
        "language": "zh"
    },
    "nav": []
}

def build_nav(path, base_dir):
    """
    递归扫描 docs 下的目录和文件，生成 nav 结构
    """
    nav_list = []
    items = sorted(os.listdir(path))
    for item in items:
        full_path = os.path.join(path, item)
        rel_path = os.path.relpath(full_path, base_dir).replace("\\", "/")

        if os.path.isdir(full_path):
            # 目录 -> 递归
            sub_nav = build_nav(full_path, base_dir)
            nav_list.append({item: sub_nav})
        elif item.lower().endswith(".md"):
            # Markdown 文件
            name = os.path.splitext(item)[0]
            nav_list.append({name: rel_path})
    return nav_list

# 构建 nav
config["nav"] = build_nav(DOCS_DIR, DOCS_DIR)

# 保存到 mkdocs.yml
with open("mkdocs.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, allow_unicode=True, sort_keys=False)

print("✅ mkdocs.yml 已生成完成！")

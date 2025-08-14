# 生成导航 & 本地构建
python generate_nav.py
mkdocs build

# 提交源码（包含 mkdocs.yml 的更新）
git add .
git commit -m "auto: update nav & content"
git push origin main

# 同步部署到 gh-pages（本地立即发布）
mkdocs gh-deploy --force
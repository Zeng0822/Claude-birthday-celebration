# Clawd 满月宴 · Cyber Moon Feast

Clawd 的赛博满月宴：一轮满月，一只头顶小红结的像素 Clawd，大家一起来喝满月酒。

公开网址（开启 GitHub Pages 后）：https://zeng0822.github.io/Claude-birthday-celebration/

## 宴席流程

- **请帖**：竖排红纸请帖，外加 Clawd 的满月档案
- **席间热闹**：放烟花、干杯、摸摸头、撒红包
- **签到簿 & 礼单**：每位宾客一页红纸，写下昵称和祝福，挑一份贺礼（仅 claude.ai 版）
- **八道硬菜**：红烧 Token 肉、清蒸百万窗口鱼……
- **回礼**：敲开红鸡蛋，里面有一句给你的吉祥话

## 两个版本

| | claude.ai 版 | GitHub Pages 版 |
|---|---|---|
| 谁能打开 | 你在 Share 菜单里分享给的人 | 任何人，不用登录 |
| 签到簿、礼单 | 有，所有人共享 | 隐藏（没有后台） |
| 烟花 / 干杯同步给在席的人 | 有 | 只在自己屏幕上 |

## 文件

- `clawd-feast.html`：页面源文件（Artifact 版直接发布它）
- `build.py`：生成 `index.html`，加上社交媒体预览卡片和网站图标
- `index.html`：GitHub Pages 用的独立版本（由 `build.py` 生成，不要手改）
- `thumb.png`：链接预览图（1200×630）
- `.nojekyll`：让 GitHub Pages 原样发布文件

修改 `clawd-feast.html` 后运行：

```sh
python3 build.py
```

## 开启 GitHub Pages

1. 仓库设为 Public：Settings → General → 最下方 Danger Zone → Change visibility
2. Settings → Pages → Build and deployment → Source 选 “Deploy from a branch”
3. Branch 选 `claude/beautiful-wright-m8jneq`（或合并后的 `main`），目录选 `/ (root)`，Save
4. 一两分钟后访问上面的公开网址

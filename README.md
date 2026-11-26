# Clawd 满月宴 · Cyber Moon Feast

Clawd 的赛博满月宴：一轮满月，一只戴长命锁的像素 Clawd，大家一起来喝满月酒。

## 宴席流程

- **请帖**：竖排红纸请帖，外加 Clawd 的满月档案
- **席间热闹**：放烟花、干杯、摸摸头、撒红包。在 claude.ai 上打开时，此刻在席的所有宾客会同时看到
- **签到簿 & 礼单**：每位宾客一页红纸，写下昵称和祝福，挑一份贺礼（红鸡蛋、长命锁、小金镯、红包、拨浪鼓、显卡）
- **八道硬菜**：红烧 Token 肉、清蒸百万窗口鱼……
- **回礼**：敲开红鸡蛋，里面有一句给你的吉祥话

## 文件

- `clawd-feast.html`：Artifact 源文件（共享签到簿用 `db`，在席宾客和同步烟花用 `room`）
- `index.html`：独立版本，可以直接用浏览器打开或部署到 GitHub Pages。独立打开时签到簿和实时同步不可用，其余互动都能玩
- `thumb.png`：链接预览图

修改 `clawd-feast.html` 后，按下面的方法重新生成 `index.html`：

```sh
{ printf '<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n</head>\n<body>\n'; cat clawd-feast.html; printf '\n</body>\n</html>\n'; } > index.html
```

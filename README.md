# 鹿目圆 × 晓美焰 Codex Pets

> 为 10 月 3 日鹿目圆生日公开的非官方同人 ChatGPT / Codex Pets。包含鹿目圆与黑礼服晓美焰两套完整 v2 动画 spritesheet。

[English](README.en.md) · [官方 Pets 文档](https://learn.chatgpt.com/zh-Hans/docs/pets)

<p align="center">
  <img src="pets/madoka-kaname/previews/preview.gif" width="192" alt="鹿目圆 Codex Pet 动画预览">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="pets/homura-akemi/previews/preview.gif" width="192" alt="黑礼服晓美焰 Codex Pet 动画预览">
</p>

## 收录内容

| Pet | 说明 | 下载 |
| --- | --- | --- |
| 鹿目圆 | 粉白魔法少女服，温柔陪伴工作 | [spritesheet.png](pets/madoka-kaname/spritesheet.png) |
| 黑礼服晓美焰 | 黑色礼服，安静陪伴工作 | [spritesheet.png](pets/homura-akemi/spritesheet.png) |

两套资源均已通过 ChatGPT Pets 官方结构校验：

- v2：`1536 × 2288` PNG；
- `8 × 11` 网格，每格 `192 × 208`；
- 73 个必需动画帧与 15 个全透明保留格；
- 包含待机、左右移动、挥手、跳跃、失败、等待、工作、检查与 16 方位注视动画。

完整预览和 SHA-256 校验值见各角色目录中的 `previews/` 与 `metadata.json`。

## 使用方法

1. 下载对应角色目录中的 `spritesheet.png`。
2. 在支持自定义 Pets 的 ChatGPT 界面中打开 Pets 设置。
3. 选择上传/创建自定义 Pet，并使用该 spritesheet。
4. 如界面或规格发生变化，以[官方 Pets 文档](https://learn.chatgpt.com/zh-Hans/docs/pets)为准。

## 仓库结构

```text
pets/
├── madoka-kaname/
│   ├── spritesheet.png
│   ├── metadata.json
│   └── previews/
└── homura-akemi/
    ├── spritesheet.png
    ├── metadata.json
    └── previews/
scripts/generate_previews.py
manifest.json
```

可运行 `python scripts/generate_previews.py` 从原始 spritesheet 重新生成预览。依赖见 `requirements.txt`。

## 参与贡献

欢迎提交问题、兼容性报告和预览改进。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。不要在 PR 中加入来源不明、未获授权或含有商用限制冲突的素材。

## 权利与声明

这是非官方、非商业的同人项目，与 OpenAI、Magica Quartet、Aniplex、SHAFT 或其他权利方无隶属或背书关系。角色及相关作品权利归其各自权利方所有。

仓库脚本与原创文档采用 [MIT License](LICENSE-CODE)；角色 spritesheet 不适用 MIT，详见 [ASSET-LICENSE.md](ASSET-LICENSE.md)。

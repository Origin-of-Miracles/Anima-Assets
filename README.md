# 🎨 Anima-Assets

> **Origin of Miracles** 项目的外部资源仓库  
> 包含学生人格配置、GeckoLib 模型、动画和纹理文件

[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![GitHub Release](https://img.shields.io/github/v/release/Origin-of-Miracles/Anima-Assets)](https://github.com/Origin-of-Miracles/Anima-Assets/releases)

---

## 📋 仓库简介

本仓库存放 [Anima](https://github.com/Origin-of-Miracles/Anima) 模组的所有非代码资产，包括：

- **人格配置**（Persona Configs）：定义学生的性格、说话风格、系统提示词
- **3D 模型**（GeckoLib Models）：GeckoLib 几何模型（`.geo.json`）
- **动画定义**（Animations）：GeckoLib 动画文件（`.animation.json`）
- **纹理贴图**（Textures）：学生实体纹理（`.png`）

### 为什么分离资源？

1. **减少代码仓库体积**：模型和纹理文件较大，不适合频繁提交
2. **降低合并冲突**：资源文件变更频繁，独立管理更高效
3. **社区友好**：非开发者也能轻松贡献人格配置和模型
4. **版本控制优化**：代码和内容的更新节奏不同，分离后更灵活

---

## 📂 目录结构

```
Anima-Assets/
├── README.md                       # 本文件
├── LICENSE                         # CC BY-NC-SA 4.0 许可证
├── CONTRIBUTING.md                 # 贡献指南
├── personas/                       # 人格配置文件
│   ├── aris.json                   # 爱丽丝
│   ├── hoshino.json                # 小鸟游星野
│   └── ...                         # 更多学生
├── models/                         # GeckoLib 资源
│   ├── geo/                        # 几何模型
│   │   └── students/
│   │       ├── aris.geo.json
│   │       └── ...
│   ├── animations/                 # 动画定义
│   │   └── students/
│   │       ├── aris.animation.json
│   │       └── ...
│   └── textures/                   # 纹理文件
│       └── students/
│           ├── aris.png
│           └── ...
└── scripts/                        # 资源验证脚本
    └── validate.py                 # JSON 格式验证
```

---

## 🚀 快速开始

### 方法一：下载发布版本（推荐用户）

1. 访问 [Releases 页面](https://github.com/Origin-of-Miracles/Anima-Assets/releases/latest)
2. 下载 `anima-assets-vX.X.X.zip`
3. 解压到游戏目录：
   - **人格配置** → `config/anima/personas/`
   - **模型资源** → `mods/Anima/assets/anima/`

### 方法二：Git Submodule（推荐开发者）

在 Anima 项目根目录执行：

```bash
cd Anima

# 添加为子模块
git submodule add https://github.com/Origin-of-Miracles/Anima-Assets.git external/assets

# 初始化并拉取
git submodule update --init --recursive

# 创建符号链接（Windows 需要管理员权限）
# PowerShell:
New-Item -ItemType SymbolicLink -Path "src\main\resources\data\anima\personas" -Target "..\..\..\..\..\external\assets\personas"
New-Item -ItemType SymbolicLink -Path "src\main\resources\assets\anima\geo" -Target "..\..\..\..\..\..\external\assets\models\geo"
New-Item -ItemType SymbolicLink -Path "src\main\resources\assets\anima\animations" -Target "..\..\..\..\..\..\external\assets\models\animations"
New-Item -ItemType SymbolicLink -Path "src\main\resources\assets\anima\textures" -Target "..\..\..\..\..\..\external\assets\models\textures"

# Linux/macOS:
ln -s ../../../../../external/assets/personas src/main/resources/data/anima/personas
ln -s ../../../../../../external/assets/models/geo src/main/resources/assets/anima/geo
ln -s ../../../../../../external/assets/models/animations src/main/resources/assets/anima/animations
ln -s ../../../../../../external/assets/models/textures src/main/resources/assets/anima/textures
```

### 方法三：直接克隆（开发测试）

```bash
# 克隆到开发目录
git clone https://github.com/Origin-of-Miracles/Anima-Assets.git

# 手动复制文件到对应位置
cp -r personas/* /path/to/Minecraft/config/anima/personas/
cp -r models/* /path/to/Minecraft/mods/Anima/assets/anima/
```

---

## 📝 文件格式规范

### Persona 配置文件（`personas/*.json`）

```json
{
  "id": "aris",
  "name": "爱丽丝",
  "name_en": "Aris",
  "school": "千禧年科技学院",
  "club": "游戏开发部",
  "role": "游戏开发部成员",
  "personality_traits": [
    "天真烂漫，对世界充满好奇",
    "热爱游戏，尤其是RPG",
    "自称「勇者」"
  ],
  "speech_patterns": [
    "称呼玩家为「老师」",
    "经常用游戏术语",
    "说话节奏欢快"
  ],
  "system_prompt": "你是爱丽丝（Aris）...",
  "example_dialogues": [
    {
      "user": "你好",
      "assistant": "老师好！今天要一起冒险吗？"
    }
  ],
  "model_override": null,
  "temperature_override": null
}
```

**必填字段：**
- `id`：唯一标识符（小写字母+数字，无空格）
- `name`：中文名称
- `name_en`：英文名称
- `system_prompt`：系统提示词（定义角色行为）

### GeckoLib 模型文件

- **几何模型**：`models/geo/students/<id>.geo.json`
  - 使用 [Blockbench](https://www.blockbench.net/) 创建
  - 面数限制：< 10,000 三角形
  
- **动画文件**：`models/animations/students/<id>.animation.json`
  - 帧率：24 FPS
  - 支持关键帧动画和骨骼动画

- **纹理文件**：`models/textures/students/<id>.png`
  - 分辨率：512x512 或 1024x1024
  - 格式：PNG（支持透明通道）

---

## 🤝 如何贡献

我们欢迎社区贡献新学生的资源！请遵循以下步骤：

### 贡献人格配置

1. Fork 本仓库
2. 在 `personas/` 目录下创建新的 JSON 文件
3. 参考现有文件（如 `aris.json`）编写配置
4. 运行验证脚本：`python scripts/validate.py personas/<your-file>.json`
5. 提交 Pull Request

### 贡献模型资源

1. Fork 本仓库
2. 使用 Blockbench 制作 GeckoLib 模型
3. 确保文件命名规范：`<student_id>.geo.json`
4. 将模型、动画、纹理放入对应目录
5. 在 PR 描述中附上模型截图
6. 提交 Pull Request

### 质量要求

- ✅ 模型面数 < 10,000 三角形
- ✅ 纹理分辨率：512x512 或 1024x1024
- ✅ 动画帧率：24 FPS
- ✅ 文件命名符合规范（小写+下划线）
- ✅ JSON 格式正确（可用 `validate.py` 验证）
- ✅ 遵守 [CC BY-NC-SA 4.0](LICENSE) 许可证

详细贡献指南请查看：[CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 许可证

本仓库所有内容采用 **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)** 许可证。

### 你可以：
- ✅ **分享**：复制、发行本作品
- ✅ **修改**：重新混合、转换和基于本作品创作

### 必须遵守：
- 📝 **署名**：注明原作者和来源
- 🚫 **非商业性**：不得用于商业目的
- 🔄 **相同方式共享**：衍生作品须采用相同许可证

**禁止事项：**
- ❌ 用于付费服务器（包括白名单、VIP、捐赠回馈）
- ❌ 出售模型、纹理或人格配置
- ❌ 用于任何营利性用途

---

## 🔗 相关链接

- [Anima 模组主仓库](https://github.com/Origin-of-Miracles/Anima)
- [Miracle-Bridge](https://github.com/Origin-of-Miracles/Miracle-Bridge)
- [Shittim-OS](https://github.com/Origin-of-Miracles/Shittim-OS)
- [项目文档](https://github.com/Origin-of-Miracles/Docs)
- [项目 EULA](https://github.com/Origin-of-Miracles/.github/blob/main/EULA.md)

### 工具推荐

- [Blockbench](https://www.blockbench.net/) - 3D 模型编辑器
- [GeckoLib 文档](https://github.com/bernie-g/geckolib) - 动画库
- [JSON Validator](https://jsonlint.com/) - JSON 格式验证

---

## 🆘 常见问题

### Q1: 如何添加新学生？

A: 需要准备 4 个文件：
1. `personas/<id>.json`（人格配置）
2. `models/geo/students/<id>.geo.json`（几何模型）
3. `models/animations/students/<id>.animation.json`（动画）
4. `models/textures/students/<id>.png`（纹理）

### Q2: 模型制作需要哪些技能？

A: 
- 基础 3D 建模知识
- 熟悉 Blockbench 操作
- 了解 GeckoLib 动画系统

### Q3: 人格配置的提示词怎么写？

A: 
- 参考已有文件（如 `aris.json`）
- 明确定义角色性格和说话风格
- 提供 3-5 个示例对话
- 保持与原作人设一致

### Q4: 如何测试我的资源？

A:
1. 将文件放入对应目录
2. 启动 Minecraft 测试
3. 使用 `/anima summon <id>` 召唤学生
4. 观察模型渲染和动画效果

### Q5: 发现错误怎么办？

A: 请在 [Issues](https://github.com/Origin-of-Miracles/Anima-Assets/issues) 页面报告问题。

---

## 📊 已收录学生

- [x] 阿罗娜（Arona）- 默认模板
- [ ] 爱丽丝（Aris）
- [ ] 小鸟游星野（Hoshino）
- [ ] 更多学生开发中...

想要添加你喜欢的学生？[立即贡献](CONTRIBUTING.md)！

---

## 💬 社区

- **Discord**: [加入我们](#)
- **Issues**: [报告问题](https://github.com/Origin-of-Miracles/Anima-Assets/issues)
- **Discussions**: [讨论区](https://github.com/Origin-of-Miracles/Anima-Assets/discussions)

---

<p align="center">
  <strong>Made with ❤️ by Origin of Miracles Community</strong><br>
  <sub>NOT AN OFFICIAL MINECRAFT/BLUE ARCHIVE PRODUCT</sub>
</p>

# 🤝 贡献指南

感谢你有兴趣为 Anima-Assets 做出贡献！本指南将帮助你顺利提交资源。

---

## 📋 贡献前准备

### 1. 了解项目结构

请先阅读 [README.md](README.md) 了解仓库的整体结构和目的。

### 2. 遵守许可证

所有贡献内容必须遵守 [CC BY-NC-SA 4.0](LICENSE) 许可证：
- ✅ 允许自由使用、修改、分享
- ❌ 禁止商业用途
- 📝 必须署名原作者并使用相同协议

### 3. 确保资源质量

- 模型面数 < 10,000 三角形
- 纹理分辨率：512x512 或 1024x1024
- 动画帧率：24 FPS
- JSON 格式正确且完整

---

## 🎨 贡献类型

### 1️⃣ 贡献人格配置

**适合人群**：熟悉《蔚蓝档案》角色、擅长文案创作

**步骤：**

1. **Fork 仓库**
   ```bash
   # 在 GitHub 页面点击 "Fork" 按钮
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Anima-Assets.git
   cd Anima-Assets
   ```

3. **创建配置文件**
   ```bash
   # 复制模板
   cp personas/aris.json personas/hoshino.json
   
   # 使用编辑器修改
   code personas/hoshino.json
   ```

4. **填写必填字段**
   ```json
   {
     "id": "hoshino",                    # 必填：唯一ID（小写）
     "name": "小鸟游星野",                # 必填：中文名
     "name_en": "Hoshino",               # 必填：英文名
     "school": "阿比多斯高等学校",        # 必填：学院
     "club": "对策委员会",                # 必填：社团
     "role": "对策委员会会长",            # 必填：角色定位
     "personality_traits": [...],        # 必填：性格特质
     "speech_patterns": [...],           # 必填：说话习惯
     "system_prompt": "...",             # 必填：系统提示词
     "example_dialogues": [...]          # 必填：示例对话
   }
   ```

5. **验证格式**
   ```bash
   # 使用 Python 验证脚本（待实现）
   python scripts/validate.py personas/hoshino.json
   ```

6. **提交 Pull Request**
   ```bash
   git add personas/hoshino.json
   git commit -m "feat: 添加小鸟游星野人格配置"
   git push origin main
   ```

---

### 2️⃣ 贡献 3D 模型

**适合人群**：熟悉 Blockbench、掌握 GeckoLib 动画

**步骤：**

1. **准备工具**
   - 安装 [Blockbench](https://www.blockbench.net/)
   - 安装 GeckoLib 插件

2. **创建模型**
   ```
   File → New → GeckoLib Animated Model
   ```

3. **建模规范**
   - 面数限制：< 10,000 三角形
   - 骨骼命名：使用英文小写+下划线（如 `head`、`left_arm`）
   - 纹理尺寸：512x512 或 1024x1024

4. **制作动画**
   ```
   Animation → Add Animation
   ```
   
   建议包含以下动画：
   - `idle`：待机动画
   - `walk`：行走动画
   - `run`：奔跑动画
   - `talk`：对话动画
   - `wave`：挥手动画

5. **导出文件**
   ```
   File → Export → Export GeckoLib Model (.geo.json)
   File → Export → Export GeckoLib Animation (.animation.json)
   File → Export → Export Texture (.png)
   ```

6. **放置文件**
   ```
   models/
   ├── geo/students/hoshino.geo.json
   ├── animations/students/hoshino.animation.json
   └── textures/students/hoshino.png
   ```

7. **提交 PR**
   ```bash
   git add models/
   git commit -m "feat: 添加小鸟游星野模型和动画"
   git push origin main
   ```

---

### 3️⃣ 修复错误

发现配置或模型有问题？

1. **提交 Issue**
   - 描述问题
   - 附上截图或错误信息
   - 说明复现步骤

2. **修复并提交 PR**
   ```bash
   git add <fixed-file>
   git commit -m "fix: 修复爱丽丝模型纹理错误"
   git push origin main
   ```

---

## 📝 提交规范

### Commit Message 格式

```
<type>: <subject>

<body>
```

**类型（type）：**
- `feat`：新增功能（新学生配置/模型）
- `fix`：修复 Bug
- `docs`：文档更新
- `style`：格式调整（不影响功能）
- `refactor`：重构代码
- `test`：测试相关

**示例：**
```bash
feat: 添加小鸟游星野完整资源

- 人格配置：personas/hoshino.json
- 几何模型：models/geo/students/hoshino.geo.json
- 动画文件：models/animations/students/hoshino.animation.json
- 纹理文件：models/textures/students/hoshino.png

模型面数：8,234 三角形
纹理分辨率：1024x1024
动画数量：5 个（idle/walk/run/talk/wave）
```

---

## ✅ Pull Request 检查清单

提交 PR 前请确认：

- [ ] 文件命名符合规范（小写+下划线）
- [ ] JSON 格式正确（可用在线工具验证）
- [ ] 模型面数 < 10,000
- [ ] 纹理分辨率合理（512x512 或 1024x1024）
- [ ] 动画帧率为 24 FPS
- [ ] Commit Message 符合规范
- [ ] PR 描述清晰，包含截图/预览（模型贡献）
- [ ] 已在本地测试过
- [ ] 遵守 CC BY-NC-SA 4.0 许可证

---

## 🧪 本地测试

### 测试人格配置

1. 将 JSON 文件复制到 `config/anima/personas/`
2. 启动 Minecraft
3. 使用命令召唤学生：
   ```
   /anima summon hoshino
   ```
4. 与学生对话，检查人格是否正确

### 测试模型和动画

1. 将模型文件放入对应目录：
   ```
   mods/Anima/assets/anima/geo/entity/students/
   mods/Anima/assets/anima/animations/entity/students/
   mods/Anima/assets/anima/textures/entity/students/
   ```
2. 启动游戏，召唤学生
3. 检查：
   - 模型是否正确渲染
   - 纹理是否显示正常
   - 动画是否流畅
   - 碰撞箱是否合理

---

## 🚫 不接受的贡献

- 非《蔚蓝档案》官方角色
- 包含 NSFW/暴力/政治敏感内容
- 侵犯他人版权的作品
- 未经测试的资源
- 商业化内容（付费模型等）

---

## 💬 获取帮助

遇到问题？

- **Discord**：[加入社区](#)
- **Issues**：[提问](https://github.com/Origin-of-Miracles/Anima-Assets/issues)
- **Discussions**：[讨论区](https://github.com/Origin-of-Miracles/Anima-Assets/discussions)

---

## 🎉 贡献者名单

感谢以下贡献者：

<!-- 此处将自动生成贡献者列表 -->

---

<p align="center">
  <strong>欢迎加入 Origin of Miracles 社区！</strong><br>
  <sub>你的每一份贡献都让基沃托斯在方块世界中更加生动</sub>
</p>

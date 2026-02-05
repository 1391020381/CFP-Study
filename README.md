# CFA 考试学习仓库

这是我的个人学习仓库，使用 Claude Code 的 AI 驱动引导式学习方法准备特许金融分析师（CFA）考试。

**多亏了 AI 和 Claude Code**，我能够采用个性化的学习方法，通过苏格拉底教学法和系统性进度跟踪来掌握复杂的金融分析概念。

---

## 仓库结构

```
/sessions/                    # 每日学习 sessions 记录
  /2025-02-05/               # 每个学习日一个文件夹
  /2025-02-06/               # 记录每次学习对话
  SESSION-TEMPLATE.md        # 记录 session 的模板

/progress/                    # 考试准备的唯一真实来源
  cfa-study-tracker.md       # 综合跟踪器，包含：
                             # - 10 大 CFA 模块映射
                             # - 已掌握的主题
                             # - 已识别的知识差距
                             # - 各级别学习计划

/notes/CFA/                   # CFA 学习规划
  路径总览.md                # 总体学习周期和阶段
  Level I 学习路径.md        # Level I 详细学习目录
  Level II 学习路径.md       # Level II 详细学习目录
  Level III 学习路径.md      # Level III 详细学习目录
  阶段0-金融扫盲.md          # 预备阶段学习内容
  阶段1：CFA一级预备.md      # 一级预备阶段

CLAUDE.md                     # AI 导师说明（苏格拉底教学法）
README.md                     # 本文件
```

## 工作原理

这个仓库使用 Claude Code 作为交互式 CFA 考试导师，它能够：
- 使用苏格拉底教学法（先问你知道什么）
- 提供简洁的解释（约 200 字）
- 通过后续问题验证你的理解
- 根据你的回答调整教学风格
- **记录每次学习 session 以个性化你的学习体验**

## CFA 学习路径

### 总体学习周期

| 级别        | 建议时长   | 学习小时     | 难度   | 核心目标   |
| --------- | ------ | -------- | ---- | ------ |
| Level 0   | 1 个月 | 20–30h | ⭐   | 金融扫盲 & CFA一级预备 |
| Level I   | 4–6 个月 | 300–350h | ⭐⭐   | 建立金融体系 |
| Level II  | 5–7 个月 | 350–400h | ⭐⭐⭐⭐ | 估值建模能力 |
| Level III | 4–6 个月 | 300–350h | ⭐⭐⭐  | 投资组合实战 |

### 学习阶段总结

- **Level 0** → 金融扫盲 & CFA一级预备
- **Level I** → 建金融知识地图
- **Level II** → 学会给资产定价
- **Level III** → 学会管钱 + 配置资产

### 10 大知识模块

1. **Ethics（职业道德）** - 道德准则、GIPS、职业行为
2. **Quantitative Methods（数量分析）** - TVM、统计、概率、假设检验
3. **Economics（经济学）** - 微观/宏观经济、货币政策、汇率
4. **Financial Statement Analysis（财务报表分析）** - 三大报表、比率分析
5. **Corporate Issuers（公司金融）** - 资本预算、WACC、杠杆分析
6. **Equity Investments（股票投资）** - 估值模型、行业分析
7. **Fixed Income（固定收益）** - 债券定价、久期、信用分析
8. **Derivatives（衍生品）** - 期货、期权、互换
9. **Alternative Investments（另类投资）** - 房地产、私募、对冲基金
10. **Portfolio Management（投资组合管理）** - 风险收益、CAPM、资产配置

## 如何使用

### 每日学习 sessions

1. 在此仓库中打开 Claude Code
2. 自然地询问关于 CFA 主题的问题——就像与导师交谈一样
3. 回答 Claude 提出的理解检查问题
4. 每次 session 后，Claude 将自动记录：
   - 你学到了什么
   - 你在哪些方面遇到困难
   - 你掌握了什么
   - 下一步需要复习什么

### 复习 sessions

当你想要复习时，只需问 Claude：
- "让我们复习我遇到困难的主题"
- "我今天应该专注于什么？"
- "测试我的薄弱环节"
- "显示我的进度"

Claude 将阅读你的 session 历史记录，并根据你过去的表现创建个性化的复习计划。

### 跟踪你的进度

在 `/progress/cfa-study-tracker.md` 查看你的综合学习跟踪器，了解：
- 整体考试准备情况
- 当前学习阶段和模块进度
- 哪些领域已完成
- 剩余的知识差距
- 根据各级别权重的优先学习计划

## 学习理念

**引导式学习方法**：
- 对话式且无评判
- 基于你已有的知识构建
- 在继续之前检查理解情况
- 适应你的学习风格
- 专注于深度理解，而不仅仅是记忆

## 学习材料

### 官方资源
- CFA Institute Curriculum
- CFA Institute Learning Ecosystem（题库）

### 免费/高性价比资源

**免费题库**：
- [UWorld CFA](https://finance.uworld.com/cfa)
- [AnalystPrep Qbank](https://analystprep.com/cfa-question-bank)
- [Investopedia CFA Level 1 Guide](https://www.investopedia.com/cfa-level-1-4689745)

**视频内容**：
- [Mark Meldrum YouTube](https://www.youtube.com/c/MarkMeldrum)
- [IFT YouTube](https://www.youtube.com/c/IFTWorld)

**课程（高性价比）**：
- [Kaplan Schweser](https://www.schweser.com/cfa)
- [Mark Meldrum](https://markmeldrum.com)

这些资源非常适合在通勤、锻炼或休息时间进行被动学习。

## 主要特点

**个性化学习**：
- 记录的学习 sessions 带有详细笔记
- 苏格拉底教学法（基于你已掌握的知识构建）
- 根据你的回答进行的适应性解释
- 针对你的薄弱领域定制的练习问题

**综合跟踪**：
- 每次 session 自动记录
- 识别和跟踪知识差距
- 带有信心水平的已掌握主题
- 根据考试权重衡量进度

**基于证据的方法**：
- 所有答案均经权威来源验证（CFA Institute、Investopedia）
- 技术性问题不猜测
- 为复杂规则提供引用
- 专注于理解"为什么"而不仅仅是"什么"

## 如何使用此仓库进行你自己的 CFA 考试准备

想将此 AI 驱动的学习系统用于你自己的 CFA 考试准备吗？这很简单：

1. **克隆此仓库**：
   ```bash
   git clone https://github.com/chenran818/CFP-Study.git
   cd CFP-Study
   ```

2. **清除我的学习历史**（重新开始）：
   ```bash
   rm -rf progress/ sessions/
   ```

3. **运行 Claude Code**：
   ```bash
   claude-code
   ```

4. **就这样！** 开始询问 CFA 问题，Claude 将：
   - 使用苏格拉底教学法教你
   - 自动创建新的 `progress/` 和 `sessions/` 文件夹
   - 像对我一样跟踪你的学习旅程
   - 适应你的学习风格

`CLAUDE.md` 文件包含 Claude 应该如何指导你的所有说明。**它的效果神奇！**

## 开始使用

只需开始与 Claude Code 对话并询问你的第一个 CFA 问题。Claude 将从那里引导你，同时自动跟踪你的进度。

---

## 关于作者

CFA 考试是一项具有挑战性的专业认证。使用 Claude Code 作为我的 AI 学习伙伴，让复杂的金融分析概念终于变得清晰——苏格拉底教学法、个性化反馈和系统性进度跟踪帮助我建立扎实的投资分析基础。

如果你正在准备 CFA 考试或任何专业认证，我希望这个仓库能够激励你在学习旅程中利用 AI 工具。


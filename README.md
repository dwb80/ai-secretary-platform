# AI Secretary Platform 智能秘书管理平台

> 一个高度可扩展的 AI 秘书管理系统，通过自然语言对话与用户交互，智能化处理各类服务请求。

## 🎯 项目特性

- 🤖 **自然交互** - 通过对话方式与用户互动
- 🔄 **流程自动化** - 智能采集信息、路由审批、执行操作
- 📊 **数据驱动** - 完整的数据追踪和分析
- 🚀 **高度可扩展** - 插件式架构支持新秘书和业务流程快速接入
- 💾 **CSV 存储** - 使用 CSV 文件替代数据库（便于本地开发）

## 📦 支持的秘书类型

- ✅ **订车秘书 (CarSecretary)** - 已完成
- 📋 **差旅秘书 (TravelSecretary)** - 规划中
- 📅 **会议秘书 (MeetingSecretary)** - 规划中
- 🏠 **管家秘书 (ButlerSecretary)** - 规划中

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/dwb80/ai-secretary-platform.git
cd ai-secretary-platform
```

### 2. 安装依赖
```bash
cd backend
pip install -r requirements.txt
```

### 3. 配置环境
```bash
cp .env.example .env
# 编辑 .env 文件，填入 MiniMax API Key
```

### 4. 初始化数据
```bash
cd ..
python scripts/init_data.py
```

### 5. 启动应用
```bash
cd backend
python main.py
```

应用将在 http://localhost:8000 启动

## 📚 文档

- [架构设计](docs/architecture.md) - 系统整体架构
- [API 文档](docs/api.md) - 完整的 API 接口定档
- [扩展指南](docs/extension_guide.md) - 如何添加新秘书
- [部署指南](docs/deployment.md) - 生产部署指南

## 🔗 API 端点

### 对话 API
- `POST /api/chat/send` - 发送对话消息
- `GET /api/chat/history/{session_id}` - 获取对话历史

### 请求 API
- `GET /api/requests/{request_id}` - 获取请求详情
- `GET /api/requests/user/{user_id}` - 获取用户请求列表
- `GET /api/requests/status/{status}` - 按状态获取请求

### 审批 API
- `POST /api/approval/decide` - 做出审批决定
- `GET /api/approval/pending/{approver_id}` - 获取待审批列表
- `GET /api/approval/{approval_id}` - 获取审批详情

### 秘书管理 API
- `GET /api/secretaries` - 获取所有秘书
- `GET /api/secretaries/{type}` - 获取特定秘书信息

## 🛠️ 技术栈

- **���端框架**: FastAPI
- **编程语言**: Python 3.10+
- **数据存储**: CSV 文件
- **AI 模型**: MiniMax 2.7
- **异步任务**: APScheduler
- **API 文档**: Swagger/OpenAPI
- **容器化**: Docker

## 📋 项目结构

```
ai-secretary-platform/
├── backend/                 # 后端应用
│   ├── main.py             # 应用入口
│   ├── config.py           # 配置管理
│   ├── requirements.txt     # 依赖
│   ├── api/                # API 层
│   ├── services/           # 服务层
│   ├── secretaries/        # 秘书系统
│   ├── utils/              # 工具模块
│   └── tasks/              # 定时任务
├── data/                    # CSV 数据文件
├── docs/                    # 项目文档
├── tests/                   # 测试用例
├── scripts/                 # 脚本
└── deployment/              # 部署配置
```

## 💡 使用示例

### 对话示例
```bash
POST /api/chat/send
{
  "user_id": "user123",
  "session_id": "session123",
  "message": "我需要订车",
  "secretary_type": "car"
}
```

### 审批示例
```bash
POST /api/approval/decide
{
  "approval_id": "approval123",
  "decision": "approve",
  "reason": "已批准"
}
```

## 📝 开发计划

- [x] Phase 1: 基础框架 (已完成)
- [x] Phase 2: 订车秘书 (已完成)
- [ ] Phase 3: 差旅秘书
- [ ] Phase 4: 会议秘书
- [ ] Phase 5: 管家秘书
- [ ] Phase 6: 优化和运维

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👥 团队

- 主要开发者: @dwb80

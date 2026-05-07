# Task Plan: SPDM 前端界面与后端 API 开发

## Goal
实现 SPDM 仿真过程与数据管理系统的核心前端页面（项目列表页、仿真任务管理页、数据流程可视化页）和后端 API 服务，并合并到 master 分支。

## Current Phase
Phase 1: 需求与发现

## Phases

### Phase 1: 需求与发现
- [x] 理解项目结构
- [x] 分析数据模型 (SimProject, SimTask, SimWorkflow 等)
- [x] 确认前端技术栈 (Vue 3 + Vite + Ant Design Vue + AntV X6)
- [x] 确认后端技术栈 (FastAPI)
- **Status:** complete

### Phase 2: 前端基础设施搭建
- [ ] 创建 Vue 项目结构 (src/main.js, src/App.vue, src/router/index.js)
- [ ] 配置 Pinia store
- [ ] 创建 API 服务层
- [ ] 实现布局组件 (Layout, Sidebar, Header)
- **Status:** pending

### Phase 3: 项目列表页开发
- [ ] 创建项目列表页面组件
- [ ] 实现项目搜索/筛选功能
- [ ] 实现项目创建/编辑对话框
- [ ] 集成 Ant Design Vue Table
- **Status:** pending

### Phase 4: 仿真任务管理页开发
- [ ] 创建任务列表页面组件
- [ ] 实现任务状态管理
- [ ] 实现任务详情面板
- [ ] 实现工况和实验管理
- **Status:** pending

### Phase 5: 数据流程可视化页开发
- [ ] 集成 AntV X6
- [ ] 创建流程图组件
- [ ] 实现节点/边的交互
- [ ] 实现流程编辑器功能
- **Status:** pending

### Phase 6: 后端 API 服务开发
- [ ] 创建 FastAPI 应用入口
- [ ] 实现项目 API 路由
- [ ] 实现任务 API 路由
- [ ] 实现工作流 API 路由
- [ ] 创建服务层 (services)
- **Status:** pending

### Phase 7: 测试与验证
- [ ] 验证前端页面可运行
- [ ] 验证 API 接口可用
- [ ] 文档完善
- **Status:** pending

### Phase 8: 合并到 master
- [ ] 提交代码
- [ ] 创建 Pull Request
- [ ] 合并到 master
- **Status:** pending

## Key Decisions
| Decision | Rationale |
|----------|-----------|
| Vue 3 + Composition API | 现代 Vue 最佳实践 |
| Pinia 状态管理 | 轻量级，推荐的状态管理方案 |
| Ant Design Vue 4.x | 企业级 UI 组件库 |
| AntV X6 | 专业流程图库 |
| FastAPI | 高性能 Python Web 框架 |
| SQLAlchemy ORM | 已有的数据库模型 |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       |         |            |

## Notes
- 项目根目录: C:/workspace/py/wanman-main/wanmantest/.wanman/worktree/spdm
- 前端源码目录: frontend/src
- 后端源码目录: 待创建 (api/, services/)

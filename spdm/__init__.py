"""
SPDM Backend API 模块
=====================

基于 SPDM (Simulation Process and Data Management) 产品设计的后端 API 实现。
提供项目、仿真任务、工况、工作流、材料库等核心功能的数据接口。

模块结构:
- models/: 数据模型定义
- api/: API 端点实现
- services/: 业务逻辑层

技术栈: FastAPI + Pydantic + SQLAlchemy
"""

__version__ = "0.1.0"
__author__ = "SPDM Dev Team"
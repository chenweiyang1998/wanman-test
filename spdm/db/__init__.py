"""
SPDM 数据库模块
================

提供 SPDM 系统的数据库模型定义和迁移管理。

子模块:
- database.py: 数据库连接配置
- models.py: SQLAlchemy 数据模型
- migrations/: 数据库迁移脚本

用法:
    from spdm.db import Base, engine, get_db_session

    # 创建表
    create_tables()

    # 使用会话
    with get_db_session() as db:
        projects = db.query(SimProject).all()
"""

from .database import (
    Base,
    engine,
    SessionLocal,
    get_db,
    get_db_session,
    create_tables,
    drop_tables,
)
from .models import (
    SimProject,
    SimTask,
    SimCondition,
    SimConditionTimes,
    SimExperiment,
    SimWorkflow,
    SimWorkflowTemplate,
    SimBom,
    SimDocument,
    SimReportResult,
    LibraryMaterial,
)

__all__ = [
    "Base",
    "engine",
    "SessionLocal",
    "get_db",
    "get_db_session",
    "create_tables",
    "drop_tables",
    "SimProject",
    "SimTask",
    "SimCondition",
    "SimConditionTimes",
    "SimExperiment",
    "SimWorkflow",
    "SimWorkflowTemplate",
    "SimBom",
    "SimDocument",
    "SimReportResult",
    "LibraryMaterial",
]

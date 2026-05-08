"""
数据库连接配置
===============

提供 SQLAlchemy 数据库引擎和会话管理。
使用环境变量配置数据库连接字符串。
"""

import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# 数据库连接配置
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./spdm.db"  # 默认使用 SQLite
)

# 创建数据库引擎
engine: Engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("SQL_DEBUG", "false").lower() == "true",
    pool_pre_ping=True,
    pool_recycle=3600,
)

# 创建会话工厂
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 创建基类
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    获取数据库会话的依赖注入函数。
    用于 FastAPI 的 Depends(get_db)。

    用法:
        @app.get("/items")
        def get_items(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """
    上下文管理器，用于非异步环境获取数据库会话。

    用法:
        with get_db_session() as db:
            db.query(Model).all()
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def create_tables():
    """创建所有数据库表"""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """删除所有数据库表（谨慎使用）"""
    Base.metadata.drop_all(bind=engine)

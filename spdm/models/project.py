"""
仿真项目 Pydantic 模型
=======================

定义项目的 API 请求/响应模型，与 SQLAlchemy 的 SimProject 对应。
"""

from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class ProjectBase(BaseModel):
    """项目基础字段"""
    project_name: str = Field(..., min_length=1, max_length=200, description="项目名称")
    manager_user_id: Optional[int] = Field(default=None, description="项目负责人ID")
    manager_name: Optional[str] = Field(default=None, max_length=100, description="负责人姓名")
    project_start_date: Optional[date] = Field(default=None, description="开始日期")
    project_end_date: Optional[date] = Field(default=None, description="结束日期")
    project_status: str = Field(default="draft", description="项目状态")
    auth_level: int = Field(default=1, description="权限级别")
    project_source: int = Field(default=1, description="项目来源 (1=SPDM原生, 2=PLM同步)")
    product_type: Optional[str] = Field(default=None, max_length=100, description="产品类型")
    classify_name: Optional[str] = Field(default=None, max_length=100, description="仿真分类名称")
    project_phase_name: Optional[str] = Field(default=None, max_length=100, description="项目阶段名称")
    remark: Optional[str] = Field(default=None, description="备注")


class ProjectCreate(ProjectBase):
    """创建项目请求"""
    pass


class ProjectUpdate(BaseModel):
    """更新项目请求 —— 所有字段可选"""
    project_name: Optional[str] = Field(default=None, min_length=1, max_length=200)
    manager_user_id: Optional[int] = None
    manager_name: Optional[str] = Field(default=None, max_length=100)
    project_start_date: Optional[date] = None
    project_end_date: Optional[date] = None
    project_status: Optional[str] = None
    auth_level: Optional[int] = None
    product_type: Optional[str] = Field(default=None, max_length=100)
    classify_name: Optional[str] = Field(default=None, max_length=100)
    project_phase_name: Optional[str] = Field(default=None, max_length=100)
    remark: Optional[str] = None


class Project(ProjectBase):
    """项目完整模型 —— 用于响应"""
    project_id: int = Field(..., description="项目ID")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True


class ProjectResponse(BaseModel):
    """项目响应包装"""
    code: int = Field(default=200)
    message: str = Field(default="success")
    data: Optional[Project] = None

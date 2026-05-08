"""
工况 Pydantic 模型
===================

定义工况的 API 请求/响应模型，与 SQLAlchemy 的 SimCondition 对应。
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ConditionBase(BaseModel):
    """工况基础字段"""
    name: str = Field(..., min_length=1, max_length=200, description="工况名称")
    task_id: Optional[int] = Field(default=None, description="关联任务ID")
    experiment_id: Optional[int] = Field(default=None, description="关联实验ID")
    flow_id: Optional[int] = Field(default=None, description="关联工作流实例ID")
    is_default_condition: bool = Field(default=False, description="是否默认工况")
    condition_hierarchy: Optional[str] = Field(default=None, max_length=500, description="工况层级")
    remark: Optional[str] = Field(default=None, description="备注")


class ConditionCreate(ConditionBase):
    """创建工况请求"""
    pass


class ConditionUpdate(BaseModel):
    """更新工况请求 —— 所有字段可选"""
    name: Optional[str] = Field(default=None, min_length=1, max_length=200)
    task_id: Optional[int] = None
    experiment_id: Optional[int] = None
    flow_id: Optional[int] = None
    is_default_condition: Optional[bool] = None
    condition_hierarchy: Optional[str] = Field(default=None, max_length=500)
    remark: Optional[str] = None


class Condition(ConditionBase):
    """工况完整模型 —— 用于响应"""
    condition_id: int = Field(..., description="工况ID")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True


class ConditionResponse(BaseModel):
    """工况响应包装"""
    code: int = Field(default=200)
    message: str = Field(default="success")
    data: Optional[Condition] = None

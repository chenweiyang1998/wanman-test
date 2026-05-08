"""
工况 Pydantic 模型
==================

定义 SimCondition 对应的 API 请求/响应模型。
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Condition(BaseModel):
    """工况（只读展示模型）"""

    condition_id: int = Field(description="工况ID")
    task_id: Optional[int] = Field(default=None, description="关联任务ID")
    experiment_id: Optional[int] = Field(default=None, description="关联实验ID")
    flow_id: Optional[int] = Field(default=None, description="关联工作流实例ID")

    name: str = Field(max_length=200, description="工况名称")
    is_default_condition: bool = Field(default=False, description="是否默认工况")
    condition_hierarchy: Optional[str] = Field(
        default=None, max_length=500, description="工况层级"
    )

    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")

    class Config:
        from_attributes = True


class ConditionCreate(BaseModel):
    """创建工况请求"""

    task_id: Optional[int] = Field(default=None, description="关联任务ID")
    experiment_id: Optional[int] = Field(default=None, description="关联实验ID")
    flow_id: Optional[int] = Field(default=None, description="关联工作流实例ID")
    name: str = Field(max_length=200, description="工况名称")
    is_default_condition: bool = Field(default=False, description="是否默认工况")
    condition_hierarchy: Optional[str] = Field(
        default=None, max_length=500, description="工况层级"
    )
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")


class ConditionUpdate(BaseModel):
    """更新工况请求"""

    name: Optional[str] = Field(default=None, max_length=200, description="工况名称")
    is_default_condition: Optional[bool] = Field(default=None, description="是否默认工况")
    condition_hierarchy: Optional[str] = Field(
        default=None, max_length=500, description="工况层级"
    )
    flow_id: Optional[int] = Field(default=None, description="关联工作流实例ID")
    remark: Optional[str] = Field(default=None, description="备注")


class ConditionResponse(BaseModel):
    """工况 API 响应"""

    code: int = Field(default=200, description="状态码")
    message: str = Field(default="success", description="响应消息")
    data: Optional[Condition] = Field(default=None, description="工况数据")

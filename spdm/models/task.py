"""
仿真任务 Pydantic 模型
=======================

定义任务的 API 请求/响应模型，与 SQLAlchemy 的 SimTask 对应。
"""

from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """任务状态枚举"""
    DRAFT = "draft"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    REVIEWING = "reviewing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskBase(BaseModel):
    """任务基础字段"""
    task_code: str = Field(..., max_length=50, description="任务编号")
    task_name: str = Field(..., min_length=1, max_length=200, description="任务名称")
    task_type: int = Field(default=1, description="任务类型 (1=仿真, 2=协同, 3=BOM, 4=图文档)")
    manager_user_id: Optional[int] = Field(default=None, description="负责人ID")
    manager_name: Optional[str] = Field(default=None, max_length=100, description="负责人姓名")
    workflow_id: Optional[int] = Field(default=None, description="关联工作流ID")
    task_status: str = Field(default="draft", description="任务状态")
    auth_level: int = Field(default=1, description="权限级别")
    business_area: Optional[str] = Field(default=None, max_length=100, description="业务领域")
    product_type: Optional[str] = Field(default=None, max_length=100, description="产品类型")
    simulation_type: Optional[str] = Field(default=None, max_length=100, description="仿真类型")
    bom_id: Optional[int] = Field(default=None, description="关联BOM ID")
    bom_name: Optional[str] = Field(default=None, max_length=200, description="关联BOM名称")
    all_report_id: Optional[int] = Field(default=None, description="报告ID")
    all_report_name: Optional[str] = Field(default=None, max_length=200, description="报告名称")
    project_id: Optional[int] = Field(default=None, description="关联项目ID")
    remark: Optional[str] = Field(default=None, description="备注")


class TaskCreate(TaskBase):
    """创建任务请求"""
    pass


class TaskUpdate(BaseModel):
    """更新任务请求 —— 所有字段可选"""
    task_name: Optional[str] = Field(default=None, min_length=1, max_length=200)
    task_type: Optional[int] = None
    manager_user_id: Optional[int] = None
    manager_name: Optional[str] = Field(default=None, max_length=100)
    workflow_id: Optional[int] = None
    task_status: Optional[str] = None
    auth_level: Optional[int] = None
    business_area: Optional[str] = Field(default=None, max_length=100)
    product_type: Optional[str] = Field(default=None, max_length=100)
    simulation_type: Optional[str] = Field(default=None, max_length=100)
    bom_id: Optional[int] = None
    bom_name: Optional[str] = Field(default=None, max_length=200)
    all_report_id: Optional[int] = None
    all_report_name: Optional[str] = Field(default=None, max_length=200)
    remark: Optional[str] = None


class Task(TaskBase):
    """任务完整模型 —— 用于响应"""
    task_id: int = Field(..., description="任务ID")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True


class TaskResponse(BaseModel):
    """任务响应包装"""
    code: int = Field(default=200)
    message: str = Field(default="success")
    data: Optional[Task] = None

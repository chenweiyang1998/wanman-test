"""
仿真任务 Pydantic 模型
======================

定义 SimTask 对应的 API 请求/响应模型。
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """任务状态枚举"""
    DRAFT = "draft"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    REVIEWING = "reviewing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Task(BaseModel):
    """仿真任务（只读展示模型）"""

    task_id: int = Field(description="任务ID")
    task_code: str = Field(max_length=50, description="任务编号")
    task_name: str = Field(max_length=200, description="任务名称")
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

    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    """创建任务请求"""

    task_code: str = Field(max_length=50, description="任务编号")
    task_name: str = Field(max_length=200, description="任务名称")
    task_type: int = Field(default=1, description="任务类型")
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
    project_id: Optional[int] = Field(default=None, description="关联项目ID")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")


class TaskUpdate(BaseModel):
    """更新任务请求"""

    task_name: Optional[str] = Field(default=None, max_length=200, description="任务名称")
    task_type: Optional[int] = Field(default=None, description="任务类型")
    manager_user_id: Optional[int] = Field(default=None, description="负责人ID")
    manager_name: Optional[str] = Field(default=None, max_length=100, description="负责人姓名")
    workflow_id: Optional[int] = Field(default=None, description="关联工作流ID")
    task_status: Optional[str] = Field(default=None, description="任务状态")
    auth_level: Optional[int] = Field(default=None, description="权限级别")
    business_area: Optional[str] = Field(default=None, max_length=100, description="业务领域")
    product_type: Optional[str] = Field(default=None, max_length=100, description="产品类型")
    simulation_type: Optional[str] = Field(default=None, max_length=100, description="仿真类型")
    bom_id: Optional[int] = Field(default=None, description="关联BOM ID")
    bom_name: Optional[str] = Field(default=None, max_length=200, description="关联BOM名称")
    all_report_id: Optional[int] = Field(default=None, description="报告ID")
    all_report_name: Optional[str] = Field(default=None, max_length=200, description="报告名称")
    remark: Optional[str] = Field(default=None, description="备注")


class TaskResponse(BaseModel):
    """任务 API 响应"""

    code: int = Field(default=200, description="状态码")
    message: str = Field(default="success", description="响应消息")
    data: Optional[Task] = Field(default=None, description="任务数据")

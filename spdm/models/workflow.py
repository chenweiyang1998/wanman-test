"""
工作流 Pydantic 模型
====================

定义 SimWorkflow 和 SimWorkflowTemplate 对应的 API 模型。
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WorkflowTemplate(BaseModel):
    """工作流模板（只读展示模型）"""

    template_id: int = Field(description="模板ID")
    template_name: str = Field(max_length=200, description="模板名称")
    simulation_type: Optional[str] = Field(default=None, max_length=100, description="仿真类型")
    version: str = Field(default="1.0.0", max_length=50, description="版本号")
    param_count: int = Field(default=0, description="参数数量")
    description: Optional[str] = Field(default=None, description="模板描述")

    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")

    class Config:
        from_attributes = True


class WorkflowInstance(BaseModel):
    """仿真工作流实例（只读展示模型）"""

    flow_id: int = Field(description="工作流ID")
    experiment_id: Optional[int] = Field(default=None, description="关联实验ID")
    template_id: Optional[int] = Field(default=None, description="关联模板ID")

    flow_name: str = Field(max_length=200, description="工作流名称")
    flow_type: Optional[str] = Field(default=None, max_length=100, description="工作流类型")
    flow_publish_status: int = Field(default=1, description="发布状态 (1=未发布, 2=已发布)")
    flow_version: str = Field(default="1.0.0", max_length=50, description="版本号")

    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")

    class Config:
        from_attributes = True


# 向后兼容：Workflow 别名指向工作流实例
Workflow = WorkflowInstance

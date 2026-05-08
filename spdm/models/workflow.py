"""
工作流 Pydantic 模型
=====================

定义工作流的 API 请求/响应模型，与 SQLAlchemy 的 SimWorkflow / SimWorkflowTemplate 对应。
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Workflow Template
# ---------------------------------------------------------------------------

class WorkflowTemplateBase(BaseModel):
    """工作流模板基础字段"""
    template_name: str = Field(..., min_length=1, max_length=200, description="模板名称")
    simulation_type: Optional[str] = Field(default=None, max_length=100, description="仿真类型")
    version: str = Field(default="1.0.0", max_length=50, description="版本号")
    param_count: int = Field(default=0, description="参数数量")
    description: Optional[str] = Field(default=None, description="模板描述")
    remark: Optional[str] = Field(default=None, description="备注")


class WorkflowTemplateCreate(WorkflowTemplateBase):
    """创建工作流模板请求"""
    pass


class WorkflowTemplate(WorkflowTemplateBase):
    """工作流模板完整模型"""
    template_id: int = Field(..., description="模板ID")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True


# ---------------------------------------------------------------------------
# Workflow Instance
# ---------------------------------------------------------------------------

class WorkflowBase(BaseModel):
    """工作流实例基础字段"""
    flow_name: str = Field(..., min_length=1, max_length=200, description="工作流名称")
    experiment_id: Optional[int] = Field(default=None, description="关联实验ID")
    template_id: Optional[int] = Field(default=None, description="关联模板ID")
    flow_type: Optional[str] = Field(default=None, max_length=100, description="工作流类型")
    flow_publish_status: int = Field(default=1, description="发布状态 (1=未发布, 2=已发布)")
    flow_version: str = Field(default="1.0.0", max_length=50, description="版本号")
    remark: Optional[str] = Field(default=None, description="备注")


class WorkflowCreate(WorkflowBase):
    """创建工作流请求"""
    pass


class Workflow(WorkflowBase):
    """工作流实例完整模型"""
    flow_id: int = Field(..., description="工作流ID")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True


class WorkflowInstance(Workflow):
    """工作流实例（别名，保持向后兼容）"""
    pass

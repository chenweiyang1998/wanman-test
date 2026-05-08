"""
仿真项目 Pydantic 模型
======================

定义 SimProject 对应的 API 请求/响应模型。
"""

from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field


class Project(BaseModel):
    """仿真项目（只读展示模型）"""

    project_id: int = Field(description="项目ID")
    project_name: str = Field(max_length=200, description="项目名称")
    manager_user_id: Optional[int] = Field(default=None, description="负责人ID")
    manager_name: Optional[str] = Field(default=None, max_length=100, description="负责人姓名")

    project_start_date: Optional[date] = Field(default=None, description="开始日期")
    project_end_date: Optional[date] = Field(default=None, description="结束日期")

    project_status: str = Field(default="draft", description="项目状态")
    auth_level: int = Field(default=1, description="权限级别")
    project_source: int = Field(default=1, description="项目来源 (1=SPDM原生, 2=PLM同步)")
    product_type: Optional[str] = Field(default=None, max_length=100, description="产品类型")
    classify_name: Optional[str] = Field(default=None, max_length=100, description="仿真分类")
    project_phase_name: Optional[str] = Field(default=None, max_length=100, description="项目阶段")

    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")

    class Config:
        from_attributes = True


class ProjectCreate(BaseModel):
    """创建项目请求"""

    project_name: str = Field(max_length=200, description="项目名称")
    manager_user_id: Optional[int] = Field(default=None, description="负责人ID")
    manager_name: Optional[str] = Field(default=None, max_length=100, description="负责人姓名")
    project_start_date: Optional[date] = Field(default=None, description="开始日期")
    project_end_date: Optional[date] = Field(default=None, description="结束日期")
    project_status: str = Field(default="draft", description="项目状态")
    auth_level: int = Field(default=1, description="权限级别")
    project_source: int = Field(default=1, description="项目来源")
    product_type: Optional[str] = Field(default=None, max_length=100, description="产品类型")
    classify_name: Optional[str] = Field(default=None, max_length=100, description="仿真分类")
    project_phase_name: Optional[str] = Field(default=None, max_length=100, description="项目阶段")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")


class ProjectUpdate(BaseModel):
    """更新项目请求"""

    project_name: Optional[str] = Field(default=None, max_length=200, description="项目名称")
    manager_user_id: Optional[int] = Field(default=None, description="负责人ID")
    manager_name: Optional[str] = Field(default=None, max_length=100, description="负责人姓名")
    project_start_date: Optional[date] = Field(default=None, description="开始日期")
    project_end_date: Optional[date] = Field(default=None, description="结束日期")
    project_status: Optional[str] = Field(default=None, description="项目状态")
    auth_level: Optional[int] = Field(default=None, description="权限级别")
    project_source: Optional[int] = Field(default=None, description="项目来源")
    product_type: Optional[str] = Field(default=None, max_length=100, description="产品类型")
    classify_name: Optional[str] = Field(default=None, max_length=100, description="仿真分类")
    project_phase_name: Optional[str] = Field(default=None, max_length=100, description="项目阶段")
    remark: Optional[str] = Field(default=None, description="备注")


class ProjectResponse(BaseModel):
    """项目 API 响应"""

    code: int = Field(default=200, description="状态码")
    message: str = Field(default="success", description="响应消息")
    data: Optional[Project] = Field(default=None, description="项目数据")

"""
材料库 Pydantic 模型
====================

定义 LibraryMaterial 对应的 API 请求/响应模型。
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Material(BaseModel):
    """材料（只读展示模型）"""

    material_id: int = Field(description="材料ID")
    material_name: str = Field(max_length=200, description="材料名称")
    material_type: Optional[str] = Field(default=None, max_length=100, description="材料类型")
    supplier: Optional[str] = Field(default=None, max_length=200, description="供应商")
    version: str = Field(default="1.0.0", max_length=50, description="数据版本")
    security: int = Field(default=0, description="安全等级 (0=公开, 1=内部, 2=机密, 3=绝密)")
    properties: Optional[str] = Field(default=None, description="附加属性 (JSON)")

    created_at: Optional[datetime] = Field(default=None, description="创建时间")
    updated_at: Optional[datetime] = Field(default=None, description="更新时间")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")

    class Config:
        from_attributes = True


class MaterialCreate(BaseModel):
    """创建材料请求"""

    material_name: str = Field(max_length=200, description="材料名称")
    material_type: Optional[str] = Field(default=None, max_length=100, description="材料类型")
    supplier: Optional[str] = Field(default=None, max_length=200, description="供应商")
    version: str = Field(default="1.0.0", max_length=50, description="数据版本")
    security: int = Field(default=0, description="安全等级")
    properties: Optional[str] = Field(default=None, description="附加属性 (JSON)")
    created_by: Optional[str] = Field(default=None, max_length=100, description="创建人")
    remark: Optional[str] = Field(default=None, description="备注")


class MaterialUpdate(BaseModel):
    """更新材料请求"""

    material_name: Optional[str] = Field(default=None, max_length=200, description="材料名称")
    material_type: Optional[str] = Field(default=None, max_length=100, description="材料类型")
    supplier: Optional[str] = Field(default=None, max_length=200, description="供应商")
    version: Optional[str] = Field(default=None, max_length=50, description="数据版本")
    security: Optional[int] = Field(default=None, description="安全等级")
    properties: Optional[str] = Field(default=None, description="附加属性 (JSON)")
    remark: Optional[str] = Field(default=None, description="备注")


class MaterialResponse(BaseModel):
    """材料 API 响应"""

    code: int = Field(default=200, description="状态码")
    message: str = Field(default="success", description="响应消息")
    data: Optional[Material] = Field(default=None, description="材料数据")

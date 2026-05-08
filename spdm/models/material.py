"""
材料库 Pydantic 模型
=====================

定义材料的 API 请求/响应模型，与 SQLAlchemy 的 LibraryMaterial 对应。
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class MaterialBase(BaseModel):
    """材料基础字段"""
    material_name: str = Field(..., min_length=1, max_length=200, description="材料名称")
    material_type: Optional[str] = Field(default=None, max_length=100, description="材料类型")
    supplier: Optional[str] = Field(default=None, max_length=200, description="供应商")
    version: str = Field(default="1.0.0", max_length=50, description="数据版本")
    security: int = Field(default=0, description="安全等级")
    properties: Optional[str] = Field(default=None, description="附加属性 (JSON)")
    remark: Optional[str] = Field(default=None, description="备注")


class MaterialCreate(MaterialBase):
    """创建材料请求"""
    pass


class MaterialUpdate(BaseModel):
    """更新材料请求 —— 所有字段可选"""
    material_name: Optional[str] = Field(default=None, min_length=1, max_length=200)
    material_type: Optional[str] = Field(default=None, max_length=100)
    supplier: Optional[str] = Field(default=None, max_length=200)
    version: Optional[str] = Field(default=None, max_length=50)
    security: Optional[int] = None
    properties: Optional[str] = None
    remark: Optional[str] = None


class Material(MaterialBase):
    """材料完整模型 —— 用于响应"""
    material_id: int = Field(..., description="材料ID")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None

    class Config:
        from_attributes = True


class MaterialResponse(BaseModel):
    """材料响应包装"""
    code: int = Field(default=200)
    message: str = Field(default="success")
    data: Optional[Material] = None

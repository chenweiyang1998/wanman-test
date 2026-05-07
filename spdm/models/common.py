"""
通用响应模型
=============

提供统一的 API 响应格式和数据分页支持。
"""

from typing import TypeVar, Generic, Optional, List, Any
from pydantic import BaseModel, Field
from enum import Enum


T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    """统一响应格式"""
    code: int = Field(default=200, description="状态码: 200=成功, 其他=错误")
    message: str = Field(default="success", description="响应消息")
    data: Optional[T] = Field(default=None, description="响应数据")
    timestamp: Optional[int] = Field(default=None, description="时间戳")

    class Config:
        json_schema_extra = {
            "example": {
                "code": 200,
                "message": "success",
                "data": {"id": 1, "name": "示例"},
                "timestamp": 1704067200
            }
        }


class PaginatedResponse(BaseModel, Generic[T]):
    """分页响应格式"""
    code: int = Field(default=200, description="状态码")
    message: str = Field(default="success", description="响应消息")
    data: List[T] = Field(default_factory=list, description="数据列表")
    total: int = Field(default=0, description="总记录数")
    page: int = Field(default=1, description="当前页码")
    page_size: int = Field(default=20, description="每页记录数")
    total_pages: int = Field(default=0, description="总页数")

    class Config:
        json_schema_extra = {
            "example": {
                "code": 200,
                "message": "success",
                "data": [{"id": 1, "name": "示例"}],
                "total": 100,
                "page": 1,
                "page_size": 20,
                "total_pages": 5
            }
        }


class ErrorResponse(BaseModel):
    """错误响应格式"""
    code: int = Field(default=500, description="错误码")
    message: str = Field(default="Internal Server Error", description="错误消息")
    detail: Optional[str] = Field(default=None, description="详细错误信息")
    timestamp: Optional[int] = Field(default=None, description="时间戳")

    class Config:
        json_schema_extra = {
            "example": {
                "code": 400,
                "message": "Bad Request",
                "detail": "Invalid project name",
                "timestamp": 1704067200
            }
        }


class SuccessResponse(BaseModel):
    """简化成功响应"""
    success: bool = Field(default=True)
    message: str = Field(default="操作成功")

    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "message": "项目创建成功"
            }
        }
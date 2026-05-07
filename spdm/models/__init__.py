"""
数据模型定义
=============

基于 SPDM 产品上下文中的数据模型设计文档。
包含: SimProject, SimTask, SimCondition, SimWorkflow, LibraryMaterial 等核心实体。
"""

from .project import Project, ProjectCreate, ProjectUpdate, ProjectResponse
from .task import Task, TaskCreate, TaskUpdate, TaskResponse, TaskStatus
from .condition import Condition, ConditionCreate, ConditionUpdate, ConditionResponse
from .workflow import Workflow, WorkflowTemplate, WorkflowInstance
from .material import Material, MaterialCreate, MaterialUpdate, MaterialResponse
from .common import BaseResponse, PaginatedResponse, ErrorResponse

__all__ = [
    # Project
    "Project", "ProjectCreate", "ProjectUpdate", "ProjectResponse",
    # Task
    "Task", "TaskCreate", "TaskUpdate", "TaskResponse", "TaskStatus",
    # Condition
    "Condition", "ConditionCreate", "ConditionUpdate", "ConditionResponse",
    # Workflow
    "Workflow", "WorkflowTemplate", "WorkflowInstance",
    # Material
    "Material", "MaterialCreate", "MaterialUpdate", "MaterialResponse",
    # Common
    "BaseResponse", "PaginatedResponse", "ErrorResponse",
]
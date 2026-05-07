"""
SPDM 数据模型定义
=================

基于 SPDM 产品上下文中的数据模型设计文档。
使用 SQLAlchemy ORM 定义所有核心数据实体。

模型列表:
1. SimProject - 仿真项目
2. SimTask - 仿真任务
3. SimCondition - 工况
4. SimConditionTimes - 工况次
5. SimExperiment - 仿真实验
6. SimWorkflow - 仿真工作流
7. SimWorkflowTemplate - 工作流模板
8. SimBom - BOM
9. SimDocument - 图文档
10. SimReportResult - 报告结果
11. LibraryMaterial - 材料库
"""

from datetime import datetime, date
from typing import Optional, List
from enum import Enum

from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Boolean,
    DateTime,
    Date,
    Float,
    Text,
    ForeignKey,
    Index,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .database import Base


class ProjectStatus(str, Enum):
    """项目状态枚举"""
    DRAFT = "draft"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class TaskType(int, Enum):
    """任务类型枚举"""
    SIMULATION = 1
    COLLABORATION = 2
    BOM = 3
    DOCUMENT = 4


class TaskStatus(str, Enum):
    """任务状态枚举"""
    DRAFT = "draft"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    REVIEWING = "reviewing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class RunStatus(int, Enum):
    """运行状态枚举"""
    PENDING = 0
    QUEUED = 1
    RUNNING = 2
    PAUSED = 3
    COMPLETED = 4
    FAILED = 5
    CANCELLED = 6
    TIMEOUT = 7
    ERROR = 8
    UNKNOWN = 9


class FlowPublishStatus(int, Enum):
    """工作流发布状态枚举"""
    UNPUBLISHED = 1
    PUBLISHED = 2


class SecurityLevel(int, Enum):
    """安全等级枚举"""
    PUBLIC = 0
    INTERNAL = 1
    CONFIDENTIAL = 2
    SECRET = 3


# ============================================================================
# SimProject - 仿真项目
# ============================================================================

class SimProject(Base):
    """
    仿真项目模型

    属性:
        project_id: 项目ID (主键)
        project_name: 项目名称
        manager_user_id: 项目负责人ID
        manager_name: 项目负责人姓名
        project_start_date: 开始日期
        project_end_date: 结束日期
        project_status: 项目状态
        auth_level: 权限级别
        project_source: 项目来源 (1=SPDM原生, 2=PLM同步)
        product_type: 产品类型
        classify_name: 仿真分类名称
        project_phase_name: 项目阶段名称
    """

    __tablename__ = "sim_project"

    # 主键
    project_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 基本信息
    project_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    manager_user_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    manager_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # 日期
    project_start_date: Mapped[Optional[datetime]] = mapped_column(Date, nullable=True)
    project_end_date: Mapped[Optional[datetime]] = mapped_column(Date, nullable=True)

    # 状态和权限
    project_status: Mapped[str] = mapped_column(
        String(50), default=ProjectStatus.DRAFT.value, index=True
    )
    auth_level: Mapped[int] = mapped_column(Integer, default=1)

    # 来源和分类
    project_source: Mapped[int] = mapped_column(Integer, default=1)
    product_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    classify_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    project_phase_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    tasks: Mapped[List["SimTask"]] = relationship(
        "SimTask", back_populates="project", cascade="all, delete-orphan"
    )
    documents: Mapped[List["SimDocument"]] = relationship(
        "SimDocument", back_populates="project", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_project_name", "project_name"),
        Index("idx_project_status", "project_status"),
        Index("idx_project_manager", "manager_user_id"),
    )


# ============================================================================
# SimTask - 仿真任务
# ============================================================================

class SimTask(Base):
    """
    仿真任务模型

    属性:
        task_id: 任务ID (主键)
        task_code: 任务编号 (自动生成)
        task_name: 任务名称
        task_type: 任务类型 (1=仿真任务, 2=协同任务, 3=BOM, 4=图文档)
        manager_user_id: 任务负责人
        workflow_id: 关联工作流ID
        task_status: 任务状态
        auth_level: 权限级别
        business_area: 业务领域
        product_type: 产品类型
        simulation_type: 仿真类型 (结构/热/流体等)
        bom_id: 关联BOM ID
        bom_name: 关联BOM名称
        all_report_name: 报告名称
        all_report_id: 报告ID
    """

    __tablename__ = "sim_task"

    # 主键
    task_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 基本信息
    task_code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    task_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    task_type: Mapped[int] = mapped_column(Integer, default=TaskType.SIMULATION.value)

    # 负责人
    manager_user_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    manager_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # 工作流关联
    workflow_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)

    # 状态和权限
    task_status: Mapped[str] = mapped_column(
        String(50), default=TaskStatus.DRAFT.value, index=True
    )
    auth_level: Mapped[int] = mapped_column(Integer, default=1)

    # 业务属性
    business_area: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    product_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    simulation_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # BOM 关联
    bom_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    bom_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # 报告关联
    all_report_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    all_report_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # 外键关联项目
    project_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_project.project_id"), nullable=True, index=True
    )

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    project: Mapped[Optional["SimProject"]] = relationship("SimProject", back_populates="tasks")
    conditions: Mapped[List["SimCondition"]] = relationship(
        "SimCondition", back_populates="task", cascade="all, delete-orphan"
    )
    experiments: Mapped[List["SimExperiment"]] = relationship(
        "SimExperiment", back_populates="task", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_task_code", "task_code", unique=True),
        Index("idx_task_name", "task_name"),
        Index("idx_task_status", "task_status"),
        Index("idx_task_project", "project_id"),
    )


# ============================================================================
# SimCondition - 工况
# ============================================================================

class SimCondition(Base):
    """
    工况模型

    属性:
        condition_id: 工况ID (主键)
        flow_id: 关联工作流实例ID
        task_id: 关联任务ID
        experiment_id: 关联实验ID
        name: 工况名称
        is_default_condition: 是否默认工况
        condition_hierarchy: 工况层级 (parent-child 关系)
    """

    __tablename__ = "sim_condition"

    # 主键
    condition_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 关联字段
    task_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_task.task_id"), nullable=True, index=True
    )
    experiment_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    flow_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)

    # 工况信息
    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    is_default_condition: Mapped[bool] = mapped_column(Boolean, default=False)
    condition_hierarchy: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    task: Mapped[Optional["SimTask"]] = relationship("SimTask", back_populates="conditions")
    condition_times: Mapped[List["SimConditionTimes"]] = relationship(
        "SimConditionTimes", back_populates="condition", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_condition_task", "task_id"),
        Index("idx_condition_name", "name"),
    )


# ============================================================================
# SimConditionTimes - 工况次
# ============================================================================

class SimConditionTimes(Base):
    """
    工况次模型

    属性:
        condition_times_id: 工况次ID (主键)
        condition_id: 所属工况ID
        run_status: 运行状态 (0~9 枚举)
        submit_time: 提交时间
        start_time: 开始执行时间
        end_time: 结束时间
        result_file_id: 结果文件ID
    """

    __tablename__ = "sim_condition_times"

    # 主键
    condition_times_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )

    # 外键
    condition_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("sim_condition.condition_id"), nullable=False, index=True
    )

    # 运行状态
    run_status: Mapped[int] = mapped_column(Integer, default=RunStatus.PENDING.value, index=True)
    run_message: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # 时间字段
    submit_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    # 结果文件
    result_file_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    condition: Mapped["SimCondition"] = relationship(
        "SimCondition", back_populates="condition_times"
    )

    __table_args__ = (
        Index("idx_condition_times_condition", "condition_id"),
        Index("idx_condition_times_status", "run_status"),
    )


# ============================================================================
# SimExperiment - 仿真实验
# ============================================================================

class SimExperiment(Base):
    """
    仿真实验模型

    属性:
        experiment_id: 实验ID (主键)
        experiment_code: 实验编号
        experiment_src: 实验来源
        experiment_name: 实验名称
        ops_user_id: 操作人ID
        workflow_name: 工作流名称
        experiment_status: 实验状态
        auth_level: 权限级别
    """

    __tablename__ = "sim_experiment"

    # 主键
    experiment_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 实验信息
    experiment_code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    experiment_src: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    experiment_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)

    # 操作人
    ops_user_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    ops_user_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # 工作流
    workflow_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # 状态和权限
    experiment_status: Mapped[str] = mapped_column(String(50), default="draft", index=True)
    auth_level: Mapped[int] = mapped_column(Integer, default=1)

    # 外键关联任务
    task_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_task.task_id"), nullable=True, index=True
    )

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    task: Mapped[Optional["SimTask"]] = relationship("SimTask", back_populates="experiments")
    workflows: Mapped[List["SimWorkflow"]] = relationship(
        "SimWorkflow", back_populates="experiment", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_experiment_code", "experiment_code", unique=True),
        Index("idx_experiment_name", "experiment_name"),
        Index("idx_experiment_status", "experiment_status"),
    )


# ============================================================================
# SimWorkflowTemplate - 工作流模板
# ============================================================================

class SimWorkflowTemplate(Base):
    """
    工作流模板模型

    属性:
        template_id: 模板ID (主键)
        template_name: 模板名称
        simulation_type: 仿真类型
        version: 版本号
        param_count: 参数数量
        description: 模板描述
    """

    __tablename__ = "sim_workflow_template"

    # 主键
    template_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 模板信息
    template_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    simulation_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0.0")
    param_count: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    workflows: Mapped[List["SimWorkflow"]] = relationship(
        "SimWorkflow", back_populates="template"
    )

    __table_args__ = (
        Index("idx_template_name", "template_name"),
    )


# ============================================================================
# SimWorkflow - 仿真工作流
# ============================================================================

class SimWorkflow(Base):
    """
    仿真工作流实例模型

    属性:
        flow_id: 工作流ID (主键)
        experiment_id: 关联实验ID
        template_id: 关联模板ID
        flow_name: 工作流名称
        flow_type: 工作流类型
        flow_publish_status: 发布状态 (1=未发布, 2=已发布)
        flow_version: 版本号
    """

    __tablename__ = "sim_workflow"

    # 主键
    flow_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 关联字段
    experiment_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_experiment.experiment_id"), nullable=True, index=True
    )
    template_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_workflow_template.template_id"), nullable=True
    )

    # 工作流信息
    flow_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    flow_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    flow_publish_status: Mapped[int] = mapped_column(
        Integer, default=FlowPublishStatus.UNPUBLISHED.value
    )
    flow_version: Mapped[str] = mapped_column(String(50), default="1.0.0")

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    experiment: Mapped[Optional["SimExperiment"]] = relationship(
        "SimExperiment", back_populates="workflows"
    )
    template: Mapped[Optional["SimWorkflowTemplate"]] = relationship(
        "SimWorkflowTemplate", back_populates="workflows"
    )

    __table_args__ = (
        Index("idx_workflow_name", "flow_name"),
        Index("idx_workflow_experiment", "experiment_id"),
    )


# ============================================================================
# SimBom - BOM
# ============================================================================

class SimBom(Base):
    """
    BOM (物料清单) 模型

    属性:
        bom_id: BOM ID (主键)
        bom_name: BOM名称
        encode: BOM编码
        version: 版本
        security: 安全等级
        unit: 单位
        file_id: 关联文件ID
        status: 状态
        change_message: 变更说明
    """

    __tablename__ = "sim_bom"

    # 主键
    bom_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # BOM 信息
    bom_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    encode: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0.0")
    security: Mapped[int] = mapped_column(Integer, default=SecurityLevel.INTERNAL.value)
    unit: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    # 文件关联
    file_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)

    # 状态
    status: Mapped[int] = mapped_column(Integer, default=1)
    change_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    __table_args__ = (
        Index("idx_bom_name", "bom_name"),
        Index("idx_bom_encode", "encode"),
    )


# ============================================================================
# SimDocument - 图文档
# ============================================================================

class SimDocument(Base):
    """
    图文档模型

    属性:
        document_id: 文档ID (主键)
        doc_name: 文档名称
        encode: 图号/编码
        version: 版本
        security: 安全等级
        file_id: 关联文件ID
        change_message: 变更说明
    """

    __tablename__ = "sim_document"

    # 主键
    document_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 文档信息
    doc_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    encode: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0.0")
    security: Mapped[int] = mapped_column(Integer, default=SecurityLevel.INTERNAL.value)

    # 文件关联
    file_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)

    # 变更信息
    change_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 外键关联项目
    project_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_project.project_id"), nullable=True, index=True
    )

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 关系
    project: Mapped[Optional["SimProject"]] = relationship("SimProject", back_populates="documents")

    __table_args__ = (
        Index("idx_document_name", "doc_name"),
        Index("idx_document_encode", "encode"),
        Index("idx_document_project", "project_id"),
    )


# ============================================================================
# SimReportResult - 报告结果
# ============================================================================

class SimReportResult(Base):
    """
    报告结果模型

    属性:
        report_id: 报告ID (主键)
        report_name: 报告名称
        report_type: 报告类型
        task_id: 关联任务ID
        experiment_id: 关联实验ID
        file_id: 报告文件ID
        report_status: 报告状态
    """

    __tablename__ = "sim_report_result"

    # 主键
    report_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 报告信息
    report_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    report_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    report_status: Mapped[str] = mapped_column(String(50), default="draft", index=True)

    # 关联字段
    task_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, ForeignKey("sim_task.task_id"), nullable=True, index=True
    )
    experiment_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)

    # 文件
    file_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    file_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    __table_args__ = (
        Index("idx_report_name", "report_name"),
        Index("idx_report_task", "task_id"),
        Index("idx_report_status", "report_status"),
    )


# ============================================================================
# LibraryMaterial - 材料库
# ============================================================================

class LibraryMaterial(Base):
    """
    材料库模型

    属性:
        material_id: 材料ID (主键)
        material_name: 材料名称
        material_type: 材料类型 (金属/塑料等)
        supplier: 供应商
        version: 数据版本
        security: 安全等级
    """

    __tablename__ = "library_material"

    # 主键
    material_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # 材料信息
    material_name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    material_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    supplier: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0.0")
    security: Mapped[int] = mapped_column(Integer, default=SecurityLevel.PUBLIC.value)

    # 附加属性 (JSON 格式存储)
    properties: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # 审计字段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_by: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    remark: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    __table_args__ = (
        Index("idx_material_name", "material_name"),
        Index("idx_material_type", "material_type"),
    )


# ============================================================================
# 模型列表导出
# ============================================================================

__all__ = [
    # 枚举
    "ProjectStatus",
    "TaskType",
    "TaskStatus",
    "RunStatus",
    "FlowPublishStatus",
    "SecurityLevel",
    # 模型
    "SimProject",
    "SimTask",
    "SimCondition",
    "SimConditionTimes",
    "SimExperiment",
    "SimWorkflow",
    "SimWorkflowTemplate",
    "SimBom",
    "SimDocument",
    "SimReportResult",
    "LibraryMaterial",
]

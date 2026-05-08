# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Project initialization
- Basic metadata files (.editorconfig, .gitignore, LICENSE)
- Initial README documentation
- Comprehensive README.md with project overview, structure, and workflow

### Changed
- Renamed readme.md to README.md (standard naming)

### Planned
- Full documentation structure
- Test coverage setup
- CI/CD pipeline configuration

## [v0.2.0] - 2026-05-07

### Added
- **SPDM 数据管理原型** (`deliverables/spdm-data-management/`)
  - `index.html` - p5.js 驱动的交互式数据可视化页面，展示 BOM、仿真任务、工况、报告等数据节点和连接线动画
  - `philosophy.md` - 设计哲学文档，阐述"数据流动生命体"的可视化理念
  - `prototype.svg` - SVG 格式原型图
  - `spdm-data-management-prototype.png` - 静态原型预览图
  - `package.json` / `package-lock.json` - Node.js 依赖配置
  - HTTP 服务器启动脚本

### Features
- 交互式节点动画展示仿真数据结构
- 品牌色彩系统（SPDM 蓝 #409EFF）
- 数据流连接线动画效果
- 响应式设计，支持多种屏幕尺寸

# 地方项目节奏配额

配额服务按地区权重、季度上限和日历规则安排申报，返回冲突来源与剩余额度。`contracts` 中提供地区和申报示例，数据文件位于挂载目录。

运行 `docker build -t q010-quota . && docker run --rm -p 8080:8080 q010-quota`，再请求 `/health`。

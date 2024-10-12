## 要求

1. 发票审批：对于数据集 a，付款方为"浙江大学"、时间在 2015 年内、审批金额在 1600 元以内的发票视为合规

2. 发票审批：对于数据集 b，付款方为"深圳市购机汇网络有限公司"、时间在 2016 年 6 月 12 日、审批金额在 2700 元以内的发票视为合规；

3. 记录每张发票的审批状态（“通过”、“不通过”、“转人工”三种）

4. 财务关系治理：基于发票信息，提取出交易主体（买方和卖方）间的交易关系，并按照金额、交易频度等信息将交易主体按照买方和卖方分类表述（例如大客户、客户、一般客户；或者重要供应商、供应商、一般供应商）。

5. 发票及治理数据归档持久化：将处理的原始数据和数据结果（包括发票图片）存入数据库中（具体数据库自选）。

6. 自选简单算法计算处理发票的统计信息，包括但不限于发票数量、审批状态比例、当前交易量最大的 Top K 个交易方等。

## 数据库关系表

1. 发票数据表（插入前先检查密码区是否已存在）

| 字段名           | 数据类型 | 说明                                 |
| ---------------- | -------- | ------------------------------------ |
| id               | Long     | 发票 ID                              |
| date             | Date     | 日期，对应（issue-date）             |
| status           | String   | 审批状态                             |
| amount           | Double   | 金额，对应（total-cover-tax-digits） |
| buyerId（外键）  | Long     | 买方，对应（payer-name）             |
| sellerId（外键） | Long     | 卖方，对应（seller-name）            |
| crypto           | String   | 密码区，对应（cryptographic-area）   |
| img_url          | String   | 发票图片地址                         |
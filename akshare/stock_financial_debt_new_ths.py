import akshare as ak
import pandas as pd
import sys
import io
from datetime import datetime

# Set stdout to UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============ 配置参数 ============
symbol = "000063"          # 股票代码
indicator = "按季度"        # 报告周期: 按季度 / 按年度 / 按单季度
# =================================

# Fetch data
stock_financial_debt_new_ths_df = ak.stock_financial_debt_new_ths(symbol=symbol, indicator=indicator)

print(f"=== {symbol} 财务债务数据分析 ===")
print()

# 1. 数据概览
print("【1. 数据概览】")
print(f"总记录数: {len(stock_financial_debt_new_ths_df)} 行")
print(f"时间范围: {stock_financial_debt_new_ths_df['report_date'].min()} 至 {stock_financial_debt_new_ths_df['report_date'].max()}")
print(f"指标数量: {stock_financial_debt_new_ths_df['metric_name'].nunique()} 个")
print()

# 2. 核心债务指标分析
print("【2. 核心债务指标最新数据】")
core_metrics = {
    'equity': '股东权益',
    'bonds_payable': '应付债券',
    'long_loan': '长期借款',
    'short_loan': '短期借款',
    'total_liability': '负债合计',
    'total_assets': '资产总计',
}

for metric_code, metric_name in core_metrics.items():
    data = stock_financial_debt_new_ths_df[stock_financial_debt_new_ths_df['metric_name'] == metric_code]
    data = data[data['value'].notna() & (data['value'] != '')]
    if not data.empty:
        latest = data.iloc[0]
        value = float(latest['value']) / 100000000  # 转换为亿元
        yoy = latest.get('yoy', '')
        yoy_str = f"同比: {float(yoy)*100:.2f}%" if yoy and yoy != '' else '同比: N/A'
        print(f"  {metric_name}: {value:.2f}亿元  ({yoy_str})")

print()

# 3. 债务结构分析
print("【3. 债务结构分析】")

# 获取最新报告期的数据
latest_report = stock_financial_debt_new_ths_df['report_date'].max()
latest_data = stock_financial_debt_new_ths_df[stock_financial_debt_new_ths_df['report_date'] == latest_report]

# 计算资产负债率
if 'total_assets' in latest_data['metric_name'].values and 'total_liability' in latest_data['metric_name'].values:
    assets = float(latest_data[latest_data['metric_name'] == 'total_assets']['value'].values[0])
    liability = float(latest_data[latest_data['metric_name'] == 'total_liability']['value'].values[0])
    if assets > 0:
        debt_ratio = (liability / assets) * 100
        print(f"  资产负债率: {debt_ratio:.2f}%")
        print(f"    - 总资产: {assets/100000000:.2f}亿元")
        print(f"    - 总负债: {liability/100000000:.2f}亿元")

print()

# 4. 保存分析结果
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"financial_debt_{symbol}_{timestamp}.csv"
stock_financial_debt_new_ths_df.to_csv(csv_file, index=False, encoding='utf-8-sig')
print(f"✓ 完整数据已保存: {csv_file}")

print()
print("【数据字段说明】")
print("字段 | 说明")
print("-----|------")
print("report_date | 报告日期")
print("report_name | 报告名称 (如2024年报)")
print("quarter_name | 季度名称")
print("metric_name | 指标名称 (英文代码)")
print("value | 指标数值 (元)")
print("yoy | 同比增长率")
print("mom | 环比增长率")

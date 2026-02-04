import akshare as ak
import sys
import io
from datetime import datetime

# Set stdout to UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============ 手动指定日期 ============
# 格式: YYYYMMDD，例如: "20260203"
date = "20260203"
# ====================================

# Fetch SZSE summary data
stock_szse_summary_df = ak.stock_szse_summary(date=date)

# Display in console
print("=== 深圳证券交易所证券类别统计 ===")
print(f"数据日期: {date}")
print()
print(stock_szse_summary_df)
print()

# Save to CSV file for later analysis
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"szse_summary_{timestamp}.csv"
stock_szse_summary_df.to_csv(csv_file, index=False, encoding='utf-8-sig')

print(f"✓ CSV文件已保存: {csv_file}")

import akshare as ak
import sys
import io
from datetime import datetime

# Set stdout to UTF-8 encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Fetch SSE summary data
stock_sse_summary_df = ak.stock_sse_summary()

# Display in console
print("=== 上海证券交易所汇总数据 ===")
print(stock_sse_summary_df)
print()

# Save to CSV file for later analysis
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f"sse_summary_{timestamp}.csv"
stock_sse_summary_df.to_csv(csv_file, index=False, encoding='utf-8-sig')

print(f"✓ CSV文件已保存: {csv_file}")

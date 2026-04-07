"""
test_tools.py — Kiểm tra từng tool hoạt động đúng trước khi chạy agent
Chạy: python test_tools.py
"""

from tools import search_flights, search_hotels, calculate_budget

print("=" * 55)
print("  TEST 1: search_flights")
print("=" * 55)

# Test case 1: Tuyến bay tồn tại
result = search_flights.invoke({"origin": "Hà Nội", "destination": "Đà Nẵng"})
print(result)

# Test case 2: Tra ngược chiều (không có trong DB nhưng phải tìm được)
result = search_flights.invoke({"origin": "Đà Nẵng", "destination": "Hà Nội"})
print("Tra ngược chiều:")
print(result)

# Test case 3: Tuyến không tồn tại
result = search_flights.invoke({"origin": "Đà Nẵng", "destination": "Phú Quốc"})
print("Tuyến không tồn tại:")
print(result)


print("=" * 55)
print("  TEST 2: search_hotels")
print("=" * 55)

# Test case 1: Lọc theo budget
result = search_hotels.invoke({"city": "Đà Nẵng", "max_price_per_night": 500_000})
print(result)

# Test case 2: Không giới hạn giá
result = search_hotels.invoke({"city": "Phú Quốc"})
print("Phú Quốc (không giới hạn):")
print(result)

# Test case 3: Budget quá thấp
result = search_hotels.invoke({"city": "Hồ Chí Minh", "max_price_per_night": 100_000})
print("Budget quá thấp:")
print(result)


print("=" * 55)
print("  TEST 3: calculate_budget")
print("=" * 55)

# Test case 1: Trong ngân sách
result = calculate_budget.invoke({
    "total_budget": 5_000_000,
    "expenses": "vé_máy_bay:890000,khách_sạn:650000"
})
print(result)

# Test case 2: Vượt ngân sách
result = calculate_budget.invoke({
    "total_budget": 3_000_000,
    "expenses": "vé_máy_bay:2100000,khách_sạn:1500000"
})
print("Vượt ngân sách:")
print(result)

# Test case 3: Sai định dạng
result = calculate_budget.invoke({
    "total_budget": 5_000_000,
    "expenses": "vé_máy_bay_890000"   # thiếu dấu :
})
print("Sai định dạng:")
print(result)

print("=" * 55)
print("  Tất cả tests hoàn thành!")
print("=" * 55)
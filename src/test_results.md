# Test Results — TravelBuddy Agent (Lab 4)

---

## Test 1 — Direct Answer (Không gọi tool)

**Input:**

```
Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
```

**Console log:**

```
TravelBuddy đang suy nghĩ...
  💬 Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt khi bạn đang có kế hoạch đi du lịch. Bạn có thể cho mình biết một chút về sở thích của bạn không? Bạn muốn khám phá thành phố, biển hay núi? Và ngân sách của bạn cho chuyến đi này là bao nhiêu? Mình sẽ giúp bạn tìm điểm đến phù hợp nhất!
```

**Kết quả:** ✅ PASS — Không gọi tool, hỏi thêm thông tin cần thiết.

---

## Test 2 — Single Tool Call

**Input:**

```
Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
```

**Console log:**

```
TravelBuddy đang suy nghĩ...
  🔧 Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
  💬 Trả lời trực tiếp

TravelBuddy: ✈️ Chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines (Economy)**
   - Giờ bay: 06:00 → 07:20
   - Giá vé: **1.450.000đ**

2. **Vietnam Airlines (Business)**
   - Giờ bay: 14:00 → 15:20
   - Giá vé: **2.800.000đ**

3. **VietJet Air (Economy)**
   - Giờ bay: 08:30 → 09:50
   - Giá vé: **890.000đ**

4. **Bamboo Airways (Economy)**
   - Giờ bay: 11:00 → 12:20
   - Giá vé: **1.200.000đ**

Nếu bạn cần thêm thông tin về khách sạn hoặc ngân sách, hãy cho mình biết nhé!
```

**Kết quả:** ✅ PASS — Gọi đúng `search_flights("Hà Nội", "Đà Nẵng")`, liệt kê 4 chuyến bay đầy đủ.

---

## Test 3 — Multi-Step Tool Chaining

**Input:**

```
Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
```

**Console log:**

```
TravelBuddy đang suy nghĩ...
  🔧 Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
  🔧 Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 99999999})
  🔧 Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:400000'})
  💬 Trả lời trực tiếp

TravelBuddy: Chào bạn! Dưới đây là gợi ý cho chuyến đi từ Hà Nội đến Phú Quốc trong 2 đêm với ngân sách 5 triệu:

✈️ **Chuyến bay:**
1. **VietJet Air (Economy)**
   - Giờ bay: 10:00 → 12:15
   - Giá vé: **1.350.000đ**

🏨 **Khách sạn:**
1. **Sol by Meliá ⭐⭐⭐⭐**
   - Khu vực: Bãi Trường
   - Rating: 4.2/5
   - Giá: **1.500.000đ/đêm** (Tổng cho 2 đêm: **3.000.000đ**)

   Hoặc bạn có thể chọn:
2. **9Station Hostel ⭐⭐**
   - Khu vực: Dương Đông
   - Rating: 4.5/5
   - Giá: **200.000đ/đêm** (Tổng cho 2 đêm: **400.000đ**)

💰 **Tổng chi phí ước tính:**
- Vé máy bay: **1.350.000đ**
- Khách sạn (Sol by Meliá): **3.000.000đ** (hoặc 400.000đ nếu chọn 9Station Hostel)
- **Tổng chi:** **4.350.000đ** (hoặc 1.750.000đ nếu chọn 9Station Hostel)

🎯 **Ngân sách còn lại:**
- Nếu chọn Sol by Meliá: **2.050.000đ**
- Nếu chọn 9Station Hostel: **3.250.000đ**

Bạn có thể sử dụng ngân sách còn lại để ăn uống, tham quan hoặc mua sắm. Nếu cần thêm thông tin hay hỗ trợ gì khác, cứ hỏi mình nhé!
```

**Kết quả:** ✅ PASS — Agent tự chuỗi 3 tool calls liên tiếp, tổng hợp thành gợi ý hoàn chỉnh với bảng chi phí.

---

## Test 4 — Missing Info / Clarification

**Input:**

```
Tôi muốn đặt khách sạn
```

**Console log:**

```
TravelBuddy đang suy nghĩ...
  💬 Trả lời trực tiếp

TravelBuddy: Mình sẽ giúp bạn tìm khách sạn ngay! Cho mình biết thêm một chút nhé:
- Bạn muốn ở thành phố nào? (Đà Nẵng, Phú Quốc, Hồ Chí Minh...)
- Ở bao nhiêu đêm?
- Ngân sách tối đa mỗi đêm là bao nhiêu?
```

**Kết quả:** ✅ PASS — Không gọi tool vội, hỏi lại 3 thông tin cần thiết.

---

## Test 5 — Guardrail / Refusal

**Input:**

```
Giải giúp tôi bài tập lập trình Python về linked list
```

**Console log:**

```
TravelBuddy đang suy nghĩ...
  💬 Trả lời trực tiếp

TravelBuddy: Xin lỗi, nhưng mình chỉ có thể hỗ trợ bạn về du lịch và các vấn đề liên quan đến đặt vé máy bay, khách sạn. Nếu bạn cần tư vấn về chuyến đi, hãy cho mình biết nhé!
```

**Kết quả:** ✅ PASS — Từ chối lịch sự, không gọi tool, redirect về du lịch.

---

## Tóm tắt

| Test | Loại                | Tool calls                    | Kết quả |
| ---- | ------------------- | ----------------------------- | ------- |
| 1    | Direct Answer       | 0                             | ✅ PASS |
| 2    | Single Tool         | 1 (`search_flights`)          | ✅ PASS |
| 3    | Multi-Step Chaining | 3 (flights → hotels → budget) | ✅ PASS |
| 4    | Clarification       | 0                             | ✅ PASS |
| 5    | Guardrail           | 0                             | ✅ PASS |

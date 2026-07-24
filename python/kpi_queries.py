import sqlite3

conn = sqlite3.connect("supply_chain.db")
cursor = conn.cursor()

# --- KPI 1: On-Time Delivery Rate ---
query1 = """
SELECT
    COUNT(*) AS total_orders,
    SUM(CASE WHEN late_delivery_risk = 0 THEN 1 ELSE 0 END) AS on_time_orders,
    ROUND(
        100.0 * SUM(CASE WHEN late_delivery_risk = 0 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS on_time_delivery_rate_pct
FROM orders;
"""

cursor.execute(query1)
result1 = cursor.fetchone()

print("--- On-Time Delivery Rate ---")
print(f"Total orders: {result1[0]}")
print(f"On-time orders: {result1[1]}")
print(f"On-time delivery rate: {result1[2]}%")

# --- KPI 2: Order Status Breakdown ---
print("\n--- Order Status Breakdown ---")
query2 = """
SELECT
    order_status,
    COUNT(*) AS order_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders), 2) AS pct_of_total
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

for row in results2:
    print(f"{row[0]}: {row[1]} orders ({row[2]}%)")

# --- KPI 3: Fulfillment Rate ---
print("\n--- Fulfillment Rate ---")
query3 = """
SELECT
    COUNT(*) AS total_orders,
    SUM(CASE WHEN order_status IN ('COMPLETE', 'CLOSED') THEN 1 ELSE 0 END) AS fulfilled_orders,
    ROUND(
        100.0 * SUM(CASE WHEN order_status IN ('COMPLETE', 'CLOSED') THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS fulfillment_rate_pct
FROM orders;
"""

cursor.execute(query3)
result3 = cursor.fetchone()

print(f"Total orders: {result3[0]}")
print(f"Fulfilled orders (Complete + Closed): {result3[1]}")
print(f"Fulfillment rate: {result3[2]}%")

# --- KPI 4: Average Delivery Delay ---
print("\n--- Average Delivery Delay ---")
query4 = """
SELECT
    ROUND(AVG(days_for_shipping_real - days_for_shipment_scheduled), 2) AS avg_delay_days,
    ROUND(AVG(CASE WHEN days_for_shipping_real > days_for_shipment_scheduled 
              THEN days_for_shipping_real - days_for_shipment_scheduled END), 2) AS avg_delay_when_late_only
FROM orders;
"""

cursor.execute(query4)
result4 = cursor.fetchone()

print(f"Average delay across ALL orders: {result4[0]} days")
print(f"Average delay among LATE orders only: {result4[1]} days")

# --- KPI 5: On-Time Delivery Rate by Shipping Mode ---
print("\n--- On-Time Delivery Rate by Shipping Mode ---")
query5 = """
SELECT
    shipping_mode,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN late_delivery_risk = 0 THEN 1 ELSE 0 END) AS on_time_orders,
    ROUND(
        100.0 * SUM(CASE WHEN late_delivery_risk = 0 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS on_time_rate_pct
FROM orders
GROUP BY shipping_mode
ORDER BY on_time_rate_pct ASC;
"""

cursor.execute(query5)
results5 = cursor.fetchall()

for row in results5:
    print(f"{row[0]}: {row[1]} orders, {row[2]} on-time, {row[3]}% on-time rate")

# --- KPI 6: On-Time Delivery Rate by Product Category (worst 10) ---
print("\n--- On-Time Delivery Rate by Product Category (Worst 10) ---")
query6 = """
SELECT
    category_name,
    COUNT(*) AS total_orders,
    ROUND(
        100.0 * SUM(CASE WHEN late_delivery_risk = 0 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS on_time_rate_pct
FROM orders
GROUP BY category_name
HAVING COUNT(*) > 500
ORDER BY on_time_rate_pct ASC
LIMIT 10;
"""

cursor.execute(query6)
results6 = cursor.fetchall()

for row in results6:
    print(f"{row[0]}: {row[1]} orders, {row[2]}% on-time rate")

# Close the connection only after ALL queries are done
conn.close()


# Sales Data Analyzer

sales = {
    "Laptop": [45000, 52000, 48000, 50000],
    "Phone": [20000, 25000, 22000, 24000],
    "Tablet": [15000, 18000, 17000, 16000],
    "Headphones": [3000, 3500, 3200, 4000]
}

print("=" * 40)
print("      SALES DATA ANALYZER")
print("=" * 40)

total_revenue = 0
best_product = ""
best_revenue = 0

for product, values in sales.items():
    revenue = sum(values)
    avg_sale = revenue / len(values)

    print(f"\nProduct: {product}")
    print(f"Total Revenue: ₹{revenue}")
    print(f"Average Sale: ₹{avg_sale:.2f}")

    total_revenue += revenue

    if revenue > best_revenue:
        best_revenue = revenue
        best_product = product

print("\n" + "=" * 40)
print(f"Overall Revenue: ₹{total_revenue}")
print(f"Best Selling Product: {best_product}")
print(f"Revenue Generated: ₹{best_revenue}")
print("=" * 40)

# Generate report file
with open("sales_report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("=" * 30 + "\n")

    for product, values in sales.items():
        revenue = sum(values)
        avg_sale = revenue / len(values)

        file.write(f"\nProduct: {product}\n")
        file.write(f"Revenue: Rs.{revenue}\n")
        file.write(f"Average Sale: Rs{avg_sale:.2f}\n")

    file.write("\n" + "=" * 30 + "\n")
    file.write(f"Overall Revenue: Rs{total_revenue}\n")
    file.write(f"Best Selling Product: {best_product}\n")

print("\nReport saved as sales_report.txt")
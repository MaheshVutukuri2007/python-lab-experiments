# Initialize counters and sums
positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

print("Enter numbers (enter -1 to stop):")

while True:
    num = float(input())

    if num == -1:
        break
    elif num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

# Calculate averages
if positive_count > 0:
    positive_avg = round(positive_sum / positive_count, 2)
else:
    positive_avg = 0.00

if negative_count > 0:
    negative_avg = round(negative_sum / negative_count, 2)
else:
    negative_avg = 0.00

# Display results
print(f"\nAverage of positive numbers: {positive_avg}")
print(f"Average of negative numbers: {negative_avg}")

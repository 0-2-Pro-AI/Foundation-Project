import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 1. Input: [Độ cứng, Độ bóng, Trọng lượng]
inputs = np.array([0.1, 0.1, 0.9])

# 2. Weights: [Quan trọng độ cứng, Quan trọng độ bóng, Ghét trọng lượng]
weights = np.array([0.1, 0.1, 0.9])

# 3. Tính toán cốt lõi
weighted_sum = np.dot(inputs, weights)
output = sigmoid(weighted_sum)

print(f"Tổng điểm: {weighted_sum}")
print(f"Xác suất là Kim Cương: {output:.4f}")

if output > 0.5:
    print("-> KẾT LUẬN: Đây là KIM CƯƠNG!")
else:
    print("-> KẾT LUẬN: Đây là CỤC ĐÁ!")

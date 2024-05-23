import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./Data/weather.csv")

selected_provinces = ["Ha Noi", "Ho Chi Minh City", "Hue"]
selected_data = data[data['province'].isin(selected_provinces)]

# Chuyển đổi cột ngày thành kiểu dữ liệu datetime
selected_data['date'] = pd.to_datetime(selected_data['date'])

# Tính toán nhiệt độ trung bình hàng ngày cho mỗi tỉnh/thành phố
average_temp = selected_data.groupby(['province', 'date'])[['max', 'min']].mean().reset_index()

# Vẽ biểu đồ
plt.figure(figsize=(20, 7))
sns.set_style("whitegrid")
sns.lineplot(data=average_temp, x='date', y='max', hue='province', palette='Set1')
plt.title('Biểu đồ nhiệt độ trung bình hàng ngày của các tỉnh/thành phố được chọn')
plt.xlabel('Ngày')
plt.ylabel('Nhiệt độ trung bình (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Tỉnh/Thành phố')
plt.show()
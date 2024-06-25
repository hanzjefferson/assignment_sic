from models import AI4IModel
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas

test_size = 0.36

model = AI4IModel()
model.csv("datasets/ai4i2020.csv")
model.preprocessing()
model.split(size=test_size,random_state=42)

model.fit()

target = model.get_fit().predict(model.get_test()[0])
result = pandas.DataFrame(model.get_test()[0])
result['Machine failure'] = target
print(result.head())

plt.scatter(range(int(test_size*len(model.x))), target)
plt.title("Prediksi Kesalahan Mesin (Machine Failure)")
plt.xlabel("Akurasi: "+str(accuracy_score(model.get_test()[1], target)*100)+"%")
plt.show()

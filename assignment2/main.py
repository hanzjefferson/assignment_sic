from models import AI4IModel
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
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
result['Type'] = model.real_type
result['Machine failure'] = target

print("Prediction Result:")
print(result.head())

accuracy = accuracy_score(model.get_test()[1], target)
print(f"\nAccuracy: {accuracy}")

conf_matrix = confusion_matrix(model.get_test()[1], target)
print(f"\nConfusion Matrix:\n{conf_matrix}")

class_report = classification_report(model.get_test()[1], target)
print(f"\nClassification Report:\n{class_report}")

plt.scatter(range(int(test_size*len(model.x))), target)
plt.title("Prediksi Kesalahan Mesin (Machine Failure)")
plt.xlabel("Akurasi: "+str(accuracy_score(model.get_test()[1], target)*100)+"%")
plt.show()

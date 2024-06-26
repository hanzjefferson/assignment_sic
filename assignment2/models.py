import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression

class BaseModel:
    def __init__(self, dataset=None, target_label=None, unused_label:str|list=None):import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression

class BaseModel:
    def __init__(self, dataset=None, target_label=None, unused_label:str|list=None):
        self._dataset = dataset
        if target_label is not None and self._dataset is not None:
            self.preprocessing(target_label, unused_label)

    def dataset(self):
        return self._dataset
    
    def preprocessing(self, target_label, unused_label: str|list=None):
        if unused_label is not None:
            self._dataset = self._dataset.drop(unused_label, axis=1)

        self.x = self._dataset.drop(target_label, axis=1)
        self.y = self._dataset[target_label]

    def split(self, size=0.4, random_state=None):
        self._split = train_test_split(self.x, self.y, test_size=size, random_state=random_state)

    def get_train(self):
        if self._split is not None:
            return (self._split[0], self._split[2])
        else:
            return None
        
    def get_test(self):
        if self._split is not None:
            return (self._split[1], self._split[3])
        else:
            return None
        
    def get_fit(self):
        if self.fit_model is None:
            self.fit()
        return self.fit_model
    
    def fit(self):
        self.fit_model = LinearRegression()
        self.fit_model.fit(*self.get_train())

    def csv(self, filename):
        self._dataset = pandas.read_csv(filename)
    
class AI4IModel(BaseModel):
    def preprocessing(self):
        super().preprocessing("Machine failure", ["UDI","Product ID","TWF","HDF","PWF","OSF","RNF"])
        self.real_type = self.x['Type']
        label_encoder = LabelEncoder()
        self.x['Type'] = label_encoder.fit_transform(self.x['Type'])

    def fit(self):
        self.fit_model = LogisticRegression()
        self.fit_model.fit(*self.get_train())
        self._dataset = dataset
        if target_label is not None and self._dataset is not None:
            self.preprocessing(target_label, unused_label)

    def dataset(self):
        return self._dataset
    
    def preprocessing(self, target_label, unused_label: str|list=None):
        if unused_label is not None:
            self._dataset = self._dataset.drop(unused_label, axis=1)

        self.x = self._dataset.drop(target_label, axis=1)
        self.y = self._dataset[target_label]

    def split(self, size=0.4, random_state=None):
        self._split = train_test_split(self.x, self.y, test_size=size, random_state=random_state)

    def get_train(self):
        if self._split is not None:
            return (self._split[0], self._split[2])
        else:
            return None
        
    def get_test(self):
        if self._split is not None:
            return (self._split[1], self._split[3])
        else:
            return None
        
    def get_fit(self):
        if self.fit_model is None:
            self.fit()
        return self.fit_model
    
    def fit(self):
        self.fit_model = LinearRegression()
        self.fit_model.fit(*self.get_train())

    def csv(self, filename):
        self._dataset = pandas.read_csv(filename)
    
class AI4IModel(BaseModel):
    def preprocessing(self):
        super().preprocessing("Machine failure", ["UDI","Product ID","TWF","HDF","PWF","OSF","RNF"])
        label_encoder = LabelEncoder()
        self.x['Type'] = label_encoder.fit_transform(self.x['Type'])

    def fit(self):
        self.fit_model = LogisticRegression()
        self.fit_model.fit(*self.get_train())

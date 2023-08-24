import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# 数据读取
titanic = pd.read_csv('train.csv')
# 平均值填充年龄缺失值
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
# 年龄的字符串改int
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1
# S填充Embarked缺失值
titanic['Embarked'] = titanic['Embarked'].fillna('S')
# Embarked 字符串改int
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2
# Cabin字段 用U填充
titanic['Cabin'] = titanic['Cabin'].fillna('U')

print(titanic.head())

from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
# SVM
from sklearn.svm import SVC

# KNN
from sklearn.neighbors import KNeighborsClassifier

alg = SVC(C=2, kernel='rbf', gamma=10, decision_function_shape='ovr')
predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

kf = KFold(n_splits=3, shuffle=True, random_state=1)
# kf  K折交叉验证  这里是3折交叉验证

test_accurate = []
for train, test in kf.split(titanic[predictors]):  # 表示 划分这些个特征做交叉验证

    train_predictors = (titanic[predictors].iloc[train, :])  # 拿出来训练的数据 pandas.iloc方法提供了基于整数的索引方式
    train_target = titanic["Survived"].iloc[train]  # 拿出来lable值
    # 模型计算
    alg.fit(train_predictors, train_target)

    test_predictions = (titanic[predictors].iloc[test, :])  # 拿出来测试的数据集

    test_target = titanic["Survived"].iloc[test]  # 拿出来测试的lable值
    # 这里有个东西需要注意，训练集  测试集 验证集

    pre_train = alg.predict(train_predictors)
    pre_test = alg.predict(test_predictions)

    test_accurate.append(accuracy_score(test_target, pre_test))
test_accurate = sum(test_accurate) / 3  # 取平均值
print(test_accurate)


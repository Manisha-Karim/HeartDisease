
# HeartDisease-Prediction-Machine-Learning-Model-Deployment-using-Django


Three datasets gathered from the UCI repository were combined to produce a unique dataset. The data was cleaned using Pandas and Numpy, and the null values were filled using a KNN imputer. Using Seaborn, EDA was used to choose the best features. Finally, four classifiers (KNN, DT, and RF) were fitted with hyperparameter tuning using GridSearchCV.



# Dataset

### Dataset Source

The Dataset was collected from UCI Machine Learning Repository. Three datasets gathered from the UCI repository were combined to produce a unique dataset.

### Dataset Description

The feature names and their meanings are:

age: age in years

sex: sex (1 = male; 0 = female)

cp: chest pain type

-- Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain -- Value 4: asymptomatic

trestbps: resting blood pressure (in mm Hg on admission to the hospital)

chol: serum cholestoral in mg/dl

fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

restecg: resting electrocardiographic results

-- Value 0: normal

-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)

-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

thalach: maximum heart rate achieved

exang: exercise induced angina (1 = yes; 0 = no)

oldpeak = ST depression induced by exercise relative to rest

slope: the slope of the peak exercise ST segment

-- Value 0: upsloping -- Value 1: flat -- Value 2: downsloping

ca: number of major vessels (0-3) colored by flourosopy

thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

and the label

Target: 13. condition: 0 = no disease, 1 = disease
# Data Pre-Processing

### Remove Null Values
1. Around 45+ percent of ca and thal are null, so drop this columns.

2. Rows of the columns which make only 3% of the dataframe altogether are also removed. The rows which had two or more null values where also removed.

3. The remaining missing values will be dealt with KNN imputer after EDA.

### Datatype and values

1. FastingBloodSugar should have 2(3 for null) values but has 4, atrestEcg should have 3 values but has 6, excerciseInducedangina should have 2 values but has 4, slope should have 3(4 for null) values but has 6. This due to the combination of 3 datasets, each has its own way of representing the same value. So, a common form is established.

2. Also, even though they are all numerical values, datatype is object. This is to be changed
## EDA

The Dataset is balanced. Heart disease is more common in males

Patients with normal ECG are equally likely to have Heart Disease. So, ECG test results are inconclusive. Multiple tests with ECG is required to diagnose heart disease

Fasting Blood Sugar is inconclusive in determining the presence of heart disease.

Asymptomatic Angina is the most common type of chest pain for Heart Disease.

Patients who do not feel any chest pain during exercise are not likely to have heart disease.

Patients with upslope in ECG is least likely to have heart disease while patients with flat is most likely to have heart disease.

1. An oldpeak(ST wave depression) of 2 or higher confirms the presence of Heart Disease in most cases

2. Heart patients usually have flat slope and a ST wave depression of 2 or higher (in most cases above 1.5) or higher.

3. The probability of heart disease increases with age.

4. From the description of the dataset it has been seen that cholestrol has outliers(large difference between mean and median). This has been further confirmed by the pairplot.

5. With the decrease in maximum heart rate, the probability of heart attack increases.

6. Heart disease probability increases with Higher Blood pressure. Blood pressure also increases with age.
# Outlier Detection and Removal

IQR capping was applied on 'age', 'atRestBps', 'cholestrol', 'maxHeartRate' to remove Outliers.
# Final Features

1. age	
2. sex	
3. chestPainType
4. atRestBps	
5. cholestrol	
6. maxHeartRate	
7. excerciseInducedangina	
8. oldpeak	
9. heartDisease	
10. slope
# Classifiers

Three classifiers (KNN, DT, and RF) were fitted with hyperparameter tuning using GridSearchCV. Random Forest had 
the highest accuracy of 86%. 







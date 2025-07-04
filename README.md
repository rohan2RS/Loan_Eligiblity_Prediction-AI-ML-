This project aims to build a model to predict loan approval status. The steps involved are:

Data Loading and Exploration: The loan-train.csv dataset is loaded and basic information, missing values, and target variable distribution are explored.
Data Cleaning: Missing values in several columns are filled using the mode or mean of the respective columns. The 'Dependents' column is cleaned and converted to integer type.
Exploratory Data Analysis (EDA): Visualizations are generated to explore the relationships between various features (Gender, Married, ApplicantIncome, LoanAmount) and the target variable (Loan_Status).
Data Preprocessing: Categorical features are encoded using LabelEncoder. The data is split into features (X) and target (y).
Model Training: A RandomForestClassifier model is trained on the preprocessed data.
Model Evaluation: The model's performance is evaluated using accuracy, classification report, and a confusion matrix.
Model Saving: The trained model is saved using pickle.

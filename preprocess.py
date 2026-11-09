import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(filepath):
    # 1. Đọc dữ liệu
    df = pd.read_csv(filepath)
    
    # 2. Xử lý dữ liệu lỗi và missing
    # Chuyển TotalCharges sang numeric, ép lỗi thành NaN và xóa dòng NaN
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    
    # Bỏ cột ID
    df = df.drop(columns=['customerID'])
    
    # 3. Mã hóa biến mục tiêu (Churn)
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # 4. One-Hot Encoding cho các biến phân loại
    df_encoded = pd.get_dummies(df, drop_first=True)
    
    # 5. Phân chia Train / Test
    X = df_encoded.drop('Churn', axis=1)
    y = df_encoded['Churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # 6. Chuẩn hóa đặc trưng liên tục
    scaler = StandardScaler()
    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    
    # Fit trên tập train và transform trên cả train và test
    X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
    X_test[num_cols] = scaler.transform(X_test[num_cols])
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    print("Pre-processing hoàn tất. Kích thước tập Train:", X_train.shape)
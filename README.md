# Bài tập lớn Học máy (CO3117) - Dự đoán khách hàng rời mạng (Telco Customer Churn)

## 1. Thông tin nhóm
- **Thành viên 1:** Nguyễn Đỗ Đăng Khoa - 2311615
- **Thành viên 2:** Lưu Chấn Kiến - 2211740
- **Thành viên 3:** Nguyễn Mạnh Trung - 2313674

## 2. Cấu trúc thư mục
- `data/`: Chứa tập dữ liệu gốc `WA_Fn-UseC_-Telco-Customer-Churn.csv`.
- `src/`: Chứa mã nguồn tiền xử lý và các notebook huấn luyện mô hình Random Forest và Gradient Boosting.
- `doc/`: Báo cáo tổng kết bài tập lớn (PDF) và slide thuyết trình.
- `requirements.txt`: Các thư viện Python cần thiết.

## 3. Môi trường thực thi
- Ngôn ngữ: Python 3
- Nền tảng thực nghiệm gốc: Google Colab
- Các thư viện chính: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

## 4. Hướng dẫn chạy code
### Cách 1: Chạy trực tiếp trên Google Colab (Khuyên dùng)
1. Tải các tệp `.ipynb` trong thư mục `src/` lên Google Colab.
2. Tải tệp `WA_Fn-UseC_-Telco-Customer-Churn.csv` vào thư mục làm việc của Colab (hoặc cập nhật lại đường dẫn file trong cell đọc dữ liệu).
3. Chọn **Runtime -> Run all** để chạy lại toàn bộ quá trình tiền xử lý, tinh chỉnh siêu tham số và đánh giá.

### Cách 2: Chạy trên máy cục bộ (Local)
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
Khởi chạy Jupyter Notebook:

Bash
jupyter notebook
Mở các tệp trong thư mục src/ và chạy lần lượt các cell từ trên xuống dưới.

5. Ghi chú về tính tái hiện (Reproducibility)
Toàn bộ quá trình chia tập dữ liệu (80% Train / 20% Test, phân tầng) và huấn luyện đều đã cố định random_state=42 để đảm bảo kết quả đánh giá (Accuracy, Precision, Recall, F1-Score, ROC-AUC) khớp hoàn toàn với báo cáo.

Link dữ liệu / mô hình dự phòng: https://github.com/khoagrai/BTL_ML.git
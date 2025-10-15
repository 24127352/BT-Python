filename = input("Nhập tên file: ").strip()

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print("----- Nội dung file -----")
    print(content)
except FileNotFoundError:
    print(f"Lỗi: file '{filename}' không tồn tại.")
except PermissionError:
    print(f"Lỗi: không có quyền đọc file '{filename}'.")
except UnicodeDecodeError:
    print(f"Lỗi: không thể giải mã file '{filename}' bằng 'utf-8'. Có thể file nhị phân hoặc mã hóa khác.")
except Exception as e:
    print(f"Lỗi không xác định: {e}")

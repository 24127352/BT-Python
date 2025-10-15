with open("output.txt", "w", encoding="utf-8") as out:
    out.write("I'm a student.\n")
    x = 1/7
    out.write(f"{x:.5f}\n")

    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    out.write(f"Tổng {a} + {b} = {a+b}\n")

    filename = input("Nhập tên file cần đọc: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            out.write("\n" + f.read())
    except FileNotFoundError:
        out.write("\n❌ Lỗi: File không tồn tại!\n")

print("✅ Đã ghi ra file output.txt")

# Phân tích input/ouput
# Input:
# - Họ và tên bệnh nhân (String)
# - Tuổi bệnh nhân (Integer)

# Output:
# - Phiếu khám điện tử gồm:
#   + Tên bệnh nhân
#   + Tuổi bệnh nhân
#   + Kết quả phân luồng
#
# - Hoặc thông báo lỗi nếu dữ liệu không hợp lệ

# Đề xuất giải pháp
# Bước 1:
# Kiểm tra dữ liệu đầu vào.
#
# - Tên không được bỏ trống.
# - Tên không được chỉ chứa khoảng trắng.
# - Tuổi phải nằm trong khoảng từ 0 đến 150.

# Nếu dữ liệu không hợp lệ:
# -> Hiển thị thông báo lỗi.

# Bước 2:
# Nếu dữ liệu hợp lệ thì thực hiện phân luồng.
# - Tuổi < 6
#   -> Bệnh nhi
# - Tuổi >= 80
#   -> Người cao tuổi
# - Các trường hợp còn lại
#   -> Khám thường

# Bước 3:
# In phiếu khám điện tử.

# pseudocode 

# Bắt đầu
# Nhập tên bệnh nhân
# Nhập tuổi bệnh nhân

# Nếu tên rỗng hoặc chỉ chứa khoảng trắng
#     Báo lỗi

# Ngược lại nếu tuổi < 0 hoặc tuổi > 150
#     Báo lỗi

# Ngược lại
#
#     Nếu tuổi < 6
#         Phân luồng bệnh nhi
#
#     Ngược lại nếu tuổi >= 80
#         Phân luồng người cao tuổi
#
#     Ngược lại
#         Phân luồng khám thường

#     In phiếu khám

# Kết thúc

# 4. SOURCE CODE

print("--- PATIENT TRIAGE SYSTEM ---")

patient_name = input("Nhập tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))


if patient_name.strip() == "" or patient_age < 0 or patient_age > 150:
    print("Tuổi bệnh nhân nhập sai hoặc chưa nhập! (0-150)!")

else:
    if patient_age < 6:
        result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
        
    elif patient_age >= 80:
        result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
        
    else:
        result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    print()
    print("--- PHIẾU KHÁM ĐIỆN TỬ ---")
    print("Tên bệnh nhân:", patient_name)
    print("Tuổi bệnh nhân:", patient_age)
    print("Kết quả:", result)

print("System process completed.")


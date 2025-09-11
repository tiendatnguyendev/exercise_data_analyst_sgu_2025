# ex3_circle.py

import math  # để sử dụng hằng số pi

def main():
    try:
        r = float(input("Nhập bán kính r của hình tròn: "))
        if r < 0:
            print("Bán kính phải là số dương!")
            return
        
        cv = 2 * math.pi * r
        dt = math.pi * r**2  # diện tích là π * r^2, không phải π * r
        
        print(f"Chu vi hình tròn: {cv:.2f}")
        print(f"Diện tích hình tròn: {dt:.2f}")
    
    except ValueError:
        print("Vui lòng nhập một số thực hợp lệ.")

if __name__ == "__main__":
    main()

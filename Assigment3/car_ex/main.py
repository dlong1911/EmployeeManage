from define import Mercedes, Audi, Vinfast

from soupsieve import select
ds_xe=[]

while True:
    print('''

    Moi ban chon chuc nang
    1. Hien thi danh sach xe
    2. Them xe moi
    3. sua thong tin Xe
    4. Luu thong tin
    0. Exit 

    ''')
    select=int(input())
    if str(select).isdigit():
        if select == 1:
            print(f"\nDanh sach Xe:")
            for i in ds_xe:
                i.show_info()
        if select == 2:
            print("Nhap thong tin xe moi")  
            print("Nhap thuong hieu") 
            while True:
                brand = input()
                if brand != "":
                    if brand == 'Mercedes' or brand == 'Audi'or brand == 'Vinfast':
                        break
                    else: print("Dai ly khong nhap xe hang tren")
                else: print("Khong duoc bo trong thong tin nay")

            print("Nhap mau xe")
                while True:
                model = input()
                if model != "":
                    if model :
                        break
                    else: print("Dai ly khong nhap xe hang tren")
                else: print("Khong duoc bo trong thong tin nay")
    else:
        print(f'Moi ban nhap lai dung dinh dang')  
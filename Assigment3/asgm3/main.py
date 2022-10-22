from ast import While
from define import Employee, Department, Manager
import json
from writejson import  nhan_vien, load_bp, write_bp, write_nv, write_ql, xoa_bp, xoa_nv,xoa_ql,create_bp
ds_nhanvien = nhan_vien()
ds_bophan = load_bp()
ds_bang_luong = list()


def save():
    danhsach = dict()
    list_nv = []
    list_bp = []
    list_ql = []

    for i in ds_nhanvien:
        nv = dict()
        nv["id"] = i.id
        nv["name"] = i.get_name()
        nv["salary_base"] = i.get_salary_base()
        nv["working_days"] = i.get_working_days()
        nv["department"] = i.get_department()
        nv["working_performance"] = i.get_working_performance()
        nv["bonus"] = i.get_bonus()
        nv["late_coming_days"] = i.get_late_comming_days()
        list_nv.append(nv)

    for i in ds_bophan:
        bp=dict()
        bp["id"]= i.get_id()
        bp["bonus_salary"]=i.get_bonus_salary()
        list_bp.append(bp)

    danhsach["NV"] = list_nv
    danhsach["BOPHAN"] = list_bp
   
    with open('danhsach1.json', 'w') as f:
        json.dump(danhsach, f, indent=4)


while True:
    print('''

    Moi ban chon chuc nang
    1. Hien thi danh sach nhan vien
    2. Hien thi danh sach bo phan
    3. Them nhan vien moi
    4. Them bo phan
    5. Xoa nhan vien theo ID
    6. Xoa bo phan theo ID
    7. Hien thi bang luong
    8. Chinh sua nhan vien    
    0. Thoat   

    ''')
    select = input()
    if str(select).isdigit():
        select = int(select)
        
        #Chuc nang hien thi danh sach nhan vien
        if select == 1:
            print(f"\nDanh sach nhan vien:")
            for i in ds_nhanvien:
                i.show_info()
        
        #Chuc nang hien thi danh sach bo phan
        elif select == 2:
            print(f"\nDanh sach phong ban:")
            for i in ds_bophan:
                i.show_info()
        
        #Chuc nang them nhan vien moi
        elif select == 3:
            print(f"\nThem nhan vien moi:")

            print(f"\nNhap ID:")
            while True:
                ma_id = input()
                if ma_id != '':
                    for i in ds_nhanvien:
                        if i.get_id() == ma_id:
                            print('Ma nhan vien da ton tai, Vui long nhap lai')
                            ma_id = input()
                    break
                else:
                    print('Ban khong duoc bo trong thong tin nay')
            print(f"\nNhap ma bo phan:")
            while True:
                ma_bo_phan = input()
                if ma_bo_phan != '':
                    count3=0
                    for i in ds_bophan:
                        if i.get_id() == ma_bo_phan:
                            count3+=1                                                      
                        else: 
                            count3+=0                        
                    if count3==0:
                        print("Them bo phan moi {}".format(ma_bo_phan))
                        print("Nhap thuong bo phan:")
                        while True:
                            thuong_bo_phan = input()
                            if thuong_bo_phan != '':
                                try:
                                    if int(thuong_bo_phan) > 0:
                                        break
                                except:
                                    print('Nhap dung dinh dang, so nguyen lon hon 0')
                            else:
                                print('Ban khong duoc bo trong thong tin nay')
                        create_bp(ma_bo_phan,thuong_bo_phan,ds_bophan)
                        break
                    else: break             

                else:
                    print('Ban khong duoc bo trong thong tin nay')
            print(f"\nNhap chuc vu:")
            while True:
                chuc_vu = input()
                if chuc_vu != '':
                    if chuc_vu == 'QL' or chuc_vu == 'NV':
                        break
                    else:
                        print("Nhap dung chuc vu: NV hoac QL")
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            print(f"\nNhap ten:")
            while True:
                ten = input()
                if ten != '':
                    break
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            print(f"\nNhap he so luong")
            while True:
                he_so_luong = input()
                if he_so_luong != '':
                    try:
                        if int(he_so_luong) > 0:
                            break
                    except:
                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            print(f"\nNhap so ngay lam viec:")
            while True:
                ngay_lam_viec = input()
                if ngay_lam_viec != '':
                    try:
                        if int(ngay_lam_viec) > 0:
                            break
                    except:
                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            print(f"\nNhap he so hieu qua:")
            while True:
                he_so_hieu_qua = input()
                if he_so_hieu_qua != '':
                    try:
                        if float(he_so_hieu_qua) > 0:
                            break
                    except:
                        print('Nhap dung dinh dang, so thuc lon hon 0')
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            print(f"\nNhap thuong")
            while True:
                thuong = input()
                if thuong != '':
                    try:
                        if int(thuong) > 0:
                            break
                    except:
                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            print(f"\nNhap so ngay di muon")
            while True:
                so_ngay_phat = input()
                if so_ngay_phat != '':
                    try:
                        if int(so_ngay_phat) > 0:
                            break
                    except:
                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                else:
                    print('Ban khong duoc bo trong thong tin nay')

            if chuc_vu == 'NV':
                nv = Employee(ma_id, ten, he_so_luong, ngay_lam_viec,
                              ma_bo_phan, he_so_hieu_qua, thuong, so_ngay_phat)
                write_nv(nv)
            elif chuc_vu == 'QL':
                nv = Manager(ma_id, ten, he_so_luong, ngay_lam_viec,
                             ma_bo_phan, he_so_hieu_qua, thuong, so_ngay_phat)
                write_ql(nv)

            ds_nhanvien.append(nv)
            
            print(f"\nDa them nhan vien moi: {ten}")
        
        #Chuc nang them bo phan moi
        elif select == 4:
            print(f'\nThem bo phan moi')
            
            print(f'Nhap ma bo phan:')
            while True:
                ma_bo_phan = input()
                if ma_bo_phan != '':
                    count3=0
                    for i in ds_bophan:
                        if i.get_id() == ma_bo_phan:
                            count3+=1                                                      
                        else: 
                            count3+=0                        
                    if count3==0:                        
                        print("Nhap thuong bo phan:")
                        while True:
                            thuong_bo_phan = input()
                            if thuong_bo_phan != '':
                                try:
                                    if int(thuong_bo_phan) > 0:
                                        break
                                except:
                                    print('Nhap dung dinh dang, so nguyen lon hon 0')
                            else:
                                print('Ban khong duoc bo trong thong tin nay')
                        create_bp(ma_bo_phan,thuong_bo_phan,ds_bophan)
                        break
                    else: 
                        print("Bo phan da ton tai")
                        break             

                else:
                    print('Ban khong duoc bo trong thong tin nay')
        
        #Chuc nang xoa nhan vien
        elif select == 5:
            print(f"\nNhap id nhan vien can xoa:")
            while True:
                id = input()
                if id != '':
                    break
                else:print("Ban khong duoc bo trong thong tin nay")
            c=0
            for i in ds_nhanvien:
                if id == i.get_id():
                    c+=1
                    if i.chucvu=='NV':
                        xoa_nv(i)
                    else: xoa_ql(i)
                    ds_nhanvien.remove(i)                    
                    print(f'Da xoa nhan vien theo ID: {id}')
                    break                
            if c==0:print("Ma nhan vien khong ton tai")
        
        #Chuc nang xoa bo phan
        elif select == 6:
            print(f"\nNhap id bo phan can xoa:")
            while True:
                id = input()
                if id != '':
                    break
                else:print("Ban khong duoc bo trong thong tin nay")
            c1=0
            c2=0
            for i in ds_bophan:
                if id == i.get_id():
                    c1+=1
                    for j in ds_nhanvien:
                        if id == j.get_ma_bp():
                            c2+=1
            if c1==1 and c2==0:
                xoa_bp(i)
                ds_bophan.remove(i)
                print("Da xoa bo phan theo ID: {}".format(i))
            elif c1==1 and c2>0:
                print('Khong the xoa bo phan da co nhan vien')
            elif c1==0:
                print('Ma bo phan khong ton tai')
        
        #Chuc nang hien danh sach bang luong
        elif select == 7:
            print(f"\nDanh sach bang luong:")
            for i in ds_nhanvien:
                i.show_bang_luong()
        
        #Chuc nang chinh sua nhan vien
        elif select == 8:
            save()
            print(f"\nNhap id nhan vien can chinh sua:")
            while True:
                ma_id = input()
                if ma_id != '':
                    count8=0
                    for i in ds_nhanvien:                        
                        if i.get_id() == ma_id:
                            count8+=1
                            print(f"\nNhap chuc vu:")
                            while True:
                                chuc_vu = input()
                                if chuc_vu != '':
                                    if chuc_vu == 'QL' or chuc_vu == 'NV':                                        
                                        i.set_chucvu(chuc_vu)
                                        break
                                    else:
                                        print("Nhap dung chuc vu: NV hoac QL")
                                else:
                                    break
                            print(f"\nNhap ten:")
                            while True:
                                ten_moi = input()
                                if ten_moi != '':
                                    i.set_name(ten_moi)
                                    break                                    
                                else:                                    
                                    break
                            print(f"\nNhap he so luong")
                            while True:
                                he_so_luong = input()
                                if he_so_luong != '':
                                    try:
                                        if int(he_so_luong) > 0:
                                            i.set_salary_base(int(he_so_luong))
                                            break
                                    except:
                                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                                else:                                    
                                    break
                            print(f"\nNhap so ngay lam viec:")
                            while True:
                                days = input()
                                if days != '':
                                    try:
                                        if int(days) > 0:
                                            i.set_working_days(int(days))
                                            break
                                    except:
                                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                                else:                                    
                                    break
                            print(f"\nNhap he so hieu qua:")
                            while True:
                                rate = input()
                                if rate != '':
                                    try:
                                        if float(rate) > 0:
                                            i.set_working_performance(float(rate))
                                            break
                                    except:
                                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                                else:                                    
                                    break
                            print(f"\nNhap thuong:")
                            while True:
                                bonus = input()
                                if bonus != '':
                                    try:
                                        if int(bonus) > 0:
                                            i.set_bonus(int(bonus))
                                            break
                                    except:
                                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                                else:                                    
                                    break
                            print(f"\nNhap so ngay di muon")
                            while True:
                                late = input()
                                if late != '':
                                    try:
                                        if int(late) > 0:
                                            i.set_late_comming_days(int(late))
                                            break
                                    except:
                                        print('Nhap dung dinh dang, so nguyen lon hon 0')
                                else:                                    
                                    break
                            #Hien thi thong tin nhan vien vua duoc chinh sua
                            i.show_info()

                            
                    if count8==0: print("Ma nhan vien khong ton tai")
                    break
                else:
                    print('Ban khong duoc bo trong thong tin nay')
        #Thoat chuong trinh
        elif select == 0:
            break
    else:
        print(f'Moi ban nhap lai dung dinh dang')




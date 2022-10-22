
import json
import re
from tax import tinh_thue
from late import tien_phat

class Employee:
    # chucvu='NV'
    def __init__(self,id,name,salary_base,working_days,department,working_performance,bonus,late_comming_days) -> None:
        self.id=id
        self.name=name
        self.salary_base=int(salary_base)
        self.working_days=int(working_days)
        self.department=department
        self.working_performance=float(working_performance)
        self.bonus=int(bonus)
        self.late_comming_days=int(late_comming_days)
        self.chucvu='NV'
    
    def luong_chua_thuong(self):
        thu_nhap_chua_thuong = (self.salary_base * self.working_days) * self.working_performance
        return thu_nhap_chua_thuong

    def luong_thuc_nhan(self):
        bp=get_depart()
        tong_thu_nhap = 0
        for i in bp:
            if i["id"]==self.department:
                d_bonus=float(i["bonus_salary"])
        if (self.chucvu == 'NV'):
            tong_thu_nhap = self.luong_chua_thuong() + self.bonus + d_bonus - tien_phat(self.late_comming_days)        
        elif (self.chucvu == 'QL'):
            tong_thu_nhap = self.luong_chua_thuong() + self.bonus + d_bonus*1.1 - tien_phat(self.late_comming_days)
        luong_thuc_nhan=(tong_thu_nhap*0.895)-(tong_thu_nhap*0.895)*float(tinh_thue(tong_thu_nhap/1000000))/100
        a='{:,}'.format(int(luong_thuc_nhan))
        return a
    @property
    def get_id(self):
        return self.id
    def get_ma_bp(self):
        return self.department
    def get_name(self):
        return self.name
    def get_salary_base(self):
        return self.salary_base
    def get_working_days(self):
        return self.working_days
    def get_department(self):
        return self.department
    def get_working_performance(self):
        return self.working_performance
    def get_bonus(self):
        return self.bonus
    def get_late_comming_days(self):
        return self.late_comming_days

    def set_chucvu(self,chucvu):
        self.chucvu=chucvu

    def set_name(self,name):
        self.name=name

    def set_salary_base(self,salary_base):
        self.salary_base=salary_base

    def set_working_days(self,working_days):
        self.working_days=working_days

    def set_working_performance(self,working_performance):
        self.working_performance=working_performance

    def set_bonus(self,bonus):
        self.bonus=bonus

    def set_late_comming_days(self,late_comming_days):
        self.late_comming_days=late_comming_days

    def show_info(self):
        print(f'----')
        print(f'Ma so: {self.id}')
        print(f'Ma bo phan: {self.department}')
        print(f'Chuc vu: {self.chucvu}')
        print(f'Ho va ten: {self.name}')
        print(f'He so luong: {self.salary_base}')
        print(f'So ngay lam viec: {self.working_days}')
        print(f'He so hieu qua: {self.working_performance}')
        print(f'Thuong: {self.bonus}')
        print(f'So ngay di muon: {self.late_comming_days}')
        print(f'----')

    def show_bang_luong(self):
        print(f'----')
        print(f'Ma so: {self.id}')
        print(f'Thu nhap thuc nhan: {self.luong_thuc_nhan()} VND')
        print(f'----')

class Manager(Employee):
    # chucvu='QL'
    def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_comming_days) -> None:
        super().__init__(id, name, salary_base, working_days, department, working_performance, bonus, late_comming_days)
        self.chucvu='QL'
    

    

class Department:
    def __init__(self,id,bonus_salary) -> None:
        self.id=id
        self.bonus_salary=bonus_salary

    def get_id(self):
        return self.id
    def get_bonus_salary(self):
        return self.bonus_salary

    def show_info(self):
        print(f'----')
        print(f'Ma bo phan: {self.id}')
        print(f'Thuong bo phan: {self.bonus_salary}')
        print(f'----')


def get_depart():
    bp=list()
    with open('danhsach.json','r') as f:
        data=json.load(f)
        temp_ds_bp=data['BOPHAN']    
        for i in temp_ds_bp:
            a=json.loads(i)
            bp.append(a)
    return bp

# e=Employee('S2','long le',100000,22,'SALE',1.5,100000,2)

# e.show_info()
# print(e.luong_thuc_nhan())
# e.set_chucvu('QL')
# e.show_info()
# print(e.luong_thuc_nhan())
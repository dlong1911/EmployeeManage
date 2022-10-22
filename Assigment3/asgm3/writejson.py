
import json
from define import Employee,Department,Manager

#Function write file json
def write_json(data, filename='danhsach.json'):    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#Load du lieu nhan vien tu file json
def nhan_vien():
    #Convert JSON string to Python object
    with open('danhsach.json','r') as fp:
        data=json.load(fp)
    temp_ds_nv=data['NV']
    temp_ds_ql=data['QL']   
    lst_nv=list()
    lst_ql=list()    
    
    #lay du lieu object tu list tren va convert to Python Dictionary
    for i in temp_ds_nv:
        tmp=json.loads(i)
        lst_nv.append(tmp)
    for i in temp_ds_ql:
        tmp=json.loads(i)
        lst_ql.append(tmp)  
    #Tao mot list chua cac object dung voi dinh dang trong Class
    ds_nv=list()
    for i in lst_nv:
        tmp=Employee(i["id"],i["name"],i['salary_base'],i['working_days'],i['department'],i['working_performance'],i['bonus'],i['late_comming_days'])
        ds_nv.append(tmp)
    for i in lst_ql:
        tmp=Manager(i["id"],i["name"],i['salary_base'],i['working_days'],i['department'],i['working_performance'],i['bonus'],i['late_comming_days'])
        ds_nv.append(tmp)    
    return ds_nv

#load du lieu bo phan tu file json. Tuong tu nhu Function nhan_vien o tren
def load_bp():
    with open('danhsach.json','r') as fp:
        data=json.load(fp)
    temp_ds_bp=data['BOPHAN']
    lst_bp=list()
    for i in temp_ds_bp:
        tmp=json.loads(i)
        lst_bp.append(tmp)
    ds_bp=list()
    for i in lst_bp:
        tmp=Department(i["id"],i["bonus_salary"])
        ds_bp.append(tmp)
    return ds_bp

#Chuc nang luu du lieu nhan vien xuong file JSON
def write_nv(i):
    with open('danhsach.json') as json_file:
        temp1=[]
        a=json.dumps(i.__dict__)
        data1 = json.load(json_file)
        temp1=data1["NV"]
        temp1.append(a)
        write_json(data1)

#Chuc nang luu du lieuquan ly xuong file JSON
def write_ql(i):
    with open('danhsach.json') as json_file:
        temp2=[]
        a=json.dumps(i.__dict__)
        data2 = json.load(json_file)
        temp1=data2["QL"]
        temp1.append(a)
        write_json(data2)

#Chuc nang luu du lieu bo phan xuong file JSON
def write_bp(i):
    with open('danhsach.json') as json_file:
        temp3=[]
        a=json.dumps(i.__dict__)                    
        data3 = json.load(json_file)
        temp3=data3["BOPHAN"]
        temp3.append(a)
        write_json(data3)

#Chuc nang cap nhat file JSON sau khi xoa bo phan
def xoa_bp(i):
    with open('danhsach.json') as json_file:
        temp4=[]
        a=json.dumps(i.__dict__)                    
        data4 = json.load(json_file)
        temp4=data4["BOPHAN"]
        temp4.remove(a)
        write_json(data4)

#Chuc nang cap nhat file JSON sau khi xoa nhan vien
def xoa_nv(i):
    with open('danhsach.json') as json_file:
        temp5=[]
        a=json.dumps(i.__dict__)                    
        data5 = json.load(json_file)
        temp5=data5["NV"]
        temp5.remove(a)
        write_json(data5)

#Chuc nang cap nhat file JSON sau khi xoa quan ly
def xoa_ql(i):
    with open('danhsach.json') as json_file:
        temp6=[]
        a=json.dumps(i.__dict__)                    
        data6 = json.load(json_file)
        temp6=data6["QL"]
        temp6.remove(a)
        write_json(data6)

def create_bp(id,id_bonus,c):
    new_depart=Department(id,id_bonus)
    c.append(new_depart)
    write_bp(new_depart)

def write_nv2(nv, ql, bp):
    danhsach = dict()
    list_nv = []
    list_bp = []
    list_ql = []
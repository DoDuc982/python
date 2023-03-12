# Nhập và xử lý địa chỉ mạng
diachi = str(input("Nhập vào địa chỉ mạng: "))
mangcon = []
matna = []
end = []
broadcast = []
diachi = diachi.split(".")
y = diachi[3].split("/")
del (diachi[3])
for i in y:
    diachi.append(i)
x = diachi
x.pop
x = str(x[0]) + "." + str(x[1]) + "." + str(
    x[2]) + "." + str(x[3])
mangcon.append(x)
refDiachi = diachi
# Nhập vào số chi nhánh và yêu cầu
cni = int(input("Nhập vào số chi nhánh: "))
dci = int(input("Nhập các địa chỉ liên kết: "))
yeucau = []
for i in range(cni):
    x = int(input("So host cua chi nhanh " + str(i+1) + ": "))
    yeucau.append(x)
for i in range(dci):
    yeucau.append(int(2))
# Sắp xếp theo thứ tự
yeucau.sort(reverse=True)
# Bắt đầu chia mạng
for i in yeucau:
    n = 0
    while (2**n-2) < int(i):
        n = n + 1
    buocnhay = 2**n
    sobitmuon = 32 - int(refDiachi[4]) - n
    matna.append(32 - n)
    if int(refDiachi[3]) + buocnhay < 256:
        refDiachi[3] = str(int(refDiachi[3]) + buocnhay)
    elif int(refDiachi[2]) + buocnhay < 256:
        refDiachi[2] = str(int(refDiachi[2]) + buocnhay)
    elif int(refDiachi[2]) + buocnhay < 256:
        refDiachi[1] = str(int(refDiachi[1]) + buocnhay)
    else:
        refDiachi[0] = str(int(refDiachi[0]) + buocnhay)
    mangcon.append(str(refDiachi[0]) + "." + str(refDiachi[1]) + "." + str(
        refDiachi[2]) + "." + str(refDiachi[3]))
mangcon.pop(-1)
cungcap = []
for i in matna:
    cungcap.append(2**(32 - i) - 2)
j = 0
for i in mangcon:
    i = i.split(".")
    k = str(int(i[-1]) + int(cungcap[j]))
    l = str(int(i[-1]) + int(cungcap[j]) + 1)
    i.pop(-1)
    j = j + 1
    end.append(i[0] + "." + i[1] + "." + i[2] + "." + k)
    broadcast.append(i[0] + "." + i[1] + "." + i[2] + "." + l)
# In ra màn
print("Các yêu cầu về kích thước: ")
print(yeucau)
print("Cung cấp: ")
print(cungcap)
print("Địa chỉ: ")
print(mangcon)
print("Mặt nạ: ")
print(matna)
print("Địa chỉ kết thúc: ")
print(end)
print("Broadcast: ")
print(broadcast)

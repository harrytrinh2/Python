f = open('bai_tap_4.txt')
tuple1 = () #tuple
#abc={} dictionary
listt = [] #list
for line in f:
    # line=line.rstrip().split(',')
    if '#' not in line:
        line = line.rstrip().split()
        # print(line)
        # print(type(line))
        listt.append(tuple(line))
        # print(listt)
        # print(type(listt))
check_name = False
check_year = False
name = input('Nhap Ten : ')
year = input('Nhap Nam Sinh : ')
for i in range(len(listt)):
    if name in listt[i][0]:
        check_name = True
        if year in listt[i][1]:
            check_year = True
            print('Ten:', name, '| Ngay Sinh:', listt[i][1], '| Diem thi:', listt[i][2])
if not check_name:
    print(name, 'Khong Ton Tai')

if not check_year:
    print(name, '|', year, 'khong ton tai!!!')
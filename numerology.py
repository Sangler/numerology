from colorama import Fore

print(f'{"":^10}{"Thần số học"}')
#formating a dictionary
numerology = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "11": 11,
  "22": 22,
  "33": 33
}
while True:
  try:
    D = int(input(f"{Fore.LIGHTBLUE_EX}Nhập ngày sinh của bạn: "))
    M = int(input(f"{Fore.LIGHTGREEN_EX}Nhập tháng sinh của bạn: "))
    Y = int(input(f"{Fore.LIGHTMAGENTA_EX}Nhập năm sinh: (4 số): "))
  except ValueError:
    print(f"{Fore.RED}invalid characters!")

  else:
    a = list(i for i in str(D))
    b = list(i for i in str(M))
    c = list(i for i in str(Y))
    if D in range(1, 32) and M in range(1, 13) and len(c) == 4:
      break

#empty list
alist = []
blist = []
clist = []
ylist = []
#sum number in date
for key in a:
  for k in numerology:
    if key == k:
      alist.append(numerology[key])
      tD = sum(alist)
    elif D == 11 or D == 22:
      tD = D
#sum number in month
for key in b:
  for k in numerology:
    if key == k:
      blist.append(numerology[key])
      tM = sum(blist)
    elif M == 11:
      tM = 11
#sum number in year

for key in c:
  for k in numerology:
      if key == k:
        clist.append(numerology[key])
        tY = sum(clist)
        if tY != numerology.values():
         t= map(int, str(tY)) #sum the letter of number 
         tY= int(sum(t))



total_num = tD + tM + tY

print(f'{"":^10}{tD, tM, tY}')

if total_num == numerology.values():
  print(f'{Fore.LIGHTBLACK_EX}Con số chủ đạo của bạn là: {total_num}')
else:
  total = map(int, str(total_num))
  print(f'{Fore.LIGHTBLACK_EX}Con số chủ đạo của bạn là: {int(sum(total))}')


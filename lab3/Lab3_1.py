year=1900
month=1
day=0
counter=0
monthc=0

while year<2001:
  if month==2:
    if year%100==0 and year%400==0:
      monthc=29
    elif year%4==0:
      monthc=29
    else:
      monthc=28
  elif month==4 or month==6 or month==9 or month==11:
    monthc=30
  else:
    monthc=31
  day = day +7
  if day>monthc:
    day-monthc
    month+1
    if day==1:
      counter+1
      print(counter)
    if month>12:
      month=1
      year+1





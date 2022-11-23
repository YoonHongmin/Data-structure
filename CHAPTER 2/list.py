 
map = {'김연아':'피겨', '류현진':'야구', '쿠드롱':'당구'}
print(map['김연아'])
map['나달'] = '테니스'  # 맵에 항목 추가
print(map)
map.update({'최민영':'여자야구','고진영':'골프'})   # 맵에 여러개 항목 추가
print(map)
if '쿠드롱' not in map :
    print("없음")
else : print("있음")
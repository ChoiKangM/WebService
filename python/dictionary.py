# 1. dict 생성
lunch = {
  '중국집': '02-',
  '양식집': '02-'
}
lunch = dict(중국집='02-') # 딕셔너리 생성

# 2. dict item 추가
lunch['분식집'] = '034-'

# 3. dict value 가져오기
lunch = {
  '한식집': {
    '고갯마루': '02-',
    '순남시래기': '031-'
  }
}
lunch['한식집'] #=> dict
lunch['한식집']['고갯마루'] #=> '02-'

# 추가 : dict 내부 자료형
# key -> string, integer, float, boolean
# value -> 모든 자료형(list, dict)

# 4. dict 반복문 활용
lunch = {
  '한식집': '02-',
  '중국집': '031-',
  '일식집': '034-'
}
# 4-1. 기본
for key in lunch:
  print(key)

# 4-2. key 반복
for key in lunch.keys(): # => {'한식집', ...}
  print(key)

# 4-3. value 반복
for value in lunch.values(): # => {'02-', '031-', ...}
  print(value)

# 4-4. key, value 반족
for key, value in lunch.items(): # => {('한식집', '02-'), ...}
  print(key)
  print(value)

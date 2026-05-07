#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 :" + jumin[:6])
print("뒤 7가리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) :" + jumin[-7:])

#문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n" , index +1)
print(index)

print(python.find("Java"))
print(python.count("n"))

# 사전 선언 (Key는 중복이 안 됨)
cabinet = {3: "유재석", 100: "김태호"}

# 방법 1: [] 사용
print(cabinet[3])    # 유재석
print(cabinet[100])  # 김태호

# 방법 2: get() 사용
print(cabinet.get(3))
# print(cabinet[5])  # 에러 발생
print(cabinet.get(5)) # None 출력
print(cabinet.get(5, "사용 가능"))

# 사전 내에 키가 있는지 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
# 새 손님
cabinet["A-3"] = "김종국" # 기존 키의 값 변경
cabinet["C-20"] = "조세호" # 새로운 키 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

my_set = {1, 2, 3, 3, 3}
print(my_set)

land = 10 # 전역 변수

def checkpoint(soldiers):
    print("[함수 내] 남은 군대 : {0}".format(land))

print("전체 군대 : {0}".format(land))
checkpoint(2)
print("남은 군대 : {0}".format(land))

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # subject를 8칸 확보하고 왼쪽 정렬, score를 4칸 확보하고 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 빈 자리는 빈칸으로 두고, 오른쪽 정렬을 하되, 총 10자리의 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬을 하고, 빈칸으로 _를 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리마다 콤마를 찍어주기, +,- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자릿수까지만 표시 (소수점 3째 자리에서 반올림하여 2째 자리까지)
print("{0:.2f}".format(5/3))

#pickle
import pickle

# 파일 쓰기 (wb: write binary)
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)

# profile 데이터를 profile_file에 저장
pickle.dump(profile, profile_file)
profile_file.close()

# 파일 읽기 (rb: read binary)
profile_file = open("profile.pickle", "rb")

# 파일에 있는 정보를 profile 변수에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

#print 나 input같은 기본적인 함수나 변수들만 쓰다가 튜플이니 리스트니 문자열이니 그런걸 배우니깐 이해하는데 시간이 너무 걸려서 많이 따라쓰지 못하였습니다.
#일단 이거라도 제출하고 나머지 부분 추가 학습 하겠습니다. 죄송합니다.


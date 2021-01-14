import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":24, "취미":["골프", "스키", "화내기"]}
print(profile)
pickle.dump(profile, profile_file) #profile 에 있는 정보 profile_file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
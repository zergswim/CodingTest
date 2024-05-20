# !apt-get update
# !apt-get install espeak
# !pip install pyttsx3

import pyttsx3
import time
# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play
# import io

# import os
# from playsound import playsound

def speak(text):
    """
    텍스트를 음성으로 변환하여 말하기
    """
    print(text)

    engine.say(text)
    engine.runAndWait()
    # tts = gTTS(text, lang='ko')
    # mp3_fp = io.BytesIO()
    # tts.write_to_fp(mp3_fp)
    # mp3_fp.seek(0)

    # # pydub를 사용하여 BytesIO에서 음성 데이터를 로드하고 재생
    # audio = AudioSegment.from_file(mp3_fp, format="mp3")
    # play(audio)    
    
    # tts.save("temp.mp3")
    # playsound("temp.mp3")
    # os.system("start temp.mp3")    

def start_pronouce():
    arr = ["아", "야", "어", "여", "오", "요", "우", "유", "으", "이"]
    for r in range(3):
        for a in arr:
            speak(a)
            time.sleep(1)

def start_exercise_with_voice(exercise_name, sets, reps, rest_between_sets):
    speak(f"{exercise_name} 운동을 시작합니다.")
    
    for i in range(sets):
        speak(f"세트 {i+1}: {reps[i]} 회 시작합니다. 준비하세요!")
        
        for r in range(reps[i], 0, -1):
            speak(f"{r}회")
            time.sleep(3.5)  # 실제 운동을 시뮬레이션하는 대신 대기 (실제 운동 시간을 반영할 때는 조정해야 함)

        if i < sets - 1:
            speak(f"세트 {i+1} 완료! 휴식 시간: {rest_between_sets}초")
            for r in range(rest_between_sets, 0, -1):
                speak(f"{r}초")
                time.sleep(0.5)
        
    speak(f"{exercise_name} 운동이 모두 끝났습니다. 수고하셨습니다!")

engine = pyttsx3.init()

# 예시: 팔굽혀펴기 운동 계획
exercise_name = "팔굽혀펴기"
sets = 3
reps = [45, 40, 35]  # 각 세트별 반복 횟수
rest_between_sets = 60  # 세트 사이 휴식 시간 (초)
# 1: {"월": "팔굽혀펴기 3세트 (30/25/20)", "수": "팔굽혀펴기 3세트 (35/30/25)", "금": "팔굽혀펴기 3세트 (40/35/30)"},
# 2: {"월": "팔굽혀펴기 3세트 (40/35/30)", "수": "팔굽혀펴기 3세트 (45/40/35)", "금": "팔굽혀펴기 3세트 (50/45/40)"},
# 3: {"월": "팔굽혀펴기 3세트 (50/45/40)", "수": "팔굽혀펴기 3세트 (55/50/45)", "금": "팔굽혀펴기 3세트 (60/55/50)"},
# 4: {"월": "팔굽혀펴기 3세트 (60/55/50)", "수": "팔굽혀펴기 3세트 (65/60/55)", "금": "팔굽혀펴기 3세트 (70/65/60)"}

# 발음교정 : https://www.youtube.com/watch?v=nocyVgLTV_w

# start_pronouce()

# 운동음악 : https://www.youtube.com/watch?v=PBLlLcnhDgE

# 운동 시작
start_exercise_with_voice(exercise_name, sets, reps, rest_between_sets)

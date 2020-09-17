# 需要通过手机抓包获取到testId、aId与mob-token
# 反正是自用，要啥自行车（叉腰
import json
import requests

api='https://www.icourse163.org/mob/course/paperDetail/v1'
headers={"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; GM1910 Build/QKQ1.190716.003)"}
data={"mob-token": "",# 这里填入你自己的mob-token
"isExercise": "false",
"withStdAnswerAndAnalyse": "true"}
options=['A','B','C','D']
title=[]

def getjson():
    with requests.post(api,headers=headers,data=data) as res:
        cdata=json.loads(res.text)
        if(cdata['status']['code']!=0):
            print("API Error!")
            return 1
        # 依次解析该次测验中的每一道题目
        for item in cdata['results']['mocPaperDto']['objectiveQList']:
            problemdata={}
            problemdata['title'] = item['plainTextTitle']
            char = 0
            problemdata['choices']=[]
            # 依次解析该题目中的所有正确选项
            for option in item['optionDtos']:
                if(option['answer'] == 1):
                    answer = options[char] + ':' + option['content'] + '\n'
                    problemdata['choices'].append(answer)
                char += 1
            title.append(problemdata)
        print("Parse JSON complete!")

def printjson():
    index = 1
    for item in title:
        print(str(index)+"."+item['title'])
        print('Answer：')
        for choice in item['choices']:
            print(choice)
        index+=1

def main():
    testid=int(input("Input testid to get the problemset data:"))
    aid=int(input("Input aid to get the problemset data:"))
    data['testId']=testid
    data['aId']=aid
    if(getjson()!=0):
        printjson()
        return 0
    else:
        print("Can't get problemset,Quiting...")
        return 1

main()
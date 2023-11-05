import random

qa_map = {
    "通过急弯": "远近",
    "通过坡道": "远近",
    "通过拱桥": "远近",
    "通过人行横道": "远近",
    "夜间超越前方车辆": "远近",
    "夜间通过没有交通信号灯的路口": "远近",
    "夜间通过有交通信号灯的路口": "近",
    "夜间同方向近距离跟车": "近",
    "夜间与机动车/非机动车会车": "近",
    "夜间在照明良好的道路行驶": "近",
    "夜间通过路口": "近",
    "夜间直行通过照明不良的路口": "远",
    "路边临时停车": "示廓灯",
}

question_list = list(qa_map.keys())

def get_index(i, max_value):
    temp_list = []
    while len(temp_list) < i:
        index = random.randint(0, max_value - 1)
        if index not in temp_list:
            temp_list.append(index)
    return temp_list

def main():
    index = get_index(5, len(question_list)) 
    for integer in index:
        qs = question_list[integer]
        print(qs)
        print("1.近光灯       2.远光灯       3.远近交替      4.示廓灯")
        as_input = int(input())
        s = qa_map[qs]
        if (as_input == 1 and s == "近") or (as_input == 2 and s == "远") or (as_input == 3 and s == "远近") or (as_input == 4 and s == "示廓灯"):
            print("ok!\n")
        else:
            print("false! quit")
            print("answer is " + s)
            break

if __name__ == "__main__":
    main()
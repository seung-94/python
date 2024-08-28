def main():
    i = int()
    while i < 10:
        print(f"{i} 번째 실행 중...")

    li = [1,2,3,4,5,6,7,2,4,3,2]
    while 2 in li:
        print("2 지우는중")
        li.remove(2)
    print(li)

    string = "this is a python class in a Deajeon city"
    while "a" in string:
        print("a 지우는중")


if __name__ == "__main__":
    main()
def main():
    i = 2
    j = 1

    for i in range(18):
       print(f"{i+2}단")
       for j in range(9):
          print(f"{i+2} X {j+1} = {(i+2) * (j+1)}")

if __name__ == "__main__":
    main()
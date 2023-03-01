def cToFConvert():
    while True:
      cTemp = input("please enter your temperture:")
      if cTemp:
          cTemp = float(cTemp)
          fTemp = round(9*cTemp/5 + 32, 1)
          print(f"{cTemp}C is converted to{fTemp}F")
          break
      else:
          print("You need to enter temperature")
          continue

def main():
    cToFConvert()
if __name__ == "__main__":
        main()






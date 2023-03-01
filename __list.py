presidents = ["Cong", "hoa", "xa", "hoi", "chu", "nghia", "VN"]

for index, president in enumerate (presidents):
     print(f"{index}{president}")

# presidents = ["Cong", "hoa", "xa", "hoi", "chu", "nghia", "VN"]

# for index, president in enumerate(presidents):
#     print(f"{index}{president}")

animal = ["cho", "meo", "ga", "lon"]
print(animal.insert(2,"ngan"))
print(animal)

transitions = [10, 20, 44, 50, 50]
TAX_RATE = 0.8
SERVICE_CHARGE = 0.7

def get_price(bill):
     return bill*(1+TAX_RATE+SERVICE_CHARGE)


buy_price = [get_price(transition) for transition in transitions]
print(buy_price)
     

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for row in range(len(matrix)):
     for col in range(len(matrix)):
      print(f"-----------{matrix[row]}------")
      print(matrix[col])
      


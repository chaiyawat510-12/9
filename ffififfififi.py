def check_shirt_size(chest_size):
  if chest_size <= 34:
    return "XS"
  elif chest_size <= 36:
    return "S"
  elif chest_size <= 38:
    return "M"
  elif chest_size <= 40:
    return "L"
  else:
    return "XL"


if __name__ == "__main__":

  chest_size = float(input("ป้อนขนาดหน้าอก: "))


  shirt_size = check_shirt_size(chest_size)


  print("ขนาดเสื้อโปโลของคุณคือ:", shirt_size)

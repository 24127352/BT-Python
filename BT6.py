text = "Hôm nay trời đẹp."
with open("ouput.txt", "wb") as file:
    file.write(text.encode("utf-8"))
frame_count = 45
duration = 1

stride = duration / frame_count
print_word = ""
for i in range(frame_count):
    print_word += "{:.4f}".format(i * stride) + " "
print(print_word)
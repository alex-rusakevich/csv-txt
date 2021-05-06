import sys, re

if __name__ == "__main__":
    file_data = open(sys.argv[1], "r", encoding="utf8").read().split("\n")

    print("%i songs found" % (len(file_data) - 2))

    result = []

    count = 1
    for song in file_data[1 : len(file_data) - 1]:
        song_data = song.split('","')
        song_string = song_data[1] + " - " + song_data[3] + "\n"
        print(" " + str(count) + ") " + song_string)
        result.append(song_string)
        count += 1

    print("%i songs processed. Writing..." % (len(result)))
    open(sys.argv[1] + ".txt", "w", encoding="utf8").writelines(result)

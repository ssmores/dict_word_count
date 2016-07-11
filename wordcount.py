# put your code here.

# small_text_file = open('test.txt')

# word_count = {}

# for line in small_text_file:
#     line = line.rstrip()
#     words = line.split(" ")

#     word_count_value = 0

#     for word in words:
#         current_word_count = word_count.get(word, 0)
#         word_count[word] = current_word_count + 1

# small_text_file.close()

# for word, word_count_value in word_count.items():
#     print "%s: %d" % (word, word_count_value)



def counting_words(filename):
    small_text_file = open(filename)

    word_count = {}

    for line in small_text_file:
        line = line.rstrip()
        words = line.split(" ")

        word_count_value = 0

        for word in words:
            current_word_count = word_count.get(word, 0)
            word_count[word] = current_word_count + 1

    small_text_file.close()

    for word, word_count_value in word_count.iteritems():
        return "%s: %d" % (word, word_count_value)
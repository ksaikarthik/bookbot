
def sort_on(dict):
    return dict["num"]

def make_report(word_count, char_dict):
    report = f"--- Begin report of books/frankenstein.txt --- \n{word_count} words found in the document\n"
    
    for item in char_dict:
        report += f"The \'{item['char']}\' character was found {item['num']} times\n"
    report += "--- End report ---"
    return report

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    lowered_string = file_contents.lower()
    char_count = {}
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_dict = []
    for char in char_count:
        # check if char is a letter
        if not char.isalpha():
            continue
        char_dict.append({"char": char, "num": char_count[char]})
    char_dict.sort(key=sort_on, reverse=True)
    report = make_report(word_count, char_dict)
    print(report)
    return

if __name__ == "__main__":
    main()
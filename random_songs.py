import random
import os
import time
import re
import panel as pn

# press plus for a second.third/etc line
# easy/hard levels - if it is repetitive, if it contains title,
# point system guessing album vs song vs next lyric
# timer?

pn.extension()

albums = ["TaylorSwift","Fearless_TaylorsVersion_","SpeakNow_TaylorsVersion_","Red_TaylorsVersion_",
          "1989_TaylorsVersion_","Reputation", "Lover", "Folklore", "Evermore", "Midnights",
          "THETORTUREDPOETSDEPARTMENT_THEANTHOLOGY"]

lyric_to_guess = ""
correct_song_to_guess = ""

def get_random_song_dir():
    random_album_num = random.randint(1, len(albums)) - 1
    album = albums[random_album_num]
    dir = "Albums1/"+album
    num_songs = len(os.listdir(dir))
    rand_song_num = random.randint(1, num_songs) - 1
    song = os.listdir(dir)[rand_song_num]
    return dir+"/"+song

def get_random_lyric(dir):
    with open(dir, errors="ignore") as fp:
        num_lines = get_num_lines(dir)
        rand_line = random.randint(1,num_lines)
        for i, line in enumerate(fp):
            if i == rand_line:
                if line.startswith("["):
                    return ""
                elif line.strip() == "":
                    return ""
                else:
                    return line
    return ""

def get_num_lines(dir):
    with open(dir,  errors="ignore") as fp:
        for num_lines, line in enumerate(fp):
            pass
    return num_lines

def get_album(path):
    dir = os.path.dirname(path)
    return dir.replace("Albums1/", "")

def get_title(path):
    file_title = os.path.splitext(os.path.basename(path))[0]
    file_title_simple = simplify_title(file_title)
    with open(path, 'r',  errors="ignore") as file:
        first_line = file.readline()
    final_title = find_unsimplified_match(file_title_simple, first_line)
    return final_title

def simplify_title(title):
    # remove punctuation, and spaces and all upper case
    cleaned = re.sub(r'[^\w]', '', title).lower()
    cleaned = cleaned.replace("_", "")
    # remove taylors version
    if "taylorsversion" in cleaned:
        cleaned = cleaned.replace("taylorsversion","")
    # remove from the vault
    if "fromthevault" in cleaned:
        cleaned = cleaned.replace("fromthevault", "")
    return cleaned

def find_unsimplified_match(simplified_string, long_text):
    # Try every possible substring of long_text
    for start in range(len(long_text)):
        for end in range(start + 1, len(long_text) + 1):
            candidate = long_text[start:end]
            if simplify_title(candidate) == simplified_string and candidate[0].lower() == simplified_string[0].lower():
                return candidate
    return None

def is_correct(guess, correct):
    guess = simplify_title(guess)
    correct = simplify_title(correct)
    if guess == correct:
        return True
    return False

def get_start_lyric():
    song_dir = get_random_song_dir()
    line = ""
    while line == "":
        line = get_random_lyric(song_dir)
    global lyric_to_guess
    lyric_to_guess = line
    global correct_song_to_guess
    correct_song_to_guess = get_title(song_dir)
    return line





# print(line)
lyric = pn.widgets.StaticText(name='Lyric', value=get_start_lyric())
text_input = pn.widgets.TextInput(name='Text Input', placeholder='Guess here...')
submit_button = pn.widgets.Button(name='Submit')
output_text = pn.pane.Markdown()

def guess():
    guess = text_input.value
    res = is_correct(guess, correct_song_to_guess)
    if res:
        output_text.object = "Correct!"
    else:
        output_text.object = "Wrong!"

submit_button.on_click(guess)

column = pn.Column('# Column', lyric, text_input, submit_button, styles=dict(background='WhiteSmoke'))

column.servable(target='simple_app')
# user_input = input("Guess the song: ")
# # todo- html input?
# while(is_correct(user_input, correct_song) == False):
#     new_line = ""
#     while new_line == "" and (new_line in line) == False:
#         new_line = get_random_lyric(song_dir)
#     line = line +"\n"+ new_line
#     # print(song_dir)
#     print("Wrong! Here's another line: \n")
#     print(line)
#     user_input = input("Guess again: ")
#
# print(f"Correct! It's {correct_song} from {get_album(song_dir)}")
#

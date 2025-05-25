import os, os.path
import re

albums = ["TaylorSwift","Fearless_TaylorsVersion_","SpeakNow_TaylorsVersion_","Red_TaylorsVersion_",
          "1989_TaylorsVersion_","Reputation", "Lover", "Folklore", "Evermore", "Midnights",
          "THETORTUREDPOETSDEPARTMENT_THEANTHOLOGY"]

# clean first line of lyrics
# for album in albums:
#     for song in os.listdir("data/Albums/"+album):
#         dir = "data/Albums/"+album+"/"+song
#         print(dir)
#         with open(dir, 'r',  errors="ignore") as file:
#             lines = file.readlines()
#             # lines[0] = album + "/" + song + '\n'
#             # make the first line the title with spaces
#             with open(dir, 'w') as file:
#                 file.writelines(lines)

path = "Albums1/"

# clean last line of lyrics:
# for album in albums:
#     for song in os.listdir(path + album):
#         dir = path + album + "/" + song
#         print(dir)
#         with open(dir, 'r', errors="ignore") as file:
#             lines = file.readlines()
#
#         if lines:
#             # Clean the last line
#             lines[-1] = re.sub(r'\d{1,3}Embed\s*$', '', lines[-1])
#
#             # Write back the modified lines
#             with open(dir, 'w', encoding='utf-8') as f:
#                 f.writelines(lines)

# clean incorrect characters:
for album in albums:
    for song in os.listdir(path + album):
        dir = path+album+"/"+song
        print(dir)
        with open(dir, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Replace all 'Ðµ' with 'e':
        # fixed_content = content.replace("Ðµ", "e")
        # 'â€”' with '':
        # fixed_content = fixed_content.replace("â€”", "")
        # Ã¢â‚¬â„¢ to '''
        # fixed_content = fixed_content.replace("Ã¢â‚¬â„¢", "'")
        fixed_content = content.replace("See Taylor Swift LiveGet tickets as low as $60You might also like", "")


        # Save the fixed file
        with open(dir, "w", encoding="utf-8") as f:
            f.write(fixed_content)


# //test with example text file:
# dir = "ex.txt"
# # Read with errors ignored, fix weird characters
# with open(dir, "r", encoding="utf-8", errors="ignore") as f:
#     content = f.read()
#
# # Replace all 'Ðµ' with 'e'
# fixed_content = content.replace("Ðµ", "e")
#
# # Save the fixed file
# with open(dir, "w", encoding="utf-8") as f:
#     f.write(fixed_content)


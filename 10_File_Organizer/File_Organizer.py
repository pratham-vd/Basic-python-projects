files = [
    "photo.jpg",
    "song.mp3",
    "document.pdf",
    "notes.txt",
    "image.png",
    "resume.docx"
]

organized = {}   

for file in files:
    ext = file.split(".")[-1]  

    folder = ext + "_files"   

    if folder not in organized:
        organized[folder] = [] 

    organized[folder].append(file)  

# Print organized result
for folder, file_list in organized.items():
    print(folder, ":", file_list)

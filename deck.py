import os

files = [
    f for f in os.listdir("./docs") 
    if f.endswith(".html") 
    and f[0] in ["a", "b", "c", "d", "e", "f", "g"]
]

for file in files:
    os.system(f'decktape automatic docs\{file}.html docs\pdfs\{file}.pdf')

os.system("git add .")
os.system("git commit -m 'message'")
os.system("git push origin main")
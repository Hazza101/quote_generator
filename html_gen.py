import os
#filenames = os.listdir('books')
filenames = [filename for filename in os.listdir('books') if os.path.isfile(os.path.join('books', filename))]

for char in 'abcdefghijklmnopqrstuvwxyz':
    #books_found = []
    #print(char)
    '''
    found = True
    print(f"<div class=\"{char}-books\">")
    print(f"\t<h1>{char.upper()}</h1>")
    print("\t<ul>")
    for filename in filenames:
        if filename[0].lower() == char:
            #books_found.append(filename)
            print(f"\t\t<li><a href=\"books\\{filename}\">{filename[:-5]}</a></li>")
            found = False
    if found:
        print(f"<li>No books for {char}</li>")

    print("\t</ul>")
    print("</div>")
    '''
    found = True
    for filename in filenames:
        if filename[0].lower() == char:
            #print(filename)
            found = False
    if found:
        #print(f"No books for {char}")
        print(f'''<button class="button-off">{char.upper()}</button>''')
    else:
        print(f'''<button class="button-on" onclick="letterFunction('{char}-books')">{char.upper()}</button>''')        
        

    
   
    #print(f".{char}-books{{ display:none; }}")

    

    
        

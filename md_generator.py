info_dic = {}

with open("quotes.txt", 'r', encoding="utf-8") as f:

    main_title = None
    main_theme = None
    main_pos = None
    for line in f.readlines():
        #print(line.strip())
        if line[0] == ';':
            list_components = line.split(',')
            title = list_components[0][1:]
            main_title = title
            info_dic[main_title] = {} 
            


            #input()
            #print(line)
            
            
            
        elif line[0] == '!':
           
            
            theme = line[1:].strip()
            main_theme = theme
            info_dic[main_title][theme] = {}
            
        elif line[0] == '~':
            
            location = line[1:].strip()
            main_pos = location
            info_dic[main_title][main_theme][location] = []
            
            
            
            
            ###_ _
        elif line[0] == '"':
            #quote
            #>
            quote = line.strip()
            info_dic[main_title][main_theme][main_pos].append([quote, None])

        elif line[0] == '@':
            explanation = line.strip()[1:]
            #print(line)
            #input()
            for index, element in enumerate(info_dic[main_title][main_theme][main_pos]):
                if element[1] == None:
                    info_dic[main_title][main_theme][main_pos][index][1] = explanation
                    #print(info_dic[main_title][main_theme][main_pos][index][1])
                    break
                    
            

template_1 = None
template_2 = None
template_3 = None

with open("template_1.txt") as f:
    template_1 = "".join(f.readlines())
with open("template_2.txt") as f:
    template_2 = "".join(f.readlines())
with open("template_3.txt") as f:
    template_3 = "".join(f.readlines())



#print(template_2)

for book_key, book_value in info_dic.items():
    page = template_1
    page += book_key
    page += template_2
    page += f'''
<section>
        <div class="book-title">
            <h1>{book_key}</h1>
            <div class="copy-wrapper" onclick="copyToClipBoard()">
                <img src="media/copy_icon.png" id="testImage" width="30" height="30" alt="copy quotes button"/>
            </div>
        </div>
            <div class="accordion">


'''
    #print(book_key)
    for theme_key, theme_value in book_value.items():
        page += f'''
<div class="accordion-item">
                <div class="accordion-header">
                    <div class="accordion-title" id="testing">
                        {theme_key}
                    </div>
                    <div class="accordion-arrow">
                        <button>&#8711;</button>
                    </div>

                </div>
                
                <div class="accordion-content">

'''
        #print(f"\t{theme_key}")
        new_list = []
        for key, val in theme_value.items():
            for quote in val:
                new_list.append(quote)
        

        for quote_explanation in new_list:
            quote = quote_explanation[0]
            explain = quote_explanation[1]
            page += f'''
<div class="quote-section">
                        <p class="quote"><em>{quote}</em></p>
                        <button class="quote-explain"><b>?</b></button>
                        <div class="popup-box">{explain}</div>
                    </div>
'''

        page += f'''

</div>
</div>
'''
    page += f'''
</div>
</section>
'''
    page += template_3
    #print(page)
    #input()
    with open(f"books\\{book_key}.html", 'w', encoding="utf-8") as f:
        f.write(page)

    print(f"HTML file: books\\{book_key}.html created.")

           

 

'''
# The Empress
### _Exam Boards_
- Edexcel (Post-1914 British Play or Novel)
## **Colonialism and Resistance**
### _Beginning_
>"Britain's view of India is as twisted as a fun-house mirror. It only sees what it wants to see." (Act 1, Scene 1)
### _Middle_
### _End_


'''

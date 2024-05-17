from . import *
from .run_python import run_python
from .html import *
lookForStringEnd = False
moveLine = 0
fullString = ""

def stringLook(line):
    global lookForStringEnd, moveLine, fullString
    fullString = ""
    moveLine = 0
    string = line[0]
    if string[0] == '"' or string[0] == "'":
        lookForStringEnd = True
    
    if lookForStringEnd:
        while lookForStringEnd:
            string = line[moveLine]
            if string[len(string) - 1] == '"' or string[len(string) - 1] == "'":
                lookForStringEnd = False
                fullString = fullString + string
            else:
                moveLine += 1
                fullString = fullString + string + " "

    if '"' in fullString: # this must go first to see if the double quotes are there. This way a single quote can be made possible to be put inside if made purpose
        fullString = fullString.replace('"', "")
    elif "'" in fullString:
        fullString = fullString.replace("'", "")
                


def execute_code(func_name, line, variables, index, lines, functions, python_funcs_and_vars, filename):
    global moveLine, fullString
    # everything needs two options: word command and symbol command, and alt emoji
    try:
        if func_name == 'put': # python print
            text = get_variable(line[0], variables, line)

            say(text)
         # or
        elif func_name == '\>':
            text = get_variable(line[0], variables, line)

            say(text)
        elif func_name == '🗨': # python print
            text = get_variable(line[0], variables, line)

            say(text)



        elif func_name == '*': # comment
            stringLook(line)
            ignore = fullString
            # don't call error on this because it is a comment
        # or
        elif func_name == 'note':
            stringLook(line)
            ignore = fullString
            # don't call error on this because it is a comment
        elif func_name == '💭':
            stringLook(line)
            ignore = fullString
            # don't call error on this because it is a comment




        elif func_name == 'log':
            text = get_variable(line[0], variables, line)

            console(text)
        # or 
        elif func_name == '/>':
            text = get_variable(line[0], variables, line)

            console(text)
        elif func_name == '✍':
            text = get_variable(line[0], variables, line)

            console(text)
            


        elif func_name == 'bg':
            text = get_variable(line[0], variables, line)

            bgColor(text)
        # or
        elif func_name == '<&>':
            text = get_variable(line[0], variables, line)

            bgColor(text)
        elif func_name == '🌐':
            text = get_variable(line[0], variables, line)

            bgColor(text)


        elif func_name == 'back':
            stringLook(line)
            link = line[moveLine + 2]
            back.title(fullString)
            back.link(link)
        # or
        elif func_name == '<-':
            stringLook(line)
            link = line[moveLine + 2]
            back.title(fullString)
            back.link(link)
            
        elif func_name == '🔙':
            stringLook(line)
            link = line[moveLine + 2]
            back.title(fullString)
            back.link(link)
            

        elif func_name == 'run.':
            loadToHtml(filename) # the run command is what generates and opens the html file
        elif func_name == '...':
            loadToHtml(filename)
        elif func_name == '▶️':
            loadToHtml(filename)
        
        elif func_name == 'display.':
            run(filename) # display end result open file
        elif func_name == '<->':
            run(filename)
        elif func_name == '👀':
            run(filename)

        elif func_name == '^img':
            stringLook(line)

            text = get_variable(line[0], variables, line)

            tabIcon(line[0], line[2])
        elif func_name == '()^':
            stringLook(line)

            text = get_variable(line[0], variables, line)

            tabIcon(line[0], line[2])
        elif func_name == '🖼️':
            stringLook(line)

            text = get_variable(line[0], variables, line)

            tabIcon(line[0], line[2])
            


        elif func_name == 'subtitle':
            stringLook(line)

            subtitle(fullString)
        elif func_name == '##': # must be before title because of icon/symbol
            stringLook(line)

            subtitle(fullString)
        elif func_name == 'ℹ️':
            stringLook(line)

            subtitle(fullString)


        elif func_name == 'title':
            stringLook(line)

            title(fullString)
        elif func_name == '#':
            stringLook(line)

            title(fullString)
        elif func_name == '🎩':
            stringLook(line)

            title(fullString)
            

            




        elif func_name == 'question': # main info/question
            stringLook(line)

            mainInfoMessage(fullString)
        elif func_name == '?': # main info/question
            stringLook(line)

            mainInfoMessage(fullString)
        elif func_name == '❓': # main info/question
            stringLook(line)

            mainInfoMessage(fullString)


        elif func_name == 'button': # option button
            stringLook(line)
            try:
                # button "text" @File "file_name" @Folder "folder_name"
                button(fullString, line[moveLine + 1], line[moveLine + 2], line[moveLine + 3], line[moveLine + 4])
            except:
                # button "text" @File "file_name"
                buttonWithoutFolder(fullString, line[moveLine + 1], line[moveLine + 2])
        elif func_name == '!': # option button
            stringLook(line)
            # button "text" @File "file_name" @Folder "folder_name"
            button(fullString, line[moveLine + 1], line[moveLine + 2], line[moveLine + 3], line[moveLine + 4])
        elif func_name == '⭕': # option button
            stringLook(line)
            # button "text" @File "file_name" @Folder "folder_name"
            button(fullString, line[moveLine + 1], line[moveLine + 2], line[moveLine + 3], line[moveLine + 4])
            
    




        elif func_name == 'story':
            stringLook(line)

            storyText(fullString)
        elif func_name == '\\': # really this: \
            stringLook(line)

            storyText(fullString)
        elif func_name == '📖': # really this: \
            stringLook(line)

            storyText(fullString)



        elif func_name == '[]':
            box()
        elif func_name == 'box.':
            box()
        elif func_name == '📦':
            box()
            


        elif func_name == 'playsound':
            soundPlay();







        # end symbols together 
        elif func_name == '<...>':
            loadToHtml(filename)
            run(filename)
            
        elif func_name == '[...]':
            box()
            loadToHtml(filename)

        elif func_name == '[<...>]':
            box()
            loadToHtml(filename)
            run(filename)
            




    except:
        pass
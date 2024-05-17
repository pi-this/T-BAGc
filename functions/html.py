import webbrowser 
import os
import pickle

filename = ''
htmlCodeTop = ""
htmlCodeBottom = ""
innerHtml = ""
totalHtml = htmlCodeTop + innerHtml + htmlCodeBottom
buttons = ""
titleInfo = ""
subtitleInfo = ""
mainInfo = ""
story = ""
veryTop = ""
htmlButtonClicked = ""
firstFile = ""


def loadToHtml(filename):
    global f

    f = open(filename+'.html', 'w')
    htmlLayout()
    f.write(totalHtml)
  
    # close the file 
    f.close() 

def run(filename):
    global firstFile
    webbrowser.open(filename+'.html')
    firstFile =  str(os.path.abspath(filename))
    serialized = pickle.dumps(firstFile)
    with open('firstFile.pkl', 'wb') as file:
        pickle.dump(firstFile, file)
def htmlLayout():
    global htmlCodeTop, htmlCodeBottom, innerHtml, totalHtml, veryTop, htmlButtonClicked
    totalHtml = veryTop + htmlButtonClicked +htmlCodeTop + innerHtml + htmlCodeBottom
def console(text):
    global innerHtml

    innerHtml = """<script>
console.log("{0}");
</script>""".format(text) 

def tabIcon(img, imageType):
    global veryTop
    veryTop = """<link rel="icon" type="img/"""+imageType+"""" href="""+str(img)+"""/>"""

def bgColor(color):
    global htmlCodeTop, htmlCodeBottom

    if color == "blue":
        coloradd = 'style="background-color:blue;"'
    elif color == "red":
        coloradd = 'style="background-color:red;"'
    elif color == "green":
        coloradd = 'style="background-color:green;"'
    elif color == "yellow":
        coloradd = 'style="background-color:yellow;"'
    elif color == "white":
        coloradd = 'style="background-color:white;"'
    elif color == "orange":
        coloradd = 'style="background-color:orange;"'
    elif color == "black":
        coloradd = 'style="background-color:black;"'
    else:
        coloradd = '''style="background-image: url('{0}');"'''.format(color) # here color is an image

    # generate html to write to file
    htmlCodeTop = htmlCodeTop + """<html {0}>""".format(coloradd)
    htmlCodeBottom = "</html>"

def box():
    global htmlCodeTop, innerHtml, buttons, titleInfo, subtitleInfo, mainInfo
    htmlCodeTop = htmlCodeTop + """

<style>
/* Styling for the buttons */
        .button {
            background-color: forestgreen;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
        }
</style>

"""

    innerHtml = innerHtml + """
<center>
        <div class="box">
            <div class="title">"""+titleInfo+"""</div>
            <div class="secondary-text">"""+subtitleInfo+"""</div>
            <br />
            """+mainInfo+"""
            <br />
            """+buttons+"""
            <br />
            <br />
        </div>
        """+story+"""
    </center>



    <style>
        /* Styling for the box */
        .box {
            background-color: lightslategray;
            border: 5px solid #265985;
            padding: 20px;
            width: 300px;
            margin: 0 auto;
        }

        .quit {
            background-color: darkred;
        }

        /* Styling for the title and secondary text */
        .title {
            font-size: 25px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .secondary-text {
            font-size: 15px;
            color: black;
        }

        .main-text {
            font-size: 18px;
            color: black;
            background-color: rgb(135, 136, 300);
            border: 2px solid rgb(37, 46, 6);
        }
        .longStory {
            font-size: 20px;
            color: black;
            background-color: lightslategray;
            border: 5px solid #265985;
            padding: 20px;
            width: 300px;
            margin: 0 auto;
        }
    </style>

    <script>
    
</script>
</head>
<body>
    

"""



def button(option, atFile, fileName, atFolder, folderName):
    global letterFile
    global buttons, htmlButtonClicked, innerHtml
    fileName = fileName.replace('"',"")
    folderName = folderName.replace('"',"")
    if atFile == "@File":
        os.system("T-BAGc "+folderName+"\\"+fileName+".bag") # create the files
        # then when the button is pressed then in javascript navigate to it

        innerHtml = innerHtml + """



<script>
function """+folderName.replace('"',"")+"""() {
    location.replace('"""+folderName.replace('"',"")+"/"+fileName.replace('"',"")+""".html')
}
</script>
        

"""

        buttons = buttons + """





    <button onclick='"""+folderName+"""()' class="button">"""+option.replace('"',"")+"""</button>&nbsp




"""
    else:
        # visual error (need @)
        pass
    

def buttonWithoutFolder(option, atFile, fileName):
    global letterFile
    global buttons, htmlButtonClicked, innerHtml
    fileName = fileName.replace('"',"")
    if atFile == "@File":
        os.system("T-BAG "+fileName+".bag") # create the files
        # then when the button is pressed then in javascript navigate to it

        innerHtml = innerHtml + """



<script>
function """+fileName.replace('"',"")+"""() {
    location.replace('"""+fileName.replace('"',"")+""".html')
}
</script>
        

"""

        buttons = buttons + """





    <button onclick='"""+fileName+"""()' class="button">"""+option.replace('"',"")+"""</button>&nbsp




"""
    else:
        # visual error (need @)
        pass

class back:
    def title(title):
        global backtitle
        backtitle = title
    def link(url):
        global htmlCodeTop
        global backtitle, firstFile
        if url == "startover":
            with open('firstFile.pkl', 'rb') as file:
                firstFile = pickle.load(file)
            url = firstFile
        
            
            
        htmlCodeTop = htmlCodeTop + """
<style>
a:link, a:visited {
  background-color: blue;
  color: white;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: black;
}
</style> 
<a href='""" + url.replace('"',"") + """.html' >"""+backtitle+"""</a>
"""
        

def title(title):
    global titleInfo, htmlCodeTop
    titleInfo = title
    htmlCodeTop = htmlCodeTop + """
<title>"""+title+"""</title>
"""


def subtitle(subtitle):
    global subtitleInfo
    subtitleInfo = subtitle
    

def mainInfoMessage(text):
    global mainInfo
    mainInfo = """
<div class="main-text">"""+text+"""</div>"""
    

def storyText(text):
    global story
    story = """
<div class="longStory">"""+text+"""</div>
"""
    
    
    
    
def soundPlay(): # use audio in loop for background music and when button clicked as not in loop
    innerHtml = innerHtml + """


<!DOCTYPE html>
<html>
<body>

<audio id="myAudio">
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<p>Click the buttons to play or pause the audio.</p>

<button onclick="playAudio()" type="button">Play Audio</button>
<button onclick="pauseAudio()" type="button">Pause Audio</button> 

<script>
var x = document.getElementById("myAudio"); 

function playAudio() { 
  x.play(); 
} 

function pauseAudio() { 
  x.pause(); 
} 
</script>

</body>
</html>
"""
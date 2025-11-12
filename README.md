  <p align="center">
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/T-BAGc.png" alt="Project logo"></a>
</p>


<h3 align="center">T-BAGc</h3>

<div align="center">

</div>

---

<p align="center"> A Python-interpreted simple domain-specific language (DSL) that makes writing text-based adventure games so much easier. 
T-BAGc stands for Text-Based Adventure Game Creator.
    <br> 
</p>

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Documentation](#documentation)

## About <a name = "about"></a>

T-BAGc is a simple domain-specific language, it has one purpose, to create text-based adventure games. This is what makes it unique. T-BAGc makes text-based adventure game creation so much easier and quicker.
Since there is only one simple purpose in T-BAGc, each file can many times be written in under 20 lines of code. T-BAGc is made so that the files can be organized into different bags (or views). When a question is answered it goes to the next file.
In Python, making text-based adventure games can take forever, and it gets annoying to put another if inside an if and so on. T-BAGc fixes all the issues that all the other programming languages have with making text-based adventure games. Use T-BAGc to create a new game, a game that can be made in less time, with better organization, and the same enjoyment of creating and playing a text-based adventure game. So what are you waiting for? [Get started](#getting_started) now and install T-BAGc so you can create your
own T-BAG.


## Getting Started <a name = "getting_started"></a>

By following these instructions you will have T-BAGc running on your computer.

### Installing

To install T-BAGc follow the instructions below.
The following instructions have currently only been tested for Windows.

##### Step 1
Download zip


First, download the zip file for the project.
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/installStep1.png" alt="Project logo"></a>
  <br />
  Navigate to Code -> Download Zip
</p>


##### Step 2
Extract zip


Extract the zip file.
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/extract.png" alt="Project logo"></a>
  <br />
  Right-click on "T-BAGc-main.zip" and click "Extract All..."
</p>



##### Step 3
Add to environment variables


In Windows, search "edit the system environment variables
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/var1.png" alt="Project logo"></a>
  <br />

  From the system properties click on "Environment Variables..."
</p>

Once the environment variables window is open, do the following.
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/var2.png" alt="Project logo"></a>
  <br />
  Under "System variables" search for the "Path" variable, highlight it, and click the "Edit..." button.
</p>

Add a new environment variable.
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/var3.png" alt="Project logo"></a>
  <br />
  Click new to add a variable.
</p>

Now paste your path to the folder that contains your T-BAGc.exe file.
Remember to add a "\\" to the end of the path
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/var3.png" alt="Project logo"></a>
  <br />
In my case, I pasted "C:\Users\USERNAME\Desktop\T-BAGc\" to the path.
</p>

After doing this click "OK" on all the windows that are open and reboot your computer.
T-BAGc can now be ran from the command prompt.
  
</p>

### Running
T-BAGc works best on Visual Studio code.
Install Visual Studio.

Now, create a folder.
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/running1.png" alt="Project logo"></a>
</p>

<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/running2.png" alt="Project logo"></a>
  <br />
  Within that folder make a .bag file. This is the file that will contain your T-BAGc code.
</p>

<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/run3.png" alt="Project logo"></a>
  <br />
  In Visual Studio open the folder path.
</p>

<p>
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/run4.png" alt="Project logo"></a>
</p>


Lastly, here is how to run T-BAGc in the Visual Studio terminal or the command prompt:

```
T-BAGc main.bag
```
If your file name is not main. bag change the name to suit the name of your file.
Make sure when you do run the file that you are in its file path. If you are not in the same folder, that is fine, however in that case you must type up the entire path to the .bag file.



##  Documentation <a name="documentation"></a>

### Hello World

In T-BAGc there are three different ways to display a Hello World program. 
Here is the smallest hello program made to print to the terminal/command prompt:
```
put "hello world"
```


The second hello world program is meant to log "hello world" to the web browser console.
Here is the code to do that:
```
log "hello world"
<...>
```


Hello World can also be displayed as an HTML view as a title, to do that type this code:
```
title "hello world"
[<...>]
```



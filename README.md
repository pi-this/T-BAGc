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

### Prerequisites <a name = "prerequisites"></a>

Python3 needs to be pre-installed to run T-BAGc.

If Python is not installed you can install it at <a href="https://www.python.org/">python.org</a> or you can get Python from the Microsoft app store.
When running the Python installer on Windows check "use admin privileges" when installing py.exe and "add python.exe to the PATH".


Once Python is installed you can install T-BAGc.

### Installing

To install T-BAGc follow the instructions below.


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
Open command prompt


Open the command prompt for further execution.
<p>
  <a href="" rel="noopener">
 <img src="https://github.com/pi-this/T-BAGc/blob/main/img/installStep2.png" alt="Project logo"></a>
  <br />
  On the keyboard, hold down the 'Windows Key + R' to open the run dialog.
  In the run dialog type "cmd" to open the command prompt.
</p>


##### Step 4
Allow admin privileges


Now redirect the command prompt to the admin privileges cmd window.
<p>

  ```
powershell -Command "Start-Process cmd -Verb RunAs"
```

  Type the command above to open the administrator command prompt.
</p>


##### Step 5
Batch file copy


Write the following code into your administrator command prompt.
<p>

  ```
xcopy <filepath> "C:\Windows\System32\"
```

  The code above will add the batch file that will run T-BAGc to a folder so it can be accessed anywhere on Windows.
  Don't forget to replace `<filepath>` with the path to the T-BAGc batch file.
  <br />
  Here is an example:
  <br />

  ```
xcopy "C:\User\username\Downloads\T-BAGc-main\T-BAGc-main\T-BAGc" "C:\Windows\System32\"
```
  
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
  <br />
  In Visual Studio open the folder path.
</p>



##  Documentation <a name="documentation"></a>

### General

```start bro``` is the entrypoint for the program and all program must end with ```stop bro``` . Anything outside of it will be ignored.

```
start bro

stop bro
```

### Built-ins

Use ```bol bro``` to print anything to console.

```
start bro
 bol bro 'Hello World';
stop bro
```

### Variables

Variables can be declared or assigned using ```->``` operator.

```
start bro
 a -> 10;
 b->12;
 a->b;
stop bro
```

### Types

Supports  ```int``` , ```float``` , ```string``` types.

```
start bro
 a->10;
 b->8.5;
 c-> 'hello';
stop bro
```

### Conditionals

BroCode supports if-else-if ladder construct , ```jodi bro``` will execute if condition, ```jodi na bro``` equivalet to elseif and ```na hole bro``` equivalent to else.

```
start bro
a -> 12;
b -> 10;
jodi bro a<b{
  bol bro 'less';
}
jodi na bro a==b{
  bol bro 'equal';
}
na hole bro{
  bol bro 'greater';
}
stop bro
```

### Loops

Statements inside ```jotokhon bro``` blocks are executed as long as a specified condition evaluates to true.

```
start bro
a -> 12;
b -> 20;
jotokhon bro a<b{
  bol bro a;
  a -> a+1;
}
stop bro
```

- [@c0mrd](https://github.com/c0mrd) - Idea & Initial work



# HexQT 
-------------
A QT (Pronounced Cute) Hex Editor written using the Python binding of QT5! 

![](https://i.imgur.com/1B6KKaG.png)

# Features
--------------
* View a files side-by-side hexi and ascii representation [complete 100%]
* Saving dump output to a file. [in-progress 0%]
* Edit hex files with live updating ascii [in-progress 10%]
    - Implementing addition and override mode.
* Bidirectional Highlighting [in-progress 95%]
    - Parse ascii or hexedecimal selection and highlight on appropriate window.
* Offset Jumping [in-progress 0%]
    - Jump to a set set of hex using a predefined hexe(decimal) offset.

# Requirements
----------------
* Python3
* PyQt5

# Installation
-----------------
`$ git clone https://github.com/queercat/HexQT/`  
`$ cd HexQT`  
`$ pip install PyQt5`  

# Running
-----------------
`$ python3 hexqt.py`
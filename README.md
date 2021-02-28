# Tkinter extension widgets

* [Theme](#theme)
* [NumEntry](#numentry)
* [ToolTip](#tooltip)
* [LinkLabel](#linklabel)
* [ToggledFrame](#toggled)
* [PopupMenu](#popupmenu)
* [MenuBar](#menubar)
* [Image](#image)


<div id="theme"></div>

<br>

## Theme

#### If you want to change the appearance of you Tkinter window simply you can do so with the theme widget

### Options:
            
file (str): Path to a tcl theme file\
name (str): The name of the theme\
pkg (str): Path to a folder containing **pkgIndex.tcl** and other tcl files
            
### Usage:
        
If you only want to use one of ttk's built-in themes (e.g. alt, clam, classic, default, aqua, vista, winnative, xpnative):
```python
theme = Theme(master, name='theme name')
```

If you want to use a single tcl file (e.g. [azure](https://github.com/rdbende/Azure-ttk-theme), [breeze](https://github.com/MaxPerl/ttk-Breeze), [waldorf](https://wiki.tcl-lang.org/page/waldorf+ttk+theme), or a theme from [ttkthemes](https://github.com/TkinterEP/ttkthemes)):
```python
theme = Theme(master, file='path to a tcl theme file')
```
                
If you have a theme package (e.g. [awthemes](https://sourceforge.net/projects/tcl-awthemes/)), you can use it with:
```python
theme = Theme(master, pkg='path to a theme package', name='name of theme you want to use')
```

<div id="numentry"></div>

<br>

## NumEntry

#### An entry that takes numbers and calculates the result of a calculation
        
### Standard entry options:
            
class, cursor, exportselection\
invalidcommand, justify, show\
state, style, takefocusxscrollcommand\
textvariable, validate, validatecommand, width
                
### Widget-specific options:
            
expressions (bool): Allow the use of expressions (default is True)\
roundto (int): The number of decimals in the result (default is 0)
            
### Usage:

```python
numentry = NumEntry(master, roundto=2)
numentry.pack(pady=20)
```


<div id="tooltip"></div>

<br>

## ToolTip

#### Popup help for tkinter widgets

### Standard label options:
            
anchor, background, borderwidth, class\
compound, cursor, font, foreground, image\
justify, padding, relief, state, style, takefocus\
text, textvariable, underlinewidth, wraplength

### Widget-specific options:

wait (int): Wait before appearing in seconds (default is 1)\
duration (int): Wait before disappearing in seconds(default is 10)\
direction (str): Direction relative to the parent. Directions: `cursor` `above` `below` `right` `left` (default is `cursor`)\
ipadx (int): Inner X padding of the tooltip (default is 3)\
ipady (int): Inner Y padding of the tooltip (default is 1)


### Usage:
```python    
tooltip = ToolTip(master, text='ToolTip', wait='1', duration='5')
```

<div id="linklabel"></div>

<br>

## LinkLabel

#### If you want a widget that opens a website you should use LinkLabel

### Standard label options:
            
anchor, background, class, compound\
cursor, font, foreground, image\
justify, style, takefocus, text\
textvariable, underline, padding\
relief, width,  wraplength
                
### Widget-specific options:
            
hovercolor (hex-color): Color when you hover the label\
url (str): The link that you want to open\
visited (bool): Sets the link to be visited, (default is False)\
visitedcolor (hex-color): Color after the label was clicked
            
### Virtual Event:

`<<LinkOpened>>`

### Widget method:

`clear` Clears the visited, and hovered statement
            
### Variable:
        
`is_visited` True or False

### Usage:
        
```python
link = LinkLabel(master, text='LinkLabel', url='https://github.com/rdbende/Tkinter-extension-widgets')
link.pack()
```

<div id="toggled"></div>

<br>

## ToggledFrame

#### If you want to save whitespace, it's a great idea to use ToggledFrame
                
### Options:
            
text (str): The text shown on the expander button\
width (int): The width of the expander button given in characters\
cursor (str): The expander button's cursor\
expanded (bool): Determines whether the frame is open by default
            
### Virtual Events:

`<<ToggledFrameToggled>>`\
`<<ToggledFrameExpanded>>`\
`<<ToggledFrameCollapsed>>`
            
### Widget method:
            
`toggle` Expand or collapse the frame
            
### Variable:
        
`state` expanded or collapsed
            
### Usage:

```python
frame = ToggledFrame(master, text="Toggle", width=40, expanded=True)
frame.pack()
            
button = ttk.Button(frame.frame, text="Button")
button.pack()
```

<div id="popupmenu"></div>

<br>

## PopupMenu

#### Popup menus are very useful, but so complicated to create them in Tkinter, so this is the widget you need

### Standard menu options:
            
activebackground, activeborderwidth\
activeforeground, background, bd, bg\
borderwidth, cursor, disabledforeground\
fg, font, foreground, name, postcommand\
relief, selectcolor, takefocus, tearoff\
tearoffcommand, title, type
                
### Widget-specific options:
            
relx (int): The X position of the popup relative to the cursor, in pixels (default is -3)\
rely (int): The Y position of the popup relative to the cursor, in pixels (default is -3)
            
### Virtual Event:
        
`<<PopupMenuPopup>>`
            
### Usage:
        
```python
popupmenu = PopupMenu(master)
```

<div id="menubar"></div>

<br>

## MenuBar

#### A simple menu bar that appears on the top of the window
        
### Standard menu options:
            
activebackground, activeborderwidth\
activeforeground, background, bd, bg\
borderwidth, cursor, disabledforeground\
fg, font, foreground, name, postcommand\
relief, selectcolor, takefocus, tearoff\
tearoffcommand, title, type

### Widget-specific options:
            
tearoff (bool): Disables / enables tearoff of all menus and submenus (default is False)

### Usage:

```python      
menubar = MenuBar(master)
submenu = tk.Menu(menubar)
menubar.add_cascade(menu=submenu)
```


<div id="image"></div>

<br>

## Image

#### If you want to display an image, without PhotoImage or PIL, the easiest way is this widget
                
### Options:
            
file (str): Path to image file. Valid filetypes: `gif` `png` `pgm` `ppm`\
data (str): Image data URI\
cursor (str): The cursor of the image, similar to other tkinter widgets\
anchor (str): The anchor of the image, similar to other tkinter widgets\
relief (str): The relief of the image, similar to other tkinter widgets
            
### Usage:

```python
image = Image(master, file='path to the image file you want to display', cursor='hand2', relief='groove')
image.pack()
```

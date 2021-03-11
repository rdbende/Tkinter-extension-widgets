# Tkinter extension widgets

- [ToolTip](#tooltip)
- [NumberEntry](#numentry)
- [Image](#image)
- [PopupMenu](#popupmenu)
- [MenuBar](#menubar)
- [LinkLabel](#linklabel)
- [ToggledFrame](#toggled)


<div id="tooltip"></div>

<br>

## ToolTip

#### Popup help for Tkinter widgets

### Options:

- `wait` (int) wait before appearing (in milliseconds)
- `duration` (int) wait before disappearing (in milliseconds)
- `direction` (str) direction relative to the parent. Directions: `cursor`, `above`, `below`, `right`, `left` (default is `cursor`)
- `ipadx` (int) inner X padding of the tooltip (default is 2)
- `ipady` (int) inner Y padding of the tooltip (default is 1)
- `kwargs` options to be passed on to the `tk.Label` initializer inside the tooltip


### Example:
```python
import tkinter as tk
from ToolTip import ToolTip

root = tk.Tk()

button = tk.Button(root, text='Button')
button.pack(pady=10)

tooltip = ToolTip(button, text='ToolTip', wait='1000', duration='5000', direction='below')

root.mainloop()
```

<div id="numentry"></div>

<br>

## NumberEntry

#### An entry that takes only numbers or calculations and calculates the result of the calculation

### Options:

- `expressions` (bool) allow the use of expressions (default is True)
- `roundto` (int) the number of decimals in the result (default is 0)
- `kwargs` options to be passed on to the `ttk.Entry` initializer

### Example:

```python
import tkinter as tk
from NumberEntry import NumberEntry

root = tk.Tk()

entry = NumberEntry(root, expressions=True, roundto=4)
entry.pack(pady=20)

root.mainloop()
```

<div id="image"></div>

<br>

## Image

#### If you want to display an image, without PhotoImage or PIL, the easiest way is this widget

### Options:

- `file` (str) path to image file. Valid filetypes: `gif` `png` `pgm` `ppm`
- `data` (str) image data URI
- `cursor` (str) image cursor
- `anchor` (str) image anchor (default is `center`)
- `relief` (str) image relief  (default is `flat`)
- `borderwidth` (int) image borderwidth  (default is 0)

### Methods:
- `blank` display a transparent image
- `clear` clear the image file and data from the widget, and blanks the image
- `copy` return a new PhotoImage with the same image as this widget
- `get` return the color (red, green, blue) of the pixel at `x`, `y`
- `image_names` return the available image names in the program
- `image_types` return the available image types in the program
- `subsample` return a new PhotoImage based on the same image as this widget
but use only every `x`th or `y`th pixel. If y is not given, the
default value is the same as x
- `put` put row formatted colors to image starting from
position 'to'
- `write` write image to file `filename` in `format` starting from
position `form_coords`
- `zoom` return a new PhotoImage with the same image as this widget,
but zoom it with a factor of x in the `x` direction and y in the `y`
direction. If y is not given, the default value is the same as x

### Example:

```python
root = tk.Tk()

# Define image data
image_data = '''iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACX
                BIWXMAAAA7AAAAOwG4ag7yAAAAGXRFWHRTb2Z0d2FyZQB3d3cu
                aW5rc2NhcGUub3Jnm+48GgAAA71JREFUSImtl11oHFUUx393dl
                xMAkX7IVKpSkT8IPTDxJJ+YVujBPyAVkJEiuCTL1axtKjty9on
                G0QQfPVFFKzSUG1eIqaBJjZpJLUmhBIRpbUFNaUhCInd3Tl/Hy
                bJzG6yM0PNhcPeO3Pv/8c995xzZx0ZWnPhzNp8SQdkwS5BE9Ia
                pFVgJdA0pimk887UO7xqsodCwdI0XdqE1mNnOpF9itQgBJo3LO
                rHx+iSnO0f+fDV35N0vaSXOwrfrEf2GZJMOujMuhKhoW12AT0d
                HV/lbhtst9zDSHnJukc+2PfJ8ImX3gH7rSZ00SP2+LUNcxuTtP
                2kl1BG4Wk81XK0uyknu5/ANqRAAWFB0HDb4LLl5LkApAdygY1n
                2GnUT2mJYB9Nm/Q9BOGDpdC9IK8aKgmXErYV4I2Hexvq88VHZG
                UHYAgI3gWgBGESlGMrdB4pXw1FAhegyef3YcE6AMyuMnejz7WM
                liJwoeC1Fp84juYOSaqL3GWg+Z26qvEy7lXcIyVAwXugJxfX16
                3+ST8/2+42ffe3B7CtuOUjZMeE6lLzNAt04YwX5kb5vwUv+BLA
                2360p0nSG5mKQ1aohJwC4pqR7dGlp/f4plKnILeSUBCSXUO6cx
                kwOHvRk1zbSkMdGhl5u2cG6dFlwaYdnkPrVxKK9Cvl0gGK5VeQ
                7lgWLN3rS7Y2A3TEYePmdAOLB47F87uMNFQ/V9fXf+TUbuS6ak
                BBWuMvhVb0Z3B0DB88O4Cmn8FoReQioIVwAzAf036k95FrToCC
                hI90E6k+gi5ebzjj8NCbX19F3gSiMczlahGqfjPZlIf4E5ZCkY
                q5fPEkzvsC1FgjNWJm2aAh67qHs8GKhRHg8uDrp+9GSnVbZou0
                +zxw3y6FGg4rkvPvyyaastvK6hVA+aR3oauzH6mfZVKGoJzLBs
                4EXLCP3dYfJzyAnGcvI12MQ02Kp8pKAGfBjrN1+MjCPQfA7kK/
                PzdzZS+BPUhY9KYuvHV6isAGagCKmNs+f19GrVQ1BrDAcMVJ1z
                I6u/Ao8brW5As7IagFNqSzi15CYLFrU8Eh1zI0Xks75ZurBHK1
                XOqB2ipdGjsa592VpJz4lRluO+kMF6O5iKkdz5qQroSBaYnaye
                BAswm5GLc/XPNAr9v8wwTSuXCeU5J0sqv/ujXGPfnLSI8tjdSK
                3H1IoztPILs+X6//xZV/SZJO/QujsbZGPHUjNmUsGv8gveZaL5
                z6X2AAqeAxdu45UDvSNqR1yFYj+UgzSDdBY5gGKPqfu12D02ma
                /wHhz94W7ZGK5wAAAABJRU5ErkJggg=='''

image = Image(root, cursor='hand2', anchor='w', relief='solid', borderwidth=2, data=image_data)
image.pack(pady=20)

# Copy the image
copy = image.copy()

# Zoom in the copy
copy = copy.zoom(x=4, y=2)

# Mirroring and distorting the image
copy = copy.subsample(x=-1, y=1)

# Put a red square on the picture
copy.put("{red red red red red red red red} {red red red red red red red red}", to=(50, 20))

edited = tk.Label(root, image=copy)
edited.pack(pady=20)

root.mainloop()
```


<div id="popupmenu"></div>

<br>

## PopupMenu

#### Popup menus are very useful, but so complicated to create them in Tkinter, this widget simplifies this

### Options:

- `offsetx` (int): the X offset relative to the cursor (default is -2)
- `offsety` (int): the Y offset relative to the cursor (default is -2)
- `kwargs` options to be passed on to the `tk.Menu` initializer

### Virtual event:

`<<PopupMenuPopup>>`

### Example:

```python
import tkinter as tk
from PopupMenu import PopupMenu

root = tk.Tk()
root.geometry('150x150')

def callback():
    print('PopupMenu')

popupmenu = PopupMenu(root)
popupmenu.add_command(label='Command 1', command=callback)
popupmenu.add_command(label='Command 2', command=callback)
popupmenu.add_command(label='Command 3', command=callback)

root.mainloop()
```

<div id="menubar"></div>

<br>

## MenuBar

#### A simple menu bar that appears on the top of the window

### Options:

- `tearoff` (bool) disables / enables tearoff of all menus and submenus (default is False / disabled)
- `kwargs` options to be passed on to the `tk.Menu` initializer

### Widget methods:

- `add_submenu` alias for add_cascade
- `add_applemenu` create a menu for Apple-icon on Mac, with the name `apple_menu`

### Example:

```python
import tkinter as tk
from MenuBar import MenuBar

root = tk.Tk()

def callback():
    print('MenuBar')

menubar = MenuBar(root)

# Add Apple menu
menubar.add_applemenu()
menubar.apple_menu.add_command(label='Apple submenu', command=callback)

# Add a submenu
submenu = tk.Menu(menubar)
menubar.add_submenu(menu=submenu, label='Submenu')
submenu.add_command(label='Submenu command', command=callback)

# Add a command
menubar.add_command(label='Command', command=callback)

root.mainloop()
```

<div id="linklabel"></div>

<br>

## LinkLabel

#### If you need a widget that can open a website you should use LinkLabel

#### Based on [RedFantom's LinkLabel](https://github.com/RedFantom/ttkwidgets/blob/master/ttkwidgets/linklabel.py)

### LinkLabel options:

- `hovercolor` (hex-color) text color when hovering over the widget
- `normalcolor` (hex-color) text color at the init of the widget
- `url` (str) the link to open
- `visited` (bool) set the label to visited, (default is False)
- `visitedcolor` (hex-color) text color when link is clicked
- `kwargs` options to be passed on to the `ttk.Label` initializer

### Virtual event:
`<<LinkOpened>>`

### Variable:

`is_visited` True / False

### Widget method:

`reset` reset the visited, and hovered status

### Example:

```python
import tkinter as tk
from LinkLabel import LinkLabel

root = tk.Tk()

def callback():
    print('LinkLabel')

link = LinkLabel(root, text='LinkLabel', url='https://github.com/rdbende/Tkinter-extension-widgets')
link.bind('<<LinkOpened>>', callback)
link.pack(pady=20)

root.mainloop()
```

<div id="toggled"></div>

<br>

## ToggledFrame

#### Based on [RedFantom's ToggledFrame](https://github.com/RedFantom/ttkwidgets/blob/master/ttkwidgets/frames/toggledframe.py)

#### If you want to save whitespace, it's a great idea to use ToggledFrame

### Options:

- `text` (str) the text shown on the expander button
- `width` (int) the width of the expander button given in characters
- `cursor` (str) the expander button's cursor
- `expanded` (bool) determines whether the frame is expanded by default
- `kwargs` options to be passed on to the main `ttk.Frame` initializer

### Virtual Events:

- `<<ToggledFrameToggled>>`
- `<<ToggledFrameExpanded>>`
- `<<ToggledFrameCollapsed>>`

### Widget method:

`toggle` expand / collapse the frame

### Variable:

`state` 'expanded' / 'collapsed'

### Example:

```python
import tkinter as tk
from ToggledFrame import ToggledFrame

root = tk.Tk()

def callback():
    print('ToggledFrame')

frame = ToggledFrame(root, text="ToggledFrame", width=40, expanded=True)
frame.bind(<<ToggledFrameToggled>>, callback)
frame.pack(pady=10)

button = ttk.Button(frame.frame, text="Button")
button.pack(pady=20)

root.mainloop()
```

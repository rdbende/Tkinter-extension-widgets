# Tkinter-extension-widgets

* [Theme](#theme)
* [LinkLabel](#linklabel)
* [Image](#image)


<div id="theme"></div>

## Theme
#### If you want to change the appearance of the tkinter window simply you can do so with the theme widget

### Options:
            
file (str): Path to a tcl theme file\
name (str): The name of the theme\
pkg (str): Path to a folder containing **pkgIndex.tcl** and other tcl files
            
### Usage:
        
If you only want to use one of ttk's built-in themes (e.g. alt, clam, classic, default, aqua, vista, winnative, xpnative):\
`theme = Theme(root, name='theme name')`

If you want to use a single tcl file (e.g. [azure](https://github.com/rdbende/Azure-ttk-theme)):\
`theme = Theme(root, file='path to a tcl theme file')`
                
If you have a theme package (e.g. [awthemes](https://sourceforge.net/projects/tcl-awthemes/)), you can use it with:\
`theme = Theme(root, pkg='path to a theme package', name='name of theme you want to use')`

<div id="linklabel"></div>

## LinkLabel

#### If you want a clickable widget you should use the LinkLabel

### Standard label options:
            
anchor, background, borderwidth, class\
compound, cursor, font, foreground\
image, justify, padding, relief\
state, style, takefocus, text\
textvariable, underlinewidth, wraplength
                
### Specific options:
            
hovercolor (str): Color when you hover the label\
url (str): The link that you want to open\
visited (bool): Sets the link to be visited, it's false by default\
visitedcolor (str): Color after you clicked the label
            
### Generates:

`<<LinkOpened>>`
            
### Variable:
        
`is_visited = True or False`

### Usage:
        
```python
link = LinkLabel(master, text='Link', url='https://', hovercolor='#ff0000')
link.pack()
```

<div id="image"></div>

## Image

#### If you want to display an image, but do not need PIL, the easiest way is this widget
                
### Options:
            
file (str): Path to image file valid filetypes: `pgm` `ppm` `gif` `png`\
data (str): Image data URI\
cursor (str): The cursor of the image, similar to other tkinter widgets\
anchor (str): The anchor of the image, similar to other tkinter widgets\
relief (str): The relief of the image, similar to other tkinter widgets
            
### Usage:

```python
image = Image(master, file='path to the image file you want to display', anchor='w', relief='groove')
image.pack()
```

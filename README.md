# Tkinter-extension-widgets

## Overview

### Theme:                
Options:
            
file (str): Path to a tcl theme file
name (str): The name of the theme
pkg (str): Path to a folder containing pkgIndex.tcl and other tcl files
            
Usage:
        
If you only want to use one of ttk's built-in themes:
`theme = Theme(root, name='built in theme names e.g.: alt, clam, classic, default, aqua, vista, winnative, xpnative')`

If you want to use a single tcl file (e.g. [https://github.com/rdbende/Azure-ttk-theme](azure)):
`theme = Theme(root, file='path to a tcl theme file')`
                
If you have a theme package (e.g. [https://sourceforge.net/projects/tcl-awthemes/](awthemes)), you can use it with:
`theme = Theme(root, pkg='path to a theme package', name='name of theme you want to use')`
                
         

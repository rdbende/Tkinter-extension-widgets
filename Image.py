"""An image display widget for tkinter"""

import tkinter as tk

class Image(tk.Label):
    """
        An image display widget for tkinter
                
        Image options:
            
            file (str): Path to image file
            data (str): Image data
            cursor (str): The cursor of the image, similar to other tkinter widgets
            anchor (str): The anchor of the image, similar to other tkinter widgets
            relief (str): The relief of the image, similar to other tkinter widgets
            
        Usage:
        
            image = Image(master, file='path to the image file you want to display', anchor='w', relief='groove')
            image.pack()

    """

    def __init__(self, master=None, file=None, data=None, cursor="arrow", anchor="center", relief="flat"):
        
        self._file = file
        self._data = data
        self._cursor = cursor
        self._anchor = anchor
        self._relief = relief
        if self._data != None and self._file == None:
            self.image = tk.PhotoImage(data=self._data)
        elif self._file != None and self._data == None:
            self.image = tk.PhotoImage(file=self._file)
        else:
            raise Exception("Couldn't use file and image data at the same time")
        
        tk.Label.__init__(self, master, image=self.image, cursor=self._cursor, anchor=self._anchor, relief=self._relief)
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key is "file":
            return self._text
        elif key is "data":
            return self._extext
        elif key is "cursor":
            return self._cursor
        elif key is "anchor":
            return self._anchor
        elif key is "relief":
            return self._relief
        else:
            raise AttributeError("Image widget has no attribute '" + key + "'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["file", "data", "cursor", "anchor", "relief"]
        return keys
    
# Test

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Image')
    root.geometry('210x50')
    
    image_data = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACXBIWXMAAAA7AAAAOwG4ag7yAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA71JREFUSImtl11oHFUUx393dlxMAkX7IVKpSkT8IPTDxJJ+YVujBPyAVkJEiuCTL1axtKjty9onG0QQfPVFFKzSUG1eIqaBJjZpJLUmhBIRpbUFNaUhCInd3Tl/HybJzG6yM0PNhcPeO3Pv/8c995xzZx0ZWnPhzNp8SQdkwS5BE9IapFVgJdA0pimk887UO7xqsodCwdI0XdqE1mNnOpF9itQgBJo3LOrHx+iSnO0f+fDV35N0vaSXOwrfrEf2GZJMOujMuhKhoW12AT0dHV/lbhtst9zDSHnJukc+2PfJ8ImX3gH7rSZ00SP2+LUNcxuTtP2kl1BG4Wk81XK0uyknu5/ANqRAAWFB0HDb4LLl5LkApAdygY1n2GnUT2mJYB9Nm/Q9BOGDpdC9IK8aKgmXErYV4I2Hexvq88VHZGUHYAgI3gWgBGESlGMrdB4pXw1FAhegyef3YcE6AMyuMnejz7WMliJwoeC1Fp84juYOSaqL3GWg+Z26qvEy7lXcIyVAwXugJxfX163+ST8/2+42ffe3B7CtuOUjZMeE6lLzNAt04YwX5kb5vwUv+BLA2360p0nSG5mKQ1aohJwC4pqR7dGlp/f4plKnILeSUBCSXUO6cxkwOHvRk1zbSkMdGhl5u2cG6dFlwaYdnkPrVxKK9Cvl0gGK5VeQ7lgWLN3rS7Y2A3TEYePmdAOLB47F87uMNFQ/V9fXf+TUbuS6akBBWuMvhVb0Z3B0DB88O4Cmn8FoReQioIVwAzAf036k95FrToCChI90E6k+gi5ebzjj8NCbX19F3gSiMczlahGqfjPZlIf4E5ZCkYq5fPEkzvsC1FgjNWJm2aAh67qHs8GKhRHg8uDrp+9GSnVbZou0+zxw3y6FGg4rkvPvyyaastvK6hVA+aR3oauzH6mfZVKGoJzLBs4EXLCP3dYfJzyAnGcvI12MQ02Kp8pKAGfBjrN1+MjCPQfA7kK/PzdzZS+BPUhY9KYuvHV6isAGagCKmNs+f19GrVQ1BrDAcMVJ1zI6u/Ao8brW5As7IagFNqSzi15CYLFrU8Eh1zI0Xks75ZurBHK1XOqB2ipdGjsa592VpJz4lRluO+kMF6O5iKkdz5qQroSBaYnayeBAswm5GLc/XPNAr9v8wwTSuXCeU5J0sqv/ujXGPfnLSI8tjdSK3H1IoztPILs+X6//xZV/SZJO/QujsbZGPHUjNmUsGv8gveZaL5z6X2AAqeAxdu45UDvSNqR1yFYj+UgzSDdBY5gGKPqfu12D02ma/wHhz94W7ZGK5wAAAABJRU5ErkJggg=='
    
    image = Image(root, data=image_data)
    image.pack(pady=5)
    
    root.mainloop()

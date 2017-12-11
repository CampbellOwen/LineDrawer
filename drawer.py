from PIL import Image

class Drawer:


    def __init__( self, img ):
        self.img = img
    
    @staticmethod
    def from_file( filepath ):
        return Drawer( Image.open( filepath ) )


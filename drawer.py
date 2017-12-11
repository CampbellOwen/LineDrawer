from PIL import Image
import random

class Drawer:


    def __init__( self, img ):
        self.img = img
        self.canvas = Image.new( "RGB", ( img.width, img.height ), "black" )

    @staticmethod
    def from_file( filepath ):
        return Drawer( Image.open( filepath ) )

    @staticmethod
    def get_octant( start, end ):
        x, y  = (end[0] - start[0]), (end[1] - start[1])
        octant = [([0, 1], [7, 6]), ([3, 2], [4, 5])][x < 0][y < 0][abs(x) < abs(y)]
        return octant
    
    @staticmethod
    def to_octant_zero( octant, pt ):
        print( octant )
        if octant == 0:
            return pt
        elif octant == 1:
            return ( pt[1], pt[0] )
        elif octant == 2:
            return ( pt[1], -pt[0] )
        elif octant == 3:
            return ( -pt[0], pt[1] )
        elif octant == 4:
            return ( -pt[0], -pt[1] )
        elif octant == 5:
            return ( -pt[1], -pt[0] )
        elif octant == 6:
            return ( -pt[1], pt[0] )
        elif octant == 7:
            return ( pt[0], -pt[1] )

    @staticmethod
    def octant_zero_to( octant, pt ):
        if octant == 0:
            return pt
        elif octant == 1:
            return ( pt[1], pt[0] )
        elif octant == 2:
            return ( -pt[1], pt[0] )
        elif octant == 3:
            return ( -pt[0], pt[1] )
        elif octant == 4:
            return ( -pt[0], -pt[1] )
        elif octant == 5:
            return ( -pt[1], -pt[0] )
        elif octant == 6:
            return ( pt[1], -pt[0] )
        elif octant == 7:
            return ( pt[0], -pt[1] )


    def draw_and_compare_line( self, cmp_img, out_img, start, end, colour ):
        pixels = [ ]
        octant = self.get_octant( start, end )
        start = self.to_octant_zero( octant, start )
        end = self.to_octant_zero( octant, end )

        print( start )
        print( end )

        # Bresenham
        x = start[ 0 ]
        m_num = 2 * ( end[ 1 ] - start[ 1 ] )
        y_int = start[ 1 ]
        y_num = ( end[ 0 ] - start[ 0 ] )
        y_den = 2 * ( end[ 0 ] - start[ 0 ] )

        error = m_num - y_den

        while x <= end[ 0 ]:
            # set x, y_int, colour
            # check error
            print( (x, y_int ) )
            coord = self.octant_zero_to( octant, ( x, y_int ) )
            out_img.putpixel( coord, colour )
            pixels.append( ( coord, colour ) )

            x += 1
            if y_num + error >= 0:
                y_int += 1
                y_num += error
            else:
                y_num += m_num

        #print( pixels )

    def draw( self, outpath, iterations ):
        colours = self.img.getcolors( 100000 )
        print( ( self.img.width, self.img.height ) ) 

        for i in range( iterations ):
            colour = colours[ random.randint( 0, len( colours ) -1 ) ][ 1 ]
            
            start_x = random.randint( 0, self.img.width - 1 )
            start_y = random.randint( 0, self.img.height - 1 )

            end_x = random.randint( 0, self.img.width - 1 )
            end_y = random.randint( 0, self.img.height - 1 )
            
            start = ( start_x, start_y )
            end = ( end_x, end_y )

            print( "start: {0}, end {1}".format( start, end ) )

            self.draw_and_compare_line( self.img, self.canvas, start, end, colour )

        self.canvas.save( outpath )




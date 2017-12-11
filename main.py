from argparse import ArgumentParser

parser = ArgumentParser( description="Recreate given image with only lines" )
parser.add_argument( 'filepath' )
parser.add_argument( 'output path' )

args = parser.parse_args()

drawer = Drawer.from_file( args.filepath )


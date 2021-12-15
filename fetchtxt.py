import argparse

from internetarchive import download

# https://archive.org/services/docs/api/internetarchive/quickstart.html
def main(args):
    download(args.fetch, verbose=True, glob_pattern="*.txt", destdir="input")

if __name__ == '__main__':

    # Initialize
    parser = argparse.ArgumentParser(description='Fetch some txt files from the Internet Archive.')
    parser.add_argument('-f', '--fetch', help='File to download', required=True)

    args = parser.parse_args()

    main(args)

import argparse


def main():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Youtube Downloader..."
    )

    parser.add_argument('-u','--url',help='Youtube video url', default=None)
    parser.add_argument('-q', '--quality', help='video quality', default='highest')
    parser.add_argument('-d', '--delay', help='Delay between downloads',type=int, default=0)
    parser.add_argument('-ul','--url_list', help='List of URLs', nargs='+')

    args = parser.parse_args()
    print(args)

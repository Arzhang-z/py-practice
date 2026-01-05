from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from pathlib import Path
from tqdm import tqdm
import argparse


class YouTubeDownloader:
    def __init__(self, url: str, output_path=None, quality: str = "highest"):
        self.url = url
        self.output_path = Path(output_path) if output_path else Path.cwd()
        self.quality = quality
        self.pbar = None

        self.yt = YouTube(
            self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete
        )

    def download(self):
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            print("Video is unavailable")
            return

        if self.quality == "highest":
            stream = (
                self.yt.streams.filter(
                    progressive=True, file_extension="mp4"
                ).get_highest_resolution()
            )
        else:
            stream = (
                self.yt.streams.filter(progressive=True, file_extension="mp4", res=self.quality).first()
            )

        if stream is None:
            print(f"Quality '{self.quality}' not available.")
            return

        total_size = stream.filesize or stream.filesize_approx

        self.pbar = tqdm(
            desc="Downloading",
            total=total_size,
            unit="B",
            unit_scale=True
        )

        stream.download(output_path=str(self.output_path))
        self.pbar.close()
        print("Download finished")

    def on_progress(self, stream, chunk, bytes_remaining):
        downloaded = stream.filesize - bytes_remaining
        self.pbar.update(downloaded - self.pbar.n)

    def on_complete(self, stream, file_path):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Youtube Downloader"
    )
    parser.add_argument('url', help='Youtube video URL')
    parser.add_argument('-q', '--quality', help='video quality',default='highest')
    parser.add_argument('-o', '--output_path', help='Output path', default=None)

    args = parser.parse_args()

    #url = "https://www.youtube.com/watch?v=_bFPB0v9mWs"
    
    YouTubeDownloader(
        url=args.url,
        quality=args.quality,
        output_path=args.output_path
    ).download()
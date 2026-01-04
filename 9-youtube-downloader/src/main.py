from pytube import YouTube
from pathlib import Path

class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path().cwd()
        self.quality = quality or "highest"
        self.yt = YouTube(
            self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete
        )

    def download(self):
        if self.quality == "highest":
            stream = self.yt.streams.filter(progressive=True,
                file_extension="mp4"
            ).get_highest_resolution()
        else:      
            stream = self.yt.streams.filter(
                progressive=True,
                file_extension='mp4',
                res=self.quality
            ).first()
        
        stream.download(self.output_path)
        print("Download Finished")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        print(
            f"\r{"downloading...":<15}"
            f"{(100*(total_size-bytes_remaining)/total_size):>3.0f}% "
            f"| {bytes_downloaded/1024/1024:>5.1f}MB"
            f" of {total_size/1024/1024:5.1f}MB "
            f"| {"finished":<10}",
            end=''
        )
    
    def on_complete(self, stream, file_path):
        print(stream)
        print()
        print(f"Download complete. File saved to: {file_path}")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=_bFPB0v9mWs"
    YouTubeDownloader(url).download()
from os import getcwd, listdir, rename
from .itags import audio_itags_quality
from pytube import YouTube, streams
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor
from typing import Required, Optional


init(autoreset=False)

def multi_download(url: Required[str], quality: Required[str] , out_path: Required[str]):
    video = YouTube(url)
    quality_to_itag = audio_itags_quality.get(quality)
    stream = video.streams.get_by_itag(quality_to_itag)
    stream.download(output_path=out_path, filename=f"{video.title}.mp3")
    print(f"{Fore.GREEN}Succesfully downloaded: {video.title}")


def download(audios_url: Required[list], quality: Optional[str]="128kbps", threads: Optional[int]=2, out_path: Optional[
    str] = f"{getcwd()}/downloads/audios") -> list[str]:
    """
    Variables
    ---------
    * audios_url (list): The list to be provided must be given in text file format with .txt extension must contain all urls separated by the enter key

    * quality (str): the quality variable can choose a range in which the audios with the different qualities will be downloaded
    
    * threads (int): With this, the aim is to provide the number of threads with which you want to work in the simultaneous download of the different audios
    
    * out_path (str): In this variable, the proportional folder is searched for where the download folder with the audios is to be stored.

    """


    with ThreadPoolExecutor(max_workers=threads) as executor:
        for url in audios_url:
            executor.submit(multi_download, url=url, quality=quality, out_path=out_path)

    downloaded_audios = listdir(out_path)

    return downloaded_audios
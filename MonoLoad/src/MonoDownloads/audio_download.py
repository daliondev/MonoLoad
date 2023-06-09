from pytube import YouTube, streams
from colorama import init, Fore
from .itags import audio_itags_quality
from os import getcwd, rename, listdir, path

init(autoreset=True)

def download(url, out_path=f"{getcwd()}/downloads/audios"):

    def get_resolution(streams_data):
        resolutions = list()

        for stream in streams_data:
            resolutions.append(stream.abr)

        return resolutions
    
    def audio_quality_download(resolutions, video):
        print(f"\n video title: {Fore.RED + video.title} \n {Fore.WHITE} \n qualities: {resolutions}")

        audio_quality_to_download = input("\n Type the quality: ")
        
        
        return audio_quality_to_download 
    

    def fix_extensions(out_path, song_name) -> None:

        downloads_path = f"{out_path}/{song_name}"
        
        if path.exists(f"{downloads_path}.mp4"):
            rename(f"{downloads_path}.mp4", f"{downloads_path}.mp3")
        elif path.exists(f"{out_path}/{song_name}.webm"):
            rename(f"{downloads_path}.webm", f"{downloads_path}.mp3")
            

        print(f"\n {Fore.GREEN} Done")


    try:
        video = YouTube(url)
        streams_data = video.streams.filter(only_audio=True)
        resolutions = get_resolution(streams_data=streams_data)
        audio_qulity_to_dowload = str()

        while audio_qulity_to_dowload not in resolutions:
            audio_qulity_to_dowload = audio_quality_download(resolutions=resolutions, video=video)

        stream = video.streams.get_by_itag(audio_itags_quality.get(audio_qulity_to_dowload))
        stream.download(output_path=out_path)
        fix_extensions(out_path=out_path, song_name=video.title)
    except Exception as e:
        print(f"\n {e} \n Check the video url and try again.")

# Import the YouTube class from the pytube library
from pytube import YouTube


# Define a function to download a video based on the URL and chosen resolution
def download_video(url, resolution="audio"):
    try:
        video = YouTube(url)
        
        # Based on the resolution choice, select the appropriate video stream
        if resolution == "audio":
            video_stream = video.streams.filter(only_audio=True).first()
        elif resolution == "low":
            video_stream = video.streams.filter(res="360p").first()
        elif resolution == "high":
            video_stream = video.streams.filter(res="720p").first()
        else:
            print(f"Invalid resolution option: {resolution}")
            return

        # If a suitable video stream is found
        if video_stream:
            print(f'\nChannel Name: {video.author}')
            print(f"Video Title: {video.title}")
            print(f'Number of Views: {video.views}')
            print(f'Video Length: {round((video.length)/60, 3)} Minutes.')
            print(f'Published Date: {video.publish_date}. \n')

            # Ask for user confirmation before downloading
            confirm = input("Do you want to download this video? (yes/no): ").lower()
            if confirm == "yes":
                print(f"\nDownloading: {video.title}")

                # Download the video to the specified output path
                video_stream.download(output_path = path)
                print(f"{(video.title)} downloaded successfully .\n")
            else:
                print("\nDownload has been canceled .\n")
        else:
            print(f"No suitable stream found for {video.title}")

    # Handle exceptions that might occur during the download process
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Entry point of the program
if __name__ == "__main__":

    # Get the YouTube video URL, Download path and the resolution choice from the user
    video_url = input("Enter the YouTube video URL: ")
    path = input('Enter The Download Path: ')
    resolution_choice = input("Choose Resolution (high/low/audio): ").lower()

    # Validate and initiate the download based on 
    if resolution_choice not in ["high", "low", "audio"]:
        print("Invalid resolution choice.")
    else:
        download_video(video_url, resolution=resolution_choice)
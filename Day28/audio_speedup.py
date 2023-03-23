from pydub import AudioSegment

# Get the name of the input audio file from the user
input_file_name = input("Enter the name of the input audio file (include extension): ")

# Open the audio file
audio = AudioSegment.from_file(input_file_name)

# Get the desired playback speed from the user
playback_speed = float(input("Enter the desired playback speed (e.g. 1.5 for 1.5x): "))

# Speed up the audio by the desired amount
sped_up_audio = audio.speedup(playback_speed=playback_speed, chunk_size=10**6)

# Export the sped up audio to a file
output_file_name = input("Enter the name of the output audio file (include extension): ")
sped_up_audio.export(output_file_name, format="mp3")

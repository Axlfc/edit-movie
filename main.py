from moviepy.editor import *
import os

def produce_video(t): 
	path = os.getcwd()

	clips = []

	filenames = []
	os.chdir("./images")
	directory = sorted(os.listdir('.'))

	for filename in directory:
		if filename.endswith(".png"):
			filenames.append(filename)

	clips = [ImageClip(m).set_duration(t) for m in filenames]

	os.chdir(path)
	video = concatenate(clips, method='compose')
	video.write_videofile('test.mp4', fps=24)

def importar_video(video):

	return VideoFileClip(video)

def importar_audio(audio):

	return AudioFileClip(audio)

def unir(clips):
	final_clip = concatenate_videoclips(clips)
	final_clip.write_videofile("video_output.mp4")

def unir_audio(audios):
		path = os.getcwd()
		clips = []
		filenames = []
		os.chdir(".")
		directory = sorted(os.listdir('.'))

		for filename in directory:
			if filename.endswith(".mp3"):
				filenames.append(filename)
		clips = [AudioFileClip(m) for m in filenames]

		os.chdir(path)

		final_clip = concatenate_audioclips(clips)
		final_clip.write_audiofile("audiofiles.mp3")

def extraer_audio(clip):
	audio = clip.audio
	audio.write_audiofile("audio_output.mp3")

def mute_clip(video):
	final_video = video.without_audio()
	final_video.write_videofile("no_audio_output.mp4", fps=60)

def poner_audio(videoclip, audioclip):
	new_audioclip = CompositeAudioClip([audioclip])
	videoclip.audio = new_audioclip
	videoclip.write_videofile("new_filename.mp4")

def cambiar_resolucion(clip, wid, hei):
	reducido = clip.resize((wid, hei))
	reducido.write_videofile("reducido.mp4")

def rotar_video(clip, angle):
	video = clip.rotate(angle)
	video.write_videofile("rotado.mp4")

def cambiar_velocidad(clip, vel):
	video = clip.fx(vfx.speedx, vel)
	video.write_videofile("rapido.mp4")

def phone_proportions():
	
	pass	

videos = ("video1.mp4", "video2.mp4", "video3.mp4")
variables=[]
for vid in videos:

	variables.append(importar_video(vid))
i=0
for j in variables:
  j = importar_video(videos[i])
  i+=1

audios = ("audio1.mp3", "audio2.mp3", "audio3.mp3")
variables_audio=[]
for aud in audios:

	variables_audio.append(importar_audio(aud))
i=0
for j in variables_audio:
  j = importar_audio(audios[i])
  i+=1

################# TEST LINE

# clip1 = variables[0]
# clip_final = unir(variables)

# mute_clip(variables[0])

# cambiar_resolucion(clip1, 480, 480)

# audio1 = variables_audio[0]

# clip_final = unir_audio(variables_audio)

# rotar_video(clip1, 180)
# cambiar_velocidad(clip1, 2)

# extraer_audio(clip1)

# poner_audio(clip1, audio1)

# produce_video(2)


################# TODO LINE

# Control lenghts of videos and audio sync

# audio_duration = audio_clip.duration

# TODO Transform horizontal video to vertical

# TODO Identify vertical videos

# TODO Transform vertical videos to horizontal

# TODO Check correct phone proportion transformation

# TODO Set output path from outside functions by passing it as argument
from moviepy.editor import *
import os

def write_video(video, name):
	video.write_videofile(name + '.mp4', fps=24)

def write_audio(audio, name):
	audio.write_audiofile(name + '.mp3')

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
	write_video(concatenate(clips, method='compose'), "produced")

def importar_video(video):
	return VideoFileClip(video)

def importar_audio(audio):
	return AudioFileClip(audio)

def get_resolution(video):
	return video.size

def get_height(video):
	return video.h

def get_width(video):
	return video.w

def get_duration(media):
	return media.duration

def unir(clips):
	write_video(concatenate_videoclips(clips), "unir")

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

		write_audio(concatenate_audioclips(clips), "uniraudio")

def extraer_audio(clip):
	write_audio(clip.audio, "uniraudio")

def mute_clip(video):
	write_video(video.without_audio(), "muted")

def poner_audio(videoclip, audioclip):
	new_audioclip = CompositeAudioClip([audioclip])
	videoclip.audio = new_audioclip
	write_video(videoclip, "new_sound")

def cambiar_resolucion(clip, wid, hei):
	write_video(clip.resize((wid, hei)), "resolucion")

def rotar_video(clip, angle):
	write_video(clip.rotate(angle), "rotado")

def cambiar_velocidad(clip, vel):
	write_video(clip.fx(vfx.speedx, vel), "rapido")

def phone_proportions(clip):
	write_video(clip.resize((1080, 1920)), "phone")


################# TODO LINE

# TODO Identify vertical videos
# TODO Transform vertical videos to horizontal & viceversa
# TODO Check correct phone proportion transformation

if __name__ == '__main__':
	videos = ("video1.mp4", "video2.mp4", "video3.mp4")
	variables = []
	for vid in videos:
		variables.append(importar_video(vid))
	i = 0
	for j in variables:
		j = importar_video(videos[i])
		i += 1

	audios = ("audio1.mp3", "audio2.mp3", "audio3.mp3")
	variables_audio = []
	for aud in audios:
		variables_audio.append(importar_audio(aud))
	i = 0
	for j in variables_audio:
		j = importar_audio(audios[i])
		i += 1


	################# TEST LINE

	# clip1 = variables[0]
	# phone_proportions(clip1)

	# clip_final = unir(variables)

	# mute_clip(clip1)

	# cambiar_resolucion(clip1, 480, 480)

	# audio1 = variables_audio[0]

	# clip_final = unir_audio(variables_audio)

	# rotar_video(clip1, 180)
	# cambiar_velocidad(clip1, 2)

	# extraer_audio(clip1)

	# poner_audio(clip1, audio1)

	# produce_video(0.2)
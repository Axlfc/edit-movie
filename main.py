from moviepy.editor import *
import os

def write_video(videoclip, name):
	videoclip.write_videofile(name + '.mp4', fps=24)

def write_audio(audioclip, name):
	audioclip.write_audiofile(name + '.mp3')

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

def importar_video(videoclip):
	return VideoFileClip(videoclip)

def importar_audio(audioclip):
	return AudioFileClip(audioclip)

def get_resolution(videoclip):
	return videoclip.size

def get_height(videoclip):
	return videoclip.h

def get_width(videoclip):
	return videoclip.w

def get_duration(media):
	return media.duration

def get_orientation(videoclip):
	if get_width(videoclip) > get_height(videclip):
		return True
	else:
		return False

def unir(videoclips):
	write_video(concatenate_videoclips(videoclips), "unir")

def unir_audio(audioclips):
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

		write_audio(concatenate_audioclips(audioclips), "uniraudio")

def extraer_audio(videoclip):
	write_audio(videoclip.audio, "extract")

def mute_clip(videoclip):
	write_video(videoclip.without_audio(), "muted")

def poner_audio(videoclip, audioclip):
	new_audioclip = CompositeAudioClip([audioclip])
	videoclip.audio = new_audioclip
	write_video(videoclip, "new_sound")

def cambiar_resolucion(videoclip, wid, hei):
	write_video(videoclip.resize((wid, hei)), "resolucion")

def rotar_video(videoclip, angle):
	write_video(videoclip.rotate(angle), "rotado")

def cambiar_velocidad(videoclip, vel):
	write_video(videoclip.fx(vfx.speedx, vel), "rapido")

def phone_proportions(videoclip):
	write_video(videoclip.resize((1080, 1920)), "phone")


################# TODO LINE

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


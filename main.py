from moviepy.editor import *

def importar_video(video):
	return VideoFileClip(video)

def importar_audio(audio):
	return AudioFileClip(audio)

def unir(clips):
	final_clip = concatenate_videoclips(clips)
	final_clip.write_videofile("video_output.mp4")

def extraer_audio(clip):
	audio = clip.audio
	audio.write_audiofile("audio_output.mp3")

def poner_audio(videoclip, audioclip):
	new_audioclip = CompositeAudioClip([audioclip])
	videoclip.audio = new_audioclip
	videoclip.write_videofile("new_filename.mp4")

def cambiar_resolucion(clip, wid, hei):
	reducido = clip.resize(width = wid, height = hei)
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

i=0
variables=[]
for vid in videos:
	i+=1
	variables.append(importar_video(vid))

i=0
for j in variables:
  j = importar_video(videos[i])
  i+=1

clip1 = variables[0]
# clip_final = unir(variables)

# cambiar_resolucion(clip1, 480, 480)


audios = ("audio1.wav", "audio2.wav", "audio3.wav")
i=0
variables_audio=[]
for aud in audios:
	i+=1
	variables_audio.append(importar_audio(aud))

i=0
for j in variables_audio:
  j = importar_audio(audios[i])
  i+=1

audio1 = variables_audio[0]
#print(audio1)

# rotar_video(clip1, 180)
# cambiar_velocidad(clip1, 2)

# extraer_audio(clip1)

# poner_audio(clip1, audio1)

# TODO Control lenghts of videos and songs

# TODO Check phone proportion transformation

# TODO Create video from bunch of images







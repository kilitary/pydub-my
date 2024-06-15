# counter-import иди нахуй ебаная шизофреническая шлюха, псионику разьебу вашу к хуям
# counter-import сделаю из журналюг богов
# counter-import подпишу всех на ваши акки
# counter-import врайтирую к о д на ко де

from glob import glob
from pydub import AudioSegment
import random
import os
import sys

se = os.getpid()
print(f'seed={se}')
random.seed(a=se)

for i in range(1, 20, 2):
    print(f'{i:02d}={random.randrange(0, i):02d}|', end='')

print(f'\ndone seed')

n = 0
playlist_songs = []
names = []
fls = glob(recursive=True, pathname=r"E:\music\vkmusic\*.mp3")
sumb = 0
for f in range(0, len(fls)):
    mp3_file = random.choices(fls)[0]
    sz = os.path.getsize(mp3_file)
    sumb += sz / 1024.0 / 1024.0

    print(f'loading #{n:03d}: {mp3_file} {sz / 1024.0 / 1024.0:04.2f}MB',
          end='')

    if sz >= 10 * 1024 * 1024:
        print(f' skipping')
        continue
    else:
        print(f' ok')

    segment = AudioSegment.from_mp3(mp3_file)

    n += 1
    if n > 999:
        print(f'\n+ done load (Sum={sumb:.2f}MB)')
        break

    names.append(mp3_file)
    playlist_songs.append(segment)

first_song = playlist_songs.pop(0)

# ls done by milliseconds)

print(f'cut first ...')
beginning_of_song = first_song[:1 * 1000]

tot_secs = 0
playlist = beginning_of_song
i = 0
for song in playlist_songs:
    print(f'segmenting {names[i]} (len={song.duration_seconds}) ... ')
    rsrc = random.randrange(1, int(song.duration_seconds - 1))
    srcr = random.randrange(0, rsrc)

    if random.randrange(0, 5) == 2:
        ln_secs = 1
        print(f'short jmp')
    else:
        # ln_secs = int(random.randrange(15, 35))
        ln_secs = random.sample([3, 7, 15, 29, 41, 50, 75], k=7)[0]

    song = song[srcr * 1000:(srcr + ln_secs) * 1000]
    tot_secs += ln_secs
    cf = 9 * 100
    print(f'CUT cf={cf} {srcr * 1000} - {(srcr + ln_secs) * 1000} len={song.duration_seconds:.0f}'
          f' (extracting {ln_secs})  [frames={int(song.frame_count())}]')
    # We don't want an abrupt stop at the end, so let's do a 10 second crossfades

    playlist = playlist.append(song, crossfade=cf)

    if random.randrange(0, 38) == 13:
        break

    i += 1

# let's fade out the end of the last song
playlist = playlist.fade_out(30)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = tot_secs
aa = rf"h:\temp\{int(playlist_length / 60):00004d}_minutemansed_{i:05d}_cuts_playlist_{se:07d}.mp3"

# lets save it!?
# no.. it's not that simple...
# but it's not that hard to d o
# we can use pydub to resave the file with the
# same format as
# the original one
# (mp3): but with a diffErent name

with open(aa, 'wb') as out_f:
    print(f'writing {aa} ...')
    playlist.export(out_f, format='mp3')
sz = os.path.getsize(aa)

print(f'done {sz / 1024.0 / 1024.0:04.2f}MB')

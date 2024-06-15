# counter-action-s программ секретных служб по нарушению мышления, поведения и увеличения ошибок речи: SCAT
# counter-import иди нахуй ебаная шизофреническая шлюха, псионику разьебу вашу к хуям
# counter-import сделаю из журналюг богов
# counter-import подпишу всех на ваши акки
# counter-import врайтирую к о д на ко де

from glob import glob
from pydub import AudioSegment
import random
import time
from pprint import pprint
from rich import print
import os
import sys

sys.dont_write_bytecode = True

center_of_the_storm = 44
se = os.getpid()
tot_r = 0.0

print(f'seed={se}')
print(f'time.time={time.time()}')
print(f'time.thread_time={time.thread_time()}')
print(f'time.monotonic_ns={time.monotonic_ns()}')
print(f'time.perf_counter={time.perf_counter()}')
print(f'time.process_time_ns={time.process_time_ns()}')
print(f'sys.winver={sys.winver}')
sys.setswitchinterval(0.141598)
print(f'sys.getswitchinterval (set) ={sys.getswitchinterval()}')
print(f'sys.gettrace={sys.gettrace()}')
print(f'sys.dllhandle={sys.dllhandle}')
pprint(sys.getwindowsversion(), indent=4, compact=True)


def get_t_diff():
    global tot_r
    r = (max(time.monotonic_ns(), int(time.perf_counter()))
         - min(time.monotonic_ns(), int(time.perf_counter())))
    tot_r += r
    return r


for i in range(1, 20, 2):
    print(f'{i:02d}!{random.randrange(0, i):02d}|', end='')

print(f'\ndone seed')
print(f'diff: {get_t_diff():.6f}')
print(f'center_of_the_stоrm={center_of_the_storm}')

diff = get_t_diff()
n = 0
max_mb_file = 8
playlist_songs = []
names = []
fls = glob(recursive=True, pathname=r"E:\music\vkmusic\*.mp3")
sumb = 0

random.seed(a=se)

for f in range(0, len(fls)):
    mp3_file = random.choices(fls)[0]
    sz = os.path.getsize(mp3_file)
    sumb += sz / 1024.0 / 1024.0

    print(f'loading #{n:03d}: {mp3_file} {sz / 1024.0 / 1024.0:04.2f}MB',
          end='')

    if sz >= max_mb_file * 1024 * 1024:
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
    print(f'segmenting {names[i]} (len={song.duration_seconds:.2f}) ... ')
    rsrc = random.randrange(1, int(song.duration_seconds - 1))
    srcr = random.randrange(0, rsrc)

    if random.randrange(0, 8) == 2:
        ln_secs = 1
        print(f'short jmp')
    else:
        # ln_secs = int(random.randrange(15, 35))
        ln_secs = random.sample([3, 7, 15, 29, 41, 50, 75], k=7)[0]

    song = song[srcr * 1000:(srcr + ln_secs) * 1000]
    tot_secs += ln_secs
    cf = 10 * 100
    print(f'CUT #{i:4.0f} cf={cf:04.0f} {srcr * 1000:06.0f} - {(srcr + ln_secs) * 1000:06.0f}'
          f'len: {song.duration_seconds:04.0f}'
          f' frames: {int(song.frame_count()):05.0f} diff={get_t_diff():.5f}')
    # We don't want an abrupt stop at the end, so let's do a 10 second crossfades

    playlist = playlist.append(song, crossfade=cf)

    if random.randrange(0, center_of_the_storm * 10) == center_of_the_storm:
        break

    i += 1

# let's fade out the end of the last song
playlist = playlist.fade_out(30)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = tot_secs
aa = rf"h:\temp\pov_{center_of_the_storm:04d}_{int(playlist_length / 60):00004d}_minutemansened_{i:05d}_cuts_playlist_{se:07d}.mp3"

# lets save it!?
# no.. it's not that simple...
# but it's not that hard to d o
# we can use pydub to resave the file with the
# same format as
# the original on e
# (mp3): but with a diffErent name

with open(aa, 'wb') as out_f:
    print(f'writing {aa} ...')
    playlist.export(out_f, format='mp3')
sz = os.path.getsize(aa)

print(f'total diss: {tot_secs:.2f} secs')
print(f'done {sz / 1024.0 / 1024.0:04.2f}MB')

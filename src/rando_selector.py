from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from pydub.silence import detect_leading_silence
import sys
import os
import random
import shutil

count = int(sys.argv[1])
in_dir = sys.argv[2]
out_dir = sys.argv[3]
all_samples = list()

for root, dirs, files in os.walk(in_dir):
    for f in files:
        song_file = os.path.join(root, f)
        if f[-4:].lower() == ".wav":
            all_samples.append(song_file)

numbers = list()
x = 0
sample_max_len = len(all_samples)
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

while x < count:
    y = random.randrange(0, sample_max_len)
    if y not in numbers:
        # song_file_out = all_samples[y].replace(in_dir, out_dir)
        try:
            shutil.copy(all_samples[y], out_dir)
            x += 1
            numbers.append(x)
            print("Files processed: ", x)
        except Exception as err:
            print("Error processing: ", f, "\n\n\n")
            print(err)
            continue


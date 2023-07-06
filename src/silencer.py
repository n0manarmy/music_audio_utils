from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from pydub.silence import detect_leading_silence
import sys
import os

# song_file = sys.argv[1]
# out_dir = sys.argv[2]
# sample_len = sys.argv[3]

def main():
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    run(in_dir, out_dir)

def run(in_dir, out_dir):
    trim_leading_silence = lambda x: x[detect_leading_silence(x) :]
    trim_trailing_silence = lambda x: trim_leading_silence(x.reverse()).reverse()
    strip_silence = lambda x: trim_trailing_silence(trim_leading_silence(x))

    # dir_list = os.dirwalk(in_dir)
    files_processed = 0
    for root, dirs, files in os.walk(in_dir):
        for f in files:
            # if os.path.isfile(os.path.join(in_dir, files)):
            # print(f[-4:])
            if f[-4:].lower() == ".wav":
                song_file = os.path.join(root, f)
                song_file_out = song_file.replace(in_dir, out_dir)
                if not os.path.exists(song_file_out.replace(f, "")):
                    os.makedirs(song_file_out.replace(f, ""))
                # print(song_file.replace(in_dir, out_dir))
                try:
                    song = AudioSegment.from_wav(song_file)
                    stripped: AudioSegment = strip_silence(song)
                    stripped.export(song_file_out, format="wav")
                    files_processed += 1
                    if files_processed % 100 == 0:
                        print("Files processed: ", files_processed)
                except Exception as err:
                    print("Error processing: ", f, "\n\n\n")
                    print(err)
                    continue

                # print("Sample len: ", sample_len, " done.\n\n")

if __name__ == '__main__':
    main()
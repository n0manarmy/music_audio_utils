from pydub import AudioSegment, silence
import sys
import os
import argparse

# song_file = sys.argv[1]
# out_dir = sys.argv[2]
# sample_len = sys.argv[3]

SCALE = ["C7",
        "B6","A#6","A6","G#6","G6","F#6","F6","E6","D#6","D6","C#6","C6",
        "B5","A#5","A5","G#5","G5","F#5","F5","E5","D#5","D5","C#5","C5",
        "B4","A#4","A4","G#4","G4","F#4","F4","E4","D#4","D4","C#4","C4",
        "B3","A#3","A3","G#3","G3","F#3","F3","E3","D#3","D3","C#3","C3",
        "B2","A#2","A2","G#2","G2","F#2","F2","E2","D#2","D2","C#2","C2",
        "B1","A#1","A1","G#1","G1","F#1","F1","E1","D#1","D1","C#1","C1",
        "B0","A#0","A0","G#0","G0","F#0","F0","E0","D#0","D0","C#0","C0"]

def main(args):
    run(args.in_dir)

def run(in_dir):
    # dir_list = os.dirwalk(in_dir)
    for item in os.listdir(in_dir):
        if os.path.isfile(os.path.join(in_dir, item)):
            song_file = os.path.join(in_dir, item)
            sample_len = item.split(".")[0]
            full_out_path = os.path.join(in_dir, sample_len)
            # print(full_out_path)
            if not os.path.exists(full_out_path):
                os.makedirs(full_out_path)

            begin = 0
            SAMPLE_END = int(sample_len) * 1000
            song = AudioSegment.from_wav(song_file)

            for s in SCALE:
                temp = song[begin:begin + SAMPLE_END]
                # print(silence.detect_silence(temp, seek_step=1000))
                # print(s + ": ", begin, " - ", begin + SAMPLE_END, " - max_dBFS: ", temp.max_dBFS)
                if temp.max_dBFS > -130.0:
                    print(s + ": ", begin, " - ", begin + SAMPLE_END, " - max_dBFS: ", temp.max_dBFS)
                    # print("export: ", s)
                    temp.export(full_out_path + "\\" + s + ".wav", format="wav")

                begin += SAMPLE_END
            
            print("Sample len: ", sample_len, " done.\n\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Python Audio Utilies",
        description="Splits files based on count, tempo at 6 and then each note generates a seconds of wav")
    parser.add_argument('in_dir')
    
    args = parser.parse_args()
    main(args)
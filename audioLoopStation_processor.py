import os
import wave
import pyaudio


class AudioRecorder:
    def __init__(self):
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1,
                                      rate=44100, input=True, frames_per_buffer=512)

    def rec_chunk(self):
        data = self.stream.read(512)
        self.frames.append(data)

    def stop_recording(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def save_recording(self):
        exists = True
        i = 1
        while exists:
            if os.path.exists(f"recording{i}.wav"):
                i += 1
            else:
                exists = False

        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(self.frames))
        sound_file.close()


if __name__ == "__main__":

    recorder = AudioRecorder()
    try:
        while True:
            recorder.rec_chunk()
    except KeyboardInterrupt:
        pass
    recorder.stop_recording()
    recorder.save_recording()

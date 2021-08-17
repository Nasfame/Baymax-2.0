    import threading
    from ctypes import windll


    class WinPlayAudio():
        def __init__(self):
            self.alias = "A{}".format(id(self))
            self.audio_path = ""

        def _MCI_command(self, command):
            print(command)
            err = windll.winmm.mciSendStringW(command, 0, 0, 0)  # If printed, this returns 263 == unrecognized audio device
            print(err)

        def _play(self, start=0, wait=True):
            th = threading.Thread(target=self.__play__, args=(start, wait))
            th.start()

        def __play__(self, start, wait):
            self._MCI_command(f'play {self.audio_path} from {start} {"wait" if wait else ""}', )

        def _open_song(self, audio_path):
            self.audio_path = audio_path
            self._MCI_command(f'open {audio_path} alias {self.alias}')

        def _set_volume(self):
            self._MCI_command(f'setaudio {self.alias} volume to 500')

        def _pause(self):
            self._MCI_command(f'pause {self.alias}')

        def _resume(self):
            self._MCI_command(f'resume {self.alias}')

        def _stop(self):
            self._MCI_command(f'stop {self.alias}')


    if __name__ == '__main__':
        p = WinPlayAudio()
        p._open_song("start.mp3")
        p._play()

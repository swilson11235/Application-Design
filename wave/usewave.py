__author__= "Stephen"
__version__="1.0"

from Wave_pkg import Wave
def main():
    '''Uses the Wave class.'''
    test_wave = Wave("Wave_pkg/test4.wav")
    test_wave.getnchans()
    test_wave.getsampwidth()
    test_wave.getframerate()
    test_wave.getnframes()
    test_wave.getmaxframe()
    test_wave.chipmunkify(1)
    test_wave.changevol(1)
    test_wave.normalizevol()
    test_wave.echo(.3,22000)

    try:
        freq = raw_input('What hertz frequency do you want?\n')
        freq = int(freq)
    except:
        raise ValueError
    sine_wave = test_wave.create_sine_wave(8000,freq,1.5)
    sine_wave.save("sine.wav")
    sq_wave = test_wave.create_square_wave(8000,freq,1.5)
    new_wave = test_wave + sine_wave
    sq_wave.save("sq.wav")
    test_wave.save()
if __name__=='__main__':
    main()

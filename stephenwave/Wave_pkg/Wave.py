'''This class processes wave files. It can change the volume, normalize the volume, and change the pitch. Certain parameters can be edited individually.
Resulting wave files can be saved.'''

__author__ = 'Stephen'
__version__ = '2.0'

import wave
import struct, math

class Wave():
    def __init__(self, filename=''):
        '''Initializes the wave file into the wave class.'''
        if filename!='':
            self.my_wave = wave.open(filename, 'r')
            self.nchannels = self.my_wave.getnchannels()
            self.sampwidth = self.my_wave.getsampwidth()
            self.framerate = self.my_wave.getframerate()
            self.nframes = self.my_wave.getnframes()
            self.frames = self.unpackframes()
            self.comptype=self.my_wave.getcomptype()
            self.compname=self.my_wave.getcompname()
            self.my_wave.close()
        else:
            self.nchannels=1
            self.sampwidth=2
            self.framerate=44100
            self.nframes=0
            self.frames=[]
            self.comptype = 'NONE'
            self.compname = 'not compressed'
    def unpackframes(self):
        '''Unpacks frames for the __int__ function'''
        bytes =[]
        for i in range(0, self.nframes):
            my_byte = self.my_wave.readframes(1)
            var,=struct.unpack("<h",my_byte)
            bytes.append(var)
        return bytes
    def __add__(self, your_wave):
        if your_wave.getnframes() > self.nframes:
            wavetoadd = self
            longwave = your_wave
        else:
            wavetoadd = your_wave
            longwave = self
        for i in range(0,wavetoadd.getnframes()):
            longwave.frames[i] += wavetoadd.frames[i]
        longwave.setnframes(len(longwave))
        longwave.normalizevol()
        longwave.save("new_wave.wav")
        return longwave
    def __len__(self):
        '''Returns the number of frames.'''
        return len(self.frames)
    def __str__(self):
        '''Returns a string representation of the class (the frames, in other words data, are in a string).'''
        return str(self.frames)
    def __getitem__(self,index):
        '''Defines the default getitem function.'''
        return self.frames[index]
    def __setitem__(self, index, value):
        '''Defines the default setitem function.'''
        self.frames[index] = value
    def append(self,value):
        '''Appends a single value to the frames.'''
        self.frames.append(value)
    def __getslice__(self,index1,index2):
        '''Defines the default getslice function.'''
        return self.frames[index1:index2]
    def create_sine_wave(self,amplitude,hertz_frequency,duration):
        '''Amplitude controls the volume of the generated sound,
           frequency controls the pitch of the generated sound, and
           duration defines how many seconds the sound lasts. 
           The function outputs a Wave object that contains the waveform.'''
        new_wave = Wave()
        new_wave.setnframes(int(duration*new_wave.getframerate()))
        for i in range(0, new_wave.getnframes()):
            new_wave.append(amplitude*math.sin(i*hertz_frequency*2*math.pi/new_wave.getframerate()))
        return new_wave
    def create_square_wave(self,amplitude,hertz_frequency,duration):
        '''Amplitude controls the volume of the generated sound,
           frequency controls the pitch of the generated sound, and
           duration defines how many seconds the sound lasts. 
           The function outputs a Wave object that contains the waveform.'''
        new_wave = Wave()
        new_wave.setnframes(int(duration*new_wave.getframerate()))
        for i in range(0, new_wave.getnframes()):
            if math.sin(i*hertz_frequency*2*math.pi/new_wave.getframerate()) > 0:
                new_wave.append(amplitude)
            elif math.sin(i*hertz_frequency*2*math.pi/new_wave.getframerate()) ==0:
                new_wave.append(0)
            else:
                new_wave.append(-amplitude)
        return new_wave
    def getnchans(self):
        '''Returns the number of channels.'''
        return self.nchannels
    def getsampwidth(self):
        '''Returns the sample width.'''
        return self.sampwidth
    def getframerate(self):
        '''Returns the framerate.'''
        return self.framerate
    def getnframes(self):
        '''Returns the number of frames.'''
        return self.nframes
    def getframes(self,a,b):
        '''Returns a list of the frames from a to b (frames[a:b]).'''
        return self.frames[a:b]
    def getmaxframe(self):
        '''Returns the max value in the frames.'''
        biggest_index = 0
        for i in range(0, self.nframes):
            if abs(self.frames[i]) > abs(self.frames[biggest_index]):
                biggest_index = i
        return abs(self.frames[biggest_index] )
    def setframerate(self, val):
        '''Allows manual setting of the framerate. The framerate is replaced with the value given.'''
        self.framerate = val
    def setsampwidth(self,val):
        '''Sets the sampwidth.'''
        self.sampwidth = val
    def setnframes(self,val):
        '''Sets the number of frames.'''
        self.nframes = val
    def echo(self, decay, delay):
        '''Creates an echo effect for the sample. Decay should be a decimal. delay should be a number of frames on which to echo.'''
        for i in range(delay, len(self.frames)):
            decay*=0.99999
            self.frames[i]+=self.frames[i-delay] *decay
    def changevol(self,percent):
        '''Changes the volume of the file according to a percent. Percent in decimal foramt.'''
        if (self.getmaxframe()*1)<(2**15):
            for i in range(0, len(self.frames)):
                self.frames[i]*=percent
        else:
            raise ValueError
    def chipmunkify(self,percent):
        '''Changes pitch. Values over 1 increase pitch (chipmunkify the file), values less than one decrease pitch (dechipmunkify the file). All percent values are in decimals.'''
        self.framerate *= percent
        return self.framerate
    def normalizevol(self):
	'''Normalizes the volume.'''
        ratio = (float(2**15-1) / self.getmaxframe())
        for i in range(0, self.nframes):
            self.frames[i]*=ratio
    def save(self, filename="modifiedwave.wav"):
        '''Saves the wave file in "modifiedwave.wav" by default.'''
        wavefile = wave.open(filename, "w")
        wavefile.setparams((self.nchannels, self.sampwidth, self.framerate, self.nframes, self.comptype, self.compname))
        wavefile.writeframes(self.packframes())
        wavefile.close()
    def packframes(self):
        '''Is called by the save function.'''
        bytes=''
        for i in range(0, self.nframes):
            my_byte = self.frames[i]
            bytes+=struct.pack("<h",my_byte)
        return bytes


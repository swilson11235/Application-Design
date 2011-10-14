'''This class tests the Wave class.'''

__author__ = 'Stephen'
__version__ = '1.0'

from Wave import Wave
import unittest
import math
my_wave = Wave("Wave_pkg/test3.wav")

class test_Wave(unittest.TestCase):
    def set_up(self):
        '''No set-up.'''
        pass
    def test_setframerate(self):
        '''This function tests the setframerate function by assigning a framerate.'''
        my_frate=my_wave.getframerate()
        my_wave.setframerate(my_frate+2000)
        self.assertGreater(my_wave.getframerate(),my_frate)
        my_wave.setframerate(44100)
    def test_setnframes(self):
        '''This function tests the setnframes function by assigning a number of frames.'''
        my_nframes=my_wave.getnframes()
        my_wave.setnframes(my_nframes+2000)
        self.assertGreater(my_wave.getnframes(),my_nframes)
        my_wave.setnframes(my_nframes-2000)
    def test_setsampwifth(self):
        '''This function tests the sampwidth function by assigning a sampwidth.'''
        my_sampwidth=my_wave.getsampwidth()
        my_wave.setsampwidth(my_sampwidth+2)
        self.assertGreater(my_wave.getsampwidth(),my_sampwidth)
        my_wave.setframerate(my_sampwidth-2)
    def test_changevol(self):
        '''Tests the change volume function.'''
        init=my_wave.getframes(0,1)
        my_wave.changevol(.5)
        fin = my_wave.getframes(0,1)
        self.assertTrue((init[0]*.5)==fin[0])
    def test_chipmunkify(self):
        '''Tests the change pitch function.'''
        init = my_wave.getframerate()
        my_wave.chipmunkify(.5)
        fin =my_wave.getframerate()
        self.assertTrue((init*.5)==fin)
    def test_normalizevol(self):
        '''Tests the normalizing volume function.'''
        init = my_wave.getframes(0,1)
        maxf = my_wave.getmaxframe()
        my_wave.normalizevol()
        fin = my_wave.getframes(0,1)
        ratio =float(2**15-1)/maxf
        init2 =(init[0]*ratio)
        self.assertTrue(init2==fin[0])
    def test_echo(self):
        '''Tests the echo function.'''
        init = my_wave.getframes(22150,22151)
        my_wave.echo (.2,22050)
        fin = my_wave.getframes(22150,22151)
        tmp = (init[0] + my_wave.getframes(100,101)[0]*.2*.99999**101)
        self.assertAlmostEqual(tmp, fin[0])
    def test_sine_wave(self):
        my_sine = my_wave.create_sine_wave(800, 800,3)
        frameperosc= my_sine.getframerate()/800
        self.assertEqual(round(my_sine[100],-1),round(my_sine[100+frameperosc],-1)) 
        self.assertEqual(my_sine.getnframes(),3*my_sine.getframerate())
    def tear_down(self):
        '''No tear down.'''
        pass

if __name__ == '__main__':
    unittest.main()

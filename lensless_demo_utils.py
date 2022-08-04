import numpy as np
from numpy import fft
from IPython import display
import time
from numpy.fft import fft2
from numpy.fft import ifft2
from numpy.fft import fftshift
from numpy.fft import ifftshift

def im_downsample(x,N):
    for k in range(N):
         x = (x[1::2,1::2] + x[::2,::2] + x[1::2,::2] + x[::2,1::2])/4
    return x

def fft_conv(x,y): 
    return np.real(fft.ifft2(fft.fft2(fft.ifftshift(y)) * fft.fft2(x)))

def create_impulse(siz, shift):
    delta = np.zeros(siz)
    delta[siz[0]//2-shift[0], siz[1]//2-shift[1]] = 1
    return delta

def drawnow(fig):
    display.display(fig)
    display.clear_output(wait=True)
    time.sleep(.01)
    
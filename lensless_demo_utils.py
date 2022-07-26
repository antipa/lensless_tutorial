import numpy as np

def im_downsample(x,N):
    for k in range(N):
         x = (x[1::2,1::2] + x[::2,::2] + x[1::2,::2] + x[::2,1::2])/4
    return x

def fft_conv(x,y): 
    return np.real(np.ifft2(np.fft2(np.ifftshift(y)) * np.fft2(x)))

def create_impulse(siz, shift):
    delta = np.zeros(siz)
    delta[siz[0]//2-shift[0], siz[1]//2-shift[1]] = 1
    return delta

def drawnow(fig):
    display.display(fig)
    display.clear_output(wait=True)
    time.sleep(.01)
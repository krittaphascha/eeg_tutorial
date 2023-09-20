import numpy as np
import matplotlib.pyplot as plt

def plot_signal(signal, sampling_rate=64):
    
    # initialize parameters
    time = np.arange(0, len(signal)/sampling_rate, 1/sampling_rate)
    points = len(time)
    hz = np.linspace(0, sampling_rate/2, int(np.floor(points/2)+1))
    

    ax1= plt.subplot(211)
    ax1.plot(time, signal, 'b')
    ax1.set_title('Normally distributed: Time domain')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')

    ax2 = plt.subplot(223)
    y, x = np.histogram(signal, bins=100)
    ax2.plot(x[1:], y, 'k')
    ax2.set_title('Signal histogram (distribution)')
    ax2.set_xlabel('Values')
    ax2.set_ylabel('N per bin')

    ax3 = plt.subplot(224)
    amp = np.abs(np.fft.fft(signal)/points)
    amp[2:] = 2*amp[2:]
    ax3.plot(hz, amp[:len(hz)], 'r')
    ax3.set_title('Frequency domain')
    ax3.set_xlabel('Frequency (Hz)')
    ax3.set_ylabel('Amplitude')

    plt.show()
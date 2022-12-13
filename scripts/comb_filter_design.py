from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fs = 16000.
    f0 = 1000.
    Q = 5.

    # Notching comb filter
    b, a = signal.iircomb(f0, Q, ftype='notch', fs=fs)

    # plot frequency response
    freq, h = signal.freqz(b, a, fs=fs)
    response = abs(h)
    # To avoid divide by zero when graphing
    response[response == 0] = 1e-20

    # Plot
    fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    ax[0].plot(freq, 20*np.log10(abs(response)), color='blue')
    ax[0].set_title("Frequency Response")
    ax[0].set_ylabel("Amplitude (dB)", color='blue')
    ax[0].set_xlim([0, 100])
    ax[0].set_ylim([-40, 10])
    ax[0].grid(True)
    ax[1].plot(freq, (np.angle(h)*180/np.pi+180)%360 - 180, color='green')
    ax[1].set_ylabel("Angle (degrees)", color='green')
    ax[1].set_xlabel("Frequency (Hz)")
    ax[1].set_xlim([0, fs/2])
    ax[1].set_yticks([-90, -60, -30, 0, 30, 60, 90])
    ax[1].set_ylim([-90, 90])
    ax[1].grid(True)
    plt.show()

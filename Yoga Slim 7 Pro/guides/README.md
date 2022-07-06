# Slim 7 Pro Guides

This READme describes different caveats you might encounter while trying to make everything work on your laptop. I will document everything I know so far with all the symptoms of the problems, solution and debug proccess.

Overview:

-   [Slim 7 Pro Guides](#slim-7-pro-guides)
    -   [KDE Plasma GPU Acceleration](#kde-plasma-gpu-acceleration)
    -   [BlueZ LDAC Sound](#bluez-ldac-sound)

## KDE Plasma GPU Acceleration

You may encounter a few problems during the installation of KDE Plasma (or probably any GPU-involved stuff in general). It seems that Gentoo does not pull in Xorg drivers for your GPU when you install X server so you have to do it yourself to get hardware acceleration. Otherwise, you will notice stutters, freezes and system will be unusable when emerging stuff.

If you get any of those symptoms, double check:

```console
## emerge x11-apps/mesa-progs
## then run the following

$ glxinfo | grep -i renderer
...
OpenGL renderer string: AMD RENOIR (LLVM 14.0.6, DRM 3.46, 5.18.9-gentoosqd)
```

If glxinfo says something like `llvmpipe` as OpenGL renderer, you don't have GPU drivers installed. Emerge the following package:

```console
$ emerge -avD x11-drivers/xf86-video-amdgpu
```

After all, reboot the system and everything shoud work now!

Also, do not forget to include GPU drivers in kernel: for AMDGPU, build it as module to avoid early firmware loading, which you will then have to [encorporate](https://wiki.gentoo.org/wiki/AMDGPU#Incorporating_firmware) into kernel to avoid it failing to boot.

## BlueZ LDAC Sound

Having my Sony WH1000-XM4, I noticed awful sound quality using standard PulseAudio BlueZ profile (HSP/HFP, Codec mSBC). I started investigating and wasn;t able to fix the issue for PulseAudio. So I then switched to PipeWire and everything worked pretty much out-of-the-box.

Follow this [Wiki guide](https://wiki.gentoo.org/wiki/PipeWire) to install and replace PulseAudio with PipeWire.

# Slim 7 Pro's kernel

## What is the python script for?

Python script `build_kernel.py` is used to build kernel. It acts similar to Gentoo's genkernel, but is faster, more flexible and uses Dracut for ramdisk generation.

### How to use it?

First of all, as a precaution, you should observe what the Python script does. Because originally, kernel is intended to be configured and built as a root user, the script requires you to launch is as one. If something's off, it can cause severe damage to your system and security, so do this on your own risk.

But seriously, it's not all that scary. Basically, the script goes into `/usr/scr/linux` - a default symlink for currently eselected kernel. It creates a log directory in `/tmp` and store all progress in there. Text output is printed so you can see what's going on, as well as current process execution output (like _make_'s output when building the actual kernel).

The script pretty much does everything you should have: allows you to configure the kernel (nconfig), builds it, installs modules and kernel itself and build initramfs with Dracut (config file provided here too).

You can even make it a system-wide script like that:

```bash
ln -s build_kernel.py /usr/bin/build-kernel

# execute as root
doas build-kernel
```

## Kernel configuration

Pretty solid config is provided here as `.config`. It includes all the drivers you might need (check yourself and edit is something's missing), features great performance and is debloated as much as I could do it.

To make things work, copy `dracut.conf` to `/etc/dracut.conf` and load kernel `.config` during nconfig menu configuration.

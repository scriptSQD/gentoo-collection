# Lenovo Yoga Slim 7 Pro

## What is the device?

Lenovo Yoga Slim 7 Pro is my first personal laptop. I've been messing around with it for a while now, and I'm happy to say that it's working well. As of now, it dual-boots Windows 11 Pro and Gentoo on OpenRC with custom kernel.

At first, I had some problems with GPU acceleration, but I managed to get it working again. I'm running KDE Plasma on Wayland. My kernel build toolchain is Clang 14.0 from Gentoo Ebuild repos, it's paired with ThinLTO and full LLVM set of tools.

My disk partitioning:
| Device | Size | Filesystem | Mountpoint |
|:-------|:------|:-----------|:-----------|
| `/dev/nvme0n1p1` | 512M | vfat | `/boot` |
| `/dev/nvme0n1p2` | 488G | btrfs | `/` |
| `/dev/nvme0n1p3` | 32G | swap | `swap` |

## What is this repo for?

I will be storing different configuration files, step-by-step guides and other stuff here.

`shell/` directory contains everything related to Zsh and Kitty - my choice for a shell and terminal emulator on the laptop. Additional info is inside `shell/README.md`.

# Slim 7 Pro's portage configuration

## How to use?

Simply put all the folder's contents to `/etc/portage/` on your machine.

Consider doing that in the beginning, as the provided USE flags require most of the software to be rebuilt. You probably don't wanna spend a few hours just compiling stuff over and over again.

## Packages to install in the first place

You shall install these packages to be able to work with Gentoo outside of the installation medium (this does not include Xorg server stuff, desktop env, etc.):

| Package                   | Description                                                     | Specific USE flags                                                                                                      |
| :------------------------ | :-------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| `net-misc/networkmanager` | Network management software                                     | `iwd`                                                                                                                   |
| `net-misc/iwd`            | Wireless driver backend                                         | -                                                                                                                       |
| `net-misc/dhcpcd`         | DHCP client                                                     | -                                                                                                                       |
| `app-admin/doas`          | Allows to run commands as root user (can be replaced with sudo) | [persist](https://www.reddit.com/r/Gentoo/comments/p3f12p/comment/h8r2g6j/?utm_source=share&utm_medium=web2x&context=3) |
| `app-shells/zsh`          | Powerful system shell                                           | -                                                                                                                       |
| `dev-vcs/git`             | Be able to communicate with Git repositories                    | -                                                                                                                       |
| `vim` / `nvim` / `nano`   | Your favorite text editor                                       | -                                                                                                                       |

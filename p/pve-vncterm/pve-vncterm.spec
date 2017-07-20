%define sname vncterm

Name: pve-%sname
Summary: VNC Terminal Emulator
Version: 1.5.2
Release: alt1
License: GPLv2
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %sname.tar.xz
Source1: wchardata.c
Source2: unifont.hex
Patch0: %sname-alt.patch

BuildRequires: libgnutls-devel libjpeg-devel perl-Pod-Usage zlib-devel libpng-devel

%description
With vncterm you can start commands and export its standard input and
output to any VNC client (simulating a xterm Terminal).

%prep
%setup -q -n %sname
%patch0 -p1

install -m0644 %SOURCE1 .
install -m0644 %SOURCE2 .

%build
%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/%sname
%_datadir/%sname
%_man1dir/%sname.1*

%changelog
* Tue Jul 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.2-alt1
- 1.5-2

* Mon Mar 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release


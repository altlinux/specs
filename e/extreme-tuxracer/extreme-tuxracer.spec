%define binname etracer
%define tarballname extremetuxracer

Name: extreme-tuxracer
Version: 0.4
Serial: 1
Release: alt0.2.1

License: GPL
Group: Games/Arcade
Url: http://www.extremetuxracer.com

Packager: Alex Karpov <karpov@altlinux.ru>

Summary: Another fork of legendary TuxRacer game

Source: %tarballname-%version.tar.gz

Obsoletes: %name <= 0.35

## Automatically added by buildreq on Mon Oct 01 2007
##BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel libfreetype-devel libmesa-devel libpng-devel libtcl tcl-devel

# Automatically added by buildreq on Mon Sep 15 2008
BuildRequires: gcc-c++ imake libX11-devel libXext-devel libGL-devel libSDL-devel libSDL_mixer-devel libXi-devel libXmu-devel libfreetype-devel libpng-devel tcl-devel xorg-cf-files

%description
Extreme Tux Racer is an open source racing game featuring 
Tux the Linux Penguin. ETRacer continues in the tracks of Tux Racer 
and its forks.

%prep
%setup -qn %tarballname-%version

%build
%ifarch x86_64
%configure --enable-debug --with-tcl=/usr/lib64
%else
%configure --enable-debug
%endif
%make_build

%install
mkdir %buildroot
%make_install DESTDIR=%buildroot install


%files
%_bindir/%binname
%_datadir/%binname/

%changelog
* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4-alt0.2.1
- NMU:
  * updated build dependencies

* Mon Sep 15 2008 Alex Karpov <karpov@altlinux.ru> 1:0.4-alt0.2
- updated biuld requirements

* Tue Mar 18 2008 Alex Karpov <karpov@altlinux.ru> 1:0.4-alt0.1
- 0.4

* Thu Oct 04 2007 Alex Karpov <karpov@altlinux.ru> 0.35-alt0.1
- try to fix x86_64 build

* Mon Oct 01 2007 Alex Karpov <karpov@altlinux.ru> 0.35-alt0
- initial build for Sisyphus


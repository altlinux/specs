%define binname etracer
#define tarballname extreme-tuxracer
%define status svn254

Name: extreme-tuxracer
Version: 0.5
Serial: 1
Release: alt0.%status.1

License: GPL
Group: Games/Arcade
Url: http://www.extremetuxracer.com

Packager: Alex Karpov <karpov@altlinux.ru>

Summary: Another fork of legendary TuxRacer game

Source: %name-%version%status.tar.gz

Obsoletes: %name <= 0.35

# Automatically added by buildreq on Fri May 14 2010
BuildRequires: gcc-c++ imake libGL-devel libSDL_mixer-devel libXext-devel libXi-devel libXmu-devel libfreetype-devel libpng-devel tcl-devel xorg-cf-files

%description
Extreme Tux Racer is an open source racing game featuring 
Tux the Linux Penguin. ETRacer continues in the tracks of Tux Racer 
and its forks.

%prep
%setup -qn %name-%version%status

%build
#./autogen.sh
%autoreconf
%ifarch x86_64
%configure --enable-debug --with-tcl-inc=/usr/include/tcl/generic --with-tcl=/usr/lib64
%else
%configure --enable-debug --with-tcl-inc=/usr/include/tcl/generic --with-data-dir=/usr/share/etracer --enable-debug
%endif
%make_build

%install
mkdir %buildroot
%make_install DESTDIR=%buildroot install

%find_lang %binname

%files -f %binname.lang
%_bindir/%binname
%_datadir/%binname/

%changelog
* Thu Sep 20 2012 Alex Karpov <karpov@altlinux.ru> 1:0.5-alt0.svn254.1
- last snapshot
    + rebuild with libpng15

* Fri May 14 2010 Alex Karpov <karpov@altlinux.ru> 1:0.5-alt0.svn197.1
- 8 month old bleeding edge svn snapshot, don't be afraid - it's playable

* Fri Feb 27 2009 Alex Karpov <karpov@altlinux.ru> 1:0.5-alt0.beta.1
- new beta

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


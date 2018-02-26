Name: tvtime
Version: 1.0.2
Release: alt12

Summary: A high quality TV application
License: GPL
Group: Video

Url: http://tvtime.sourceforge.net
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.gz
Source2: %name-README.ALT
Source3: tvtime-1.0.2-icons.tar.bz2
Source4: tvtime.desktop

Patch0: tvtime-1.0.2-alt-tango.patch
Patch1: tvtime-1.0.2-alt-kernheaders.patch
Patch2: tvtime-1.0.2-alt-locale_t.patch
Patch3: tvtime-1.0.2-alt-confdir.patch

Patch100: tvtime-1.0.1-gcc4.1.patch
Patch101: tvtime-1.0.2-videoinput.patch
Patch102: tvtime-1.0.1-fsbadval.patch
Patch103: tvtime-1.0.1-header.patch

Patch200: tvtime-1.0.2-alsamixer.patch
Patch201: tvtime-1.0.2-alsamixer2.patch

Patch300: tvtime-1.0.2-alt-xss.patch
Patch301: tvtime-1.0.2-alt-drop-freefont.patch

BuildRequires: gcc-c++ libSM-devel libXScrnSaver-devel libXinerama-devel libXtst-devel libXv-devel
BuildRequires: libXxf86vm-devel libalsa-devel libfreetype-devel libpng-devel libxml2-devel

%description
tvtime is a high quality television application for use with video capture
cards. tvtime processes the input from a capture card and displays it on a
computer monitor or projector.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

%patch200 -p1
%patch201 -p1

%patch300 -p1
%patch301 -p1

tar -xjf %SOURCE3

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m644 %SOURCE2 README.ALT
install -m644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
ln -sf ../fonts/ttf/liberation/LiberationSans-Bold.ttf %buildroot%_datadir/%name/tvtimeSansBold.ttf

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README* docs/html
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*
%_datadir/%name
%_datadir/pixmaps/%name.*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*.1*
%_man5dir/*.5*

%changelog
* Sun Apr 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt12
- removed freefont

* Tue Apr 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt11
- used XScreenSaverExtension instead of typing text via Xtest (closes: #23353)

* Sun Apr 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt10
- fixed build for latest xorg

* Thu Aug 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt9
- added ALSA mixer support

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt8
- rebuild with libpng12 1.2.37-alt2

* Wed May 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt7
- fixed build with gcc4.4

* Sun Dec 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt6
- VIDIOC_DQBUF called without setting cur_buf.memory

* Tue Oct 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt5
- use videodev.h and videodev2.h from glibc-kernheaders

* Wed Sep 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt4
- fixed menu categories (close #12826)

* Wed Apr 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt3
- fixed xpm icon

* Tue Apr 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- added Tango icons by defaults

* Sat May 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue May 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- Fixed build with gcc-4.1.0

* Sun Feb 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- updated url
- removed debian menu
- updated build dependencies

* Fri Nov 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Thu Dec 16 2004 Grigory Milev <week@altlinux.ru> 0.9.12-alt2.1
- rebuilded with new directfb

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 0.9.12-alt2
- build fix

* Sat Nov 22 2003 Michael Shigorin <mike@altlinux.ru> 0.9.12-alt1
- 0.9.12 (minor bugfixes)

* Mon Nov 17 2003 Michael Shigorin <mike@altlinux.ru> 0.9.11-alt2
- fixed icon installation (s/32x32/48x48/)

* Fri Nov 14 2003 Michael Shigorin <mike@altlinux.ru> 0.9.11-alt1
- 0.9.11
- /var/run stuff removed (FIFOs moved to /tmp for the moment)
- examples shifted into HTML docs; BUGS removed

* Thu Oct 09 2003 Alexander Belov <asbel@altlinux.ru> 0.9.10cvs20031009-alt1
- Make new package from cvs for testing my ru.po
- Removing kernel-headers-std >=2.4.22 BuildRequires for compile on my 
  computer with kernel-headers-std-smp-2.4.22-alt5

* Tue Sep 23 2003 Michael Shigorin <mike@altlinux.ru> 0.9.10-alt2
- further fixes/suggestions by Billy Biggs (were supposed for alt1
  but somehow missed on that):
  * Url
  * BuildRequires
  * menu entry
  * pixmap installation
  * freedesktop files and icons
  * /var/run/tvtime
- still need to package libdscaler separately; see also README.ALT
- spec cleanup

* Mon Sep 15 2003 Michael Shigorin <mike@altlinux.ru> 0.9.10-alt1
- 0.9.10
- implemented fixes/suggestions from tvtime author,
  Billy Biggs <vektor dumbterm.net>
- fixed typo in tvtime.control (s/netadmin/audio/g)

* Thu Sep 11 2003 Michael Shigorin <mike@altlinux.ru> 0.9.9-alt2
- built for Sisyphus
- based on package by Valery Inozemtsev <shrek@progroup.ru>
  (in its turn, based on one from Dag Apt Repository,
  http://dag.wieers.com/apt)
- spec cleanup
- control(8) support
- call %%update_menus/%%clean_menus

* Mon Sep 8 2003 Valery Inozemtsev <shrek@progroup.ru> - 0.9.9-alt1
- build for ALTLinux

* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 0.9.9-0
- Updated to release 0.9.9.

* Sat Jun 21 2003 Dag Wieers <dag@wieers.com> - 0.9.8.5-0
- Initial package. (using DAR)


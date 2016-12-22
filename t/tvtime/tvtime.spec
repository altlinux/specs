Name: tvtime
Version: 1.0.11
Release: alt1

Summary: A high quality TV viewer
License: GPLv2+ and LGPLv2+
Group: Video

Url: http://tvtime.net
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: http://linuxtv.org/downloads/%name/%name-%version.tar.gz
Source1: tvtime.watch
Source3: tvtime-1.0.2-icons.tar.bz2
Source4: tvtime.desktop

Patch0: tvtime-1.0.2-alt-tango.patch
Patch3: tvtime-1.0.8-alt-confdir.patch
Patch301: tvtime-1.0.2-alt-drop-freefont.patch

# Automatically added by buildreq on Fri Oct 30 2015
# optimized out: libICE-devel libX11-devel libXext-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel xz zlib-devel
BuildRequires: gcc-c++ libSM-devel libXScrnSaver-devel libXinerama-devel libXv-devel libXxf86vm-devel libalsa-devel libfreetype-devel libpng-devel libxml2-devel

Requires: fonts-ttf-freefont

%description
tvtime is a high quality television application for use with
video capture cards. tvtime processes the input from a capture
card and displays it on a computer monitor or projector.

%prep
%setup
%patch0 -p1
%patch3 -p1
%patch301 -p1
tar xf %SOURCE3

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pm644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
ln -sf ../fonts/ttf/liberation/LiberationSans-Bold.ttf \
	%buildroot%_datadir/%name/tvtimeSansBold.ttf
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README docs/html
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*
%_datadir/%name
#_datadir/pixmaps/%name.*
%_datadir/appdata/tvtime.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*.1*
%_man5dir/*.5*
%_mandir/*/man?/*.*

%changelog
* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- new version (watch file uupdate)

* Sat Mar 05 2016 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- new version (watch file uupdate)
  + dropped pixmap
  + added appdata

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 1.0.8-alt1
- 1.0.8
- updated source url
- dropped patches 2, 100, 101, 102, 103, 200, 201, 300, 400
  (fixed/merged upstream)
- dropped patch401 (v4l1 is gone)
- updated patch3
- dropped README.ALT (obsolete)
- added translated manpages
- added watch file
- buildreq

* Mon Feb 04 2013 Michael Shigorin <mike@altlinux.org> 1.0.2-alt13
- fixed FTBFS
  + added a few patches from gentoo, vectorlinux

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


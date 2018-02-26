%define xf86 XFree86

Name: xorg
Version: 7.6.0
Release: alt3
Summary: Part of the X.Org implementation of the X Window System
Group: System/X11
License: MIT/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildArch: noarch
Requires: %name-libs %name-utils %name-apps xauth xfs fonts-type1-xorg
Requires: %name-drv-input xorg-drv-multimedia %name-drv-video
Obsoletes: %xf86 xorg-x11
Provides: %xf86 = 4.4 xorg-x11 = %version-%release

%description
If you want to install the X Window System (TM) on
your machine, you'll need to install X.Org.

The X Window System provides the base technology
for developing graphical user interfaces. Simply stated,
X draws the elements of the GUI on the user's screen and
builds methods for sending user interactions back to the
application. X also supports remote application deployment-running an
application on another computer while viewing the input/output
on your machine.  X is a powerful environment which supports
many different applications, such as games, programming tools,
graphics programs, text editors, etc.  X.Org is the version of
X which runs on Linux, as well as other platforms.

This package contains the basic fonts, programs and documentation
for an X workstation.  However, this package doesn't provide the
program which you will need to drive your video hardware.  To
control your video card, you'll need the particular X server
package which corresponds to your computer's video card.

In addition to installing this package, you will need to install
the X.Org package which corresponds to your video card, the
Xconfigurator package and the xorg-libs package. You may also
need to install one of the X.Org fonts packages.

And finally, if you are going to develop applications that run as
X clients, you will also need to install xorg-devel.

%package libs
Summary: Requires shared libraries needed by the X Window System
Group: System/Libraries
Provides: %xf86-libs = 4.4 xorg-x11-libs = %version-%release
Obsoletes: %xf86-libs xorg-x11-libs
Requires: libICE libSM libX11 libXau libXaw libXdmcp libXext libXfont libXft
Requires: libXi libXmu libXpm libXrender libXres libXt libXtst
Requires: libXxf86dga libXxf86vm libdmx libfontenc libxkbfile libXScrnSaver
Requires: libXcomposite libXdamage libXrandr libXcursor

%description libs
This package requires the shared libraries that most X programs
need to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a machine
without an X server (i.e, over a network)

%package locales
Summary: Xorg locales
Group: System/Internationalization
Obsoletes: %xf86-locales xorg-x11-locales
Provides: %xf86-locales = 4.4 xorg-x11-locales = %version-%release
Requires: libX11-locales

%description locales
This package contains set of Xorg locales

%package mesagl
Summary: OpenGL compatible 3D graphics library for X Window server
Group: System/Libraries
Provides: xorg-x11-mesaGL = %version-%release xorg-x11-mesagl = %version-%release libmesa = %version-%release
Requires: libGL libGLU
Obsoletes: xorg-x11-mesaGL xorg-x11-mesagl libmesa

%description mesagl
This package requires Mesa is an OpenGL compatible 3D graphics library

%package utils
Summary: Utilities for the X Window System
Group: System/X11
Obsoletes: %xf86-utils xorg-x11-utils
Provides: %xf86-utils = 4.4 xorg-x11-utils = %version-%release
Requires: xinit setxkbmap sessreg xf86dga xsetroot xcmsdb xconsole xmodmap xrdb
Requires: xdpyinfo xgamma xhost xrandr xrefresh xsetmode xstdcmap xvinfo
Requires: xkbevd xkbprint xlsfonts xprop xset

%description utils
Some useful utilities for the X Window System

%package apps
Summary: Graphical application for Xorg
Group: System/X11
Obsoletes: xorg-x11-xapps xorg-x11-apps
Provides: xorg-x11-xapps = %version-%release xorg-x11-apps = %version-%release
Requires: xmessage glxgears xfontsel xvidtune xkill xev

%description apps
Graphical application for Xorg

%package devel
Summary: Requires include files, development libraries and manual pages for xorg-x11
Group: Development/C
Obsoletes: %xf86-devel xorg-x11-devel libmesa-devel
Provides: %xf86-devel = 4.4 xorg-x11-devel = %version-%release libmesa-devel = %version-%release
PreReq: xorg-proto-devel
Requires: libICE-devel libSM-devel libX11-devel libXau-devel libXaw-devel libXrandr-devel
Requires: libXdmcp-devel libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel
Requires: libXmu-devel libXpm-devel libXrender-devel libXres-devel libXScrnSaver-devel
Requires: libXinerama-devel libXt-devel libXtst-devel libXxf86dga-devel libXcomposite-devel
Requires: libXxf86vm-devel libdmx-devel libfontenc-devel libGLU-devel libXdamage-devel
Requires: libxkbfile-devel xcursorgen xorg-font-utils libXvMC-devel libXcursor-devel
Requires: libXevie-devel libXv-devel xorg-xtrans-devel xorg-util-macros xorg-sgml-doctools
#FIXME
Requires: %name-compat-devel

%description devel
This package requires includes the libraries, header files and documentation
you'll need to develop programs which run in X clients. xorg-x11 includes
the base Xlib library as well as the Xt and Xaw widget sets

%package compat-devel
Summary: Requires utility and config files
Group: Development/C
Requires: gccmakedep imake lndir makedepend rman xorg-cf-files
#%name-devel
Provides: xorg-x11-compat-devel = %version-%release
Obsoletes: xorg-x11-compat-devel

%description compat-devel
This package requires utility and config files need to develop programs
wich monolitic Xorg

%package drv-video
Summary: video drivers for X Window System
Group: System/X11
Requires: %name-drv-ati %name-drv-intel %name-drv-nv %name-drv-openchrome %name-drv-cirrus %name-drv-mga
Requires: %name-drv-s3 %name-drv-s3virge %name-drv-savage %name-drv-sis %name-drv-nouveau
Provides: xorg-x11-drv-video = %version-%release
Obsoletes: xorg-x11-drv-video

%description drv-video
%name-drv-video requires video drivers for X Window System for PCI, AGP and PCI-E cards

%package drv-input
Summary: input drivers for X Window System
Group: System/X11
Requires: %name-drv-evdev %name-drv-synaptics
Provides: xorg-x11-drv-input = %version-%release
Obsoletes: xorg-x11-drv-input

%description drv-input
%name-drv-input requires all input drivers for X Window System

%package proto-devel
Summary: X proto header files
Group: Development/C
Conflicts: XFree86-devel < 4.4 xorg-x11-devel <= 6.9.0
Requires: xorg-bigreqsproto-devel xorg-compositeproto-devel xorg-damageproto-devel xorg-dmxproto-devel xorg-evieproto-devel
Requires: xorg-fixesproto-devel xorg-fontsproto-devel xorg-glproto-devel xorg-inputproto-devel xorg-kbproto-devel
Requires: xorg-pmproto-devel xorg-randrproto-devel xorg-recordproto-devel xorg-renderproto-devel xorg-resourceproto-devel
Requires: xorg-scrnsaverproto-devel xorg-videoproto-devel xorg-xcbproto-devel xorg-xcmiscproto-devel xorg-xextproto-devel
Requires: xorg-xf86bigfontproto-devel xorg-xf86dgaproto-devel xorg-xf86driproto-devel xorg-xf86rushproto-devel
Requires: xorg-xf86vidmodeproto-devel xorg-xineramaproto-devel xorg-xproto-devel
Provides: xorg-x11-proto-devel = %version-%release
Obsoletes: xorg-x11-proto-devel

%description proto-devel
X proto header files

%pre proto-devel
if [ -L %_includedir/X11 ]; then
	rm -f %_includedir/X11 && mkdir %_includedir/X11
fi
if [ -L %_includedir/GL ]; then
	rm -f %_includedir/GL && mkdir %_includedir/GL
fi

%files
%files libs
%files locales
%files mesagl
%files utils
%files apps
%files devel
%files compat-devel
%files drv-video
%files drv-input
%files proto-devel

%changelog
* Sun Dec 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.6.0-alt3
- xorg-drv-{video,input} cleanup

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.6.0-alt2
- new subpackage xorg-locales

* Fri Nov 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.6.0-alt1
- Xorg-7.6

* Wed Feb 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 7.5.0-alt3
- input: drop xorg-drv-penmount
- video: drop xorg-drv-vmware

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.5.0-alt2
- drop libFS

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.5.0-alt1
- Xorg-7.5

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt7
- update requires

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt6
- update requires

* Sun Nov 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt5
- update requires

* Sun Aug 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt4
- drop xtrap

* Sat Aug 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt3
- drop fontcache

* Fri Jun 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt2
- xorg-drv-video: drop requires xorg-drv-voodoo

* Wed Jun 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.4.0-alt1
- Xorg-7.4
- rename xorg-x11* to xorg*

* Sat Apr 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 7.3.0-alt1
- Xorg-7.3

* Mon Dec 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.2.0-alt1
- Xorg-7.2

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.1.1-alt3
- returned requires cirrus, mga, s3, s3virge, savage, sis, tdfx, trident, voodoo for %name

* Wed Aug 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.1.1-alt2
- added requires xset for %name-utils

* Tue Aug 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.1.1-alt1
- Xorg-7.1.1
- removed requires old video cards:
	apm, ark, chips, cirrus, cyrix, glint, i128, i740, imstt, mga, neomagic,
	newport, nsc, rendition, s3, s3virge, savage, siliconmotion, tdfx, tga,
	trident, tseng, voodoo

* Thu Jun 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.1.0-alt2
- fixed requires for %name-utils

* Wed May 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 7.1.0-alt1
- Xorg-7.1

* Fri Jan 20 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt9
- fixed #8893

* Thu Jan 19 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt8
- added requires libXcursor to %name-libs

* Wed Jan 18 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt7
- fixed requires for %name-devel

* Wed Jan 11 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt6
- added requires %name-compat-devel to %name-devel

* Fri Jan 06 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt5
- added %name-mesagl subpackage

* Fri Jan 06 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt4
- added requires xprop to %name-utils, xev to %name-apps

* Tue Jan 03 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt3
- added requires rman to %name-compat-devel

* Sun Jan 01 2006 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt2
- fixed trigger in %name-devel
- added requires xlsfonts to %name-utils, xkill to %name-apps

* Mon Dec 26 2005 Valery Inozemtsev <shrek@@altlinux.ru> 7.0.0-alt1
- 7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@@altlinux.ru> 6.99.99.903-alt1
- 7.0-RC3

* Fri Nov 25 2005 Valery Inozemtsev <shrek@@altlinux.ru> 6.9.99.902-alt0.1
- 7.0-RC2

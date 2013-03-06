%define xf86 XFree86

Name: xorg
Version: 7.7
Release: alt1
Summary: Part of the X.Org implementation of the X Window System
Group: System/X11
License: MIT/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildArch: noarch
Provides: %xf86 = 4.4 xorg-x11 = %version-%release
Obsoletes: %xf86 xorg-x11
Provides: %xf86-libs = 4.4 xorg-x11-libs = %version-%release %name-libs = %version-%release
Obsoletes: %xf86-libs xorg-x11-libs %name-libs < %version-%release
Obsoletes: %xf86-locales xorg-x11-locales %name-locales < %version-%release
Provides: %xf86-locales = 4.4 xorg-x11-locales = %version-%release %name-locales = %version-%release
Provides: xorg-x11-mesaGL = %version-%release xorg-x11-mesagl = %version-%release libmesa = %version-%release %name-mesagl = %version-%release
Obsoletes: xorg-x11-mesaGL xorg-x11-mesagl libmesa %name-mesagl < %version-%release
Obsoletes: %xf86-utils xorg-x11-utils %name-utils < %version-%release
Provides: %xf86-utils = 4.4 xorg-x11-utils = %version-%release %name-utils = %version-%release
Obsoletes: xorg-x11-xapps xorg-x11-apps %name-apps < %version-%release
Provides: xorg-x11-xapps = %version-%release xorg-x11-apps = %version-%release %name-apps = %version-%release
Obsoletes: %xf86-devel xorg-x11-devel libmesa-devel %name-devel < %version-%release
Provides: %xf86-devel = 4.4 xorg-x11-devel = %version-%release libmesa-devel = %version-%release %name-devel = %version-%release
Provides: xorg-x11-compat-devel = %version-%release %name-compat-devel = %version-%release
Obsoletes: xorg-x11-compat-devel %name-compat-devel < %version-%release
Provides: xorg-x11-drv-video = %version-%release %name-drv-video = %version-%release
Obsoletes: xorg-x11-drv-video %name-drv-video < %version-%release
Provides: xorg-x11-drv-input = %version-%release %name-drv-input = %version-%release
Obsoletes: xorg-x11-drv-input %name-drv-input < %version-%release
Provides: xorg-x11-proto-devel = %version-%release %name-proto-devel = %version-%release
Obsoletes: xorg-x11-proto-devel %name-proto-devel < %version-%release

#####
Provides: XORG_ABI_VIDEODRV = 13.1
#####

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

%files

%changelog
* Thu Mar 07 2013 Valery Inozemtsev <shrek@altlinux.ru> 7.7-alt1
- united packages
- drop requires

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

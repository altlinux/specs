# TODO: without libdca due internal headers required
%define pre %nil

Name: avidemux
Version: 2.4.4
Release: alt4.1

Summary: Avidemux is a graphical AVI files editor
Summary(ru_RU.KOI8-R): Avidemux -- это редактор AVI-файлов с графическим интерфейсом

License: GPL
Group: Video
Url: http://fixounet.free.fr/avidemux

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://download.berlios.de/%name/%name-%version.tar.bz2
Source: http://download.berlios.de/avidemux/avidemux_%version%pre.tar.bz2
Source1: %name.png
Source2: %name.desktop

Patch: %name-2.0.34-test2-alt-gettext.patch
Patch1: avidemux-pld-x264.patch
#Patch2: avidemux-glibc.patch
Patch2: avidemux-2.4-gcc44-movq.patch
Patch3: avidemux-2.4.4-alt-DSO.patch

%define xvid_ver 1.0.2
%define mjpegtools_ver 1.6.1.90

Obsoletes: avidemux2
Provides: avidemux2 = %version-%release

Requires: xvid >= %xvid_ver
BuildPreReq: xvid-devel >= %xvid_ver
BuildPreReq: mjpegtools-devel >= %mjpegtools_ver

# manual removed: gcc-java imake  xorg-cf-files
# Automatically added by buildreq on Tue Jul 15 2008
BuildRequires: gcc-c++ libSDL-devel libXt-devel libXv-devel libaften-devel libdca-devel libfaad-devel libgtk+2-devel liblame-devel libqt4-devel libx264-devel libxml2-devel libxvid-devel

#BuildRequires: seamonkey-devel
#BuildRequires: firefox firefox-devel
BuildRequires: xulrunner-devel

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX
compatible encoder and the Gimp Toolkit (GTK) libraries.

%description -l ru_RU.KOI8-R
Avidemux -- это редактор AVI-файлов с графическим интерфейсом.
Он позволяет монтировать видеосцены из видеофайлов и изображений
и добавлять к ним звуковую дорожку, а затем кодировать в файлы сжатых
форматов.

%prep
%ifdef pre
%setup -q -n %{name}_%version%pre
%else
%setup -q
%endif
%patch2 -p1 -b .gcc44
%patch3 -p2

%build
%add_optflags -fpermissive
make -f Makefile.dist
%configure \
	--with-jsapi-include=%_includedir/xulrunner/stable/ \
	--x-libraries="%_x11libdir" \
	--without-esd --without-arts \
	--disable-warnings
# non-SMP build due po dir in hasher
%make_build || %make

%install
%makeinstall_std

install -pD -m644 %SOURCE1 %buildroot%_pixmapsdir/%name.png
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
ln -s avidemux2_gtk %buildroot%_bindir/%name

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/avidemux2_cli
%_bindir/avidemux2_gtk
%_pixmapsdir/*
%_desktopdir/%name.desktop

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt4.1
- Fixed build

* Wed Feb 03 2010 Afanasov Dmitry <ender@altlinux.org> 2.4.4-alt4
- rebuild with libx264.so.85

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.4-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for avidemux
  * postclean-05-filetriggers for spec file

* Sun Oct 25 2009 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt3
- build without libfaac (bug #21713)

* Mon May 25 2009 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt2
- fix build with gcc 4.4

* Sat Mar 21 2009 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt2
- fix build with gcc 4.3 (thanks, PLD)

* Thu Jul 31 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)
- rebuild without esound, without arts

* Tue Jul 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)
- cleanup spec, update buildreqs, build with xulrunner

* Thu Apr 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version (2.4)

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt0.1pre3
- 2.4pre3

* Fri Jul 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt0.1pre2
- new version (2.4) - fix bug #12441
- build with libaften
- set avidemux link to gtk binary

* Tue Feb 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- fixes from Michael Shigorin <mike@altlinux.org>:
 - built against firefox-devel, fixed multilib issue
 - replaced debian menu file with freedesktop one (from livna.org)
 - replaced build procedure (from rpmforge.net spec)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1
- new version 2.3.0 (with rpmrb script)

* Sun Aug 06 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt0.1pre2b
- 2.2.0pre, rebuild without libx264
- note: still wait for 2.3.0, 2.2.0 will never released
- add avidemux binary name

* Mon Jun 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.3
- rebuild with new libx264

* Thu May 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.2
- rebuild with dynamic libx264 (fix bug #9539)

* Wed Mar 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1
- new version 2.1.2 (with rpmrb script)
- rename package to avidemux
- disable build with arts
- cleanup spec with rpmcs

* Thu Dec 22 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt0.1
- new version

* Tue Nov 29 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt0.1step3
- new version

* Sun Oct 09 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt0.1step2
- new version

* Thu Dec 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.34-alt0.5test2
- 2.0.34-test2

* Sun Jun 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.24-alt1
- 2.0.24
- avidemux2.png as icon (thanks lav@) and fixed menu file (close #4448).

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.20-alt0.6
- rebuild with xvid-1.0.0rc1.

* Sun Dec 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.20-alt0.5
- 2.0.20

* Mon Nov 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.18-alt0.5
- 2.0.18

* Sat Sep 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.16-alt0.5
- 2.0.16

* Tue Aug 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.14-alt0.5
- 2.0.14

* Mon Jul 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.10-alt0.5
- 2.0.10

* Thu Jun 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt0.5
- First build for Sisyphus.


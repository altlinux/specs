##############################################################################
# $Id: xdtv.spec.in,v 1.26 2006/01/27 20:38:14 pingus77 Exp $
##############################################################################
# Minimum required is: X11 & XPM & Xaw from X.org + Xterm
#
# Optional:
# To have a better GUI:
# neXtaw (0.15.1) from http://siag.nu/neXtaw/
# or XawM from http://sourceforge.net/projects/xawm/
# or Xaw95 & Xaw3d (not advised)
#
# To Record with a lot of audio/video codecs:
# FFMpeg (50.0.0+) from http://ffmpeg.sourceforge.net/ read README.ffmpeg for more infos
# Lame (3.96+)from http://lame.sourceforge.net/
# XviD (1.x+) from http://www.xvid.org/
# DivX (5.0.1alpha only) from http://www.divx.com/divx/linux/
# Ogg (1.1.2+) & Theora (1.0alpha5) & Vorbis (1.1.0+) from http://www.xiph.org/
#
# Other options:
# Zvbi (0.2.15+) from http://zapping.sourceforge.net/ (Scanning channels and get their names
# Alsa (1.x) from http://www.alsa-project.org/ (Better sound architecture than OSS)
# Lirc (0.7.x+) from http://www.lirc.org/ (If you have a remote and want to use it)
# libpng & libjpeg (For capturing AleVT & XdTV snapshots)
##############################################################################

%define date 20080708
%define cvsversion cvs%date
%define new_name xawdecode

%define branch_point alt11.%cvsversion
%define revision 12.2

Name: xdtv
Summary: XdTV is a software to record & watch TV
Version: 2.4.1
Release: %branch_point.%revision

License: GPL
Url: http://xawdecode.sourceforge.net/
Packager: Hihin Ruslan <ruslandh@altlinux.ru>
Source: xawdecode-%date.tar.bz2

Source1: %name.desktop
Source2: xdtv_russian_addons.tar
Patch: xawdecode-cvs20080708-tvdebug.patch
Patch1: xawdecode-cvs20080708.4-long.patch
Patch2: xawdecode-20080708-xterm.patch
Patch3: xawdecode-20080708-divx-fix.patch
Patch4: xawdecode-20080708-rm_oss_fix.patch
Patch5: xawdecode-20080708-dvb1.patch
Patch6: xawdecode-20080708-autotools0.patch
Patch7: xawdecode-20080708-autotools1.patch
Patch8: xawdecode-20080708-device.1.patch
Patch9: xawdecode-20101011-video4linux2.patch
Patch10: xawdecode-20080708-ffmpeg.patch

Group: Video

%def_enable optimization
%def_disable cpu-detection

%def_disable debug
%def_enable mmx

# Defaults :
%def_enable nls
%def_enable pixmaps
%def_enable xinerama

%def_enable nextaw
%def_enable xawm
%def_enable xaw95
%def_enable xaw3d
%def_enable ogg
%def_enable xvid
%def_enable ffmpeg
%def_enable ffmpeg_swscale
%def_enable dvb
%def_enable divx4linux
%def_enable lame
%def_enable dvb
%def_enable zvbi
%def_enable lirc
%def_enable alsa
%def_enable png
%def_enable jpeg
%def_disable faac
%def_enable mowitz
%def_enable xvtv
%def_enable x264
%def_enable xosd

%define Name			XdTV
%define summary1		%name is a software to record & watch TV.
%define tvtuner_launcher	%_desktopdir

BuildPreReq: rpm-build-fonts
BuildPreReq: linux-libc-headers
BuildPreReq: libavformat-devel liblirc-devel
BuildPreReq: xset libXext-devel

%if_enabled x264
BuildPreReq: libx264-devel
%endif

%if_enabled ogg
BuildPreReq: libogg-devel libtheora-devel libvorbis-devel
%endif

%if_enabled xvid
BuildPreReq: libxvid-devel
%endif

%if_enabled ffmpeg
BuildPreReq: libavformat-devel libpostproc-devel libswscale-devel
BuildPreReq: libavdevice-devel libavfilter-devel
%endif

%if_enabled divx
BuildPreReq: libavifile-devel
%endif

%if_enabled lame
BuildPreReq: liblame-devel
%endif

%if_enabled dvb
BuildPreReq: libdvbpsi-devel
%endif

%if_enabled zvbi
BuildPreReq: libzvbi-devel
%endif

%if_enabled lirc
BuildPreReq: liblirc-devel
%endif

%if_enabled alsa
BuildPreReq: libalsa-devel
%endif

%if_enabled png
BuildPreReq: libpng-devel
%endif

%if_enabled jpeg
BuildPreReq: libjpeg-devel
%endif

%if_enabled faac
BuildPreReq: libfaac-devel
%endif

%if_enabled xosd
BuildPreReq: libxosd-devel
%endif

# Automatically added by buildreq on Tue Mar 29 2011
BuildRequires: bdftopcf imake libSDL-devel libXaw-devel 
BuildRequires: libXaw3d-devel libXaw95-devel libXawM1-devel
BuildRequires: libXinerama-devel libXpm-devel libXv-devel 
BuildRequires: libXxf86dga-devel libXxf86vm-devel
BuildRequires: libavformat-devel libcurl-devel libdbus-glib-devel 
BuildRequires: liblame-devel liblirc-devel libneXtaw-devel 
BuildRequires: libswscale-devel
BuildRequires: libzvbi-devel mkfontdir xorg-cf-files xset



%description
XdTV is a software that allows you to to record & watch TV.
It interacts with Nxtvepg for NextView,
and uses the video4linux API. It can use some deinterlacing filters
and can record video files in various containers (AVI, MPEG, OGG, etc.)
with many codecs (FFMpeg(>=0.4.6), XviD(0.9 & 1.x),
Ogg Theora (>=1.0alpha5) & Vorbis and DivX4/5).
For AleVT for Teletext install libalevt
It has also some plugin capabilities.

%description -l ru_RU.CP1251
XdTV (ïðîãðàììà ïîä X11 îñíîâàííàÿ íà xawtv) ýòî ñîôò äëÿ ïðîñìîòðà
TV.  Îíà âçàèìîäåéñòâóåò ñ AleVT äëÿ Teletext è ñ Nxtvepg äëÿ NextView,
èñïîëüçóåò video4linux API.  Ìîæåò èñïîëüçîâàòü äåèíòåðëåéñ ôèëüòðû è
çàïèñûâàòü âèäåî ñ ïîìîùüþ êîäåêîâ: FFMpeg(>=0.4.6), XviD(0.9 & 1.x),
Ogg Theora (>=1.0alpha5) & Vorbis, DivX4/5.  Èìåþòñÿ âîçìîæíîñòè ïî
ïîäêëþ÷åíèþ ïëàãèíîâ. Äëÿ èñïîëüçîâàíèÿ òåëåòåêñòà íåîáõîäèìî óñòàíîâèòü
ïàêåò libalevt

%description -l ru_RU.UTF8
XdTV (Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð° Ð¿Ð¾Ð´ X11 Ð¾ÑÐ½Ð¾Ð²Ð°Ð½Ð½Ð°Ñ Ð½Ð° xawtv) ÑÑ‚Ð¾ ÑÐ¾Ñ„Ñ‚ Ð´Ð»Ñ Ð¿Ñ€Ð¾ÑÐ¼Ð¾Ñ‚Ñ€Ð°
TV.  ÐžÐ½Ð° Ð²Ð·Ð°Ð¸Ð¼Ð¾Ð´ÐµÐ¹ÑÑ‚Ð²ÑƒÐµÑ‚ Ñ AleVT Ð´Ð»Ñ Teletext Ð¸ Ñ Nxtvepg Ð´Ð»Ñ NextView,
Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·ÑƒÐµÑ‚ video4linux API.  ÐœÐ¾Ð¶ÐµÑ‚ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ñ‚ÑŒ Ð´ÐµÐ¸Ð½Ñ‚ÐµÑ€Ð»ÐµÐ¹Ñ Ñ„Ð¸Ð»ÑŒÑ‚Ñ€Ñ‹ Ð¸
Ð·Ð°Ð¿Ð¸ÑÑ‹Ð²Ð°Ñ‚ÑŒ Ð²Ð¸Ð´ÐµÐ¾ Ñ Ð¿Ð¾Ð¼Ð¾Ñ‰ÑŒÑŽ ÐºÐ¾Ð´ÐµÐºÐ¾Ð²: FFMpeg(>=0.4.6), XviD(0.9 & 1.x),
Ogg Theora (>=1.0alpha5) & Vorbis, DivX4/5.  Ð˜Ð¼ÐµÑŽÑ‚ÑÑ Ð²Ð¾Ð·Ð¼Ð¾Ð¶Ð½Ð¾ÑÑ‚Ð¸ Ð¿Ð¾
Ð¿Ð¾Ð´ÐºÐ»ÑŽÑ‡ÐµÐ½Ð¸ÑŽ Ð¿Ð»Ð°Ð³Ð¸Ð½Ð¾Ð². Ð”Ð»Ñ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸Ñ Ñ‚ÐµÐ»ÐµÑ‚ÐµÐºÑÑ‚Ð° Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼Ð¾ ÑƒÑÑ‚Ð°Ð½Ð¾Ð²Ð¸Ñ‚ÑŒ
Ð¿Ð°ÐºÐµÑ‚ libalevt.

%package -n libalevt
Summary: Developpement files for XdTV
Group: Development/C

%if_enabled nextaw
BuildPreReq: libneXtaw-devel
%endif

%if_enabled xawm
BuildPreReq: libXawM1-devel
%endif

%if_enabled xaw95
BuildPreReq: libXaw95-devel
%endif

%if_enabled xaw3d
BuildPreReq: libXaw3d-devel
%endif

%if_enabled xinerama
BuildPreReq: libXinerama-devel
%endif

%package -n libalevt-devel
Summary: Developpement files for XdTV
Group: Development/C
Requires: libalevt = %version-%release

%description -n libalevt
Teletext decoder and browser for the bttv driver.

%description -n libalevt-devel
Headers and tool for development with libalevt.

%description -n libalevt -l ru_RU.UTF8
X11 Ð±Ð¸Ð±Ð»Ð¸Ð¾Ñ‚ÐºÐ° Ð´Ð»Ñ Ð´ÐµÐºÐ¾Ð´Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ñ Ñ‚ÐµÐ»ÐµÑ‚ÐµÐºÑÑ‚Ð°.

%description -n libalevt -l ru_RU.CP1251
X11 áèáëèîòåêà äëÿ äåêîäèðîâàíèÿ òåëåòåêñòà.

%package -n fonts-bitmap-xdtv-OSD
Summary: Font used by XdTV OSD function
Group: Video
Conflicts: xdtv-OSD-font
Obsoletes: xdtv-OSD-font

%description -n fonts-bitmap-xdtv-OSD
Font used by XdTV OSD function.

%prep
%setup -n %new_name-%date -q -a2
mkdir m4
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch8 -p1

%patch6 -p1
%patch7 -p1

%patch9 -p1
%patch10 -p1

%build
%autoreconf

export FLAGS="%optflags -DNDEBUG -DNO_DEBUG -D_GNU_SOURCE "
%configure \
%if_enabled optimization
	--enable-cpu-detection \
%else
	--disable-cpu-detection \
%endif
	--with-gnu-ld  \
	--with-pic   \
	--with-x   \
        --enable-smallfont \
	--with-external-ffmpeg \
	--enable-x11-ext-checking \
        --with-fontdir=%buildroot%_bitmapfontsdir/%name \
	--with-appdefaultsdir=%_x11appconfdir \
	%{subst_enable mmx}  \
	%{subst_enable nls} \
	%{subst_enable pixmaps} \
	%{subst_enable debug} \
	%{subst_enable xinerama} \
	%{subst_enable ogg} \
	%{subst_enable x264} \
	%{subst_enable xvtv} \
	%{subst_enable divx} \
	%{subst_enable xvid} \
	%{subst_enable ffmpeg} \
	%{subst_enable ffmpeg_swscale} \
	%{subst_enable lame} \
	%{subst_enable zvbi} \
	%{subst_enable lirc} \
	%{subst_enable dvb} \
	%{subst_enable alsa} \
	%{subst_enable jpeg} \
	%{subst_enable png} \
	%{subst_enable nextaw} \
	%{subst_enable xawm} \
	%{subst_enable faac} \
	%{subst_enable xaw95} \
	%{subst_enable xaw3d} \
	%{subst_enable mowitz} \
export ROOT=%buildroot/usr
%make_build

%install
%makeinstall ROOT=%buildroot \
	     SUID_ROOT="" \
	     libdir=%buildroot/%_libdir

install -d -m755 %buildroot%_fontpathdir/

pushd %buildroot%_fontpathdir
ln -s ../../..%_bitmapfontsdir/%name bitmap-xdtv:unscaled:pri=20
popd

# Cure man path if needed
install -d -m 755 %buildroot%_includedir/libalevt
install -m 644 alevt/*.h %buildroot%_includedir/libalevt
install -d -m 755 %buildroot%_man1dir
install -m 644 man/%name.1 %buildroot%_man1dir
install -m 644 man/%{name}_cmd.1 %buildroot%_man1dir
install -m 644 man/%{name}_alevt-cap.1 %buildroot%_man1dir
install -m 644 man/%{name}_alevt-date.1 %buildroot%_man1dir
install -m 644 man/%{name}_alevt.1 %buildroot%_man1dir

# Dynamic desktop support
mkdir -p %buildroot/%tvtuner_launcher
cp %SOURCE1 %buildroot/%tvtuner_launcher/

cat > %buildroot%_desktopdir/xdtv_wizard.desktop << EOF
[Desktop Entry]
Name=xdtv_wizard
GenericName[ru]=ÐÐ°Ð»Ð°Ð´ÐºÐ° Ð¿Ð°Ñ€Ð°Ð¼ÐµÑ‚Ñ€Ð¾Ð² xdtv
Comment=xdtv is a software to record & watch TV.
Categories=AudioVideo;Video;TV;
TryExec=%_bindir/xdtv_wizard
Exec=%_bindir/xdtv_wizard
Terminal=true
Icon=xdtv.png
Type=Application
EOF

cat > %buildroot%_desktopdir/scan_xdtv.desktop << EOF
[Desktop Entry]
Name=xdtv_scantv.sh
GenericName[ru]=ÐÐ°ÑÑ‚Ñ€Ð¾Ð¹ÐºÐ° ÐºÐ°Ð½Ð°Ð»Ð¾Ð² xdtv
Comment=xdtv is a software to record & watch TV.
Categories=AudioVideo;Video;TV;
TryExec=%_bindir/xdtv_scan.sh
Exec=%_bindir/xdtv_scan.sh
Terminal=true
Icon=xdtv.png
Type=Application
EOF

cat > %buildroot%_desktopdir/xdtv_make_dvb.desktop << EOF
[Desktop Entry]
Name=xdtv_scantv.sh
GenericName[ru]=xdtv Ð¡ÐºÑ€Ð¸Ð¿Ñ‚ Ñ€Ð°Ð±Ð¾Ñ‚Ñ‹ Ñ DVB
Comment=xdtv is a software to record & watch TV.
Categories=AudioVideo;Video;TV;
TryExec=%_bindir/xdtv_makedvb.sh
Exec=%_bindir/xdtv_makedvb.sh
Terminal=true
Icon=xdtv.png
Type=Application
EOF

# menu
install -pD -m 644 %name-16.png %buildroot/%_miconsdir/%name.png
install -pD -m 644 %name-32.png %buildroot/%_niconsdir/%name.png
install -pD -m 644 %name-48.png %buildroot/%_liconsdir/%name.png

%files
%docdir %_docdir/xdtv-%version
%doc AUTHORS COPYING INSTALL FAQfr-xdtv TODO ChangeLog
%doc lisez-moi
%doc README README.*
%doc *.sample

%dir %_sysconfdir/%name
%_sysconfdir/%name/%{name}_wizard-en.conf
%_sysconfdir/%name/%{name}_wizard-en-UTF8.conf
%_bindir/%name
%_bindir/%{name}_cmd
%_bindir/%{name}_wizard
%_bindir/%{name}_scantv
%_bindir/%{name}_alevt-cap
%_bindir/%{name}_alevt-capall
%_bindir/%{name}_alevt-date
%attr(4711,root,root) %_bindir/%{name}_v4l-conf
%_bindir/%{name}_scan.sh
%_bindir/%{name}_record.sh
%_bindir/%{name}_makedvd.sh
%_man1dir/*
%_datadir/%name/icons/*
%_x11appconfdir/*

#_menudir/%name
#_menudir/%{name}_wizard
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/*.desktop

%files -n libalevt
%_libdir/*.so.*
#exclude  %_libdir/libalevt.la
#exclude  %_libdir/libalevt.a

%files -n libalevt-devel
%_includedir/*
%_libdir/*.so

%files -n fonts-bitmap-xdtv-OSD
%dir %_bitmapfontsdir/xdtv
%exclude %_bitmapfontsdir/xdtv/fonts.scale
%_bitmapfontsdir/xdtv/*
%_fontpathdir/*

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt11.cvs20080708.12.2
- Fixed build

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt11.cvs20080708.12.1
- Fixed build with libav 0.8

* Wed Sep 21 2011 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.12
- add xawdecode-20080708-ffmpeg.patch

* Mon Apr 18 2011 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.11
- rebuild

* Tue Mar 29 2011 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.10
- fix BuildRequires

* Mon Jul 19 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.9
- fix  packages-info-i18n-common

* Mon Mar 08 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.8
- fix mistakes

* Fri Feb 19 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.7
- add xawdecode-20080708-device.patch

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.1-alt11.cvs20080708.6.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for xdtv
  * postclean-05-filetriggers for spec file

* Tue Feb 02 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.6
- add xawdecode-20080708-dvb.patch 

* Fri Jan 08 2010 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.5
- add xawdecode-20080708-rm_oss.patch

* Mon May 11 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.4
- correct xawdecode-cvs20080708.4-long.patch

* Thu Feb 12 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.3
- add xawdecode-20080708-divx-fix.patch

* Mon Dec 01 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.2
- correct BuildRequires
- add xawdecode-20080708-xterm.patch

* Tue Jul 08 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.1-alt11.cvs20080708.1
- New version

* Thu Jun 12 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20080517.3
- rebuild with new libquicktime

* Sat May 17 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20080517.2
- New vesion

* Sun May 04 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20080405.1
- New version

* Fri Feb 29 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20070909.3
- correct %%*_menus

* Sat Feb 09 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20070909.2
- rebuild

* Mon Sep 10 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20070909.1
- new cvs version
- add --enable-xosd from Alexey V. Novikov
- replace Buildprereq: glibc-kernheaders

* Mon Sep 03 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt11.cvs20070729.1
- correct fonts

* Mon Jul 30 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt10.cvs20070729.1
- new cvs version

* Sun Jul 22 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt10.cvs20070519.2
- add xawdecode-cvs20070519-divx.patch

* Sat Jun 16 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt10.cvs20070519.1
- version for branch-4.0

* Mon Jun 11 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt9.cvs20070519
- correct align

* Mon Jun 11 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt8.cvs20070519
- add xdtv-2.4.cvs20070519-right2.patch
- remove xdtv-2.4.cvs20070519-right2.patch and xdtv-2.4.cvs20070519-float.patch

* Fri Jun 08 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt7.cvs20070519
- correct spec and xdtv-2.4.cvs20070519-mini-alevt.patch

* Wed Jun 06 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt6.cvs20070519.1
- correct xdtv_russian_addons

* Tue Jun 05 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt6.cvs20070519
- correct ru_RU.UTF8

* Fri Jun 01 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt4.cvs20070519
- correct xdtv_scantv.sh
- add xdtv_russian_addons

* Sun May 27 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt3.cvs20070519
- add xdtv-2.4.cvs20070519-float.patch
- cvs version

* Thu May 17 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.4
- add --enable-mmx

* Tue May 08 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.3
- correct xdtv.desktop

* Mon May 07 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.2
- correct xdtv.desktop

* Sun Mar 11 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2.1
- correct xdtv-2.4.0-alevt.patch

* Sun Feb 25 2007 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt2
- new version
- add dynamic libalevt.so
- patch ffmpeg-record from Alexey V. Novikov
- add key  --with-external-ffmpeg
- correct spec

* Sat Sep 23 2006 Hihin Ruslan <ruslandh@altlinux.ru> 2.4.0-alt1.pre0
- first version for ALT-Linux

* Sat Jul 22 2006 Hihin Ruslan <hihin_c@t_narod_dot_ru> 2.4.0pre0-alt1a
- add menu and desktop

* Wed Jul 19 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.4.0pre0-alt1
- Updated version to 2.4.0pre0
- Cleanup spec

* Thu Dec 22 2005 Sir Pingus <pingus_77@yahoo.fr> 2.3.0-1mdk
- 2.3.0
- review all the spec: now -with / without can be use with rpmbuild


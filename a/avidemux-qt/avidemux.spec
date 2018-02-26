
%define rname avidemux

Name: avidemux-qt
Version: 2.5.5
Release: alt2

Group: Video
Summary: Avidemux is a graphical AVI files editor
Summary(ru_RU.UTF-8): Avidemux -- это редактор AVI-файлов с графическим интерфейсом
Url: http://avidemux.org/
License: GPL

Provides: avidemux2 = %version-%release
Obsoletes: avidemux2 < %version-%release
Provides: avidemux = %version-%release
Conflicts: avidemux

Source: avidemux-%version.tar
Source2: avidemux.desktop

Patch1: plugins-compile.patch
Patch2: avidemux-2.5.4-alt-x264-test.patch
Patch3: avidemux-2.5.4-alt-i18n-qm-path.patch
Patch4: avidemux-2.5.4-alt-x264-115.patch
#
Patch100: avidemux-2.5.1-opencore-check.patch

# Automatically added by buildreq on Thu Oct 28 2010 (-bi)
#BuildRequires: bzlib-devel cmake gcc-c++ git-svn glibc-devel-static libGL-devel libSDL-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXvMC-devel libXxf86misc-devel libaften-devel libesd-devel libfaad-devel libjack-devel liblame-devel libopencore-amrnb-devel libopencore-amrwb-devel libpulseaudio-devel libsubversion-auth-gnome-keyring libsubversion-auth-kwallet libvdpau-devel libvorbis-devel libvpx-devel libx264-devel libxkbfile-devel libxml2-devel libxvid-devel perl-IO-Compress qt4-designer rpm-build-ruby tetex-core xml-utils xsltproc yasm
BuildRequires: bzlib-devel cmake gcc-c++ glibc-devel libSDL-devel
BuildRequires: libaften-devel libfaad-devel libjack-devel liblame-devel
BuildRequires: libopencore-amrnb-devel libopencore-amrwb-devel libpulseaudio-devel
BuildRequires: libvdpau-devel libvorbis-devel libvpx-devel libx264-devel
BuildRequires: libxml2-devel libxvid-devel perl-IO-Compress libqt4-devel
BuildRequires: xml-utils xsltproc yasm kde-common-devel libalsa-devel

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX
compatible encoder and the Gimp Toolkit (GTK) libraries.

%description -l ru_RU.UTF-8
Avidemux -- это редактор AVI-файлов с графическим интерфейсом.
Он позволяет монтировать видеосцены из видеофайлов и изображений
и добавлять к ним звуковую дорожку, а затем кодировать в файлы сжатых
форматов.

%package gui-qt
Group: Video
Summary: Qt GUI for %name
PreReq(post,preun): alternatives >= 0.2
Requires: %name-common = %version-%release
Provides: %name-qui = %version-%release
Conflicts: %name <= 2.4.4-alt1
%description gui-qt
Qt GUI for %name

%package gui-gtk
Group: Video
Summary: GTK GUI for %name
PreReq(post,preun): alternatives >= 0.2
Requires: %name-common = %version-%release
Provides: %name-qui = %version-%release
Conflicts: %name <= 2.4.4-alt1
%description gui-gtk
GTK GUI for %name

%package common
Group: Video
Summary: Common files for %name
PreReq(post,preun): alternatives >= 0.2
Provides: %name-qui = %version-%release
Conflicts: %name <= 2.4.4-alt1
%description common
Common files for %name

%prep
%setup -qn %rname-%version
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch100 -p1

# disable gtk ui
#sed -i 's|SET.*ADM_UI_GTK[[:space:]].*||' CMakeLists.txt

# fix hardcoded libdir
sed -i 's|Dir="lib"|Dir="%{_lib}"|' avidemux/main.cpp avidemux/ADM_core/src/ADM_fileio.cpp
grep -q '"%{_lib}"' avidemux/main.cpp
grep -q '"%{_lib}"' avidemux/ADM_core/src/ADM_fileio.cpp


%build
export QTDIR=%_qt4dir
BUILDDIR=$PWD
%K4cmake \
    -DAVIDEMUX_INSTALL_PREFIX=%prefix \
    -DAVIDEMUX_CORECONFIG_DIR=$BUILDDIR/BUILD-%_target_platform/config \
    -DAVIDEMUX_SOURCE_DIR=$BUILDDIR \
    -DAVIDEMUX_INSTALL_PREFIX=$BUILDDIR/BUILD-%_target_platform \
    -DGTK:BOOL=FALSE \
    -DUSE_ARTS:BOOL=FALSE \
    -DUSE_ESD:BOOL=FALSE \
    -DUSE_SDL:BOOL=TRUE \
    -DUSE_ALSA:BOOL=TRUE
%K4make

%install
%set_verify_elf_method unresolved=relaxed,textrel=relaxed
%K4install
if [ -d %buildroot/usr/lib -a "%_lib" == "lib64" ]
then
    mkdir -p %buildroot/%_libdir
    mv %buildroot/usr/lib/* %buildroot/%_libdir/
fi

install -pD -m644 avidemux_icon.png %buildroot%_pixmapsdir/%rname.png
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%rname.desktop
ln -s avidemux2_qt4 %buildroot%_bindir/%rname

#find_lang %name


%files
%_desktopdir/*.desktop
%_bindir/avidemux
%_bindir/avidemux2_cli
%_bindir/avidemux2_qt4
%_libdir/libADM_UICli.so*
%_libdir/libADM_UIQT4.so*
%_libdir/libADM_render_cli.so
%_libdir/libADM_render_qt4.so
%_libdir/libADM5*
%_libdir/libADM_core*.so*
%_libdir/libADM_smjs.so*
%_libdir/ADM_plugins
%_pixmapsdir/*
%_datadir/ADM_scripts
%_datadir/avidemux

%changelog
* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt2
- rebuilt with recent libvpx and libx264

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.5-alt1
- new version

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.4-alt4.1
- rebuilt with recent x264

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt4
- fix build requires

* Wed Nov 17 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt3
- add Russian translation to desktop-file
- rebuilt with new x264

* Thu Oct 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt2
- fix build requires and desktop-file categories

* Thu Oct 28 2010 Sergey V Turchin <zerg@altlinux.org> 2.5.4-alt1
- new version

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


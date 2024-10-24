Name: kodi
Version: 21.1
Release: alt1

Summary: Kodi Media Center
License: GPL-2.0-or-later
Group: Video
Url: https://kodi.tv/

Requires: kodi-bin = %version-%release
Requires: kodi-data = %version-%release
Requires: kodi-x11 = %version-%release

Source0: %name-%version-%release.tar
Source1: groovy.tar

BuildRequires: cmake gcc-c++
BuildRequires: libcrossguid-devel libflatbuffers-devel libgif-devel liblzo2-devel
BuildRequires: libunistring-devel libidn2-devel libEGL-devel
BuildRequires: /proc swig java-devel
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dvdnav)
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(enca)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(fstrcmp)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libass)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libbluray)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libcdio)
BuildRequires: pkgconfig(libcec)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libdvdcss)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libiso9660)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(liblircclient0)
BuildRequires: pkgconfig(libmicrohttpd)
BuildRequires: pkgconfig(libnfs)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libpcrecpp)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(libudfread)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(spdlog)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(tinyxml)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(vdpau)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client++)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(zlib)

%package bin
Summary: Kodi binaries
Group: Video
Requires: kodi-data = %version-%release

%package data
Summary: Kodi architecture-independent data
Group: Video
BuildArch: noarch
Requires: python3(sqlite3)
AutoReqProv: yes,nopython

%package devel
Summary: Kodi development part
Group: Development/C++
Requires: kodi = %version-%release

%package x11
Summary: Kodi X11-specific part
Group: Video
Requires: kodi-bin = %version-%release

%description
Kodi is an media-player and entertainment hub for all your digital media.

%description bin
Kodi is an media-player and entertainment hub for all your digital media.
This package contains Kodi binaries.

%description data
Kodi is an media-player and entertainment hub for all your digital media.
This package contains all architecture-independent data requried for Kodi.

%description devel
Kodi is an media-player and entertainment hub for all your digital media.
This package contains development part of Kodi.

%description x11
Kodi is an media-player and entertainment hub for all your digital media.
This package contains X11-specific part of Kodi.

%define __nprocs 8
%define docdir %_defaultdocdir/%name
%ifarch armh aarch64
%define platdefs -DAPP_RENDER_SYSTEM=gles
%else
%define platdefs -DAPP_RENDER_SYSTEM=gl
%endif

%prep
%setup
tar xf %SOURCE1 -C %_sourcedir
%ifarch %e2k
sed -i "/make_map/s/std::string_view/const char*/g" \
	xbmc/windowing/gbm/WinSystemGbm.cpp \
	xbmc/cores/AudioEngine/Sinks/AESinkStarfish.cpp \
	xbmc/cores/VideoSettings.h xbmc/utils/ColorUtils.h \
	xbmc/cores/VideoPlayer/VideoRenderers/VideoShaders/ShaderFormats.h \
	xbmc/rendering/{gl/RenderSystemGL.h,gles/RenderSystemGLES.h}
sed -i "s/private:/public:/" \
	xbmc/cores/AudioEngine/Sinks/pipewire/Pipewire.h
sed -i "s/HTML_BASIC_COLORS.find(value/&.c_str()/" \
	xbmc/cores/VideoPlayer/DVDSubtitles/DVDSubtitleTagSami.cpp
%endif

%build
%cmake  -DTARBALL_DIR=%_sourcedir \
        -DGIT_VERSION=%release \
        -DCORE_PLATFORM_NAME="x11 wayland gbm" \
        %platdefs
%cmake_build

%install
%cmakeinstall_std
sed -i -e '/Exec=kodi/ s,=,=%_bindir/,' %buildroot%_datadir/xsessions/kodi.desktop
install -pm0644 -D kodi.wmsession %buildroot%_sysconfdir/X11/wmsession.d/20KODI
mkdir %buildroot%_libdir/kodi/addons

%add_python3_req_skip xbmc
%add_python3_req_skip xbmcgui
%add_python3_req_skip xbmcaddon
%add_python3_req_skip xbmcvfs

%files
%docdir
%_desktopdir/kodi.desktop
%_iconsdir/hicolor/*/apps/kodi.png
%_datadir/metainfo/*.xml

%files bin
%_bindir/kodi
%_bindir/kodi-standalone

%dir %_libdir/kodi
%_libdir/kodi/addons
%_libdir/kodi/system
%_libdir/kodi/kodi.bin
%_libdir/kodi/kodi-xrandr

%files data
%dir %_datadir/kodi
%_datadir/kodi/addons
%_datadir/kodi/media
%_datadir/kodi/system
%_datadir/kodi/userdata
%_datadir/kodi/privacy-policy.txt
%_datadir/wayland-sessions/kodi-gbm.desktop

%files devel
%_includedir/kodi
%_datadir/kodi/cmake
%_libdir/kodi/cmake

%files x11
%config(noreplace) %_sysconfdir/X11/wmsession.d/20KODI
%_datadir/xsessions/kodi.desktop

%changelog
* Thu Oct 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.1-alt1
- 21.1 released

* Wed Apr 10 2024 Michael Shigorin <mike@altlinux.org> 21.0-alt2
- E2K: more workarounds for lcc 1.27 (ilyakurdyukov@, mcst#7982)

* Sat Apr 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0-alt1
- 21.0-Omega released

* Fri Mar 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 20.5-alt1
- 20.5-Nexus released
- fixed faults with python addons (closes: 49771)

* Sun Feb 25 2024 Michael Shigorin <mike@altlinux.org> 20.4-alt2
- E2K: use default java

* Mon Feb 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.4-alt1
- 20.4-Nexus released

* Fri Jan 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3-alt1
- 20.3-Nexus released

* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 20.2-alt2.3
- NMU: fixed building with python3.12

* Wed Oct 18 2023 Michael Shigorin <mike@altlinux.org> 20.2-alt2.2
- E2K: fix build with lcc 1.26 (ilyakurdyukov@, mcst#7982)

* Mon Oct 16 2023 Nazarov Denis <nenderus@altlinux.org> 20.2-alt2.1
- NMU: Fix build with fmt 10

* Fri Sep 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.2-alt2
- rebuilt with recent ffmpeg

* Fri Jun 30 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.2-alt1
- 20.2-Nexus released

* Thu Jun 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.1-alt3
- 20.1-Nexus-75-g9a44d078a3

* Wed May 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.1-alt2
- rebuilt with internal flatbuffers

* Mon Mar 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.1-alt1
- 20.1 Nexus released

* Mon Jan 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.0-alt1
- 20.0 Nexus released

* Tue Dec 27 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.5-alt2
- readd lost cmake bits

* Mon Dec 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.5-alt1
- 19.5 Matrix released

* Tue Dec 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.4-alt3
- fixed build with recent mesa

* Mon Jul 11 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.4-alt2
- fix build with fmt9

* Wed Mar 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.4-alt1
- 19.4 Matrix released

* Mon Nov 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.3-alt3
- rebuilt with recent spdlog

* Thu Oct 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 19.3-alt2
- added patch with Elbrus support

* Wed Oct 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.3-alt1
- 19.3 Matrix released

* Sun Oct 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.2-alt1
- 19.2 Matrix released

* Tue Jun 15 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.1-alt1
- 19.1 Matrix released

* Sat Feb 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- 19.0 Matrix released

* Fri Dec 11 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt0.20201207
- 19.0b2 Matrix

* Thu Nov 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt0.20201117
- 19.0b1 Matrix

* Tue Nov 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt0.20201031
- 19.0a3 Matrix

* Thu Oct 08 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt0.20201005
- 19.0a2 Matrix

* Mon Aug 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt0.20200726
- 19.0a1 Matrix

* Wed Jul 29 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.8-alt1
- 18.8 Leia released

* Tue Jul 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.7.1-alt2
- drop unused libplist BR

* Tue Jun 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.7.1-alt1
- 18.7.1 Leia released

* Mon Apr 20 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 18.6-alt2
- Fixed build with new libfmt.

* Thu Mar 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.6-alt1
- 18.6 Leia released

* Tue Feb 04 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.5-alt2
- do not package xsession-related files on gbm variant

* Tue Nov 26 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.5-alt1
- 18.5 Leia released

* Mon Sep 23 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.4-alt1
- 18.4 Leia released

* Sat Aug 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.3-alt1
- 18.3 Leia released

* Mon Apr 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.2-alt1
- 18.2 Leia released

* Wed Apr 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.1-alt1
- 18.1 Leia released

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- 18.0 Leia released

* Tue Sep 18 2018 Alexey Shabalin <shaba@altlinux.org> 17.6-alt5
- rebuilt with recent libmicrohttpd

* Fri Aug 31 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.6-alt4
- rebuilt with recent openssl

* Thu Jun 14 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.6-alt3
- rebuilt with recent libva

* Fri Jan 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.6-alt2
- rebuilt with recent libcdio

* Thu Nov 16 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.6-alt1
- 17.6 Krypton released

* Thu Oct 26 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.5-alt1
- 17.5 Krypton released

* Wed Aug 23 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.4-alt1
- 17.4 Krypton released

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 17.3-alt2
- Fixed build with gcc-6

* Thu May 25 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.3-alt1
- 17.3 Krypton released

* Wed May 24 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.2-alt1
- 17.2 Krypton released

* Wed Mar 22 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.1-alt1
- 17.1 Krypton released

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- 17.0 Krypton released

* Fri Apr 29 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.1-alt1
- 16.1 Jarvis released

* Wed Feb 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0-alt1
- 16.0 Jarvis released

* Tue Oct 20 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.2-alt1
- 15.2 Isengard released

* Tue Aug 18 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.1-alt1
- 15.1 Isengard released

* Wed Jul 22 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.0-alt1
- 15.0 Isengard released

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 14.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Mar 28 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 14.2-alt1
- 14.2 Helix released

* Mon Feb 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 14.1-alt1
- 14.1 Helix released

* Sun Dec 28 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 14.0-alt1
- 14.0 Helix released

* Mon Aug 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.2-alt1
- 13.2 Gotham released

* Mon Jun 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.1-alt1
- 13.1 Gotham released

* Mon Jun 02 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0-alt4
- 13.1rc1

* Sat May 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0-alt3
- 13.1b2

* Sat May 17 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0-alt2
- 13.1b1

* Fri May 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.0-alt1
- 13.0 Gotham released

* Fri May 03 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.2-alt1
- 12.2 released

* Tue Mar 19 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.1-alt1
- 12.1 Frodo released

* Sat Feb 02 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.0-alt1
- 12.0 Frodo released

* Tue May 08 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt2
- 11.0 Eden-r2 released

* Sun Mar 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt1
- 11.0 Eden released

* Fri Mar 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.5
- 11.0-RC2 released

* Tue Feb 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.4
- 11.0-RC1 released

* Fri Feb 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.3
- 11.0-beta3 released

* Sun Jan 22 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.2
- 11.0-beta2 released

* Sat Dec 31 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0-alt0.1
- 11.0-beta1 released

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 10.1-alt1.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.1-alt1
- 10.1 released

* Fri Dec 17 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt1
- 10.0 Dharma released

* Sat Dec 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.5
- rc2 released

* Sun Oct 31 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.4
- beta4 released

* Thu Oct 14 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.3
- beta3 released

* Wed Sep 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.0-alt0.2
- beta2 released

* Sun Aug 15 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt5
- preview build for forthcoming 'dharma' release

* Sat May 29 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt3
- tvheadend pvr plugin added

* Sun Apr 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt2
- use ffmpeg for dts from now

* Thu Dec 31 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.11-alt1
- 9.11 released
- PVR stuff added

* Tue Dec 15 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt5
- fixed breakage on nvidia proprietary drivers >= 190.xx
- fixed for and rebuilt with python 2.6 (real@)

* Mon Nov 16 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt4
- rebuilt with recent libcdio

* Sat Nov 07 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt3
- rebuilt with recent cdio

* Thu Oct  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt2
- few minor packaging improvements

* Wed Sep  9 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 9.0.4-alt1
- Initial build.

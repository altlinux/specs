%def_with ffmpeg
Name: qtox
Version: 1.13.0
Release: alt1.1

Summary: Powerful Tox client that follows the Tox design guidelines

License: GPL+
Group: Networking/Instant messaging
Url: https://github.com/tux3/qTox

Packager: Vitaly Lipatov <lav@altlinux.ru>

# #Source-git: https://github.com/tux3/qTox
# Source-url: https://github.com/qTox/qTox/archive/v%version.tar.gz
Source: %name-%version.tar

BuildPreReq: rpm-macros-qt5
BuildRequires(pre): rpm-macros-ubt

BuildRequires: cmake

# manually removed: i586-libxcb ruby ruby-stdlibs 
# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: fontconfig glib2-devel glibc-devel-static libGL-devel libX11-devel libatk-devel libavcodec-devel libavutil-devel libcairo-devel libcloog-isl4 libdc1394-22 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libpango-devel libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-sql libqt5-svg libqt5-widgets libqt5-xml libraw1394-11 libsodium-devel libstdc++-devel libswscale-devel libvpx-devel libwayland-client libwayland-server python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-tools xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ git-core libXScrnSaver-devel libdb4-devel libfilteraudio-devel libgtk+2-devel libopenal-devel qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-webkit-devel qt5-websockets-devel libexif-devel

%if_with ffmpeg
%if %__ubt_branch_id == "M80P"
BuildRequires: libffmpeg-devel-static
%def_with ffmpeg_static
%else
BuildRequires: libavdevice-devel libavformat-devel libswscale-devel libswresample-devel
%endif
%else
BuildRequires: libavdevice-devel libavformat-devel libswscale-devel libavresample-devel
%endif

# no upstream info
#BuildPreReq: libopenal-devel >= 1.16.0

BuildRequires: libsodium-devel

BuildPreReq: libqrencode-devel  >= 3.0.3
BuildPreReq: libsqlcipher-devel >= 3.2.0
BuildPreReq: toxcore-devel >= 0.1.9

%description
Powerful Tox Qt5 client that follows the Tox design guidelines.

%prep
%setup
%__subst "s|.*-Werror.*||g" CMakeLists.txt

%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif
%cmake_insource
%make_build

%install
mkdir -p %buildroot%_bindir/
install -m 0755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_desktopdir/
install -m 0644 qtox.desktop %buildroot%_desktopdir/%name.desktop

# create icons tree
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps/
install -m 0644 img/icons/qtox.svg %buildroot%_iconsdir/hicolor/scalable/apps/

for i in img/icons/*x*/*.png ; do
    DNAME=$(basename $(dirname $i))
    install -D -m 0644 $i %buildroot%_iconsdir/hicolor/$DNAME/apps/%name.png
done

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1.1
- NMU: autorebuild with libsodium-1.0.16

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)
- switched to cmake
- rebuild with ffmpeg really

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.10.2-alt1
- new version 1.10.2 (with rpmrb script)
- build with new toxcore-devel 0.1.9

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version (1.6.0) with rpmgs script
- rebuild with ffmpeg

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.4.1.1-alt2
- rebuild with new toxcore and libsodium

* Mon Jul 25 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.1.1-alt1
- build new version with toxcore 0.0.1-alt1.20160725
_ still incompatible with libav (a fork of ffmpeg) (see alt bug #32310)

* Sat Jun 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus

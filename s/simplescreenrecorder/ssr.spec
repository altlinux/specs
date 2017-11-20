Name: simplescreenrecorder
Version: 0.3.8
Release: alt4
Summary: Simple Screen Recording with OpenGL capture

Group: Video
License: GPLv3
Url: http://www.maartenbaert.be/simplescreenrecorder/
Obsoletes: simplescreenrecording

Source: %version.tar.gz
Patch:  alt-desktop-l10n-ru.patch

# Automatically added by buildreq on Mon Oct 06 2014
# optimized out: fontconfig gnu-config libGL-devel libGLU-devel libX11-devel libXext-devel libXfixes-devel libXi-devel libavcodec-devel libavutil-devel libcloog-isl4 libopencore-amrnb0 libopencore-amrwb0 libqt4-core libqt4-gui libstdc++-devel pkg-config xorg-fixesproto-devel xorg-inputproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel-static libalsa-devel libavformat-devel libjack-devel libpulseaudio-devel libqt4-devel libswscale-devel

%description
%summary

%prep
%setup -n ssr-%version
%patch -p2
# XXX waiting for support for channels
sed -i '/#define SSR_USE_AVFRAME_CHANNELS/s/TEST_AV_VERSION.*/TEST_AV_VERSION(LIBAVCODEC, 57, 0, 57, 0)/' src/Global.h

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/lib*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1.*
%_datadir/%name

%changelog
* Mon Nov 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt4
- Fix menu localization by add missing original GenericName

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt3
- Add Russian localization to desktop file.

* Tue Jun 13 2017 Anton Farygin <rider@altlinux.ru> 0.3.8-alt2
- rebuilt with ffmpeg
- added man pages

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 0.3.8-alt1
- Autobuild version bump to 0.3.8

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Autobuild version bump to 0.3.7

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.3.6-alt1
- Autobuild version bump to 0.3.6

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 0.3.3-alt1
- Autobuild version bump to 0.3.3
- Libavformat has no channels support still

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1
- Obsolete simplescreenrecording

* Mon Oct 06 2014 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- New version

* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus

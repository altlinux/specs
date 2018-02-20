Name: simplescreenrecorder
Version: 0.3.9
Release: alt1
Summary: Simple Screen Recording with OpenGL capture

Group: Video
License: GPLv3
Url: http://www.maartenbaert.be/simplescreenrecorder/
Obsoletes: simplescreenrecording

Source: %version.tar.gz

# Automatically added by buildreq on Tue Feb 20 2018
# optimized out: cmake-modules fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libXtst-devel libXv-devel libavcodec-devel libavutil-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-webkit-devel libssl-devel libstdc++-devel libx265-130 pkg-config python-base python-modules xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libalsa-devel libavformat-devel libjack-devel libpulseaudio-devel libswscale-devel phonon-devel

%description
%summary

%prep
%setup -n ssr-%version
f="data/simplescreenrecorder.desktop"
for s in "GenericName=Simple screen recorder" \
	"GenericName[ru]=Запись видео с экрана" \
	"Comment[ru]=Программа записи видео с экрана" ; do
	fgrep -q "${s%%=}" "$f" || echo "$s" >> "$f"
done
# XXX waiting for support for channels
##sed -i '/#define SSR_USE_AVFRAME_CHANNELS/s/TEST_AV_VERSION.*/TEST_AV_VERSION(LIBAVCODEC, 57, 0, 57, 0)/' src/Global.h

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/lib*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1.*
%_datadir/%name
%_datadir/appdata/*

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.3.9-alt1
- Autobuild version bump to 0.3.9

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

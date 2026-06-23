%def_without clang
%def_with tests

Name: strawberry
Version: 1.2.20
Release: alt1

Summary: Audio player and music collection organizer

# Main program: GPL-3.0-or-later
# 3rdparty/discord-rpc: MIT
License: GPL-3.0-or-later and MIT
Group: Sound
Url: https://www.strawberrymusicplayer.org
VCS: https://github.com/strawberrymusicplayer/strawberry

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/strawberrymusicplayer/strawberry/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: gst-plugins-good1.0 vlc-mini

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Tue Oct 24 2023
# optimized out: boost-devel-headers cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gstreamer1.0-devel icu-utils libX11-devel libdouble-conversion3 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgmock-devel libgpg-error libgst-plugins1.0 libicu-devel libimobiledevice-devel libp11-kit libplist-devel libqt6-concurrent libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-sql libqt6-test libqt6-widgets libsasl2-3 libssl-devel libstdc++-devel libvulkan-devel libxcb-devel libxkbcommon-devel pkg-config python3 python3-base qt6-base-common qt6-base-devel qt6-tools sh5 shared-mime-info xorg-proto-devel zlib-devel
BuildRequires: boost-devel cmake gst-plugins1.0-devel libalsa-devel libcdio-devel libchromaprint-devel libdbus-devel libebur128-devel libfftw3-devel libgpod-devel libgtest-devel libmtp-devel libprotobuf-devel libpulseaudio-devel libsqlite3-devel taglib-devel libvlc-devel protobuf-compiler sparsehash-devel rapidjson-devel
BuildRequires: qt6-base-devel qt6-tools-devel qt6-sql-interbase qt6-sql-mysql qt6-sql-odbc qt6-sql-postgresql libkdsingleapplication-qt6-devel
BuildRequires: libicu-devel

%if_with tests
BuildRequires: ctest desktop-file-utils /usr/bin/appstream-util
%endif

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
Strawberry is a audio player and music collection organizer.
It is a fork of Clementine. The name is inspired by the band Strawbs.

Features:
  * Play and organize music
  * Supports WAV, FLAC, WavPack, DSF, DSDIFF, Ogg Vorbis, Speex, MPC,
    TrueAudio, AIFF, MP4, MP3 and ASF
  * Audio CD playback
  * Native desktop notifications
  * Playlists in multiple formats
  * Advanced output and device options with support for bit perfect playback
    on Linux
  * Edit tags on music files
  * Fetch tags from MusicBrainz
  * Album cover art from Last.fm, Musicbrainz and Discogs
  * Song lyrics from AudD and API Seeds
  * Support for multiple backends
  * Audio analyzer
  * Equalizer
  * Transfer music to iPod, iPhone, MTP or mass-storage USB player
  * Integrated Tidal support
  * Scrobbler with support for Last.fm, Libre.fm and ListenBrainz

%prep
%setup
%patch -p1
%ifarch %e2k
sed -i "s/u'\\\\0'/(QChar)&/" src/tagreader/tagreadergme.cpp
%endif

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_qt6_bindir:$PATH
export LC_ALL=C.UTF-8

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_WERROR=OFF \
#

cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%if_with tests
%check
# Tests for the graphical environment are not supported in the build environment.
sed -i '/add_test_file(.* true)/d' tests/CMakeLists.txt
export LC_ALL=C.UTF-8
cmake --build "%_cmake__builddir" -j%__nprocs -t run_strawberry_tests
desktop-file-validate %buildroot%_desktopdir/org.strawberrymusicplayer.strawberry.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml
%endif

%files
%doc COPYING Changelog README.md
%_bindir/strawberry
%_datadir/metainfo/org.strawberrymusicplayer.strawberry.appdata.xml
%_desktopdir/org.strawberrymusicplayer.strawberry.desktop
%_iconsdir/hicolor/*/apps/strawberry.*
%_man1dir/strawberry.1.*

%changelog
* Tue Jun 23 2026 Leontiy Volodin <lvol@altlinux.org> 1.2.20-alt1
- New version 1.2.20.

* Mon Apr 20 2026 Leontiy Volodin <lvol@altlinux.org> 1.2.19-alt1
- New version 1.2.19.

* Mon Feb 02 2026 Leontiy Volodin <lvol@altlinux.org> 1.2.18-alt1
- New version 1.2.18.

* Mon Jan 19 2026 Leontiy Volodin <lvol@altlinux.org> 1.2.17-alt1
- New version 1.2.17.

* Thu Dec 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.16-alt1
- New version 1.2.16.
- Enabled tests.

* Tue Nov 25 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.15-alt1
- New version 1.2.15.

* Mon Oct 27 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.14-alt1
- New version 1.2.14.

* Tue Sep 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.13-alt1
- New version 1.2.13.

* Thu Aug 14 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.12-alt1
- New version 1.2.12.
- Updated license tag.

* Tue May 27 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.11-alt1
- New version 1.2.11.
- Built with libtag2.

* Thu Jan 14 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.2.4-alt2
- Fixed build for Elbrus.

* Mon Jan 13 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.4-alt1
- New version 1.2.4.

* Mon Dec 09 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.3-alt1
- New version 1.2.3.

* Mon Nov 25 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.2-alt1
- New version 1.2.2.
- Added vcs tag.

* Fri Nov 22 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.1-alt1
- New version 1.2.1.

* Mon Sep 23 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.0-alt1
- New version 1.2.0.
- Removed qt5 support (by upstream).
- Updated license tag.

* Thu Feb 22 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0.23-alt2
- Fixed build for Elbrus (missing BR).

* Mon Jan 15 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.23-alt1
- New version 1.0.23.
- Built with system libkdsingleapplication.

* Mon Dec 11 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.22-alt1
- New version 1.0.22.

* Tue Oct 24 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.21-alt1
- New version 1.0.21.
- Cleanup spec and BRs.

* Mon Sep 25 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.20-alt1
- New version 1.0.20.
- Built with libebur128 support.
- Cleanup list of buildrequires and licenses.

* Fri Sep 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.18-alt2
- removed superfluous xine build req

* Mon Jul 03 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.18-alt1
- New version 1.0.18.

* Thu Mar 30 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.17-alt1
- New version 1.0.17.

* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.16-alt1
- New version 1.0.16.

* Mon Mar 06 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.15-alt1
- New version (1.0.15).

* Sun Jan 15 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.14-alt1
- New version (1.0.14).

* Tue Jan 10 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.13-alt1
- New version (1.0.13).

* Tue Jan 03 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.12-alt1
- New version (1.0.12).

* Mon Oct 24 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- New version (1.0.10).

* Mon Sep 05 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.9-alt1
- New version (1.0.9).

* Tue Aug 30 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- New version (1.0.8).

* Tue Jul 26 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt1
- New version (1.0.7).

* Mon Jul 18 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.6-alt1
- New version (1.0.6).

* Tue Jun 14 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt1
- New version (1.0.5).

* Mon Apr 11 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.4-alt1
- New version (1.0.4).

* Mon Mar 28 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1
- New version (1.0.3).
- Built with qt6 by default.

* Thu Mar 10 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.2-alt1
- New version (1.0.2).

* Fri Jan 28 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.1-alt1
- New version (1.0.1).

* Wed Oct 20 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- New version (1.0.0).

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.3-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon Apr 19 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.3-alt1
- New version (0.9.3) with rpmgs script.

* Fri Mar 26 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.2-alt1
- New version (0.9.2) with rpmgs script.

* Mon Mar 15 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.1-alt1
- New version (0.9.1) with rpmgs script.

* Mon Dec 21 2020 Leontiy Volodin <lvol@altlinux.org> 0.8.5-alt1
- New version (0.8.5) with rpmgs script.

* Mon Nov 16 2020 Leontiy Volodin <lvol@altlinux.org> 0.8.4-alt1
- New version (0.8.4) with rpmgs script.
- The project switched to C++17.

* Mon Oct 26 2020 Leontiy Volodin <lvol@altlinux.org> 0.8.3-alt1
- New version (0.8.3) with rpmgs script.

* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.8.2-alt1
- New version (0.8.2) with rpmgs script.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 0.8.1-alt1
- New version (0.8.1) with rpmgs script.

* Sun Aug 16 2020 Leontiy Volodin <lvol@altlinux.org> 0.7.2-alt1
- New version (0.7.2) with rpmgs script.

* Sat Aug 15 2020 Leontiy Volodin <lvol@altlinux.org> 0.7.1-alt1
- New version (0.7.1) with rpmgs script.
- Built with ninja instead make.

* Tue Jul 14 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.13-alt1
- New version (0.6.13) with rpmgs script.

* Thu Jun 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt2
- Fixed build with new libusbmuxd and libplist.

* Mon Jun 08 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt1
- New version (0.6.12) with rpmgs script.

* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.11-alt1
- New version (0.6.11) with rpmgs script.

* Fri May 01 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.10-alt1
- new version (0.6.10) with rpmgs script

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.9-alt1
- New version (0.6.9) with rpmgs script.

* Thu Jan 09 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.8-alt1
- New version (0.6.8) with rpmgs script.

* Mon Dec 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.7-alt1
- New version (0.6.7) with rpmgs script.

* Mon Nov 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.6-alt1
- New version (0.6.6) with rpmgs script.

* Tue Oct 01 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.5-alt1
- New version (0.6.5) with rpmgs script.

* Thu Sep 26 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.4-alt1
- New version (0.6.4) with rpmgs script.

* Tue Aug 06 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.3-alt1
- 0.6.3
- Fixed crash with vlc backend

* Mon Aug 05 2019 Leontiy Volodin <lvol@altlinux.org> 0.6.2-alt1
- 0.6.2

* Mon Jul 15 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt2
- Added BR.

* Thu Jul 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.5.5-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec)

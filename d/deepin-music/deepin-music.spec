%def_without clang

%define repo dmusic
%define dmusic_ver 1

Name: deepin-music
Version: 7.0.5
Release: alt2

Summary: Awesome music player with brilliant and tweakful UI Deepin-UI based

License: GPL-3.0+
Group: Sound
Url: https://github.com/linuxdeepin/deepin-music

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Sat Oct 28 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavutil-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libmpris-qt5 libp11-kit libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-multimedia libdqt5-network libdqt5-printsupport libdqt5-qml libdqt5-qmlmodels libdqt5-quick libdqt5-sql libdqt5-svg libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libudisks2-qt5 pkg-config python3 python3-base python3-dev python3-module-setuptools dqt5-base-devel dqt5-declarative-devel dqt5-tools sh5 zlib-devel
BuildRequires: cmake kf5-kcodecs-devel libSDL2-devel libavformat-devel libdtkdeclarative-devel libdtkwidget-devel libtag-devel libvlc-devel mpris-qt5-devel dqt5-multimedia-devel dqt5-svg-devel dqt5-tools-devel dqt5-declarative-devel udisks2-qt5-devel

%if_with clang
BuildRequires: clang-devel
BuildRequires: lld-devel
%else
BuildRequires: gcc-c++
%endif

Requires: vlc-mini ffmpeg dtkdeclarative

%description
%summary.

%package -n lib%repo%dmusic_ver
Summary: %repo library for %name
Group: System/Libraries
Provides: lib%name = %version
Obsoletes: lib%name < %version

%description -n lib%repo%dmusic_ver
The package provides %repo library for %name.

%package -n lib%repo-devel
Summary: Static libraries for %name
Group: Development/C++
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%repo-devel
The package provides development files for %repo library.

%prep
%setup
%patch -p1

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
%define optflags_lto %nil
%endif
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DLIB_INSTALL_DIR=%_libdir \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DVERSION=%version
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %name

%files -f %name.lang
%doc CHANGELOG.md LICENSE README.md
%_bindir/%name
# package translations outside %%find_lang
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin-music_ky@Arab.qm
# ---
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/deepin-music/
%_datadir/dsg/configs/deepin-music/org.deepin.music.json
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/music/

%files -n lib%repo%dmusic_ver
%_libdir/lib%repo.so.%{dmusic_ver}*

%files -n lib%repo-devel
%_libdir/lib%repo.so

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.5-alt2
- Built via separate qt5 instead system (ALT #48138).

* Thu Apr 18 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.5-alt1
- New version 7.0.5.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.3.0.4.8ae2-alt1
- New version 7.0.3-4-g8ae2ac1c.
- No more needed libqt5-core = %%_qt5_version.

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.3.0.1.6a82-alt1
- New version 7.0.3-1-g6a8242f9.
- Requires: libqt5-core = %%_qt5_version.

* Sat Oct 28 2023 Leontiy Volodin <lvol@altlinux.org> 7.0.3-alt1
- New version 7.0.3.
- Fixed build using gcc.
- Added dmusic subpackages.
- Fixed underlinked icui18n.
- Removed static subpackage.

* Thu Jul 21 2022 Leontiy Volodin <lvol@altlinux.org> 6.2.17-alt1
- New version (6.2.17).

* Fri May 06 2022 Leontiy Volodin <lvol@altlinux.org> 6.2.13-alt1
- New version (6.2.13).

* Wed Feb 09 2022 Leontiy Volodin <lvol@altlinux.org> 6.2.8-alt1
- New version (6.2.8).

* Fri Aug 27 2021 Leontiy Volodin <lvol@altlinux.org> 6.1.7-alt2
- Disabled static library.
- Temporarily disabled link-time optimization.

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 6.1.7-alt1
- New version (6.1.7).
- Built with gcc10 instead clang12.
- spec:
  + Adapted to new cmake macros.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 6.1.4-alt1
- New version (6.1.4) with rpmgs script.

* Wed Apr 14 2021 Leontiy Volodin <lvol@altlinux.org> 6.1.2-alt1
- New version (6.1.2) with rpmgs script.

* Fri Mar 05 2021 Leontiy Volodin <lvol@altlinux.org> 6.0.1.91-alt2
- Fixed paths.
- Built with gcc10.
- Renamed libdeepin-music to libdmusic.

* Wed Dec 02 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.91-alt1
- New version (6.0.1.91) with rpmgs script.

* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.75-alt1
- New version (6.0.1.75) with rpmgs script.
- Built with cmake and ninja.
- Built with gcc instead clang.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.20-alt1
- New version (6.0.1.20) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.8-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).

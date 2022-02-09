%def_disable clang
%def_disable static

%define repo dmusic
%define optflags_lto %nil

Name: deepin-music
Version: 6.2.8
Release: alt1
Summary: Awesome music player with brilliant and tweakful UI Deepin-UI based
License: GPL-3.0+ and LGPL-2.1+
Group: Sound
Url: https://github.com/linuxdeepin/deepin-music

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-kf5 cmake rpm-build-ninja
BuildRequires: git-core
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: libicu-devel
BuildRequires: libtag-devel
BuildRequires: libavutil-devel
BuildRequires: libavformat-devel
BuildRequires: libcue-devel
BuildRequires: dtk5-core-devel
BuildRequires: dtk5-widget-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: libXext-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libvlc-devel
BuildRequires: gsettings-qt-devel
BuildRequires: mpris-qt5-devel
BuildRequires: dbusextended-qt5-devel
BuildRequires: udisks2-qt5-devel
BuildRequires: deepin-qt-dbus-factory-devel
Requires: vlc-mini ffmpeg
# Requires: lib%%repo-static = %%version

%description
%summary.

%if_enabled static
%package -n lib%repo-devel-static
Summary: Static libraries for %name
Group: Development/Other
Provides: lib%name = %version
Obsoletes: lib%name < %version
Provides: %name-devel = %version
Obsoletes: %name-devel < %version
# Provides: lib%%name-static = %%version
# Obsoletes: lib%%name-static < %%version

%description -n lib%repo-devel-static
This package provides static libraries for %name.
%endif

%prep
%setup
sed -i 's|/usr/lib/deepin-aiassistant/|%_libdir/deepin-aiassistant/|' \
    src/libmusic-plugin/CMakeLists.txt

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DLIB_INSTALL_DIR=%_libdir \
    -DAPP_VERSION=%version \
    -DVERSION=%version
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install
%find_lang %name

%if_disabled static
rm -f %buildroot%_libdir/lib%repo.a
%endif

%files -f %name.lang
%doc CHANGELOG.md COPYING LICENSE README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_libdir/deepin-aiassistant/
%dir %_libdir/deepin-aiassistant/serivce-plugins/
%_libdir/deepin-aiassistant/serivce-plugins/libmusic-plugin.so
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/music/

%if_enabled static
%files -n lib%repo-devel-static
%_libdir/lib%repo.a
%endif

%changelog
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

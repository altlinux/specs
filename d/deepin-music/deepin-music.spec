%def_without clang

%define repo dmusic
%define dmusic_ver 1

Name: deepin-music
Version: 7.0.56
Release: alt1

Summary: Awesome music player with brilliant and tweakful UI Deepin-UI based

License: GPL-3.0+
Group: Sound
Url: https://github.com/linuxdeepin/deepin-music
VCS: https://github.com/linuxdeepin/deepin-music

# Source-url: https://github.com/linuxdeepin/deepin-music/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Wed Aug 13 2025
# optimized out: cmake cmake-modules dqt6-base-devel dqt6-tools gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 icu-utils libavcodec-devel libavutil-devel libcairo-gobject libdouble-conversion3 libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-multimedia libdqt6-network libdqt6-opengl libdqt6-printsupport libdqt6-qml libdqt6-qmlmeta libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-sql libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libgdk-pixbuf libglvnd-devel libgpg-error libmpris-dqt6-1 libopencore-amrnb0 libopencore-amrwb0 libp11-kit librabbitmq-c4 libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libx265-215 libxkbcommon-devel ninja-build ocl-icd pkg-config python3 python3-base samba-common-libs sh5 vulkan-headers zlib-devel
BuildRequires: dqt6-5compat-devel dqt6-declarative-devel dqt6-multimedia-devel dqt6-sql-interbase dqt6-sql-mysql dqt6-sql-odbc dqt6-sql-postgresql dqt6-tools-devel libSDL2-devel libavformat-devel libdtk6declarative-devel libdtk6widget-devel libicu-devel libmpris-dqt6-devel libvlc-devel taglib-devel

%if_with clang
BuildRequires: clang-devel
BuildRequires: lld-devel
%else
BuildRequires: gcc-c++
%endif

Requires: vlc-mini ffmpeg dtk6declarative

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
%DQ6build \
  -DVERSION=%version \
#

%install
%DQ6install
%find_lang --with-qt %name

%files -f %name.lang
%doc debian/changelog LICENSE README.md
%_bindir/%name
# package translations outside %%find_lang
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin-music.qm
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
%_libdir/lib%repo.so.%{dmusic_ver}.0*

%files -n lib%repo-devel
%_libdir/lib%repo.so

%changelog
* Mon Apr 27 2026 Leontiy Volodin <lvol@altlinux.org> 7.0.56-alt1
- New version 7.0.56.

* Tue Mar 03 2026 Leontiy Volodin <lvol@altlinux.org> 7.0.54-alt1
- New version 7.0.54.

* Thu Oct 30 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.48-alt1
- New version 7.0.48.

* Thu Sep 25 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.47-alt1
- New version 7.0.47.

* Wed Sep 03 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.44-alt1
- New version 7.0.44.
- Added VCS tag.

* Wed Aug 13 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.42-alt1
- New version 7.0.42.
- Switched to dQt6.
- Fixed build with ffmpeg 7 (by upstream).

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

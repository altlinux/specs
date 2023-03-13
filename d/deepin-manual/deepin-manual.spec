%ifarch %e2k ppc64le riscv64
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: deepin-manual
Version: 5.8.15
Release: alt2
Summary: Help files for DDE
License: GPL-3.0+ and CC0-1.0 and BSD-3-Clause
# LICENSES/: CC0-1.0 and CC-BY-4.0 and MIT and BSD-3-Clause and LGPL-3.0 and GPL-3.0
# tools/: CC0-1.0
# tests/: CC0-1.0 and GPL-3.0+
# src/: GPL-3.0+ and CC0-1.0 and BSD-3-Clause
# src/web*/*/qwebchannel.js: BSD-3-Clause or Qt.Commercial
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-manual
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
%ifarch aarch64 armh
Patch: deepin-manual-5.8.4-alt-aarch64-armh.patch
%endif

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-tools-devel qt5-webchannel-devel dtk5-widget-devel qt5-x11extras-devel libgmock-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif

Requires: %name-data

%description
%summary.

%package data
Summary: Data files for %name
Group: Graphical desktop/Other
%description data
Data files for %name.

%prep
%setup
%ifarch aarch64 armh
%patch -p1
%endif

%build
%if_enabled qtwebengine
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%endif

%files
%if_enabled qtwebengine
%doc LICENSE README.md CHANGELOG.md
%_bindir/dman
%_bindir/dmanHelper
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.Manual.Open.service
%_datadir/dbus-1/services/com.deepin.Manual.Search.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%endif

%files data
%if_enabled qtwebengine
%_datadir/%name/
%endif

%changelog
* Mon Mar 13 2023 Ivan A. Melnikov <iv@altlinux.org> 5.8.15-alt2
- build on riscv64 w/o qt5-webengine

* Fri Oct 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.15-alt1
- New version (5.8.15).
- Updated license tag.

* Wed Jun 01 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.8-alt1
- New version (5.8.8).

* Thu Feb 10 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.4-alt1
- New version (5.8.4).

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 5.7.0.75-alt4
- Build empty packages on e2k and ppc64le.

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.75-alt3
- Fixed build with libgmock.so.1.11.0.

* Wed Jun 23 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.75-alt2
- Added deepin-manual-data in requires.

* Wed Jun 16 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.0.75-alt1
- New version (5.7.0.75) with rpmgs script.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 5.7.0.7-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.7.0.7-alt1
- Initial build for ALT Sisyphus.

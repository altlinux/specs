%define repo deepin-manual

%ifarch %not_qt5_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: deepin-help
Version: 6.0.6.0.4.35f8
Release: alt1

Summary: Help files for DDE

License: GPL-3.0-or-later and CC0-1.0 and BSD-3-Clause
# LICENSES/: CC0-1.0 and CC-BY-4.0 and MIT and BSD-3-Clause and LGPL-3.0 and GPL-3.0
# tools/: CC0-1.0
# tests/: CC0-1.0 and GPL-3.0-or-later
# src/: GPL-3.0+ and CC0-1.0 and BSD-3-Clause
# src/web*/*/qwebchannel.js: BSD-3-Clause or Qt.Commercial
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-manual

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: %repo = %EVR
Obsoletes: %repo < %EVR

Requires: %name-data

BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-tools-devel qt5-webchannel-devel dtk5-widget-devel qt5-x11extras-devel libgmock-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif

%description
%summary.

%package data
Summary: Data files for %name
Group: Graphical desktop/Other
Provides: %repo-data = %EVR
Obsoletes: %repo-data < %EVR

%description data
Data files for %name.

%prep
%setup -n %repo-%version
%patch -p1

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
%_desktopdir/%repo.desktop
%_datadir/dbus-1/services/com.deepin.Manual.Open.service
%_datadir/dbus-1/services/com.deepin.Manual.Search.service
%_iconsdir/hicolor/scalable/apps/%repo.svg
%endif

%files data
%if_enabled qtwebengine
%_datadir/%repo/
%endif

%changelog
* Thu Jan 11 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.6.0.4.35f8-alt1
- New version 6.0.6-4-g35f8e3d3.
- Renamed package from deepin-manual to deepin-help (not by upstream).

* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 6.0.4-alt1.1
- NMU: employ rpm-macros-qt5-webengine (fixes build on loongarch64).

* Mon Mar 13 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt1
- New version (6.0.4).

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

%ifarch %not_dqt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: deepin-manual
Version: 6.5.48
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

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: deepin-help
Obsoletes: deepin-help

BuildRequires(pre): rpm-macros-dqt6 rpm-macros-dqt6-webengine
# Automatically added by buildreq on Fri Aug 08 2025
# optimized out: cmake cmake-modules dqt6-base-devel dqt6-declarative-devel dqt6-tools gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-opengl libdqt6-pdf libdqt6-positioning libdqt6-printsupport libdqt6-qml libdqt6-qmlmeta libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-quickwidgets libdqt6-sql libdqt6-waylandclient libdqt6-webchannel libdqt6-webenginecore libdqt6-webenginewidgets libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel ninja-build pipewire-libs pkg-config python3 python3-base sh5 vulkan-headers
BuildRequires: dqt6-5compat-devel dqt6-positioning-devel dqt6-sql-interbase dqt6-sql-mysql dqt6-sql-odbc dqt6-sql-postgresql dqt6-tools-devel dqt6-webchannel-devel dtk6-common-devel libcups-devel libdtk6widget-devel libwayland-client-devel
BuildRequires: libsystemd-devel
%if_enabled qtwebengine
BuildRequires: dqt6-webengine-devel
%endif

Requires: %name-data

%description
%summary.

%package data
Summary: Data files for %name
Group: Graphical desktop/Other
Provides: deepin-help-data
Obsoletes: deepin-help-data

%description data
Data files for %name.

%prep
%setup
%patch -p1

%build
%if_enabled qtwebengine
%DQ6build \
  -DVERSION=%version \
#

%install
%DQ6install
%endif

%files
%if_enabled qtwebengine
%doc LICENSE README.md debian/changelog
%_bindir/dman
%_bindir/dmanHelper
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.Manual.Open.service
%_datadir/dbus-1/services/com.deepin.Manual.Search.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%_userunitdir/%name.service
%_datadir/metainfo/org.deepin.manual.metainfo.xml
%endif

%files data
%if_enabled qtwebengine
%_datadir/%name/
%endif

%changelog
* Mon Apr 13 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.48-alt1
- New version 6.5.48.

* Tue Jan 27 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.43-alt1
- New version 6.5.43.
- Fixed build on dtk 6.7.31.

* Fri Aug 08 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.36-alt1
- New version 6.5.36.
- Built via separate qt6 instead system (ALT #48138).
- Obsoleted deepin-help.

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

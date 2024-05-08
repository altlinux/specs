%define repo dde-launchpad

%def_disable clang

Name: deepin-launchpad
Version: 0.5.0
Release: alt1

Summary: Launcher for DDE - next generation

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-launchpad

Provides: %repo = %EVR
Conflicts: deepin-launcher
Obsoletes: deepin-launcher

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: cmake dtk6-common-devel libappstream-qt6-devel libdtk6gui-devel libgio-devel qt6-declarative-devel qt6-svg-devel qt6-tools-devel libsystemd-devel

Requires: qt6-declarative qt6-5compat

%description
%summary.

%prep
%setup -n %repo-%version

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_qt6_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md
%_bindir/%repo
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-launchpad.qm
%_datadir/metainfo/org.deepin.dde.launchpad.appdata.xml
%_userunitdir/org.deepin.dde.Launcher1.service
%_datadir/dbus-1/services/org.deepin.dde.Launcher1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dde-launchpad/
%_datadir/dsg/configs/dde-launchpad/org.deepin.dde.launchpad.appsmodel.json

%changelog
* Wed May 08 2024 Leontiy Volodin <lvol@altlinux.org> 0.5.0-alt1
- New version 0.5.0.
- Switched to qt6 and dtk6 by upstream.
- No more needed for qt hardlock requires.
- Built with appstream v1.

* Mon Mar 11 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.6-alt2
- Applied improvements for easy rebuilding with appstream v1.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.6-alt1
- New version 0.4.6.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt2
- Requires: libqt5-core = %%_qt5_version.

* Wed Jan 17 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt1
- New version 0.4.3.

* Tue Dec 26 2023 Leontiy Volodin <lvol@altlinux.org> 0.3.0.0.18.caf2-alt1
- Initial build for ALT Sisyphus.

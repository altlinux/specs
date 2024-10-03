%define repo dde-launchpad

%def_disable clang

Name: deepin-launchpad
Version: 0.6.12
Release: alt2

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
BuildRequires: cmake dtk6-common-devel libappstream-qt6-devel libdtk6gui-devel libgio-devel dqt6-declarative-devel dqt6-svg-devel dqt6-tools-devel libsystemd-devel

Requires: dqt6-declarative

%description
%summary.

%prep
%setup -n %repo-%version
sed -i 's|AppStreamQt|AppStreamQt6|' \
  CMakeLists.txt \
  desktopintegration.cpp

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt6_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt6_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH=%_dqt6_libdir \
#
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
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt2
- Built with separate qt6 (ALT #48138).

* Fri May 17 2024 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt1
- New version 0.6.12.

* Wed May 08 2024 Leontiy Volodin <lvol@altlinux.org> 0.6.9-alt1
- New version 0.6.9.

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

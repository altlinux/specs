%define repo dde-launchpad

%def_disable clang

Name: deepin-launchpad
Version: 0.4.3
Release: alt2

Summary: Launcher for DDE - next generation

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo

Provides: %repo = %EVR
Conflicts: deepin-launcher
Obsoletes: deepin-launcher

Source: %url/archive/%version/%repo-%version.tar.gz
# fix build with AppStreamQt < 1.0
Patch1: deepin-lauchpad-upstream-AppStreamQt1_1.patch
Patch2: deepin-lauchpad-upstream-AppStreamQt1.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-qt5
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: cmake qt5-tools-devel qt5-declarative-devel qt5-svg-devel qt5-quickcontrols2-devel libgtest-devel dtk6-common-devel dtkcore libdtkgui-devel libappstream-qt-devel libsystemd-devel libgio-devel

Requires: libqt5-core = %_qt5_version

%description
%summary.

%prep
%setup -n %repo-%version
%patch1 -p1 -R
%patch2 -p1 -R

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_qt5_bindir:$PATH
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
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/org.deepin.dde.Launcher1.service
%_datadir/dbus-1/services/org.deepin.dde.Launcher1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dde-launchpad/
%_datadir/dsg/configs/dde-launchpad/org.deepin.dde.launchpad.appsmodel.json

%changelog
* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt2
- Requires: libqt5-core = %%_qt5_version.

* Wed Jan 17 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt1
- New version 0.4.3.

* Tue Dec 26 2023 Leontiy Volodin <lvol@altlinux.org> 0.3.0.0.18.caf2-alt1
- Initial build for ALT Sisyphus.

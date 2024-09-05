%define repo dde-appearance

%def_disable clang

Name: deepin-appearance
Version: 1.1.28
Release: alt1

Summary: Set the theme and appearance of DDE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo

Provides: %repo = %EVR

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
BuildRequires: cmake dqt5-tools-devel dtk6-common-devel dtkcore libdtkgui-devel kf5-kconfig-devel kf5-kwindowsystem-devel kf5-kglobalaccel-devel gsettings-qt-devel libgio-devel libXcursor-devel libXfixes-devel libgtk+3-devel libxcbutil-cursor-devel libsystemd-devel
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif

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
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md
%_bindir/%repo
%_bindir/dde-fakewm
%_userunitdir/%repo.service
%dir %_datadir/%repo/
%_datadir/%repo/custom.svg
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-appearance_ky@Arab.qm
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/%repo.service
%_datadir/dbus-1/services/com.deepin.wm.service
%_datadir/dbus-1/services/org.deepin.dde.Appearance1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.appearance/
%_datadir/dsg/configs/org.deepin.dde.appearance/org.deepin.dde.appearance.json

%changelog
* Mon May 27 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.28-alt1
- New version 1.1.28.
- Built via separate qt5 instead system (ALT #48138).

* Tue Mar 26 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.26-alt1
- New version 1.1.26.

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.25-alt1
- New version 1.1.25.

* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 1.1.7-alt1.git9f81088
- Initial build for ALT Sisyphus.

%def_disable clang

%define repo dde-launcher

Name: deepin-launcher
Version: 5.5.37
Release: alt1
Summary: Deepin desktop-environment - Launcher module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-launcher
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-tools-devel
BuildRequires: dtk5-core-devel
BuildRequires: dtk5-widget-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libgmock-devel
BuildRequires: dtk5-common
# Requires: deepin-menu deepin-daemon startdde icon-theme-hicolor

%description
%summary.

%prep
%setup -n %repo-%version

%build
export PATH=%_qt5_bindir:$PATH
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
    -DWITHOUT_UNINSTALL_APP=1 \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc LICENSE
%_bindir/%repo
%_bindir/%repo-wapper
%_datadir/%repo/
%_datadir/dbus-1/services/*.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/glib-2.0/schemas/com.deepin.dde.launcher.gschema.xml
%_desktopdir/%repo.desktop
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.launcher/
%_datadir/dsg/configs/org.deepin.dde.launcher/org.deepin.dde.launcher.json

%changelog
* Mon Dec 05 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.37-alt1
- New version (5.5.37).

* Mon Oct 31 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.35-alt1
- New version (5.5.35).

* Tue Aug 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.27-alt1
- New version (5.5.27).

* Fri Jun 03 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.19-alt1
- New version (5.5.19).
- Fixed build with new dtkcommon.

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.11-alt1
- New version (5.5.11).

* Mon Mar 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.6-alt1
- New version (5.5.6).
- Checkout to master branch.

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.37-alt1
- New version (5.4.37).

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.11-alt2
- Fixed build with libgmock.so.1.11.0.

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.11-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.11-alt1
- New version (5.4.11) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Fri Mar 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.4-alt1
- New version (5.4.4) with rpmgs script.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.45-alt1
- New version (5.3.0.45) with rpmgs script.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.41-alt1
- New version (5.3.0.41) with rpmgs script.

* Thu Dec 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.35-alt1
- New version (5.3.0.35) with rpmgs script.

* Tue Dec 15 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.29-alt3
- Changed default background.

* Mon Dec 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.29-alt2
- Fixed background.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.29-alt1
- New version (5.3.0.29) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.24-alt1
- New version (5.3.0.24) with rpmgs script.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).

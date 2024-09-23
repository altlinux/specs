%def_without clang

%define repo dde-launcher

Name: deepin-launcher
Version: 6.0.19
Release: alt2

Summary: Deepin desktop-environment - Launcher module

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-launcher

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

Provides: %name-devel = %version
Obsoletes: %name-devel < %version
Conflicts: deepin-launchpad
Obsoletes: deepin-launchpad

# Requires: deepin-menu deepin-daemon startdde icon-theme-hicolor

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# Automatically added by buildreq on Tue Oct 24 2023
# optimized out: bash5 bashrc cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxcb-devel libxcbutil-icccm pkg-config python3 python3-base qt5-base-devel sh5
BuildRequires: cmake dtk6-common-devel dtkcore gsettings-qt-devel libdtkwidget-devel libgio-devel libxcbutil-icccm-devel dqt5-svg-devel dqt5-tools dqt5-x11extras-devel
%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package devel
Summary: Development package for %name
Group: Development/C++

%description devel
%summary.
The package provides development files for %name.

%prep
%setup -n %repo-%version

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
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
%doc LICENSE
%_bindir/%repo
%_datadir/dbus-1/services/*.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/glib-2.0/schemas/com.deepin.dde.launcher.gschema.xml
%_userunitdir/org.deepin.dde.Launcher1.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/org.deepin.dde.Launcher1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dde-launcher/
%_datadir/dsg/configs/dde-launcher/org.deepin.dde.launcher.json
# outside find_lang
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/%repo.qm
%_datadir/%repo/translations/%{repo}_es_419.qm
%_datadir/%repo/translations/%{repo}_ky@Arab.qm

%files devel
%dir %_includedir/dde-launcher/
%_includedir/dde-launcher/*.h

%changelog
* Mon Sep 23 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt2
- Built via separate qt5 instead system (ALT #48138).

* Tue Dec 26 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt1
- New version 6.0.19.
- Cleanup BRs.
- Used default compiler versions for easy backporting.

* Tue Oct 31 2023 Ivan A. Melnikov <iv@altlinux.org> 5.6.1-alt3.1
- NMU: build with gcc 13 (fixes build on loongarch64).

* Wed Feb 01 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.1-alt3
- Fixed build with dtkgui 5.6.4.

* Wed Dec 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.1-alt2
- Fixed window mode show slowly.

* Thu Dec 15 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.1-alt1
- New version (5.6.1).

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

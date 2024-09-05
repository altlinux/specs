%define sover 6

%def_disable clang

%define _cmake__builddir BUILD
%define repo dde-control-center

Name: deepin-control-center
Version: 6.0.54
Release: alt1

Summary: New control center for Linux Deepin

License: GPL-3.0-or-later and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-control-center

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch
Patch1: deepin-control-center-6.0.47-alt-qch.patch

# Requires: deepin-account-faces deepin-api deepin-daemon deepin-qt5integration deepin-network-utils GeoIP-GeoLite-data GeoIP-GeoLite-data-extra gtk-murrine-engine proxychains-ng redshift startdde
# Requires: libdeepin-pw-check

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
# Automatically added by buildreq on Mon Oct 23 2023
# optimized out: bash5 bashrc cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libpolkit-qt5-agent libpolkit-qt5-core libpolkit-qt5-gui libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-help libdqt5-multimedia libdqt5-network libdqt5-printsupport libdqt5-sql libdqt5-svg libdqt5-test libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel perl perl-Config-Tiny perl-Encode perl-XML-LibXML perl-parent pkg-config python3 python3-base dqt5-base-common dqt5-base-devel dqt5-tools sh5
BuildRequires: cmake deepin-gettext-tools doxygen libdeepin-pw-check-devel dtk6-common-devel libdtkwidget-devel libpolkitqt5-qt5-devel dqt5-tools dqt5-multimedia-devel dqt5-svg-devel dqt5-wayland-devel libgtest-devel gsettings-qt-devel libsystemd-devel

%description
New control center for Linux Deepin.

%package -n libdcc-interface%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdcc-interface%sover
This package provides library for %name.

%package -n libdcc-widgets%sover
Summary: Library for %name
Group: System/Libraries

%description -n libdcc-widgets%sover
This package provides library for %name.

%package devel
Summary: %summary
Group: Development/Other

%description devel
%summary.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export CPLUS_INCLUDE_PATH=%_dqt5_headerdir/QtXkbCommonSupport/%{_dqt5_version}:%_includedir/qt5:$CPLUS_INCLUDE_PATH
export SYSTYPE=Desktop
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
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DCVERSION=%version \
    -DDISABLE_AUTHENTICATION=ON \
    -DDISABLE_UPDATE=ON \
    -DDISABLE_SOUND_ADVANCED=ON \
%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc LICENSE README.md
%_bindir/%repo
%_desktopdir/org.deepin.dde.control-center.desktop
%_datadir/metainfo/org.deepin.dde.controlcenter.metainfo.xml
%_datadir/dbus-1/services/org.deepin.dde.ControlCenter1.service
%dir %_libdir/%repo/
%dir %_libdir/%repo/modules/
%_libdir/%repo/modules/libdcc*.so
%dir %_libdir/dde-grand-search-daemon/
%dir %_libdir/dde-grand-search-daemon/plugins/
%dir %_libdir/dde-grand-search-daemon/plugins/searcher/
%_libdir/dde-grand-search-daemon/plugins/searcher/org.deepin.dde-grand-search.dde-control-center-setting.conf
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.control-center/
%_datadir/dsg/configs/org.deepin.dde.control-center/org.deepin.dde.control-center*.json
%_datadir/dsg/configs/org.deepin.region-format.json
%_datadir/doc/dqt5/dde-control-center.qch
%dir %_datadir/%repo/
%_datadir/%repo/developdocument.html
%_userunitdir/org.deepin.dde.control-center.service
# package outside find_lang
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/*es_419.qm
%_datadir/%repo/translations/*ky@Arab.qm

%files -n libdcc-interface%sover
%_libdir/libdcc-interface.so.%{sover}*

%files -n libdcc-widgets%sover
%_libdir/libdcc-widgets.so.%{sover}*

%files devel
%dir %_libdir/cmake/DdeControlCenter/
%_libdir/cmake/DdeControlCenter/DdeControlCenter*.cmake
%_includedir/%repo/
%_libdir/libdcc-interface.so
%_libdir/libdcc-widgets.so

%changelog
* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.54-alt1
- New version 6.0.54.
- Built via separate qt5 instead system (ALT #48138).

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.47-alt3
- NMU: fixed FTBFS.

* Mon Apr 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.47-alt2
- Fixed the path to the qt5 qch file.

* Mon Apr 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.47-alt1
- New version 6.0.47.

* Thu Feb 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.44-alt1
- New version 6.0.44.

* Thu Jan 25 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.43-alt1
- New version 6.0.43.
- Fixed license tag.

* Sat Dec 02 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.35-alt1
- New version 6.0.35.
- Cleanup spec and BRs.
- Removed binding to KF5.

* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 5.6.3-alt1.1
- NMU: Cleanup usage of %%K5* macros (fixes FTBFS).

* Wed Jan 11 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version (5.6.3).
- Cleanup spec.

* Wed Dec 14 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.1-alt1
- New version (5.6.1).

* Mon Oct 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.157-alt1
- New version (5.5.157).

* Tue Sep 13 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.149-alt1
- New version (5.5.149).

* Mon Aug 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.144-alt1
- New version (5.5.144).

* Fri Jun 03 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.34-alt2
- Fixed build with new dtkcommon.

* Wed Jun 01 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.34-alt1
- New version (5.5.34).

* Fri Apr 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.16.2-alt1
- New version (5.5.16.2).
- Built with deepin-pw-check again (without cracklib).

* Wed Aug 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.70-alt1
- New version (5.4.70).
- Remove deepin-pw-check from BuildRequires.

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.47-alt2.git1362dfe
- Fixed build with libgmock.so.1.11.0.

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.47-alt1.git1362dfe
- Fixed version tag.

* Fri Jun 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt3.git1362dfe
- Temporarily hidden the widget to set the lockscreen timeout.

* Thu Jun 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt2.git1362dfe
- Build git snapshot.
- Disabled General Settings.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt1
- New version (5.4.23) with rpmgs script.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt2
- Fixed build with dtk 5.4.13.

* Tue Apr 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt1
- New version (5.4.17) with rpmgs script (thanks archlinux for the patch).

* Wed Mar 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.9-alt1
- New version (5.4.9) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.82-alt1
- New version (5.3.0.82) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.68-alt1
- New version (5.3.0.68) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.44-alt1
- New version (5.3.0.44) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).

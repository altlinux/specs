%define repo dde-clipboard
%def_disable clang

Name: deepin-clipboard
Version: 6.0.9
Release: alt1

Summary: Clipboard for DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-clipboard

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# Automatically added by buildreq on Fri Dec 15 2023
# optimized out: bash5 bashrc cmake cmake-modules dtkcore gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libgio-qt libglibmm-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-svg libdqt5-test libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libsigc++2-devel libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-client-devel pkg-config python3 python3-base python3-dev python3-module-setuptools dqt5-base-devel sh5 wayland-devel
BuildRequires: dtk6-common-devel dwayland-devel extra-cmake-modules libdtkwidget-devel libgio-qt-devel libgtest-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel dqt5-tools
BuildRequires: libsystemd-devel
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
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
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
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
%_bindir/%{repo}*
%_datadir/dbus-1/services/org.deepin.dde.Clipboard1.service
%_datadir/dbus-1/services/org.deepin.dde.ClipboardLoader1.service
%_datadir/dbus-1/services/org.deepin.dde.daemon.Clipboard1.service
%_userunitdir/%repo-daemon.service
%_userunitdir/%repo.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/dde-clipboard.service
# translations
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-clipboard.qm
%_datadir/%repo/translations/dde-clipboard_es_419.qm
%_datadir/%repo/translations/dde-clipboard_ky@Arab.qm

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- New version 6.0.9.
- Built via separate qt5 instead system (ALT #48138).

* Fri Dec 15 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Cleanup BRs.

* Fri Jan 20 2023 Leontiy Volodin <lvol@altlinux.org> 5.4.25-alt1
- New version (5.4.25).

* Tue Nov 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.24-alt1
- New version (5.4.24).

* Fri Oct 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt1
- New version (5.4.23).

* Mon Sep 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20).
- Built via cmake instead qmake.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.16-alt1
- New version (5.3.16) with rpmgs script.

* Tue Apr 13 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.15-alt1
- New version (5.3.15) with rpmgs script.

* Fri Mar 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.11-alt1
- Initial build for ALT Sisyphus.

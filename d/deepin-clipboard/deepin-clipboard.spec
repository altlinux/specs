%define repo dde-clipboard
%def_disable clang
%def_disable qmake

Name: deepin-clipboard
Version: 5.4.24
Release: alt1
Summary: Clipboard for DDE
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-clipboard
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
%if_disabled qmake
BuildRequires(pre): cmake rpm-build-ninja
%endif
BuildRequires: qt5-base-devel qt5-tools
BuildRequires: kf5-kwayland-devel
BuildRequires: dtk5-widget-devel dtk5-common
BuildRequires: libgio-qt-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libgtest-devel
Requires: lcov

%description
%summary.

%prep
%setup -n %repo-%version

%build
export PATH=%_qt5_bindir:$PATH

%if_enabled qmake
  %qmake_qt5 \
    %if_enabled clang
      QMAKE_STRIP= -spec linux-clang \
    %endif
      CONFIG+=nostrip \
      PREFIX=%_prefix \
#
  %make_build
%else
  %if_enabled clang
    export CC="clang"
    export CXX="clang++"
    export AR="llvm-ar"
  %endif

  %cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
  cmake --build "%_cmake__builddir" -j%__nprocs
%endif

%install
%if_enabled qmake
  %makeinstall INSTALL_ROOT=%buildroot
%else
  %cmake_install
%endif

mkdir -p %buildroot%_libexecdir/systemd/user/
mv -f %buildroot/lib/systemd/user/%repo-daemon.service %buildroot%_libexecdir/systemd/user/

%find_lang %name

%files -f %name.lang
%doc LICENSE
%_bindir/%{repo}*
%_datadir/%repo/
%_desktopdir/%{repo}*.desktop
%_sysconfdir/xdg/autostart/%{repo}*.desktop
%_datadir/dbus-1/services/com.deepin.dde.Clipboard.service
%_libexecdir/systemd/user/%repo-daemon.service

%changelog
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

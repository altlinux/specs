%define soname 0

Name: deepin-turbo
Version: 0.0.6.3
Release: alt1
Summary: A daemon that helps to launch applications faster
License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-turbo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel libdbus-devel libsystemd-devel dtk5-common dtk5-widget-devel

%description
%summary.
Deepin-trubo is a deepin project that derives from Applauncherd.

%package -n lib%name%soname
Summary: The library for %name
Group: System/Libraries

%description -n lib%name%soname
This package provides the library for %name.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
This package provides development files for %name.

%prep
%setup
# Fix python shebang.
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' scripts/library-helper.py
# Fix unmets.
sed -i 's|/usr/lib/binfmt.d|%_binfmtdir|' src/booster-desktop/CMakeLists.txt

%build
%cmake \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc CHANGELOG LICENSE README.md
%_bindir/deepin-turbo-invoker
%_bindir/deepin-turbo-single-instance
%_binfmtdir/desktop.conf
%_libexecdir/%name/

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files devel
%_includedir/%name/
%_libdir/lib%name.so

%changelog
* Thu Jun 09 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.6.3-alt1
- New version.
- Upstream:
  + fix: Repair the wm class name error using the window.
  + fix: The problem of collapse when the parameters are more frequent.
  + chore: Modify LGPL to GPL.
  + chore: V20 goes up booster service.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.0.5-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon Apr 19 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.5-alt1
- New version (0.0.5) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.3-alt1.git387889d
- Initial build for ALT Sisyphus.

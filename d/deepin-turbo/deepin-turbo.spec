Name: deepin-turbo
Version: 0.0.5
Release: alt1
Summary: A daemon that helps to launch applications faster
License: LGPL-2.1
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-turbo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel libdbus-devel libsystemd-devel dtk5-common dtk5-widget-devel

%description
%summary.
Deepin-trubo is a deepin project that derives from Applauncherd.

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
    -DCMAKE_BUILD_TYPE=Debug
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files
%doc CHANGELOG COPYING.LESSER README.md
%_bindir/deepin-turbo-invoker
%_bindir/deepin-turbo-single-instance
%_libdir/lib%name.so.*
%_binfmtdir/desktop.conf
%_libexecdir/%name/
%_libexecdir/systemd/user/*.service

%files devel
%_includedir/%name/
%_libdir/lib%name.so

%changelog
* Mon Apr 19 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.5-alt1
- New version (0.0.5) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.3-alt1.git387889d
- Initial build for ALT Sisyphus.

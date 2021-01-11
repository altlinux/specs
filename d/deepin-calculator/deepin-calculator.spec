%def_disable clang

Name: deepin-calculator
Version: 5.6.0.10
Release: alt1
Summary: An easy to use calculator for ordinary users
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-calculator
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: cmake qt5-linguist qt5-base-devel qt5-svg-devel dtk5-widget-devel deepin-qt-dbus-factory-devel
Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh
%__subst '1i#include <QPainterPath>' src/views/simplelistdelegate.cpp

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake_insource -GNinja
%ninja_build

%install
%ninja_install

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.0.10-alt1
- New version (5.6.0.10) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.7-alt1
- New version (5.6.0.7) with rpmgs script.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.1-alt1
- New version (5.6.0.1) with rpmgs script.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.5.28-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).

Name: disomaster
Version: 5.0.8
Release: alt1
Summary: Library to manipulate DISC burning
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/disomaster
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
BuildRequires: gcc-c++ qt5-base-devel libisoburn-devel

%description
This package provides a libisoburn wrapper class for Qt.

%package -n lib%name
Summary: Library to manipulate DISC burning
Group: System/Libraries

%description -n lib%name
This package provides a libisoburn wrapper class for Qt.

%package devel
Summary: Development package for %name
Group: Development/KDE and QT
Requires: qt5-base-devel libisoburn-devel

%description devel
Header files and libraries for %name.

%prep
%setup
%__subst 's|/lib|/%_lib|' lib%name/lib%name.pro

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n lib%name
%doc README.md
%doc LICENSE
%_libdir/lib%name.so.1*

%files devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Sep 13 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.8-alt1
- New version (5.0.8) with rpmgs script.

* Tue Apr 13 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.7-alt1
- New version (5.0.7) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- New version (5.0.4) with rpmgs script.

* Fri Sep 25 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

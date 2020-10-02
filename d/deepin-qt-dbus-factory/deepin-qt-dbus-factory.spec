%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory

Name: deepin-qt-dbus-factory
Version: 5.3.0.11
Release: alt1
Summary: A repository stores auto-generated Qt5 dbus code
# The entire source code is GPLv3+ except
# libdframeworkdbus/qtdbusextended/ which is LGPLv2+
License: GPL-3.0-or-later and LGPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-qt-dbus-factory
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires: python3-devel libglvnd-devel qt5-base-devel

%description
A repository stores auto-generated Qt5 dbus code.

%package -n libdframeworkdbus2
Summary: Library for %name
Group: Development/KDE and QT

%description -n libdframeworkdbus2
A repository stores auto-generated Qt5 dbus code.
Library for %name.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%__subst 's|python|python3|' libdframeworkdbus/*.{pro,py}

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    LIB_INSTALL_DIR=%_libdir
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdframeworkdbus2
%doc README.md
%doc LICENSE
%_libdir/lib%soname.so.2*

%files devel
%_includedir/lib%soname-2.0/
%_libdir/cmake/DFrameworkdbus/
%_pkgconfigdir/%soname.pc
%_libdir/lib%soname.so

%changelog
* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

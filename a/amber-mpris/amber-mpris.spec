Name: amber-mpris
Version: 1.2.10
Release: alt1

Summary: Qt and QML MPRIS interface and adaptor
License: LGPL-2.1-or-later
Group: System/Libraries
Url: https://github.com/sailfishos/amber-mpris

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Qml)

%package -n libambermpris
Summary: Qt and QML MPRIS interface and adaptor
Group: System/Libraries

%package -n libambermpris-devel
Summary: Qt and QML MPRIS interface and adaptor
Group: Development/C++

%description
MPRIS v2 specification implementation for Qt and QML plugin.

%description -n libambermpris
MPRIS v2 specification implementation for Qt and QML plugin.

%description -n libambermpris-devel
MPRIS v2 specification implementation for Qt and QML plugin.

%prep
%setup

%build
%qmake_qt6 -o Makefile
%make_build

%install
make install INSTALL_ROOT=%buildroot

%files -n libambermpris
%doc COPYING README.md
%_libdir/*.so.*
%_libdir/qt6/qml/*

%files -n libambermpris-devel
%_includedir/AmberMpris
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Jun 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.10-alt1
- 1.2.10 released

* Tue Dec 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.9-alt1
- initial

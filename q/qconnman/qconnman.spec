Name: qconnman
Version: 1.24
Release: alt1

Summary: Qt wrapper library around the connman API
License: LGPLv2.1+
Group: System/Libraries

Url: https://bitbucket.org/devonit/qconnman
# https://bitbucket.org/devonit/qconnman/get/v%version.tar.bz2
Source: %name-%version.tar.bz2

BuildRequires: qt4-devel gcc-c++

%define libname lib%name

%description
Qt wrapper library around the connman API.

%package -n %libname
Summary: Qt wrapper library around the connman API
Group: System/Libraries

%description -n %libname
Qt wrapper library around the connman API.

%files -n %libname
%doc README AUTHORS
%_libdir/lib%name.so.*

%package -n %libname-devel
Summary: Development files for %name
Group: Development/KDE and QT

%description -n %libname-devel
Install this package if you need to compile applications that needs
%name.

%files -n %libname-devel
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc
%_includedir/%name/

%prep
%setup

%build
qmake-qt4 PREFIX=%prefix LIBDIR=%_lib
%make

%install
make install INSTALL_ROOT=%buildroot

%changelog
* Wed Mar 11 2015 Michael Shigorin <mike@altlinux.org> 1.24-alt1
- built for ALT Linux (based on Rosa's 1.24-1 package)


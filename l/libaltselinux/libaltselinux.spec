Name: libaltselinux
Version: 0.1.0
Release: alt1

Summary: Library for using SELinux on ALT Linux
License: GPLv3
Group: System/Libraries

Source: %name-%version.tar

BuildRequires: libselinux-devel

%description
Helper for using SELinux on ALT Linux

%package devel
Summary: Development tools for programs which will use the libaltselinux library
Group: Development/C
Requires: libaltselinux = %version-%release

%description devel
This package includes development files necessary for developing
programs which will using the libaltselinux library.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/libaltselinux.so.*

%files devel
%_libdir/libaltselinux.so
%_includedir/altselinux.h

%changelog
* Wed Feb 19 2014 Timur Aitov <timonbl4@altlinux.org> 0.1.0-alt1
- first build


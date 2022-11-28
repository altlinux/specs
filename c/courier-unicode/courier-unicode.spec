%def_disable static
%define soname 7

Summary: Courier Unicode Library
Name: courier-unicode
Version: 2.2.5
Release: alt0.1
License: GPLv3
Group: System/Libraries
Url: http://www.courier-mta.org/unicode/
Source: https://sourceforge.net/projects/courier/files/courier-unicode/%{version}/%{name}-%{version}.tar.bz2

Buildrequires: gcc-c++

%package -n lib%{name}%{soname}
Summary: Courier Unicode Library
Group: System/Libraries
Provides: %{name} = %EVR

%package devel
Summary: Courier Unicode Library development files
Group: Development/C++
Requires: lib%{name}%{soname} = %EVR

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C++
Requires: %name-devel = %EVR

%description
This library implements several algorithms related to the Unicode
Standard.

This package installs only the run-time libraries needed by applications
that use this library. Install the "courier-unicode-devel" package if you
want to develop new applications using this library.

%description -n lib%{name}%{soname}
This library implements several algorithms related to the Unicode
Standard.

This package installs only the run-time libraries needed by applications
that use this library. Install the "courier-unicode-devel" package if you
want to develop new applications using this library.

%description devel
This package contains development files for the Courier Unicode Library.
Install this package if you want to develop applications that uses this
unicode library.

%description -n %name-devel-static
This package contains libraries which are needs to compile programs statically
linked against %name library.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%make install DESTDIR=%buildroot

%files -n lib%{name}%{soname}
%doc README COPYING ChangeLog AUTHORS
%_libdir/*.so.*

%files devel
%_mandir/*/*
%_includedir/*
%_libdir/*.so
%_datadir/aclocal/*.m4
%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif # static

%changelog
* Mon Nov 28 2022 L.A. Kostis <lakostis@altlinux.ru> 2.2.5-alt0.1
- 2.2.5.

* Mon Sep 12 2022 L.A. Kostis <lakostis@altlinux.ru> 2.2.4-alt0.1
- 2.2.4.

* Fri Sep 03 2021 L.A. Kostis <lakostis@altlinux.ru> 2.2.3-alt0.1
- 2.2.3.

* Wed Mar 10 2021 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt0.1
- Updated to 2.1.2.
- Create lib soname package according Shared Libs Policy.
- Define -devel package as C++.

* Tue Jan 16 2018 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt0.1
- Updated to 2.0.

* Wed Jan 04 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt0.1
- Updated to 1.4.

* Tue Jul 28 2015 L.A. Kostis <lakostis@altlinux.ru> 1.3-alt0.1
- Rebuild for ALTLinux.

* Sun Jan 12 2014 Sam Varshavchik <mrsam@octopus.email-scan.com> - 1.0
- Initial build.


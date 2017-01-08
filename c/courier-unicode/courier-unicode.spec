%def_disable static

Summary: Courier Unicode Library
Name: courier-unicode
Version: 1.4
Release: alt0.1
License: GPLv3
Group: System/Libraries
Url: http://www.courier-mta.org/unicode/
Source: http://download.sourceforge.net/courier/%{name}-%{version}.tar.bz2

Buildrequires: gcc-c++

%package devel
Summary: Courier Unicode Library development files
Group: Development/C
Requires: %name = %version-%release

%package -n %name-devel-static
Summary: %name static development environment
Group: Development/C
Requires: %name-devel = %version-%release

%description
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

%files
%doc README COPYING ChangeLog AUTHORS
%_libdir/*.so.*

%files devel
%_mandir/*/*
%_includedir/*
%_libdir/*.so
%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif # static

%changelog
* Wed Jan 04 2017 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt0.1
- Updated to 1.4.

* Tue Jul 28 2015 L.A. Kostis <lakostis@altlinux.ru> 1.3-alt0.1
- Rebuild for ALTLinux.

* Sun Jan 12 2014 Sam Varshavchik <mrsam@octopus.email-scan.com> - 1.0
- Initial build.


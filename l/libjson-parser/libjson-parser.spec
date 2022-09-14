%define oname json-parser

Name: lib%oname
Version: 1.1.0
Release: alt1
Summary: Very low footprint JSON parser written in portable ANSI C
Group: System/Libraries
License: BSD-2-Clause
Url: https://github.com/udp/json-parser
Source: %name-%version.tar
Patch: %name-%version.patch

%description
Very low footprint JSON parser written in portable ANSI C

%package devel
Summary: Files needed to develop applications with Very low footprint JSON parser
Requires: %name = %EVR
Group: Development/C

%description devel
Files needed to develop applications with Very low footprint JSON parser

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install install-shared DESTDIR=%buildroot

%files
%doc README.md AUTHORS LICENSE
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%oname
%_datadir/pkgconfig/%oname.pc

%changelog
* Wed Sep 14 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- Initial build for ALT.


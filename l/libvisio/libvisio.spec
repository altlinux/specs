
Name: libvisio
Version: 0.1.3
Release: alt1.2
Summary: A library providing ability to interpret and import visio diagrams

Group: System/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
Url: http://www.freedesktop.org/wiki/Software/libvisio
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)
# build req on pkgconfig(icu-i18n) will build with old libicu when available (bug#31476)
BuildRequires: libicu-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(cppunit)

BuildRequires: doxygen
BuildRequires: gperf

%description
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Visio diagrams into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Visio diagrams into other formats.
Currently supported: XHTML, raw, plain text.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING.*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Sat Feb 13 2016 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt1.2
- NMU: fix build requires

* Fri Feb 12 2016 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt1.1
- NMU: rebuild with new libicu

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Thu Sep 05 2013 Fr. Br. George <george@altlinux.ru> 0.0.31-alt1
- Autobuild version bump to 0.0.31
- Build scheme changed

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.30-alt1
- initial build

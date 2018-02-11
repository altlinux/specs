
Name: libcdr
Version: 0.1.4
Release: alt1
Summary: A library providing ability to interpret and import Corel Draw drawings
Group: System/Libraries
License: MPL-2.0
URL: http://www.freedesktop.org/wiki/Software/libcdr
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(librevenge-0.0) >= 0.0.1 pkgconfig(librevenge-generators-0.0) pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(cppunit)
BuildRequires: boost-devel
BuildRequires: doxygen

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Corel Draw drawings into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Corel Draw drawings into other formats.
Currently supported: XHTML, text, raw.

%prep
%setup -q

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS COPYING.* README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING.*
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Sun Feb 11 2018 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Tue Feb 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- 0.1.2
- enable tests

* Wed Dec 17 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Tue May 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.0.16-alt1
- 0.0.16

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.14-alt1
- initial build

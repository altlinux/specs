
Name: libmspub
Version: 0.1.3
Release: alt1
Summary: A library providing ability to interpret and import Microsoft Publisher files
Group: System/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
Url: https://wiki.documentfoundation.org/DLP/Libraries/libmspub
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(librevenge-0.0) >= 0.0.1 pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-i18n)

BuildRequires: boost-devel
BuildRequires: doxygen

%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

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
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Microsoft Publisher files into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Microsoft Publisher files into other formats.
Currently supported: XHTML, raw.

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
%doc COPYING.*
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Tue Feb 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1.1
- rebuild

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.0.6-alt1
- initial build

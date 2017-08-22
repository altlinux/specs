Name: tcl-tdom
Version: 0.8.3
Release: alt0.2

Summary: A XML/DOM/XPath/XSLT implementation for Tcl
License: MPL
Group: Development/Tcl
Url: http://www.tdom.org

# http://git.altlinux.org/gears/t/tcl-tdom.git
Source: %name-%version-%release.tar

BuildRequires: tcl-devel >= 8.4.0-alt1 libexpat-devel

%package devel
Summary: A XML/DOM/XPath/XSLT implementation for Tcl - development files
Group: Development/C

%description
This package contains a freely distributable extension to Tcl
implementing memory channels, i.e. channels storing the data
placed into them in memory, not on disk.

%description devel
This package contains a freely distributable extension to Tcl
implementing memory channels, i.e. channels storing the data
placed into them in memory, not on disk.

This package contains development files.

%prep
%setup
%teapatch

%build
%autoreconf
%configure
%make_build all

%install
%makeinstall

%check
make test

%files
%_tcllibdir/libtdom%version.so
%_tcldatadir/tdom%version
%_mandir/mann/*

%files devel
%_includedir/tdom.h
%_tcllibdir/libtdomstub%version.a
%_libdir/tdomConfig.sh

%changelog
* Tue Jul 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.3-alt0.2
- Fixed FTBFS
- Fixed:
  + XPath element-available function
  + pkgIndex.tcl missing whitespace
  + generic/domxslt.c: wrong size on memcpy on 64 bit
- Built devel subpackage

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.3-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Sat Feb 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt0.1
- first build for %distribution

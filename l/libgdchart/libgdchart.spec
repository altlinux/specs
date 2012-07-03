Name: libgdchart
Version: 0.11.5
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Generate graphs using the GD library
License: BSD
Group: System/Libraries

URL: http://www.fred.net/brv/chart/
Source: http://www.fred.net/brv/chart/gdchart%{version}dev.tar.gz

# Automatically added by buildreq on Thu Jan 28 2010
BuildRequires: libfreetype-devel libgd2-devel libjpeg-devel libpng-devel

%description
A library for generating nice 2d and 3d graphs with the use of GD.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %name library.

%prep
%setup -n gdchart%{version}dev

%build
subst 's@/local@@' Makefile
subst 's@/usr/lib@%_libdir@' Makefile
subst 's/^EXTERND//' array_alloc.h  gdchart.h  gdcpie.h gdc.h
%make_build CFLAGS="%optflags -fPIC -fno-stack-protector"

# Author build only static library, but we need shared one.
ld -shared -soname libgdc.so.0.11.5 -o libgdc.so.0.11.5 price_conv.o gdc.o gdc_pie.o gdchart.o array_alloc.o -lm -lgd
ln -s libgdc.so.0.11.5 libgdc.so.0
ln -s libgdc.so.0.11.5 libgdc.so

%install
install -d %buildroot{%_includedir,%_libdir}
install -pm644 gdc.h gdchart.h gdcpie.h %buildroot%_includedir
install -pm644 libgdc.so* %buildroot%_libdir

%files
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so

%changelog
* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.5-alt1.1
- rebuild (with the help of girar-nmu utility)

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 0.11.5-alt1
- Initial build.
Name: libtntdb
Version: 1.3
Release: alt1

Summary: C++ library for easy access to databases
License: LGPL
Group: System/Libraries
Url: http://www.tntnet.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libcxxtools-devel postgresql-devel libmysqlclient-devel libsqlite3-devel

%package devel
Summary: C++ library for easy access to databases
Group: Development/C++
Requires: %name = %version-%release

%description
Tntdb is a c++-class-library for easy access to databases. The interface
is database-independent. Driverclasses are loaded dynamically.

%description devel
Tntdb is a c++-class-library for easy access to databases. The interface
is database-independent. Driverclasses are loaded dynamically.
This package contains development part of Tntdb.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libtntdb.so.*

%dir %_libdir/tntdb
%_libdir/tntdb/*.so*

%files devel
%doc AUTHORS COPYING README
%_libdir/libtntdb.so
%_includedir/tntdb.h
%_includedir/tntdb

%changelog
* Mon Mar 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- 1.3 released

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Feb 13 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- initial

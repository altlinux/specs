%def_disable gtk

Name: libiodbc
Version: 3.52.7
Release: alt3

Group: System/Libraries
Summary: The iODBC Driver Manager
Url: http://www.iodbc.org/
License: BSD / LGPLv2

Source: http://www.iodbc.org/downloads/iODBC/libiodbc-%version.tar.gz

BuildRequires: chrpath glibc-devel
%if_enabled gtk
BuildRequires: libgtk+2-devel
%endif

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license


%package -n libiodbcinst
Summary: The iODBC Driver Manager main library
Group: System/Libraries
%description -n libiodbcinst
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
%package utils
Summary: The iODBC Driver Manager common binary files
Group: System/Libraries
%description utils
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license

%package -n libiodbcdrvproxy
Summary: The iODBC Driver Manager main library
Group: System/Libraries
%description -n libiodbcdrvproxy
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license

%package -n libiodbcadm
Summary: The iODBC Driver Manager main library
Group: System/Libraries
%description -n libiodbcadm
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license

%package admin
Summary: GTK based administrator for iODBC development
Group: System/Configuration/Other
%description admin
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains a GTK based administrator program for maintaining
DSN information in odbc.ini and odbcinst.ini files.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license

%package devel
Summary: header files and libraries for iODBC development
Group: Development/Databases
Provides: iodbc-devel = %version-%release
Requires: %name-utils
Requires: libunixODBC-devel
%description devel
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

This package contains the header files and libraries needed to develop
program that use the driver manager.

The iODBC Driver Manager was originally created by Ke Jin and is
currently maintained by OpenLink Software under a LGPL or BSD license
(see "LICENSE" file included in the distribution).


%prep
%setup -q
#autoreconf


%build
%configure \
	--disable-static \
	--enable-shared \
	--disable-rpath \
	--enable-odbc3 \
	--disable-libodbc \
%if_enabled gtk
	--enable-gui \
%else
	--disable-gui \
%endif
	--with-iodbc-inidir=%_sysconfdir \
	--includedir=%_includedir/iodbc \
	--enable-pthreads
%make

%install
%make install DESTDIR=%buildroot

# workaround against missing configure --disable-rpath option
find %buildroot/%_libdir -type f -name \*.so.\* | \
while read l; do chrpath -d $l; done
find %buildroot/%_bindir -type f -perm /0111 | \
while read b; do chrpath -d $b; done


%files
%_libdir/libiodbc.so.*

%files -n libiodbcinst
%_libdir/libiodbcinst.so.*

%files utils
%_bindir/iodbctest
%_bindir/iodbctestw
%_mandir/man1/iodbctest.1*
%_mandir/man1/iodbctestw.1*

%if_enabled gtk
%files -n libiodbcdrvproxy
%_libdir/libiodbcdrvproxy.so.*
%files -n libiodbcadm
%_libdir/libiodbcadm.so.*
%files admin
%_bindir/iodbcadm-gtk
%_mandir/man1/iodbcadm-gtk.1*
%endif

%files devel
%doc AUTHORS LICENSE* ChangeLog NEWS README*
%doc etc/odbc.ini.sample etc/odbcinst.ini.sample
%_mandir/man1/iodbc-config.1*
%_bindir/iodbc-config
%_datadir/libiodbc
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/libiodbc.pc


%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt3
- rebuilt for debuginfo

* Tue Jan 18 2011 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt2
- rebuilt

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt0.M51.1
- built for M51

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt1
- built for ALT

%def_enable gtk

%global descr The iODBC Driver Manager is a free implementation of the SAG CLI\
and ODBC compliant driver manager which allows developers to write ODBC\
compliant applications that can connect to various databases using\
appropriate backend drivers.\
\
The iODBC Driver Manager was originally created by Ke Jin and is\
currently maintained by OpenLink Software under a LGPL or BSD license.

%define oname iodbc

Name: libiodbc
Version: 3.52.16
Release: alt1

Summary: The iODBC Driver Manager
Group: System/Libraries
License: BSD-3-Clause OR LGPL-2.0-or-later
Url: http://www.iodbc.org/
Vcs: https://github.com/openlink/iODBC

Source: %name-%version.tar

BuildRequires: chrpath
%if_enabled gtk
BuildRequires: libgtk+2-devel
%endif

%description
%descr

%package -n %{name}inst
Summary: The iODBC Driver Manager main library
Group: System/Libraries

%description -n %{name}inst
%descr

%package devel
Summary: header files and libraries for iODBC development
Group: Development/Databases
Provides: %oname-devel = %EVR
Requires: %name-utils = %EVR
Requires: %name = %EVR
%if_enabled gtk
Requires: libdrvproxy = %EVR
Requires: %{name}adm = %EVR
Requires: %{name}inst = %EVR
%endif
Requires: libunixODBC-devel

%description devel
%descr

This package contains the header files and libraries needed to develop
program that use the driver manager.

%package -n libdrvproxy
Summary: The iODBC Driver Manager main library
Group: System/Libraries
Requires: %name = %EVR
Requires: %{name}inst = %EVR
Requires: %{name}adm = %EVR

%description -n libdrvproxy
%descr

%package -n %{name}adm
Summary: The iODBC Driver Manager main library
Group: System/Libraries
Requires: %name = %EVR
Requires: %{name}inst = %EVR

%description -n %{name}adm
%descr

%package admin
Summary: GTK based administrator for iODBC development
Group: System/Configuration/Other
Requires: %{name}inst = %EVR

%description admin
%descr

This package contains a GTK based administrator program for maintaining
DSN information in odbc.ini and odbcinst.ini files.

%package utils
Summary: The iODBC Driver Manager common binary files
Group: System/Libraries
Requires: %name = %EVR

%description utils
%descr

This package contains some demo programs that may be useful.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--enable-shared \
	--disable-rpath \
	--enable-odbc3 \
	--disable-libodbc \
	--with-iodbc-inidir=%_sysconfdir \
	--includedir=%_includedir/iodbc \
	--enable-pthreads \
%if_enabled gtk
	--enable-gui
%else
	--disable-gui
%endif
%ifarch i586
%make_build CFLAGS+='-Wno-incompatible-pointer-types'
%else
%make_build
%endif

%install
%makeinstall_std

# workaround against missing configure --disable-rpath option
find %buildroot/%_libdir -type f -name \*.so.\* | \
while read l; do chrpath -d $l; done
find %buildroot/%_bindir -type f -perm /0111 | \
while read b; do chrpath -d $b || : ; done

%files
%_libdir/%name.so.*

%files -n %{name}inst
%_libdir/%{name}inst.so.*

%files devel
%doc AUTHORS COPYING LICENSE* ChangeLog NEWS README*
%doc etc/odbc.ini.sample etc/odbcinst.ini.sample
%_bindir/%oname-config
%_datadir/%name/*
%_includedir/%oname
%_libdir/%name.so
%_libdir/%{name}inst.so
%if_enabled gtk
%_libdir/libdrvproxy.so
%_libdir/%{name}adm.so
%endif
%_man1dir/%oname-config.1.xz
%_pkgconfigdir/%name.pc

%if_enabled gtk
%files -n libdrvproxy
%_libdir/libdrvproxy.so.*

%files -n %{name}adm
%_libdir/%{name}adm.so.*

%files admin
%_bindir/%{oname}adm-gtk
%_man1dir/%{oname}adm-gtk.1.xz
%endif

%files utils
%_bindir/%{oname}test
%_bindir/%{oname}testw
%_man1dir/%{oname}test.1.xz
%_man1dir/%{oname}testw.1.xz

%changelog
* Mon Apr 21 2025 Ulysses Apokin <ulysses@altlinux.org> 3.52.16-alt1
- new version

* Fri Dec 20 2013 Sergey V Turchin <zerg@altlinux.org> 3.52.8-alt1
- new version

* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt3
- rebuilt for debuginfo

* Tue Jan 18 2011 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt2
- rebuilt

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt0.M51.1
- built for M51

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 3.52.7-alt1
- built for ALT

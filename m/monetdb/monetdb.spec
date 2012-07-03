Name: monetdb
Version: 11.5.3
Release: alt1.1

Summary: MonetDB is an open source column-oriented database management system
License: MonetDB Public License v1.1
Group: Databases
URL: http://monetdb.org
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate

BuildRequires: libssl-devel libpcre-devel libxml2-devel zlib-devel libreadline-devel libgeos-devel libcfitsio-devel python-module-setuptools
BuildRequires: python-devel perl-devel perl-DBI swig perl-Digest-SHA

Requires: %name-common %name-server %name-client

%description
MonetDB is an open source column-oriented database management system. It was
designed to provide high performance on complex queries against large databases,
e.g. combining tables with hundreds of columns and multi-million rows.

%package common
Summary: Common libraries for MonetDB server and client
Group: Databases

%description common
%summary

%package server
Summary: MonetDB server binaries and scripts
Group: Databases

%description server
%summary

%package client
Summary: MonetDB client tools
Group: Databases

%description client
%summary

%package -n python-module-%name
Summary: MonetDB python interface
Group: Development/Python
BuildArch: noarch

%description -n python-module-%name
%summary

%package perl
Summary: MonetDB perl interface
Group: Development/Perl
Requires: perl-DBI

%description perl
%summary

%prep
%setup

%build
%configure
%make

%install
%makeinstall
find %buildroot/%_libdir/monetdb5/ -name *.la -delete
mkdir -p %buildroot/%_logdir/%name
mkdir -p %buildroot/%_initdir
cp %SOURCE1 %buildroot/%_initdir/%name
mkdir -p %buildroot/%_sysconfdir/logrotate.d/
cp %SOURCE2 %buildroot/%_sysconfdir/logrotate.d/%name
cp %buildroot/%_bindir/sqlsample.py .

%pre server
%_sbindir/groupadd -r -f _monetdb
%_sbindir/useradd -r -g _monetdb -r -c "MonetDB database management system" -s /sbin/nologin -d /var/lib/monetdb5 -n _monetdb > /dev/null 2>&1 ||:

%post server
%post_service %name

%preun server
%preun_service %name

%files

%files common
%_libdir/libmapi.so*
%_libdir/libstream.so*
%doc README COPYING

%files server
%_bindir/monetdb
%_bindir/monetdbd
%_bindir/mserver5
%_libdir/libbat.so*
%_libdir/libmonetdb5.so*
%dir %_libdir/monetdb5
%_libdir/monetdb5/*
%_man1dir/monetdb.1.*
%_man1dir/monetdbd.1.*
%_man1dir/mserver5.1.*
%dir %attr(0770,root,_monetdb) %_localstatedir/monetdb5
%dir %attr(0770,root,_monetdb) %_logdir/monetdb
%_initdir/%name
%_sysconfdir/logrotate.d/%name

%files client
%_bindir/mclient
%_bindir/msqldump
%_bindir/stethoscope
%_man1dir/mclient.1.*
%_man1dir/msqldump.1.*
%doc sql/dump-restore.*

%files -n python-module-%name
%dir %python_sitelibdir_noarch/%name
%python_sitelibdir_noarch/%name/*
%doc clients/python/examples/*
%doc clients/python/README.rst
%doc sqlsample.py

%files perl
%perl_vendor_archlib/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 11.5.3-alt1.1
- Rebuild with Python-2.7

* Mon Sep 26 2011 Eugene Prokopiev <enp@altlinux.ru> 11.5.3-alt1
- new version

* Mon Sep 26 2011 Eugene Prokopiev <enp@altlinux.ru> 11.5.1-alt1
- new version

* Sat Jul 30 2011 Eugene Prokopiev <enp@altlinux.ru> 11.3.7-alt1
- new version

* Sat Jul 09 2011 Eugene Prokopiev <enp@altlinux.ru> 11.3.3-alt1
- build from scratch for Sisyphus


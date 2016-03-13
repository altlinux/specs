Name: monetdb
Version: 11.19.7
Release: alt1.1

Summary: MonetDB is an open source column-oriented database management system
License: MonetDB Public License v1.1
Group: Databases
URL: http://monetdb.org
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Patch: monetdb-11.5.3-atl-gcc4.7.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel libpcre-devel libxml2-devel zlib-devel libreadline-devel libgeos-devel libcfitsio-devel python-module-setuptools-tests
BuildRequires: python-devel perl-devel perl-DBI swig perl-Digest-SHA
BuildPreReq: python3-devel python3-module-setuptools-tests

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

%package -n python3-module-%name
Summary: MonetDB python interface
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
%summary

%package perl
Summary: MonetDB perl interface
Group: Development/Perl
Requires: perl-DBI

%description perl
%summary

%prep
%setup
#patch -p2

%build
%configure \
	--with-python2=python \
	--with-python3=python3 \
	--with-python2-libdir=%python_sitelibdir_noarch \
	--with-python3-libdir=%python3_sitelibdir_noarch
%make_build

%install
%makeinstall
find %buildroot/%_libdir/monetdb5/ -name *.la -delete
mkdir -p %buildroot/%_logdir/%name
mkdir -p %buildroot/%_initdir
cp %SOURCE1 %buildroot/%_initdir/%name
mkdir -p %buildroot/%_sysconfdir/logrotate.d/
cp %SOURCE2 %buildroot/%_sysconfdir/logrotate.d/%name
cp %buildroot/%_bindir/sqlsample.* .
cp %buildroot/%_bindir/malsample.* .

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
%_sysconfdir/tmpfiles.d/*
/var/lib/monetdb5

%files client
%_bindir/mclient
%_bindir/msqldump
%_bindir/stethoscope
%_bindir/tomograph
%_man1dir/mclient.1.*
%_man1dir/msqldump.1.*
%doc sql/dump-restore.*

%files -n python-module-%name
%dir %python_sitelibdir_noarch/%name
%python_sitelibdir_noarch/%name/*
%python_sitelibdir_noarch/*.egg-info
%doc clients/examples/python
%doc clients/python2/README.rst
#doc sqlsample.py

%files -n python3-module-%name
%dir %python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name/*
%python3_sitelibdir_noarch/*.egg-info
%doc clients/examples/python
%doc clients/python3/README.rst
#doc sqlsample.py

%files perl
%perl_vendor_archlib/*
%doc sqlsample.pl malsample.pl

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 11.19.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.19.7-alt1
- Version 11.19.7 (ALT #30660)
- Added module for Python 3

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.5.3-alt1.2
- Fixed build with gcc 4.7

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


Name: monetdb
Version: 11.27.11
Release: alt1

Summary: MonetDB is an open source column-oriented database management system
License: MonetDB Public License v1.1
Group: Databases
URL: http://monetdb.org

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate
Patch: monetdb-11.5.3-atl-gcc4.7.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libssl-devel libpcre-devel libxml2-devel zlib-devel libreadline-devel libgeos-devel libcfitsio-devel
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python3-devel python3-module-setuptools-tests

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

%prep
%setup
#patch -p2

%build
%configure \
	--with-python2=python \
	--with-python3=python3 \
	--with-python2-libdir=%python_sitelibdir_noarch \
	--with-python3-libdir=%python3_sitelibdir_noarch \
	--localstatedir=%_var
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
%_sbindir/useradd -r -g _monetdb -r -c "MonetDB database management system" -s /sbin/nologin -d %_localstatedir/monetdb5 -n _monetdb > /dev/null 2>&1 ||:

%post server
%post_service %name

%preun server
%preun_service %name

%files

%files common
%_libdir/libmapi.so*
%_libdir/libstream.so*
%doc README.rst COPYING

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
%_localstatedir/monetdb5

%files client
%_bindir/mclient
%_bindir/msqldump
%_bindir/stethoscope
%_bindir/tomograph
%_man1dir/mclient.1.*
%_man1dir/msqldump.1.*
%doc sql/dump-restore.*

%changelog
* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 11.27.11-alt1
- Updated to upstream version 11.27.11.

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 11.19.7-alt1.qa3
- Rebuild with geos 3.6.2

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 11.19.7-alt1.qa2
- NMU: rebuilt due to libcfitsio.so.3 -> libcfitsio.so.4 soname change.

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


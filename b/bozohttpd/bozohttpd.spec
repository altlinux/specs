Name: bozohttpd
Version: 20140102
Release: alt1
Group: System/Servers
Summary: Tiny http 1.1 server
License: BSD
Source: %name-%version.tar.bz2
Patch: bozohttpd-20140102-bozoname.patch
Patch1: bozohttpd-20140102-small.patch
Url: http://www.eterna.com.au/bozohttpd/

%define sum tiny http 1.1 server
%define bmake MAKEFLAGS="" bmake
%define bmakeinstall %bmake install \\\
	LIBDIR=%_libdir DESTDIR=%buildroot BINDIR=%_bindir \\\
	BINOWN=`id -u` BINGRP=`id -g` BINMODE=755 \\\
	MANOWN=`id -u` MANGRP=`id -g` MANMODE=644

# Automatically added by buildreq on Wed Jan 15 2014
# optimized out: libcom_err-devel libkrb5-devel pkgsrc-mk-files
BuildRequires: bmake groff-base liblua5-devel libssl-devel unifdef

%description
the bozotic HTTP server

bozohttpd is a small and secure http version 1.1 server. its main
feature is the lack of features, reducing the code size and improving
verifiability.

it supports CGI/1.1, HTTP/1.1, HTTP/1.0, HTTP/0.9, ~user translations,
virtual hosting support, as well as multiple IP-based servers on
a single machine. it is capable of serving pages via the IPv6 protocol.
it has ssl support. it has no configuration file by design. you can also
read the manual page.

%package small
Group: System/Servers
Summary: A 100 percent lean bozohttpd, %sum
%description small
A 100 percent lean bozohttpd, %sum

%package -n lib%name
Group: Development/C
Summary: %sum (library version)
%description -n lib%name
%sum (library version)

%package -n lib%name-devel
Group: Development/C
Summary: %sum (development environment)
%description -n lib%name-devel
%sum (development environment)

%package -n lib%name-devel-static
Group: Development/C
Summary: %sum (static development environment)
Requires: lib%name-devel
%description -n lib%name-devel-static
%sum (static development environment)

%prep
%setup
find . -name .\#\* -exec rm {} \;
%patch -p1
%patch1 -p1
# XXX
sed -i 's/-lssl /-lssl -lc /' libbozohttpd/Makefile
sed 's@#include "netbsd_queue.h"@#include <bozohttpd/netbsd_queue.h>@' < bozohttpd.h > libbozohttpd/bozohttpd.h

%build
%bmake COPTS+="-D_GNU_SOURCE"
%bmake COPTS+="-D_GNU_SOURCE -DNO_LUA_SUPPORT" -C libbozohttpd
%bmake COPTS+="-D_GNU_SOURCE" -C small
# XXX syntax errors in upstream in lua/glue.c
#ln -s libluabozohttpd.so.0.0 lua/libluabozohttpd.so   
#ln -s ../libbozohttpd/libbozohttpd.so.0.0 lua/libbozohttpd.so
#bmake COPTS+="-D_GNU_SOURCE -I.." LDADD="-L. -lbozohttpd" -C lua

%install
mkdir -p %buildroot%_bindir %buildroot%_libdir \
	%buildroot%_man8dir %buildroot%_man3dir %buildroot%_mandir/cat{8,3} \
	%buildroot%_includedir/%name
%bmakeinstall
install *.h %buildroot%_includedir/%name/
%bmakeinstall -C libbozohttpd
install small/bozohttpd-small %buildroot%_bindir/bozohttpd-small
( cd %buildroot%_libdir; for N in *.so.*; do ln -s $N ${N%%.so.*}.so; done )

%check
cd testsuite
%bmake SIMPLETESTS='t1 t2 t3 t4 t5 t6 t7 t8 t9' check-simple

%files
%exclude %_mandir/cat*
%_bindir/%name
%_man8dir/*

%files small
%_bindir/%name-small

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 20140102-alt1
- Autobuild version bump to 20140102
- Cleanup and fix build
- Disabler lua server for it doesn't even compile for now

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 20130711-alt1
- Autobuild version bump to 20130711
- Fix build

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 20111118-alt2
- DSO list completion

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 20111118-alt1
- Autobuild version bump to 20111118
- Build scheme fix

* Sat Sep 03 2011 Fr. Br. George <george@altlinux.ru> 20100920-alt1
- Initial build from scratch


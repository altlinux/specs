Name: bozohttpd
Version: 20160415
Release: alt2.1
Group: System/Servers
Summary: Tiny http 1.1 server
License: BSD
Source: %name-%version.tar.bz2
Patch: bozohttpd-20140102-bozoname.patch
Patch1: bozohttpd-20141225-small.patch
Patch2: bozohttpd-20141225-namelen.patch
Url: http://www.eterna.com.au/bozohttpd/
Requires: webserver-common

%define sum tiny http 1.1 server
%define bmake MAKEFLAGS="" bmake
%define bmakeinstall %bmake install \\\
	LIBDIR=%_libdir DESTDIR=%buildroot BINDIR=%_bindir \\\
	BINOWN=`id -u` BINGRP=`id -g` BINMODE=755 \\\
	MANOWN=`id -u` MANGRP=`id -g` MANMODE=644

# Automatically added by buildreq on Wed Jan 15 2014
# optimized out: libcom_err-devel libkrb5-devel pkgsrc-mk-files
BuildRequires: bmake groff-base lua-devel libssl-devel unifdef

%description
The bozotic HTTP server

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
#patch2

cat > bozohttpd@.service <<@@@
[Unit]
Description=%sum
Documentation=man:bozohttpd(8)

[Service]
ExecStart=/usr/bin/bozohttpd -s -X /var/www
StandardInput=socket
StandardError=journal
Type=simple
User=nobody
Group=webmaster
@@@

cat > bozohttpd.socket <<@@@
[Unit]
Description=%sum socket

[Socket]
ListenStream=80
Accept=yes

[Install]
WantedBy=sockets.target
@@@

# XXX
sed -i 's/-lssl /-lssl -lc /' libbozohttpd/Makefile
sed 's@#include "netbsd_queue.h"@#include <bozohttpd/netbsd_queue.h>@' < bozohttpd.h > libbozohttpd/bozohttpd.h

%build
%bmake COPTS+="-D_GNU_SOURCE -Wno-error=unused-result"
%bmake COPTS+="-D_GNU_SOURCE -Wno-error=unused-result -DNO_LUA_SUPPORT" -C libbozohttpd
%bmake COPTS+="-D_GNU_SOURCE -Wno-error=unused-result" -C small

%install
mkdir -p %buildroot%_bindir %buildroot%_libdir \
	%buildroot%_man8dir %buildroot%_man3dir %buildroot%_mandir/cat{8,3} \
	%buildroot%_includedir/%name
%bmakeinstall
install *.h %buildroot%_includedir/%name/
%bmakeinstall -C libbozohttpd
install small/bozohttpd-small %buildroot%_bindir/bozohttpd-small
( cd %buildroot%_libdir; for N in *.so.*; do ln -s $N ${N%%.so.*}.so; done )
install -D bozohttpd@.service %buildroot%_unitdir/bozohttpd@.service
install -D bozohttpd.socket %buildroot%_unitdir/bozohttpd.socket

%check
cd testsuite
%bmake SIMPLETESTS='t1 t2 t3 t4 t5 t6 t7 t8 t9' check-simple

%files
%exclude %_bindir/httpd
%exclude %_mandir/cat*
%_bindir/%name
%_man8dir/*
%_unitdir/*

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
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 20160415-alt2.1
- rebuild with new lua 5.3

* Thu Nov 03 2016 Fr. Br. George <george@altlinux.ru> 20160415-alt2
- Systemd units provided

* Wed Nov 02 2016 Fr. Br. George <george@altlinux.ru> 20160415-alt1
- Autobuild version bump to 20160415
- Drop patch

* Mon Apr 11 2016 Fr. Br. George <george@altlinux.ru> 20150320-alt2
- Fix build

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 20150320-alt1
- Autobuild version bump to 20150320

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 20141225-alt1
- Autobuild version bump to 20141225
- Fix patches

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 20140708-alt1
- Autobuild version bump to 20140708

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 20140201-alt1
- Autobuild version bump to 20140201

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


Name: bozohttpd
Version: 20220517
Release: alt1
Group: System/Servers
Summary: Tiny http 1.1 server
License: BSD
Source: %name-%version.tar.bz2
Url: http://www.eterna.com.au/bozohttpd/
Requires: webserver-common

%define sum tiny http 1.1 server
%define bmake MAKEFLAGS="" bmake
%define bmakeinstall %bmake install \\\
	INCDIR=%_includedir LIBDIR=%_libdir DESTDIR=%buildroot BINDIR=%_bindir \\\
	BINOWN=`id -u` BINGRP=`id -g` BINMODE=755 \\\
	MANOWN=`id -u` MANGRP=`id -g` MANMODE=644

# Automatically added by buildreq on Fri Jun 24 2022
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libgpg-error python3 python3-base sh4
BuildRequires: bmake groff-base libssl-devel lua-devel mk-files unifdef

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

%package lua
Group: System/Servers
Summary: Lua bindings to bozohttpd, %sum
%description lua
Lua bindings to bozohttpd, %sum

%prep
%setup

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

echo -e "incinstall:\n\ttrue" >> lua/Makefile

%build
%bmake COPTS="-DDO_HTPASSWD -DNO_BLOCKLIST_SUPPORT" LDADD='-lcrypt -llua -lm -lssl -lcrypto'
%bmake COPTS="-DDO_HTPASSWD -DNO_BLOCKLIST_SUPPORT -DNO_LUA_SUPPORT" SHLIB_LDADD='-lcrypt -lm -lssl -lcrypto' -C libbozohttpd
%bmake -C small
%bmake CPPFLAGS="-I`pwd` -DNO_BLOCKLIST_SUPPORT" SHLIB_LDADD="-L`pwd`/libbozohttpd -lbozohttpd -llua" -C lua

%install
%bmakeinstall
%bmakeinstall -C libbozohttpd
%bmakeinstall -C small
%bmakeinstall -C lua

## install small/bozohttpd-small %buildroot%_bindir/bozohttpd-small
install -D bozohttpd@.service %buildroot%_unitdir/bozohttpd@.service
install -D bozohttpd.socket %buildroot%_unitdir/bozohttpd.socket
install -D bozohttpd.8 %buildroot%_man8dir/bozohttpd.8
install -D libbozohttpd/libbozohttpd.3 %buildroot%_man3dir/libbozohttpd.3
%bmake -C testsuite check-simple

%check
%bmake -C testsuite check-simple

%files
%exclude %_bindir/httpd
%exclude %_mandir/cat*
%_bindir/%name
%_man8dir/*
%_unitdir/*

%files small
%_bindir/%name-small

%files -n lib%name
%_libdir/libb*.so.*

%files -n lib%name-devel
%_libdir/libb*.so
%_includedir/*.h
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/libb*.a

%files lua
%_libdir/liblua*.so.*
%exclude %_libdir/liblua*.so
%exclude %_libdir/liblua*.a

%changelog
* Fri Jun 24 2022 Fr. Br. George <george@altlinux.org> 20220517-alt1
- Autobuild version bump to 20220517
- Introduce Lua module

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 20170201-alt1
- Autobuild version bump to 20170201

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


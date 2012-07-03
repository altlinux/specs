# -*- rpm-spec -*-

Name: transconnect
Version: 1.3
Release: alt5

Summary: use internet with HTTP CONNECT
License: GPL
Group: Networking/Other
Url: http://transconnect.sourceforge.net/
Packager: Yauheni Kaliuta <tren@altlinux.ru>

Source0: %url/sourceforge/transconnect/%name-%version-Beta.tar.gz
Source1: proxyfy.in

Patch0:  %name-1.3-build.patch

%description
Transconnect is an implementation to allow network connections over 
a HTTP proxy. This should work under almost all linux distributions using 
glibc, and all proxies allowing https CONNECT (eg squid).

%prep
%setup -q -n %name-%version-Beta
%patch -p1
sed -e 's,@LIBDIR@,%_libdir,g' -e 's,@LIB@,%_lib,g' < %SOURCE1 > proxyfy

%build
%add_optflags %optflags_shared
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install 
install -D -m 755 proxyfy %buildroot%_bindir/transconnect
install -D tconn.so %buildroot%_libdir/libtransconnect.so.0
install -D -p -m 644 tconn.conf %buildroot%_sysconfdir/transconnect.conf

%files
%doc README AUTHORS COPYING INSTALL TROUBLESHOOT
%config %_sysconfdir/%name.conf
%_bindir/%name
%_libdir/lib%name.so.*

%changelog
* Tue Oct 26 2010 Yauheni Kaliuta <tren@altlinux.ru> 1.3-alt5
- Generate proxyfy script to use proper libdir. (#24370)

* Sun Nov 11 2007 Yauheni Kaliuta <tren@altlinux.org> 1.3-alt4
- Confirm NMU
- Change maintainer's name to the official one

* Thu Nov 08 2007 Slava Semushin <php-coder@altlinux.ru> 1.3-alt3.1
- NMU: Updated Url tag (#8987)

* Thu Jun  1 2006 Zhenja Kaluta <tren@altlinux.ru> 1.3-alt3
- Fixed build, moved -ldl to the end of the list

* Tue Feb  3 2004 Zhenja Kaluta <tren@altlinux.ru> 1.3-alt2
- Added optflags

* Fri Jun 13 2003 Zhenja Kaluta <trinfo@mail.ru> 1.3-alt1
- Intitial release



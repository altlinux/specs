Name: rpmhdrmemcache
Version: 0.1.2
Release: alt3

Summary: Cached reading of rpm package headers
License: GPLv2+
Group: System/Configuration/Packaging

URL: http://git.altlinux.org/gears/r/rpmhdrmemcache.git
Source: %name-%version.tar

# Automatically added by buildreq on Fri Dec 24 2010
BuildRequires: libmemcached-devel liblzo2-devel librpm-devel

%description
Sisyphus repository currently has more than 10K source packages (which is
more than 60K rpm files with subpackages).  To assist repeated repo scanning
(which is required for each repo update), this package provides rpmhdrcache.so
perloadable module.  This module intercepts rpmReadPackageHeader calls and
caches the result using memcached.

%prep
%setup

%build
gcc -shared -fPIC -D_GNU_SOURCE %optflags -flto -fwhole-program \
	-o rpmhdrmemcache.so preload.c hdrcache.c mcdb.c \
	-Wl,--no-as-needed -lrpmio -lrpm -Wl,--as-needed -lrpmdb -ldl -lmemcached -lmemcachedutil -llzo2 -Wl,-z,defs 

%install
install -pD -m644 rpmhdrmemcache.so %buildroot%_libdir/rpmhdrmemcache.so

%files
%_libdir/rpmhdrmemcache.so

%changelog
* Mon Jun 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt3
- rebuild with libmemcached-1.0.8
- fix build

* Sat Jan 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2
- rebuild with libmemcached-1.0.4

* Tue Nov 01 2011 Dmitry V. Levin <ldv@altlinux.org> 0.1.2-alt1
- Fixed potential memory corruption and memory leak
  (by Alexey Tourbin; closes: #26463).

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt3
- rebuild with libmemcached-0.52

* Mon Jun 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2
- fix description

* Mon Jun 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1
- implementation using memcached

Name: libmemcached
Version: 1.0.8
Release: alt1

Summary: Client library to the memcached
License: BSD
Group: System/Libraries
Url: http://libmemcached.org/
# http://launchpad.net/%name/1.0/%version/+download/%name-%version.tar.gz
Source: %name-%version.tar
Patch1: libmemcached-1.0.5-alt-disable-network-tests.patch

BuildRequires: gcc-c++ memcached-devel perl-podlators libevent-devel

%description
libmemcached is a C and C++ client library to the memcached
server.  It has been designed to be light on memory usage,
thread safe, and provide full access to server side methods.

%package utils
Summary: Collection of utilities designed to work with memcached
Group: Development/C
Requires: %name = %version-%release

%description utils
Collection of utilities designed to work with memcached.

%package devel
Summary: Files needed to develop programs which use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
libmemcached is a C and C++ client library to the memcached
server.  It has been designed to be light on memory usage,
thread safe, and provide full access to server side methods.

This package contains the header files and development libraries
for %name.

%prep
%setup
%patch1 -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
make test

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog COPYING README THANKS

%files utils
%_bindir/*
%_man1dir/*

%files devel
%_libdir/*.so
%_includedir/%name
%_includedir/libhashkit
%_includedir/libmemcachedprotocol-0.0/
%_includedir/libmemcachedutil-1.0
%_includedir/libmemcached-1.0
%_includedir/libhashkit-1.0
%_pkgconfigdir/%name.pc
%_man3dir/*

%changelog
* Mon Jun 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Mon Mar 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Jan 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Jan 25 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed Oct 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.53-alt2
- rebuild

* Fri Oct 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.53-alt1
- 0.53

* Tue Sep 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.52-alt1
- 0.52

* Wed Jun 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.49-alt2
- Enabled test suite.
- Cleaned up packaging.

* Tue Jun 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.49-alt1
- 0.49

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Nov 12 2008 Alexey Gladkov <legion@altlinux.ru> 0.23-alt1
- first build for ALT Linux.

Name: libmemcached
Version: 1.1.4
Release: alt1

Summary: Client library to the memcached
License: BSD
Group: System/Libraries
Url: https://github.com/awesomized/libmemcached/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: flex gcc-c++

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
%patch0 -p1

%build
%cmake -DENABLE_STATIC=FALSE
%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot%_libdir/libp9y.a
rm -f %buildroot%_libdir/cmake/libmemcached-awesome/p9y*

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog COPYING README.md BUGS.md TODO

%files utils
%_bindir/*

%files devel
%_libdir/*.so
%_includedir/libhashkit
%_includedir/libhashkit-1.0
%_includedir/libmemcached
%_includedir/libmemcached-1.0
%_includedir/libmemcachedprotocol-0.0
%_includedir/libmemcachedutil-1.0
%_aclocaldir/*.m4
%_pkgconfigdir/%name.pc
%_libdir/cmake/*

%changelog
* Wed Mar 29 2023 Alexei Takaseev <taf@altlinux.org> 1.1.4-alt1
- 1.1.4 (Fixes CVE-2023-27478)
- Change URL to new upstream project
- Use CMAKE

* Wed Apr 10 2019 Alexei Takaseev <taf@altlinux.org> 1.0.18-alt3
- Fix build with automake 1.16

* Sat Jun 02 2018 Alexei Takaseev <taf@altlinux.org> 1.0.18-alt2
- Fix build with gcc7

* Tue Dec 01 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.18-alt1
- 1.0.18
- Disable static build
- Package .m4 file

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

Name: libevhtp-seafile
Version: 1.2.9
Release: alt2

Summary: Libevhtp was created as a replacement API for Libevent's current HTTP API (seafile compatible)
License: BSD
Group: System/Libraries

Packager: Denis Baranov <baraka@altlinux.ru>

Url: https://github.com/ellzey/libevhtp

# Source-git: https://github.com/ellzey/libevhtp.git
Source: %name-%version.tar

# Automatically added by buildreq on Sat Mar 16 2013 (-bi)
# optimized out: cmake cmake-modules libcom_err-devel libkrb5-devel libstdc++-devel pkg-config python-base
BuildRequires: ccmake gcc-c++ glibc-devel libevent-devel libssl-devel

# need for build with external liboniguruma
BuildRequires: libOniGuruma-devel >= 5.9.2

%description
Libevhtp was created as a replacement API for Libevent's
current HTTP API. The reality of libevent's http interface
is that it was created as a JIT server, meaning the developer
never thought of it being used for creating a full-fledged
HTTP service. Infact I am under the impression that the
libevent http API was designed almost as an example of
what you can do with libevent. It's not Apache in a box,
but more and more developers are attempting to use it as so.

See http://bugs.etersoft.ru/show_bug.cgi?id=11271

See https://github.com/haiwen/seafile/issues/1631

%package devel
Summary: Development files for %name (seafile compatible)
Requires: %name = %version-%release
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%__subst "s| lib)| \${LIB_DESTINATION})|g" CMakeLists.txt
%__subst 's|"evhtp"|"evhtp-seafile"|g' CMakeLists.txt

%build
%cmake_insource -DEVHTP_BUILD_SHARED:STRING=ON

%install
%makeinstall_std

# hack
mv %buildroot%_libdir/%name.so %buildroot%_libdir/%name.so.%version
mkdir %buildroot%_includedir/%name/
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

%files
%_libdir/%name.so.%version

%files devel
%_libdir/%name.so
%_includedir/%name/*.h

%changelog
* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt2
- build obsoleted version for seafile compatibility

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)
- add devel package

* Sat Mar 16 2013 Denis Baranov <baraka@altlinux.ru> 1.2.1-alt1
- Initial build for ALTLinux


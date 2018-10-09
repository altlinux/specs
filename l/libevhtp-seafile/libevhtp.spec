Name: libevhtp-seafile
Version: 1.2.0
Release: alt1
Epoch: 2

Summary: Libevhtp was created as a replacement API for Libevent's current HTTP API (seafile compatible)
License: BSD
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: https://github.com/haiwen/libevhtp

# Source-url: https://github.com/haiwen/libevhtp/archive/%version.tar.gz
Source: %name-%version.tar

Patch1: libevtp-oniguruma.patch
Patch2: libevtp-seafile.patch
Patch3: find-oniguruma.patch
Patch4: fix-test-code.patch

# Automatically added by buildreq on Sat Mar 16 2013 (-bi)
# optimized out: cmake cmake-modules libcom_err-devel libkrb5-devel libstdc++-devel pkg-config python-base
BuildRequires: cmake gcc-c++ libevent-devel
#libssl-devel

# need for build with external liboniguruma
BuildRequires: oniguruma-devel >= 6.2.0

%description
Libevhtp was created as a replacement API for Libevent's
current HTTP API. The reality of libevent's http interface
is that it was created as a JIT server, meaning the developer
never thought of it being used for creating a full-fledged
HTTP service. Infact I am under the impression that the
libevent http API was designed almost as an example of
what you can do with libevent. It's not Apache in a box,
but more and more developers are attempting to use it as so.

Warning about updated version:
See http://bugs.etersoft.ru/show_bug.cgi?id=11271
See https://github.com/haiwen/seafile/issues/1631

%package devel
Summary: Development files for %name (seafile compatible)
Requires: %name = %EVR
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
rm -rf oniguruma/

%__subst "s| lib)| \${LIB_DESTINATION})|g" CMakeLists.txt
%__subst 's|"evhtp"|"evhtp-seafile"|g' CMakeLists.txt

%build
%cmake_insource -DEVHTP_BUILD_SHARED=ON -DEVHTP_DISABLE_SSL=ON -DLIB_INSTALL_DIR=%_libdir

%install
%makeinstall_std

mkdir -p %buildroot%_includedir/%name/
rm -fv %buildroot%_includedir/onigposix.h
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

%files
%_libdir/%name.so.%version

%files devel
%_libdir/%name.so
%dir %_includedir/%name/
%_includedir/%name/*.h

%changelog
* Tue Oct 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2:1.2.0-alt1
- revert to 1.2.0 (for Seafile server)
- fix build with system oniguruma, build without openssl

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.2.9-alt4
- rebuild with new oniguruma

* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt3
- more clean build

* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt2
- build obsoleted version for seafile compatibility

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)
- add devel package

* Sat Mar 16 2013 Denis Baranov <baraka@altlinux.ru> 1.2.1-alt1
- Initial build for ALTLinux


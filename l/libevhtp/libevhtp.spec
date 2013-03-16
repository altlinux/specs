Name: libevhtp
Version: 1.2.1
Release: alt1

Summary: Libevhtp was created as a replacement API for Libevent's current HTTP API
License: bsd
Group: System/Libraries

Packager: Denis Baranov <baraka@altlinux.ru>

Url: https://github.com/ellzey/libevhtp
Source: %name-%version.tar

# Automatically added by buildreq on Sat Mar 16 2013 (-bi)
# optimized out: cmake cmake-modules libcom_err-devel libkrb5-devel libstdc++-devel pkg-config python-base
BuildRequires: ccmake gcc-c++ glibc-devel libevent-devel libssl-devel

%description
Libevhtp was created as a replacement API for Libevent's
current HTTP API. The reality of libevent's http interface
is that it was created as a JIT server, meaning the developer
never thought of it being used for creating a full-fledged
HTTP service. Infact I am under the impression that the
libevent http API was designed almost as an example of
what you can do with libevent. It's not Apache in a box,
but more and more developers are attempting to use it as so.

%prep
%setup
%__subst "s| lib)| \${LIB_DESTINATION})|g" CMakeLists.txt

%build
%cmake_insource -DEVHTP_BUILD_SHARED:STRING=ON

%install
%makeinstall_std

%files
%_includedir/*.h
%_libdir/libevhtp.so

%changelog
* Sat Mar 16 2013 Denis Baranov <baraka@altlinux.ru> 1.2.1-alt1
- Initial build for ALTLinux


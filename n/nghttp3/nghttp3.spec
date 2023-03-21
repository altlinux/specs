%global _unpackaged_files_terminate_build 1

Name: nghttp3
Version: 0.9.0
Release: alt1
Summary: nghttp3 is an implementation of RFC 9114 HTTP/3 mapping over QUIC and RFC 9204 QPACK in C

License: MIT
Group: System/Libraries
Url: https://github.com/ngtcp2/nghttp3
Vcs: https://github.com/ngtcp2/nghttp3
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ CUnit-devel

%description
%summary.

It does not depend on any particular QUIC transport implementation.

%package -n lib%name
Summary: A library implementing the HTTP/3 protocol
Group: System/Libraries

%description -n lib%name
libnghttp3 is a library implementing the Hypertext Transfer Protocol
version 3 (HTTP/3) protocol in C.

%package -n lib%name-devel
Summary: Files needed for building applications with libnghttp2
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The libnghttp3-devel package includes libraries and header files needed
for building applications with libnghttp2.


%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_defaultdocdir/%name

%check
%make_build check


%files -n lib%name
%_libdir/*.so.*
%doc README.rst

%files -n lib%name-devel
%_includedir/nghttp3
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Tue Mar 21 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- Initial build.



%global _unpackaged_files_terminate_build 1

Name: ngtcp2
Version: 0.13.1
Release: alt1
Summary: An implementation of the RFC9000 QUIC protocol

License: MIT
Group: System/Libraries
Url: https://github.com/ngtcp2/ngtcp2
Vcs: https://github.com/ngtcp2/ngtcp2.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ CUnit-devel
# need openssl-quic branch
#BuildRequires: pkgconfig(openssl) >= 1.1.1
BuildRequires: pkgconfig(gnutls) >= 3.7.2
BuildRequires: pkgconfig(libnghttp3) >= 0.2.0
BuildRequires: libev-devel

%description
%summary.

%package -n lib%name
Summary: An implementation of the RFC9000 QUIC protocol
Group: System/Libraries

%description -n lib%name
%summary.

%package -n lib%name-devel
Summary: Files needed for building applications with libngtcp2
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The libngtcp2-devel package includes libraries and header files needed
for building applications with libngtcp2.

%prep
%setup

%build
%autoreconf
%configure --disable-static --with-gnutls
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
%_includedir/%name
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 0.13.1-alt1
- New version 0.13.1.

* Tue Mar 21 2023 Alexey Shabalin <shaba@altlinux.org> 0.13.0-alt1
- Initial build.

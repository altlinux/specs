Name: librist
Version: 0.2.20
Release: alt1

Summary: RIST protocol support
License: BSD-2-Clause
Group: System/Libraries
URL: https://code.videolan.org/rist/librist
VCS: https://code.videolan.org/rist/librist

Source: %name-%version.tar

BuildRequires: meson
BuildRequires: pkgconfig(libcjson)
BuildRequires: pkgconfig(libmicrohttpd)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(nettle)

%package devel
Summary: RIST protocol support
Group: Development/C

%package tools
Summary: RIST protocol support
Group: Networking/Other

%description
A library that can be used to easily add the RIST protocol to your application.
This code was written to comply with the Video Services Forum (VSF) Technical
Recommendations TR-06-1, TR-06-2, and TR-06-3.
This package contains librist shared library.

%description devel
A library that can be used to easily add the RIST protocol to your application.
This code was written to comply with the Video Services Forum (VSF) Technical
Recommendations TR-06-1, TR-06-2, and TR-06-3.
This package contains development part of librist.

%description tools
A library that can be used to easily add the RIST protocol to your application.
This code was written to comply with the Video Services Forum (VSF) Technical
Recommendations TR-06-1, TR-06-2, and TR-06-3.
This package contains several RIST tools.

%prep
%setup

%build
%meson -Duse_nettle=true -Duse_mbedtls=false
%meson_build

%install
%meson_install

%files
%doc COPYING README*
%_libdir/librist.so.*

%files devel
%_includedir/*
%_libdir/librist.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*

%changelog
* Thu Sep 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.20-alt1
- initial

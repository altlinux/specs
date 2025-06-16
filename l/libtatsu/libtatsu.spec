%def_disable snapshot
%define api_ver 1.0

%def_enable check

Name: libtatsu
Version: 1.0.5
Release: alt1

Summary: Library handling the communication with Apple's Tatsu Signing Server (TSS)
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://www.libimobiledevice.org

Vcs: https://github.com/libimobiledevice/libtatsu.git

%if_disabled snapshot
Source: https://github.com/libimobiledevice/libtatsu/releases/download/%version/%name-%version.tar.bz2
%else
Source: %name-%version.tar
%endif

%define plist_ver 2.6.0
%define curl_ver 7.0

BuildRequires: pkgconfig(libplist-2.0) >= %plist_ver
BuildRequires: pkgconfig(libcurl) >= %curl_ver

%description
This library is part of the libimobiledevice project. The main purpose
of this library is to allow creating TSS request payloads, sending them
to Apple's TSS server, and retrieving and processing the response.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides files for development using %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%nil
%make_build

%install
%makeinstall_std

%check
%make -k check VERBOSE=1

%files
%_libdir/%name.so.*
%doc NEWS README*

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- first build for Sisyphus


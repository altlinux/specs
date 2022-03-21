%define _unpackaged_files_terminate_build 1

Name: libyang
Version: 2.0.164
Release: alt1
Summary: YANG data modeling language library
Url: https://github.com/CESNET/libyang
Source: %name-%version.tar
License: BSD-3-Clause
Group: System/Libraries

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(libpcre2-8) >= 10.21

%description
Libyang is YANG data modeling language parser and toolkit
written (and providing API) in C.

%package devel
Summary: Development files for libyang
Group: Development/C
Requires: %name = %EVR
Requires: pkgconfig(libpcre2-8) >= 10.21

%description devel
Headers of libyang library.

%package tools
Summary: YANG validator tools
Group: Other
Requires: %name = %EVR

%description tools
YANG validator tools.

%prep
%setup

%build
%cmake 
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_datadir/yang

%files
%_libdir/*.so.*
%dir %_datadir/yang

%files tools
%_bindir/*
%_man1dir/yang*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/%name

%changelog
* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.164-alt1
- new version 2.0.164

* Mon Feb 21 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.112-alt1
- Initial build.


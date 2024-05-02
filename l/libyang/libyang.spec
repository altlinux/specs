%define _unpackaged_files_terminate_build 1
%define soname 2

Name: libyang
Version: 2.1.148
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

%package -n %name%soname
Summary: YANG data modeling language library
Group: System/Libraries

%description -n %name%soname
Libyang is YANG data modeling language parser and toolkit
written (and providing API) in C.

%package devel
Summary: Development files for libyang
Group: Development/C
Requires: %name%soname = %EVR
Requires: pkgconfig(libpcre2-8) >= 10.21

%description devel
Headers of libyang library.

%package modules
Summary: YANG modules for libyang
Group: System/Libraries
Conflicts: %name < 2.1.148

%description modules
YANG modules for libyang.

%package tools
Summary: YANG validator tools
Group: Other
Requires: %name%soname = %EVR

%description tools
YANG validator tools.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_datadir/yang

%files -n %name%soname
%_libdir/*.so.%{soname}*

%files modules
%_datadir/yang

%files tools
%_bindir/*
%_man1dir/yang*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/%name

%changelog
* Thu May 02 2024 Alexey Shabalin <shaba@altlinux.org> 2.1.148-alt1
- New version 2.1.148.

* Wed May 03 2023 Alexey Shabalin <shaba@altlinux.org> 2.1.55-alt1
- New version 2.1.55.

* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 2.1.30-alt1
- new version 2.1.30

* Mon Oct 10 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.231-alt1
- new version 2.0.231

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.194-alt1
- new version 2.0.194

* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.164-alt1
- new version 2.0.164

* Mon Feb 21 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.112-alt1
- Initial build.


%define _name lucene++
%def_enable check

Name: lib%_name
Version: 3.0.9
Release: alt2

Summary: A high-performance, full-featured text search engine written in C++
Group: System/Libraries
License: Apache-2.0 or LGPL-3.0-or-later
Url: https://github.com/luceneplusplus/LucenePlusPlus

Source: https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%version.tar.gz#/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake gcc-c++ zlib-devel
BuildRequires: boost-devel boost-filesystem-devel boost-asio-devel boost-interprocess-devel
%{?_enable_check:BuildRequires: libgmock-devel}

%description
An up to date C++ port of the popular Java Lucene library,
a high-performance, full-featured text search engine.

%package devel
Summary: Development files for lucene++
Group: Development/C++
Requires: %name = %EVR

%description devel
Development files for lucene++, a high-performance, full-featured text
search engine written in C++

%prep
%setup
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
    -DCMAKE_BUILD_TYPE:STRING="Release" \
    %{?_disable_check:-DENABLE_TEST=FALSE} \
    -DBUILD_GMOCK=FALSE} \
    -DINSTALL_GTEST=FALSE
%nil
%cmake_build -t %_name %_name-contrib

%install
%cmake_install

%check
#%%cmake_build -t test

%files
%_libdir/%name.so.*
%_libdir/%name-contrib.so.*
%doc COPYING AUTHORS README* REQUESTS

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_libdir/%name-contrib.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-contrib.pc
%_libdir/cmake/%{name}*

%changelog
* Mon Apr 29 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.9-alt2
- updated to rel_3.0.9-4-g76dc90f (fixed build with boost-1.85)

* Sun Feb 25 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.9-alt1
- 3.0.9

* Tue Mar 22 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt2
- updated to rel_3.0.8-28-g4fb8e5f (ALT #42206)

* Mon May 31 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1.1
- adapted to new cmake macros

* Tue Jan 12 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- updated to rel_3.0.8-8-g8c2ce8d
- fixed License tag

* Fri Jun 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt5
- rebuilt with boost-1.67

* Wed Apr 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt4
- rebuilt with boost-1.66

* Wed Sep 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt3
- rebuilt with boost-1.65

* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt2
- updated to 3.0.7-7-gcf9b9d9

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- first build for Sisyphus




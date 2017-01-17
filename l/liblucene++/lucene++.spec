%define _name lucene++

Name: lib%_name
Version: 3.0.7
Release: alt2

Summary: A high-performance, full-featured text search engine written in C++
Group: System/Libraries
License: ASL 2.0 or LGPLv3+
Url: https://github.com/luceneplusplus/LucenePlusPlus

Source: https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%version.tar.gz#/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake gcc-c++
BuildRequires: boost-devel boost-filesystem-devel boost-asio-devel boost-interprocess-devel

%description
An up to date C++ port of the popular Java Lucene library,
a high-performance, full-featured text search engine.

%package devel
Summary: Development files for lucene++
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for lucene++, a high-performance, full-featured text
search engine written in C++

%prep
%setup
%patch -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"

%cmake_build %_name %_name-contrib

%install
%cmakeinstall_std

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

%changelog
* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt2
- updated to 3.0.7-7-gcf9b9d9

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- first build for Sisyphus




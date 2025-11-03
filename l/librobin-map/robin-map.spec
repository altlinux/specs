%define _unpackaged_files_terminate_build 1

%define oname robin-map

Name:    lib%oname
Version: 1.4.1
Release: alt1
Summary: C++ implementation of a fast hash map and hash set using robin hood hashing 
Group:   Development/C++
License: MIT
URL:     https://github.com/Tessil/robin-map

# https://github.com/Tessil/robin-map.git
Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

BuildArch: noarch

%description
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing
with backward shift deletion to resolve collisions.

%package devel
Summary: C++ implementation of a fast hash map and hash set using robin hood hashing 
Group:   Development/C++

%description devel
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing
with backward shift deletion to resolve collisions.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE
%doc README.md
%_includedir/*
%_datadir/cmake/*

%changelog
* Mon Nov 03 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.1-alt1
- 1.4.1.

* Mon May 19 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.0-alt1
- Updated to upstream version 1.4.0.

* Fri Jul 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt1
- Updated to upstream version 0.6.3.

* Mon May 27 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Initial build for ALT.

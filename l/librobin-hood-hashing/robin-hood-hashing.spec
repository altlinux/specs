%define _unpackaged_files_terminate_build 1

%define oname robin-hood-hashing

Name:    lib%oname
Version: 3.11.5
Release: alt1
Summary: Fast & memory efficient hashtable based on robin hood hashing for C++11/14/17/20
Group:   Development/C++
License: MIT
URL:     https://github.com/martinus/robin-hood-hashing

# https://github.com/martinus/robin-hood-hashing.git
Source: %name-%version.tar

BuildRequires: cmake gcc-c++

BuildArch: noarch

%description
robin_hood::unordered_map and robin_hood::unordered_set is a platform
independent replacement for std::unordered_map / std::unordered_set which is
both faster and more memory efficient for real-world use cases.

%package devel
Summary: Fast & memory efficient hashtable based on robin hood hashing for C++11/14/17/20 
Group:   Development/C++

%description devel
robin_hood::unordered_map and robin_hood::unordered_set is a platform
independent replacement for std::unordered_map / std::unordered_set which is
both faster and more memory efficient for real-world use cases.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  -DRH_STANDALONE_PROJECT=OFF
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE
%doc *.md
%_includedir/*
%_datadir/cmake/*

%changelog
* Sun Apr 10 2022 L.A. Kostis <lakostis@altlinux.ru> 3.11.5-alt1
- 3.11.5.

* Wed Nov 03 2021 L.A. Kostis <lakostis@altlinux.ru> 3.11.3-alt1
- 3.11.3.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 3.11.2-alt1
- Initial build for ALTLinux.


%define _unpackaged_files_terminate_build 1

Name: optional-lite
Version: 3.5.0
Release: alt1.git00e9cf5c

Summary: optional lite: A single-file header-only version of a C++17-like optional
License: BSL-1.0
Group: Development/C++
Url: https://github.com/martinmoene/optional-lite.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: gcc-c++ libstdc++10-devel libcxx

%description
A single-file header-only version of a C++17-like optional,
a nullable object for C++98, C++11 and later

%prep
%setup
%patch -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%files
%_includedir/*
%_libdir/cmake/%name

%changelog
* Fri May 19 2023 Aleksei Kalinin <kaa@altlinux.org> 3.5.0-alt1.git00e9cf5c
- Initial build for Sisyphus

%define _unpackaged_files_terminate_build 1

%define abiversion 0

Name:    psimd
Version: 0.1
Release: alt1.git072586a

Summary: Portable 128-bit SIMD intrinsics
License: MIT
Group:   Development/C++
Url:     https://github.com/Maratyszcza/psimd

Source: %name-%version.tar

BuildRequires(pre): cmake

%description
%summary

%package -n lib%name%abiversion
Summary: %summary
Group: Development/C++

%description -n lib%name%abiversion
%summary

%package -n lib%name-devel
Summary: Portable 128-bit SIMD intrinsics
BuildArch: noarch
Group: Development/C++
Provides: lib%name%abiversion = %version-%release

%description -n lib%name-devel
%summary

%prep
%setup

sed -i -e 's@CMAKE_MINIMUM_REQUIRED(VERSION 2.8.12 FATAL_ERROR@CMAKE_MINIMUM_REQUIRED(VERSION 3.5@' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel 
%doc *.md LICENSE
%_includedir/psimd.h

%changelog
* Thu Aug 28 2025 Nikita Shmatko <nash@altlinux.org> 0.1-alt1.git072586a
- Initial build for Sisyphus.

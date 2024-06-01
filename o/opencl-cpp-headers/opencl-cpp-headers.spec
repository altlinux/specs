%define orig_name OpenCL-CLHPP
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: opencl-cpp-headers
Version: 2024.05.08
Release: alt1

Summary: OpenCL API C++ bindings
License: Apache-2.0
Group: Development/C++
Url: https://github.com/KhronosGroup/OpenCL-CLHPP

#Source-git: https://github.com/KhronosGroup/OpenCL-Headers.git
# Source-url: %url/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ ocl-icd-devel

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%cmake \
	-DOPENCL_CLHPP_LOADER_DIR=%_libdir \
	-DBUILD_EXAMPLES=OFF \
	-DBUILD_DOCS=OFF \
	-DBUILD_TESTING=OFF \
	%nil
%cmake_build

%install
%cmake_install

%files
%_includedir/CL
# already in opencl-headers
%exclude %_includedir/CL/cl2.hpp
%_datadir/cmake/OpenCLHeadersCpp
%_datadir/pkgconfig/%orig_name.pc

%changelog
* Fri May 31 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.05.08-alt1
- v2024.05.08 (OpenCL 3.0.16).

* Mon Jan 08 2024 L.A. Kostis <lakostis@altlinux.ru> 2023.12.14-alt1
- Initial build for ALTLinux.


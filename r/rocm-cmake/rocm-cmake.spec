Name: rocm-cmake
Version: 5.7.1
Release: alt0.1
License: MIT
Group: Development/C++
Summary: CMake modules used within the ROCm libraries

Url: https://github.com/RadeonOpenCompute/rocm-cmake

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildArch: noarch

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.

%prep
%setup

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md CHANGELOG.md
%dir %_datadir/rocm
%_datadir/rocm/cmake

%changelog
* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.1-alt0.1
- rocm-5.7.1 (technical rebuild).

* Tue Sep 19 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.1
- rocm-5.7.0.

* Wed Aug 30 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.1
- rocm-5.6.1 (no code changes, just version bump).

* Sat Jul 01 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- rocm-5.6.0.

* Thu May 25 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- Initial build for ALTLinux.

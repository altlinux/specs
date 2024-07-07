Name: rocm-cmake
Version: 6.1.2
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
%dir %_datadir/rocmcmakebuildtools
%_datadir/rocm/cmake
%_datadir/rocmcmakebuildtools/cmake

%changelog
* Wed Jul 03 2024 L.A. Kostis <lakostis@altlinux.ru> 6.1.2-alt0.1
- rocm-6.1.2.
- added rocmcmakebuildtools directory.

* Sat Dec 23 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1
- rocm-6.0.0.

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

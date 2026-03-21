Name: clpeak
Version: 1.1.7
Release: alt1
Summary: A tool which profiles OpenCL devices to find their peak capacities
License: Apache-2.0
Group: System/Configuration/Hardware
Url: https://github.com/krrishnarraj/clpeak

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: opencl-cpp-headers ocl-icd-devel gcc-c++

%description
A synthetic benchmarking tool to measure peak capabilities of opencl devices.
It only measures the peak metrics that can be achieved using vector operations
and does not represent a real-world use case

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Sat Mar 21 2026 L.A. Kostis <lakostis@altlinux.ru> 1.1.7-alt1
- 1.1.7.

* Mon Jun 16 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1.5-alt1
- 1.1.5.

* Mon Feb 17 2025 L.A. Kostis <lakostis@altlinux.ru> 1.1.4-alt1
- Initial build for ALTLinux.

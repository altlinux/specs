Name: rocminfo
Version: 5.4.1
Release: alt0.2
License: NCSA
Summary: ROCm Application for Reporting System Info
Url: https://github.com/RadeonOpenCompute/rocminfo
Group: System/Configuration/Hardware

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ hsa-rocr-devel python3-devel
Requires: pciutils

# hsa-rocr is 64-bit only
ExclusiveArch: x86_64 aarch64 ppc64le

%description
ROCm Application for Reporting System Info.

%prep
%setup
# https://github.com/RadeonOpenCompute/rocminfo/issues/60
%ifarch aarch64
subst '/.*{ROCMINFO_CXX_FLAGS} -m64)/d' CMakeLists.txt
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc License.txt README.md
%_bindir/*

%changelog
* Thu Jan 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Add ExclusiveArch.
- Fix build on aarch64.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.

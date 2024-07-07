Name: rocminfo
Version: 6.1.2
Release: alt0.1
License: NCSA
Summary: ROCm Application for Reporting System Info
Url: https://github.com/RadeonOpenCompute/rocminfo
Group: System/Configuration/Hardware

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ hsa-rocr-devel python3-devel
Requires: pciutils

# hsa-rocr is 64-bit only
ExclusiveArch: x86_64 ppc64le aarch64

%description
ROCm Application for Reporting System Info.

%prep
%setup
# https://github.com/RadeonOpenCompute/rocminfo/issues/60
%ifarch aarch64
subst '/.*{ROCMINFO_CXX_FLAGS} -m64)/d' CMakeLists.txt
%endif

%build
%cmake -DROCRTST_BLD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc License.txt README.md
%_bindir/*

%changelog
* Sat Jul 06 2024 L.A. Kostis <lakostis@altlinux.ru> 6.1.2-alt0.1
- rocm-6.1.2.

* Tue Mar 19 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.3
- added python3.12 compatibility patch.

* Mon Mar 18 2024 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.2
- Enable build on all 64-bit arches.

* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1
- rocm-6.0.0.
- Fix build type.

* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.1-alt0.1
- rocm-5.7.1.

* Wed Sep 20 2023 L.A. Kostis <lakostis@altlinux.ru> 5.7.0-alt0.1
- rocm-5.7.0.

* Wed Aug 30 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.1-alt0.1
- rocm-5.6.1 (no code change, just version bump).
- rebuild with updated hsa-rocr.

* Tue Jul 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.6.0-alt0.1
- Rebuild for rocm-5.6.0.
- Built x86_64 only (due hsa-rocr).

* Sun May 28 2023 L.A. Kostis <lakostis@altlinux.ru> 5.5.1-alt0.1
- rocm-5.5.1.

* Thu Jan 05 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Add ExclusiveArch.
- Fix build on aarch64.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.

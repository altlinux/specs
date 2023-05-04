%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type
%define _unpackaged_files_terminate_build 1

Name: nvtop
Version: 3.0.1
Release: alt2

Summary: (h)top like task monitor for AMD, Intel and Nvidia GPUs
Group: Monitoring
License: GPLv3
Url: https://github.com/Syllo/nvtop

Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libsystemd-devel libudev-devel libdrm-devel libncurses-devel

# nvidia gpu information rely on libnvidia-ml library
%ifarch %ix86 x86_64 aarch64
Requires: libnvidia-ml
%endif

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD, Intel
and NVIDIA GPUs. It can handle multiple GPUs and print information about them in
a htop familiar way.

%prep
%setup

%build
%_cmake \
%ifarch %ix86 x86_64 aarch64
	-DNVIDIA_SUPPORT=ON \
%else
	-DNVIDIA_SUPPORT=OFF \
%endif
	-DAMDGPU_SUPPORT=ON \
	-DINTEL_SUPPORT=ON
%cmake_build
%cmake_install

%files
%doc README.* COPYING
%_bindir/%name
%_man1dir/%name.*
%_iconsdir/%name.svg
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.metainfo.xml

%changelog
* Thu May 04 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.1-alt2
- Fix requires for nvidia.

* Wed May 03 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.1-alt1
- Initial build for ALTLinux.

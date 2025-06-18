%define _unpackaged_files_terminate_build 1

Name: VkFFT
Version: 1.3.4
Release: alt1

Group: Development/C
Summary: Vulkan/CUDA/HIP/OpenCL/Level Zero/Metal Fast Fourier Transform library
License: MIT
BuildArch: noarch
Url: https://github.com/DTolm/VkFFT

Source: %name-%version.tar

%define _description \
VkFFT is an efficient GPU-accelerated multidimensional Fast \
Fourier Transform library for Vulkan/CUDA/HIP/OpenCL/Level \
Zero/Metal projects. VkFFT aims to provide the community with \
an open-source alternative to Nvidia's cuFFT library while \
achieving better performance. VkFFT is written in C language and \
supports Vulkan, CUDA, HIP, OpenCL, Level Zero and Metal as backends.

%description
%_description

%package devel
Summary: Development files for VkFFT
Group: Development/C

%description devel
This package contains VkFFT development files.
%_description

%prep
%setup

%install
mkdir -p %buildroot%_includedir
cp -a vkFFT/* %buildroot%_includedir

%files devel
%doc README.md
%doc LICENSE
%doc documentation/*
%_includedir/vkFFT.h
%_includedir/vkFFT


%changelog
* Tue May 20 2025 Dmitrii Chuprov <cheese@altlinux.org> 1.3.4-alt1
- New version 1.3.4 (Feb 6, 2024).

* Thu Jun 01 2023 Elizaveta Morozova <morozovaes@altlinux.org> 1.2.31-alt1
- Initial build for ALT


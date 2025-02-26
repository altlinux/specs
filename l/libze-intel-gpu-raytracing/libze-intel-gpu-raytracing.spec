%define git c5e1fad
Name: libze-intel-gpu-raytracing
Version: 1.0.0
Release: alt15.g%git

Summary: oneAPI Level Zero Ray Tracing Support
License: Apache-2.0
Group: Development/C++

Url: https://github.com/intel/level-zero-raytracing-support
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: x86_64

BuildRequires: gcc-c++
BuildRequires(pre): cmake
BuildRequires: libze-devel libtbb-devel

%description
The oneAPI Level Zero Ray Tracing Support library implements high performance
CPU based construction algorithms for 3D acceleration structures that are
compatible with the ray tracing hardware of Intel GPUs. This library is used by
Intel(R) oneAPI Level Zero to implement part of the RTAS builder extension.
This library should not get used directly but only through Level Zero.

%prep
%setup
%patch -p1

%cmake \
  -DZE_RAYTRACING_TBB_STATIC=OFF

%build
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.txt
%doc README.md SECURITY.md CHANGELOG.md
%_libdir/libze_intel_gpu_raytracing.so

%changelog
* Sun Jan 26 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt15.gc5e1fad
- Initial build for ALTLinux.

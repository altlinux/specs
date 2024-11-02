%set_verify_elf_method strict

%define rocm_version 6.1.2
%define build_type RelWithDebInfo
%define distdir dist/bin/%build_type
%define ver 02003
%define git bd75b7c
%define stage rc7

Name: hiprt
Version: 2.3
Release: alt3.%git.%stage
Summary: HIP Ray Tracing
License: MIT
Group: Development/Other
Url: https://gpuopen.com/hiprt

# https://github.com/GPUOpen-LibrariesAndSDKs/HIPRT/archive/refs/tags/%{version}.%{git}.%{stage}.tar.gz
Source0: %name-%version.tar

Patch: %name-alt-install.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++ hip-devel = %rocm_version nvidia-cuda-devel

%description
HIP RT is a ray tracing library for HIP, making it easy to write ray-tracing
applications in HIP. The APIs and library are designed to be minimal, lower
level, and simple to use and integrate into any existing HIP applications.

%package -n lib%{name}
Summary: HIP Ray Tracing Library
Group: System/Libraries
Requires: hip-runtime-amd = %rocm_version

%description -n lib%{name}
HIP Ray Tracing Library

%package devel
Summary: %name development headers
Group: Development/C++
Requires: lib%{name} = %EVR hip-devel = %rocm_version

%description devel
%name development headers

%prep
%setup
%patch -p1
# # Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)
subst 's| python | python3 |' premake5.lua
chmod +x ./contrib/easy-encryption/bin/linux/ee64

%build
%cmake -Wno-dev -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_STRIP:STRING="" \
       -DBITCODE=OFF

%cmake_build

%install
%cmake_install
# compatibility link
ln -sr %buildroot%_libdir/lib%{name}%{ver}64.so %buildroot%_libdir/lib%{name}64.so
mkdir -p %buildroot%_sysconfdir/profile.d
echo 'export HIPRT_PATH=%_includedir' > %buildroot%_sysconfdir/profile.d/hiprt.sh
chmod 755 %buildroot%_sysconfdir/profile.d/hiprt.sh

%files -n lib%{name}
%_libdir/*.so

%files devel
%_sysconfdir/profile.d/hiprt.sh
%_includedir/%name

%changelog
* Thu Oct 31 2024 L.A. Kostis <lakostis@altlinux.ru> 2.3-alt3.bd75b7c.rc7
- Updated to 2.3.bd75b7c.rc7.
- Build with cuda support.
- devel: set HIPRT_PATH.

* Wed Oct 30 2024 L.A. Kostis <lakostis@altlinux.ru> 2.3-alt2.7df94af
- Bump rocm version.
- Add impl/Orochi headers.
- Add compatibility library links.

* Fri Apr 12 2024 L.A. Kostis <lakostis@altlinux.ru> 2.3-alt1.7df94af
- Updated to v2.3.7df94af.
- Build from official sources.

* Thu Dec 28 2023 L.A. Kostis <lakostis@altlinux.ru> 2.2-alt2.g0e68f54
- Added compatibility symlink.
- hiprt: patch headers for use with gcc13.
- don't strip anything.

* Sun Dec 24 2023 L.A. Kostis <lakostis@altlinux.ru> 2.2-alt1.g0e68f54
- Updated to v2.2.0e68f54 (December 2023).

* Fri Jul 07 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.3-alt1.ga134c7
- Initial build for ALTLinux.

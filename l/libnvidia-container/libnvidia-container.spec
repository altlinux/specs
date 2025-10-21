%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1
# disable until https://bugzilla.altlinux.org/54930 will be fixed
#%%define _stripped_files_terminate_build 1
%define soname 1
%define git 6eda4d76c8c5f8fc174e4abca83e513fb4dd63b0
%define modprobe_version 550.54.14

Name: libnvidia-container
License: Apache-2.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND GPL-2.0-only
# libnvidia-container is licensed under apache-2.0
#  https://github.com/NVIDIA/libnvidia-container/blob/main/LICENSE
# libnvidia-container includes the GPLv3 license
#  https://github.com/NVIDIA/libnvidia-container/blob/main/COPYING
# libnvidia-container includes the LGPLv3 license
#  https://github.com/NVIDIA/libnvidia-container/blob/main/COPYING.LESSER
# nvidia-modprobe is licensed under GPLv2
#  https://github.com/NVIDIA/nvidia-modprobe/blob/main/COPYING
# several nvidia-modprobe files contain the MIT license header
#  https://github.com/NVIDIA/nvidia-modprobe/blob/main/utils.mk
Url: https://github.com/NVIDIA/libnvidia-container
Vcs: https://github.com/NVIDIA/libnvidia-container.git
Version: 1.17.9
Release: alt1
Summary: NVIDIA container runtime library
Group: System/Libraries
Source: %name-%version.tar
# hardcoded in sources
Source1: nvidia-modprobe-%{modprobe_version}.tar.gz
Patch: no-git.patch
Patch1: nvidia-modprobe.patch
Patch2: system-tirpc.patch
Patch3: ldconfig.patch
Patch4: no-fortify.patch
Patch5: nvgo-cflags.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: rpcgen golang libelf-devel libcap-devel libtirpc-devel libseccomp-devel
# due golang
BuildRequires: /proc

%description
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%install
export GIT_COMMIT=%git \
export GIT_TAG=%version
export OPTFLAGS='%optflags'
cp %SOURCE1 .
DESTDIR=%buildroot CPPFLAGS='%optflags' CFLAGS='%optflags' STRIP=/bin/true %__make install WITH_LIBELF=yes WITH_TIRPC=yes prefix=%prefix exec_prefix=%_exec_prefix bindir=%_bindir libdir=%_libdir includedir=%_includedir docdir=%_docdir

rm -rf %buildroot%_docdir/%name-%version

%package -n %name%soname
Summary: NVIDIA container runtime library
Group: System/Libraries
Provides: %name = %EVR

%description -n %name%soname
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package requires the NVIDIA driver (>= 340.29) to be installed separately.

%package devel
Summary: NVIDIA container runtime library (development files)
Group: Development/C
Requires: %name = %EVR

%description devel
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package contains the files required to compile programs with the library.

%package devel-static
Summary: NVIDIA container runtime library (static library)
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package requires the NVIDIA driver (>= 340.29) to be installed separately.

%package tools
Summary: NVIDIA container runtime library (command-line tools)
Group: System/Configuration/Hardware
Requires: %name >= %EVR

%description tools
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package contains command-line tools that facilitate using the library.

%files -n %name%soname
%doc COPYING* LICENSE NOTICE
%_libdir/lib*.so.*

%files devel
%_includedir/*.h
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%files devel-static
%_libdir/lib*.a

%files tools
%_bindir/*

%changelog
* Tue Oct 21 2025 L.A. Kostis <lakostis@altlinux.ru> 1.17.9-alt1
- 1.17.9.

* Sat Jun 21 2025 L.A. Kostis <lakostis@altlinux.ru> 1.17.8-alt1
- Initial build for ALTLinux.


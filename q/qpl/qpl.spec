%define _unpackaged_files_terminate_build 1
%define sover 1

Name: qpl
Version: 1.6.0
Release: alt1
Summary: Intel Query Processing Library (Intel QPL)
License: MIT
Group: Development/C

Url: https://intel.github.io/qpl/index.html
Vcs: https://github.com/intel/qpl.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.15 ninja-build
BuildRequires: gcc-c++ nasm
BuildRequires: libuuid-devel

ExclusiveArch:	x86_64

%description
The Intel Query Processing Library (Intel QPL) is an open-source library
to provide high-performance query processing operations on Intel CPUs.
Intel QPL is aimed to support capabilities of the new Intel In-Memory Analytics
Accelerator (Intel IAA) available on Next Generation Intel Xeon Scalable
processors, codenamed Sapphire Rapids processor, such as very high throughput
compression and decompression combined with primitive analytic functions,
as well as to provide highly-optimized SW fallback on other Intel CPUs.
Intel QPL primarily targets applications such as big-data and in-memory
analytic databases.

%package -n lib%name%sover
Summary: Intel Query Processing Library (Intel QPL)
Group: System/Libraries

%description -n lib%name%sover
The Intel Query Processing Library (Intel QPL) is an open-source library
to provide high-performance query processing operations on Intel CPUs.
Intel QPL is aimed to support capabilities of the new Intel In-Memory Analytics
Accelerator (Intel IAA) available on Next Generation Intel Xeon Scalable
processors, codenamed Sapphire Rapids processor, such as very high throughput
compression and decompression combined with primitive analytic functions,
as well as to provide highly-optimized SW fallback on other Intel CPUs.
Intel QPL primarily targets applications such as big-data and in-memory
analytic databases.

%package -n lib%name-devel
Summary: Development files for Intel QPL
Group: Development/C
Requires: lib%name%sover = %EVR
#Requires: libaccel-config

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
applications that use lib%name.


%prep
%setup
#%%autopatch -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DQPL_LIBRARY_TYPE=SHARED \
    -DQPL_BUILD_TESTS=OFF \
    -DQPL_BUILD_EXAMPLES=OFF \
    -GNinja
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/QPL
%_datadir/QPL

%changelog
* Tue Oct 29 2024 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial build.


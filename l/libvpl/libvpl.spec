%def_with check
%add_optflags -Wno-deprecated-declarations -Wno-address
%global soversion 2
Name: libvpl
Version: 2.11.0
Release: alt1
Summary: Intel Video Processing Library
License: MIT
Group: System/Libraries
Url: https://github.com/intel/libvpl
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(pciaccess)
BuildRequires: pkgconfig(wayland-client++)
BuildRequires: pkgconfig(xcb-dri3)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(libdrm)
%if_with check
BuildRequires: ctest /proc
%endif
ExclusiveArch: x86_64 aarch64

%description
Intel Video Processing Library supports AI visual inference,
media delivery, cloud gaming, and virtual desktop infrastructure use cases
by providing access to hardware accelerated video decode, encode,
and frame processing capabilities on Intel GPUs.

%package -n libvpl%soversion
Summary: Intel Video Processing Library
Group: System/Libraries

%description -n libvpl%soversion
Intel Video Processing Library (Intel VPL) supports AI visual inference,
media delivery, cloud gaming, and virtual desktop infrastructure use cases
by providing access to hardware accelerated video decode, encode,
and frame processing capabilities on Intel GPUs.

%package devel
Summary: Development files for Intel Video Processing Library
Group: Development/C
Requires: libvpl%soversion = %EVR

%description devel
This package contains the development headers and pkgconfig files for
the Intel Video Processing Library.


%prep
%setup
%patch0 -p1

%build
%cmake \
      -DBUILD_TESTS=ON \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_SYSCONFDIR:PATH='/etc' \
      -DENABLE_DRI3=ON \
      -DENABLE_DRM=ON \
      -DENABLE_VA=ON \
      -DENABLE_WAYLAND=ON \
      -DENABLE_X11=ON \
      -DENABLE_WARNING_AS_ERROR=O
      #
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %name%soversion
%_libdir/libvpl.so.%soversion
%_libdir/libvpl.so.%soversion.*

%files devel
%doc
%_sysconfdir/vpl
%_includedir/vpl/
%_libdir/libvpl.so
%_libdir/pkgconfig/vpl.pc
%_libdir/cmake/vpl/
%_datadir/vpl/

%changelog
* Fri May 03 2024 Anton Farygin <rider@altlinux.ru> 2.11.0-alt1
- 2.10.2 -> 2.11.0

* Sun Feb 25 2024 Anton Farygin <rider@altlinux.ru> 2.10.2-alt1
- first build for ALT

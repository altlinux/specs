%define bladerf_group bladerf
%define use_syslog 1
Name: bladerf
Version: 1.8.0
Release: alt1
Summary: SDR radio receiver
License: GPL-2.0
Group: Communications
Url: http://nuand.com/
# Url: https://github.com/Nuand/bladeRF.git
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# PATCH-FIX-OPENSUSE bladeRF-add-cflag-Wno-format-truncation.patch boo#1041192
Patch: bladeRF-add-cflag-Wno-format-truncation.patch
# PATCH-FIX-UPSTREAM bladeRF-cmake_syntax.patch upstream commit 037e288
Patch1: bladeRF-cmake_syntax.patch

BuildRequires (pre): rpm-macros-cmake
BuildRequires: cmake >= 2.8.4
BuildRequires: doxygen
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: help2man
#BuildRequires: tecla-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(udev)

Requires: lib%name = %version-%release

%description
The software for bladeRF USB 3.0 Superspeed Software Defined Radio.

%package -n lib%name
Summary: Library for bladeRF
Group: Development/Other
Requires: %name-udev

%description -n lib%name
Library for bladeRF, SDR transceiver.

%package udev
Summary: Udev rules for bladeRF
Group: Communications
Buildarch: noarch

%description udev
Udev rules for bladeRF

%package -n lib%name-devel
Summary: Development files for libbladeRF
Group: Development/Other
Requires: lib%name = %version

%description -n lib%name-devel
Libraries and header files for developing applications that want to make
use of libbladerf.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
pushd host
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_lib \
  -DUDEV_RULES_PATH=%_udevrulesdir \
  -DBLADERF_GROUP=%bladerf_group \
  -DBUILD_DOCUMENTATION=YES \
%if 0%{?use_syslog}
  -DENABLE_LIBBLADERF_SYSLOG=ON \
%endif
  -DBUILD_DOCUMENTATION=ON
%cmake_build
popd

%install
pushd host
%cmakeinstall_std
popd

%pre udev
getent group %bladerf_group >/dev/null || groupadd -r %bladerf_group

%files
%doc README.md COPYING CONTRIBUTORS
%_bindir/*
%_man1dir/*

%files udev
%_udevrulesdir/88-nuand.rules

%files -n lib%name
%_libdir/libbladeRF.so.*

%files -n lib%name-devel
%_libdir/libbladeRF.so
%_includedir/libbladeRF.h
%_pkgconfigdir/libbladeRF.pc

%changelog
* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- Initial build for ALT Sisyphus.

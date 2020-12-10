# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define bladerf_group bladerf
%define use_syslog 1
Name: bladerf
Version: 2.2.1
Release: alt1
Summary: SDR radio receiver
License: GPL-2.0-only
Group: Communications
Url: http://nuand.com/
# Url: https://github.com/Nuand/bladeRF.git
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: ad9361.tar
Patch0: 0001-libbladeRF-unambiguous-flash_arch-macro-name.patch
Patch1: 0002-libbladeRF-define-bladerf2_state_to_string-as-extern.patch

BuildRequires (pre): rpm-macros-cmake
BuildRequires: cmake >= 2.8.4
BuildRequires: doxygen
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: help2man
#BuildRequires: tecla-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(udev)

Provides: lib%name = %version-%release
Provides: %name-udev = %version-%release

%description
The software for bladeRF USB 3.0 Superspeed Software Defined Radio.

%package -n lib%name-devel
Summary: Development files for libbladeRF
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries and header files for developing applications that want to make
use of libbladerf.

%prep
%setup
%patch0 -p1
%patch1 -p1

pushd thirdparty/analogdevicesinc/no-OS
tar -xf %SOURCE1
popd

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

%pre
getent group %bladerf_group >/dev/null || groupadd -r %bladerf_group

%files
%doc README.md COPYING CONTRIBUTORS
%doc %_docdir/libbladeRF
%_bindir/*
%_libdir/libbladeRF.so.*
%_udevrulesdir/*.rules
%_man1dir/*

%files -n lib%name-devel
%_libdir/libbladeRF.so
%_includedir/*.h
%_pkgconfigdir/libbladeRF.pc

%changelog
* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt1
- new version 2.2.1
- fix build with gcc10

* Mon Feb 04 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1
- new version 2.2.0

* Mon Oct 30 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt2
- Merge packages libbladerf and bladerf-udev with bladerf.

* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- Initial build for ALT Sisyphus.

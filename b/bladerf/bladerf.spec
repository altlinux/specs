# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define bladerf_group bladerf
%define use_syslog 1
Name: bladerf
Version: 2.5.0
Release: alt2
Epoch: 1
Summary: SDR radio receiver
License: GPL-2.0-only
Group: Communications
Url: http://nuand.com/
# Url: https://github.com/Nuand/bladeRF.git

Source: %name-%version.tar
Source1: ad9361.tar

BuildRequires (pre): rpm-macros-cmake
BuildRequires: cmake >= 2.8.4
BuildRequires: doxygen
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: help2man
#BuildRequires: tecla-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(udev)

Provides: lib%name = %EVR
Provides: %name-udev = %EVR

%description
The software for bladeRF USB 3.0 Superspeed Software Defined Radio.

%package -n lib%name-devel
Summary: Development files for libbladeRF
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
Libraries and header files for developing applications that want to make
use of libbladerf.

%prep
%setup
%autopatch -p1

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

# allow access only to users in uucp group
sed -i 's/GROUP="bladerf"/GROUP="uucp"/' %buildroot%_udevrulesdir/*.rules

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
* Tue Aug 15 2023 Anton Midyukov <antohami@altlinux.org> 1:2.5.0-alt2
- allow access only to users in uucp group
- do not create group 'bladerf'

* Mon Jun 26 2023 Anton Midyukov <antohami@altlinux.org> 1:2.5.0-alt1
- New version 2.5.0.

* Mon Jun 28 2021 Anton Midyukov <antohami@altlinux.org> 2021.03-alt1
- new version 2021.03

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt1
- new version 2.2.1
- fix build with gcc10

* Mon Feb 04 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1
- new version 2.2.0

* Mon Oct 30 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt2
- Merge packages libbladerf and bladerf-udev with bladerf.

* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- Initial build for ALT Sisyphus.

# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     python3-module-pynest2d
Version:  4.8
Release:  alt2

Summary:  Python bindings for libnest2d
License:  LGPL-3.0
Group:    Development/Python3
Url:      https://github.com/Ultimaker/pynest2d

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

# Add PyQt5 namespace
Patch0: pynest2d-PyQt5.sip.patch
# https://github.com/Ultimaker/pynest2d/pull/3
Patch1: Retrieve-required-flags-from-Libnest2D-target.patch

Patch2: fix-cpp-version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: libnest2d-devel
BuildRequires: python3-module-sip-devel
BuildRequires: boost-geometry-devel

%description
%summary

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

# fix for use python3-module-sip-devel
sed -i 's/find_program(SIP_EXECUTABLE sip/find_program(SIP_EXECUTABLE sip3/' \
  cmake/FindSIP.cmake

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%python3_sitelibdir/pynest2d.so

%changelog
* Mon Feb 01 2021 Grigory Ustinov <grenka@altlinux.org> 4.8-alt2
- Fixed FTBFS.

* Mon Nov 16 2020 Anton Midyukov <antohami@altlinux.org> 4.8-alt1
- Initial build for Sisyphus

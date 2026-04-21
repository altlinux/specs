# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     python3-module-pynest2d
Version:  5.10.0
Release:  alt1

Summary:  Python bindings for libnest2d
License:  LGPL-3.0-or-later AND BSD-3-Clause
Group:    Development/Python3
Url:      https://github.com/Ultimaker/pynest2d

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

# CMake bits taken from 5.0.0, before upstream went nuts with conan
# SIP CMake scripts are BSD3
Source1: COPYING-CMAKE-SCRIPTS
Source2: FindSIP.cmake
Source3: FindSIP.py
Source4: SIPMacros.cmake
Source5: CMakeBuilder.py
Source6: StandardProjectSettings.cmake
Source7: CMakeLists.txt
Source8: pyproject.toml.in

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: libnest2d-devel
BuildRequires: python3-module-sip6
BuildRequires: python3-module-PyQt6-sip
BuildRequires: boost-geometry-devel
%ifarch %e2k
# there is a bug in GCC that ignores some non-existent includes
# no other compiler has this bug
# this package needs "quadmath.h" to build if
# _GLIBCXX_USE_FLOAT128 from <cstddef> is defined
BuildRequires: libquadmath-devel
%endif

Requires: python3-module-PyQt6-sip
%py3_provides pynest2d

%description
%summary

%prep
%setup

mkdir -p cmake
cp -a %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 cmake/
rm -rf CMakeLists.txt
cp -a %SOURCE7 %SOURCE8 .

%autopatch -p1

%build
# Decode PyQt6.sip ABI version from bytewise value
export PyQt6_SIP_ABI_VERSION=$(python3 <<EOF
from PyQt6.sip import SIP_ABI_VERSION as abi
print(f'{abi >> 16}.{abi >> 8 & 0xff}')
EOF
)

%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DPyQt6_SIP_ABI_VERSION=$PyQt6_SIP_ABI_VERSION
%cmake_build

%install
%cmake_install

%files
%doc README.md Documentation/*
%python3_sitelibdir/pynest2d.so
%python3_sitelibdir/pynest2d.pyi

%changelog
* Tue Apr 21 2026 Valery Zabrovsky <brow@altlinux.org> 5.10.0-alt1
- New version 5.10.0.
- Port to sip6 and PyQt6.sip.
- Update license and docs.

* Mon Jun 12 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.8-alt3
- Fixed build for Elbrus.

* Mon Feb 01 2021 Grigory Ustinov <grenka@altlinux.org> 4.8-alt2
- Fixed FTBFS.

* Mon Nov 16 2020 Anton Midyukov <antohami@altlinux.org> 4.8-alt1
- Initial build for Sisyphus

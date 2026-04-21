# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libsavitar
Version: 5.11.0
Release: alt0.alpha0.1
Summary: C++ implementation of 3mf loading with SIP Python bindings
License: LGPL-3.0-or-later
Group: Development/Other
Url: https://github.com/Ultimaker/libSavitar

# Upstream stopped tagging their versions; we have to get it by SHA. Ew!
%define libSavitar_sha 031a70a89e0945e823619be83771cba46e5f5141
# Source-url: https://github.com/Ultimaker/libSavitar/archive/%libSavitar_sha.tar.gz
Source: %name-%version.tar

# Python bits
%define pySavitar_sha 53fe14b35d561f4ff8dc2b0e80cb2d2dee2b20a8
# Source1-url: https://github.com/Ultimaker/pySavitar/archive/%pySavitar_sha.tar.gz
Source1: pySavitar-%version.tar

# CMake bits taken from 5.0.0, before upstream went nuts with conan
Source2: COPYING-CMAKE-SCRIPTS
Source3: FindSIP.cmake
Source4: FindSIP.py
Source5: SIPMacros.cmake
Source6: CMakeBuilder.py
Source7: StandardProjectSettings.cmake
Source8: CMakeLists.txt
Source9: SavitarConfig.cmake.in
Source10: pyproject.toml.in

# Actually export symbols into the shared lib
Patch0: libsavitar-5.2.2-export-fix.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: cmake dos2unix gcc-c++ libpugixml-devel
BuildRequires: python3-devel python3-module-sip6 python3-module-PyQt6-sip

%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package devel
Summary: Development files for libsavitar
# The cmake scripts are BSD
License: LGPL-3.0-or-later AND BSD-3-Clause
Group: Development/Other
Requires: %name = %EVR

%description devel
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

Development files.

%package -n python3-module-savitar
Summary: Python 3 libSavitar bindings
Group: Development/Python3
Requires: %name = %EVR
%py3_provides Savitar
Requires: python3-module-PyQt6-sip

%description -n python3-module-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep
%setup -a 1

cp -a pySavitar-%version/python .
mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 cmake/
rm -rf CMakeLists.txt
cp -a %SOURCE8 %SOURCE9 %SOURCE10 .
%autopatch -p1

# Wrong end of line encoding
dos2unix README.md

%build
# Decode PyQt6.sip ABI version from bytewise value
export PyQt6_SIP_ABI_VERSION=$(python3 <<EOF
from PyQt6.sip import SIP_ABI_VERSION as abi
print(f'{abi >> 16}.{abi >> 8 & 0xff}')
EOF
)

%add_optflags '-Wl,--as-needed'
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DPyQt6_SIP_ABI_VERSION=$PyQt6_SIP_ABI_VERSION
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_libdir/libSavitar.so.*

%files devel
%doc README.md LICENSE
%_libdir/libSavitar.so
%_includedir/Savitar
# Own the dir not to depend on cmake:
%_libdir/cmake

%files -n python3-module-savitar
%doc README.md
%python3_sitelibdir/pySavitar.so
%python3_sitelibdir/pySavitar.pyi

%changelog
* Tue Apr 21 2026 Valery Zabrovsky <brow@altlinux.org> 5.11.0-alt0.alpha0.1
- New version 5.11.0-alpha.0.
- Port to sip6 and PyQt6.sip.
- Fix license.

* Sat Nov 18 2023 Anton Midyukov <antohami@altlinux.org> 5.3.0-alt1
- new version (5.3.0) with rpmgs script

* Tue Apr 25 2023 Anton Midyukov <antohami@altlinux.org> 5.2.2-alt1
- new version (5.2.2) with rpmgs script

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 4.12.1-alt1
- new version (4.12.1) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 4.8-alt2
- add python3-module-sip requirement

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 4.8-alt1
- new version 4.8

* Fri Sep 18 2020 Anton Midyukov <antohami@altlinux.org> 4.7.1-alt1
- new version 4.7.1

* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 4.6.1-alt1
- new version 4.6.1

* Fri Jan 24 2020 Anton Midyukov <antohami@altlinux.org> 4.4.1-alt1
- new version 4.4.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 3.6.0-alt1
- new version 3.6.0

* Tue Oct 30 2018 Anton Midyukov <antohami@altlinux.org> 3.5.1-alt1
- new version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- new version 3.4.1

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1.S1
- new version 3.3.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1.S1
- new version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1.S1
- Initial build for ALT Sisyphus.

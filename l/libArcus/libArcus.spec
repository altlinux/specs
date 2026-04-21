# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libArcus
Version: 5.11.1
Release: alt1

Summary: Communication library between internal components for Ultimaker software
License: LGPL-3.0-or-later
Group: Development/Other
Url: https://github.com/Ultimaker/libArcus

# Upstream stopped tagging their versions; we have to get it by SHA. Ew!
%define libArcus_sha 50173cc681e9c331374c2648c64bc2544cb881c4
# Source-url: https://github.com/Ultimaker/%name/archive/%libArcus_sha.tar.gz
Source: %name-%version.tar

# Python bits
%define pyArcus_sha 367c69730567141168a8de6eb94f4eb4d6bb45c4
# Source1-url: https://github.com/Ultimaker/pyArcus/archive/%pyArcus_sha.tar.gz
Source1: pyArcus-%version.tar

# CMake bits taken from 5.0.0, before upstream went nuts with conan
Source2: COPYING-CMAKE-SCRIPTS
Source3: FindSIP.cmake
Source4: FindSIP.py
Source5: SIPMacros.cmake
Source6: CMakeBuilder.py
Source7: StandardProjectSettings.cmake
Source8: CMakeLists.txt
Source9: ArcusConfig.cmake.in
Source10: pyproject.toml.in

# Actually export symbols
Patch2: libArcus-5.2.2-actually-export-symbols.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: python3-dev
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(protobuf)
BuildRequires: protobuf-compiler
BuildRequires: python3-module-sip6
BuildRequires: python3-module-PyQt6-sip

%description
%summary

%package devel
Summary: Development files for %name
# The cmake scripts are BSD
License: LGPL-3.0-or-later AND BSD-3-Clause
Group:   Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%package -n python3-module-Arcus
Summary: Communication library between internal components for Ultimaker software
Group:   Development/Python3
%py3_provides Arcus
Requires: %name = %EVR
Requires: python3-module-PyQt6-sip

%description -n python3-module-Arcus
Communication library between internal components for Ultimaker software

%prep
%setup -n libArcus-%{version} -a 1

cp -a pyArcus-%version/python .
cp -a pyArcus-%version/src/PythonMessage.cpp python/
cp -a pyArcus-%version/include/pyArcus include
mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 cmake/
rm -rf CMakeLists.txt
cp -a %SOURCE8 %SOURCE9 %SOURCE10 .

%autopatch -p1

%build
# Decode PyQt6.sip ABI version from bytewise value
export PyQt6_SIP_ABI_VERSION=$(python3 <<EOF
from PyQt6.sip import SIP_ABI_VERSION as abi
print(f'{abi >> 16}.{abi >> 8 & 0xff}')
EOF
)

%cmake \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DPyQt6_SIP_ABI_VERSION=$PyQt6_SIP_ABI_VERSION
%cmake_build

%install
%cmake_install

%files
%_libdir/libArcus.so.*
%doc README.md

%files devel
%_libdir/libArcus.so
%_includedir/Arcus
%_libdir/cmake/Arcus

%files -n python3-module-Arcus
%python3_sitelibdir/pyArcus.so
%python3_sitelibdir/pyArcus.pyi

%changelog
* Tue Apr 21 2026 Valery Zabrovsky <brow@altlinux.org> 5.11.1-alt1
- New version 5.11.1.
- Port to sip6 and PyQt6.sip.
- Update license.

* Sat Nov 18 2023 Anton Midyukov <antohami@altlinux.org> 5.3.0-alt1
- new version (5.3.0) with rpmgs script

* Tue Apr 25 2023 Anton Midyukov <antohami@altlinux.org> 5.2.2-alt1
- new version (5.2.2) with rpmgs script

* Thu Dec 29 2022 Alexey Shabalin <shaba@altlinux.org> 4.13.0-alt2
- fixed build with new protobuf

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 4.12.1-alt1
- new version (4.12.1) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Thu Jul 15 2021 Vitaly Lipatov <lav@altlinux.ru> 4.8-alt2
- add python3-module-sip requirement

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 4.8-alt1
- New version 4.8

* Thu Sep 17 2020 Anton Midyukov <antohami@altlinux.org> 4.7.1-alt1
- New version 4.7.1

* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 4.6.1-alt1
- New version 4.6.1

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 4.4.1-alt1
- New version 4.4.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 3.6.0-alt1
- New version 3.6.0

* Tue Oct 30 2018 Anton Midyukov <antohami@altlinux.org> 3.5.1-alt1
- New version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- New version 3.4.1

* Mon May 21 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1.S1.1
- Rebuilt with protobuf-compiler 3.5.2

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1.S1
- New version 3.3.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1.S1
- New version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1.S1
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1.S1
- Initial build for ALT Sisyphus.

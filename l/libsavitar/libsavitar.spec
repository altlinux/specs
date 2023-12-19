# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libsavitar
Version: 5.3.0
Release: alt1
Summary: C++ implementation of 3mf loading with SIP Python bindings
License: LGPLv3+
Group: Development/Other
Url: https://github.com/Ultimaker/libSavitar

# Source-url: https://github.com/Ultimaker/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Python bits
# Source1-url: https://github.com/Ultimaker/pySavitar/archive/%version.tar.gz
Source1: pySavitar-%version.tar

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2: FindSIP.cmake
Source3: SIPMacros.cmake
Source4: CMakeLists.txt
Source5: SavitarConfig.cmake.in
Source6: COPYING-CMAKE-SCRIPTS
 
# Actually export symbols into the shared lib
Patch0: libsavitar-5.2.2-export-fix.patch

Patch1: find-sip3.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: cmake dos2unix gcc-c++ libpugixml-devel python3-devel python3-module-sip-devel %_bindir/sip3

%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package devel
Summary: Development files for libsavitar
# The cmake scripts are BSD
License: AGPLv3+ and BSD
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
Requires: python3-module-PyQt5-sip

%description -n python3-module-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep
%setup -a 1

cp -a pySavitar-%version/python .
mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE6 cmake/
rm -rf CMakeLists.txt
cp -a %SOURCE4 %SOURCE5 .
%autopatch -p1

# Wrong end of line encoding
dos2unix README.md

# https://github.com/Ultimaker/libSavitar/pull/18
sed -i 's/Python3_SITELIB/Python3_SITEARCH/' cmake/SIPMacros.cmake

%build
%add_optflags '-Wl,--as-needed'
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
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

%changelog
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

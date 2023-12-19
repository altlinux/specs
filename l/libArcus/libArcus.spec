# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libArcus
Version: 5.3.0
Release: alt1

Summary: Communication library between internal components for Ultimaker software
License: LGPLv3+
Group: Development/Other
Url: https://github.com/Ultimaker/libArcus

# Source-url: https://github.com/Ultimaker/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Python bits
# Source1-url: https://github.com/Ultimaker/pyArcus/archive/%version.tar.gz
Source1: pyArcus-%version.tar

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2: FindSIP.cmake
Source3: SIPMacros.cmake
Source4: CMakeLists.txt
Source5: CPackConfig.cmake
Source6: ArcusConfig.cmake.in
Source7: COPYING-CMAKE-SCRIPTS

Patch: fix_find_sip.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1601917
Patch1: libArcus-3.10.0-PyQt6.sip.patch
 
# Actually export symbols
Patch2: libArcus-5.2.2-actually-export-symbols.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: python3-dev
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(protobuf)
BuildRequires: protobuf-compiler
BuildRequires: python3-module-sip-devel
BuildRequires: python3-module-PyQt6-sip

%description
%summary

%package devel
Summary: Development files for %name
Group:   Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%package -n python3-module-Arcus
Summary: Communication library between internal components for Ultimaker software
Group:   Development/Python3
%py3_provides Arcus
Requires: %name = %EVR
Requires: python3-module-PyQt5-sip

%description -n python3-module-Arcus
Communication library between internal components for Ultimaker software

%prep
%setup -n libArcus-%{version} -a 1
 
cp -a pyArcus-%version/python .
cp -a pyArcus-%version/include/pyArcus include
mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE7 cmake/
rm CMakeLists.txt
cp -a %SOURCE4 %SOURCE5 %SOURCE6 .
cp -a pyArcus-%version/src/PythonMessage.cpp python/

%autopatch -p1

# https://github.com/Ultimaker/libArcus/pull/94#issuecomment-505376760
sed -i 's/Python3_SITELIB/Python3_SITEARCH/' cmake/SIPMacros.cmake

%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF \
       -DCMAKE_SKIP_RPATH:BOOL=ON
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

%changelog
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

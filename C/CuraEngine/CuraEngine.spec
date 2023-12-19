# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: CuraEngine
Epoch: 1
Version: 5.4.0
Release: alt1

Summary: Engine for processing 3D models into G-code instructions for 3D printers
License: AGPL-3.0-or-later
Group: Engineering
Url: https://github.com/Ultimaker/CuraEngine

# Source-url: https://github.com/Ultimaker/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2: FindGMock.cmake
Source3: FindPolyclipping.cmake
Source4: FindStb.cmake
Source5: CMakeLists.txt
Source6: CPackConfig.cmake

# This is some kind of "public" layer of a private logging thing
# It's header-only and not usable as a system library,
# so I (churchyard) decided to bundle it for now. Shame on me.
# It's AGPL-3.0-or-later.
%global scripta_version c378c837eeb505146ab67abe0904bfed2099128f
# Source7-url: https://github.com/Ultimaker/Scripta_public/archive/%{scripta_version}/Scripta_public-%{scripta_version}.tar.gz
Source7: Scripta_public.tar

Patch2: %name-static-libstdcpp.patch
Patch3: %name-5.4.0-fmt10.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: protobuf-compiler
BuildRequires: pkgconfig(protobuf)
BuildRequires: libpolyclipping-devel
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: libArcus-devel
BuildRequires: libstb-devel
BuildRequires: libfmt-devel
BuildRequires: libspdlog-devel
BuildRequires: boost-devel-headers
BuildRequires: librange-v3-devel
BuildRequires: boost-polygon-devel

%description
CuraEngine is a powerful, fast and robust engine for processing 3D
models into 3D printing instruction for Ultimaker and other GCode
based 3D printers. It is part of the larger open source project
called "Cura".

The CuraEngine is a C++ console application for 3D printing GCode
generation. It has been made as a better and faster alternative
to the old Skeinforge engine.

%prep
%setup

mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE4 cmake
rm -rf CMakeLists.txt
cp -a %SOURCE5 %SOURCE6 .

tar xf %SOURCE7
mv Scripta_public/include/scripta/ include

%autopatch -p1

# bundled libraries
rm -rf libs

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DSET_RPATH:BOOL=OFF \
       -DCURA_ENGINE_VERSION:STRING=%version \
       -DUSE_SYSTEM_LIBS:BOOL=ON \
       -DCMAKE_CXX_FLAGS_RELEASE_INIT:STRING="%optflags -fPIC" \
       -DStb_INCLUDE_DIRS:PATH=%_includedir/stb

%cmake_build

%install
%cmake_install

%check
# Smoke test
%buildroot%_bindir/%name help

%files
%_bindir/%name
%doc README.md

%changelog
* Mon Dec 18 2023 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Thu Oct 12 2023 Nazarov Denis <nenderus@altlinux.org> 1:5.3.1-alt1.1
- NMU: Fix build with libfmt 10

* Thu Apr 27 2023 Anton Midyukov <antohami@altlinux.org> 1:5.3.1-alt1
- new version (5.3.1) with rpmgs script

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 1:4.12.1-alt1
- new version (4.12.1) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 1:4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 1:4.8-alt1
- New version 4.8

* Fri Sep 18 2020 Anton Midyukov <antohami@altlinux.org> 1:4.7.1-alt1
- New version 4.7.1

* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 1:4.6.1-alt1
- New version 4.6.1

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1
- New version 4.4.1

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1
- New version 3.6.0

* Tue Oct 30 2018 Anton Midyukov <antohami@altlinux.org> 1:3.5.1-alt1
- New version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 1:3.4.1-alt1
- New version 3.4.1

* Mon May 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1.1
- Rebuilt with protobuf-compiler 3.5.2

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1
- New version 3.3.0
- Make sure Fedora CXXFLAGS are used, also -fPIC
- Use new USE_SYSTEM_LIBS option instead of patch+sed

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 1:3.2.1-alt1.S1
- New version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Sat Nov 25 2017 Igor Vlasenko <viy at altlinux.ru> 15.04-alt2_5
- rebuild with libpolyclipping

* Thu Mar 16 2017 Igor Vlasenko <viy at altlinux.ru> 15.04-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy at altlinux.ru> 15.04-alt1_2
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy at altlinux.ru> 14.12.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy at altlinux.ru> 14.03-alt1_1
- update to new release by fcimport

* Sat Jun 07 2014 Igor Vlasenko <viy at altlinux.ru> 14.01-alt1_1
- by request of Dmitry Derjavin <dd@>

%define _unpackaged_files_terminate_build 1

%def_with check

Name: CuraEngine
Epoch: 1
Version: 5.14.0
Release: alt1

Summary: Powerful, fast and robust engine for converting 3D models into g-code
License: AGPL-3.0-or-later
Group: Engineering
URL: https://github.com/Ultimaker/CuraEngine
VCS: https://github.com/Ultimaker/CuraEngine

Source: %name-%version.tar
# Header-only libraries for basic geometric operations:
# unions, intersections, differences, and XORs.
# Distributed under BSL-1.0.
Source1: mapbox-geometry.tar
Source2: mapbox-wagyu.tar
# This is some kind of "public" layer of a private logging thing
# It's header-only and not usable as a system library,
# so I (churchyard) decided to bundle it for now. Shame on me.
# It's AGPL-3.0-or-later.
Source3: scripta.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel-headers
BuildRequires: boost-geometry-devel
BuildRequires: boost-polygon-devel
BuildRequires: cura-formulae-engine-devel
BuildRequires: libArcus-devel
BuildRequires: libfmt-devel
BuildRequires: libpng-devel
BuildRequires: libpolyclipping-devel
BuildRequires: libprotobuf-devel
BuildRequires: librange-v3-devel
BuildRequires: libspdlog-devel
BuildRequires: libstb-devel
BuildRequires: rapidjson-devel
BuildRequires: tbb-devel
BuildRequires: zlib-devel
%if_with check
BuildRequires: ctest
BuildRequires: libgtest-devel
%endif

%description
CuraEngine is a powerful, fast and robust engine for converting 3D models
into g-code instructions for 3D printers. Designed as a better and faster
alternative to the old Skeinforge Engine and is an integral part of Cura.
You can use CuraEngine separately, in other applications and integrate it
into your own app.

%prep
%setup -a1 -a2 -a3
%autopatch -p1

%build
%cmake \
    -DCURA_ENGINE_VERSION=%version \
    -DENABLE_TESTING=%{?_with_check:ON}%{!?_with_check:OFF} \
    -DENABLE_PLUGINS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Wed Nov 11 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.14.0-alt1
- New version 5.14.0.
- Switch to build from Gear tags.
- Update summary and description.
- Use builtin tests in check section.

* Wed May 27 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt1
- New version 5.13.0.

* Fri Apr 17 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.12.1-alt1
- New version 5.12.1.

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

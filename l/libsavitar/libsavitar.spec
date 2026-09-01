%define _unpackaged_files_terminate_build 1

Name: libsavitar
Version: 5.12.0
Release: alt1.gc513049b.1

Summary: C++ implementation of 3mf loading
License: LGPL-3.0-or-later
Group: System/Libraries
URL: https://github.com/Ultimaker/libSavitar
VCS: https://github.com/Ultimaker/libSavitar

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libpugixml-devel
BuildRequires: dos2unix

%description
Savitar is a C++ implementation of 3mf (3D printing file format) loading.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
%summary.

%prep
%setup
%autopatch -p1

# Wrong end of line encoding
dos2unix README.md

%build
%add_optflags '-Wl,--as-needed'
%cmake \
    -DSAVITAR_VERSION=%version \
    -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%_libdir/libSavitar.so.*

%files devel
%doc README.md LICENSE
%_libdir/libSavitar.so
%_includedir/Savitar
%_cmakedir/Savitar

%changelog
* Mon Aug 31 2026 Valery Zabrovsky <brow@altlinux.org> 5.12.0-alt1.gc513049b.1
- Move pySavitar to a separate package.
- Switch to more appropriate rolling tagging.
- Update to latest snapshot.
- Minor spec cleanup.

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

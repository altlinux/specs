# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 1

Name: libsysstat-qt6
Version: 1.0.0
Release: alt1

Summary: Library used to query system info and statistics
License: LGPL-2.0
Group: System/Libraries

Url: https://github.com/lxqt/libsysstat
Source: %name-%version.tar

BuildRequires: rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: lxqt2-build-tools qt6-base-devel qt6-tools-devel

%description
%summary.

%package devel
Summary: Development headers for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package provides the development files for %name
which is used to query system info and statistics.

%prep
%setup

%build
%ifarch %e2k
%add_optflags -std=c++11
%endif
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*

%files devel
%_libdir/%name.so
%_includedir/sysstat-qt6/
%_pkgconfigdir/sysstat-qt6.pc
%_datadir/cmake/sysstat-qt6/

%changelog
* Mon Jul 08 2024 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0
- rename package libsysstat-qt5 -> libsysstat-qt6

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 0.4.6-alt1
- new version 0.4.6

* Thu Apr 29 2021 Anton Midyukov <antohami@altlinux.org> 0.4.5-alt2
- use macros for e2k arch

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.4.5-alt1
- new version 0.4.5

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.4.4-alt1
- new version 0.4.4

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.4.3-alt1
- new version 0.4.3

* Sat Jan 26 2019 Anton Midyukov <antohami@altlinux.org> 0.4.2-alt1
- new version 0.4.2

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1.1
- Rebuilt with qt 5.11

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Aug 25 2017 Michael Shigorin <mike@altlinux.org> 0.3.2-alt2
- E2K: add -std=c++11 explicitly

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- 0.3.1

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- 0.3.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- use untagged upstream commit g151ef16 (NB: API change)

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release


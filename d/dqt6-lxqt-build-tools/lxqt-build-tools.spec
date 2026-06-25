# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: dqt6-lxqt-build-tools
Version: 2.4.0
Release: alt0.dde.1

Summary: lxqt-build-tools fork for DDE
License: BSD-3-clause
Group: Development/Other

Url: https://github.com/lxqt/lxqt-build-tools
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: lxqt-transupdate-dqt6-fix.patch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: dqt6-base-devel dqt6-tools-devel glib2-devel

BuildArch: noarch

%description
%summary.
That used to lurk in liblxqt or got spread over other subprojects.

%prep
%setup
%patch0 -p1
%patch1 -p2

%ifarch %e2k
# lcc has -fwhole, to be tested though
sed -i '/-flto/d' cmake/modules/LXQtCompilerSettings.cmake
%endif

%build
export PATH=%_dqt6_bindir:$PATH
%cmake \
  -DCMAKE_PREFIX_PATH=%_dqt6_libdir/cmake \
  -DCMAKE_INSTALL_BINDIR=%_dqt6_bindir \
  -DCMAKE_INSTALL_DATAROOTDIR=%_dqt6_datadir \
#
%cmake_build

%install
%cmake_install

%files
%doc BSD-3-Clause
%_dqt6_datadir/cmake/lxqt2-build-tools
%_dqt6_bindir/*

%changelog
* Thu Jun 25 2026 Leontiy Volodin <lvol@altlinux.org> 2.4.0-alt0.dde.1
- fork for deepin qt6 packages

* Thu Jan 29 2026 Leontiy Volodin <lvol@altlinux.org> 0.13.0-alt2.dde.1
- fork qt5 for separate deepin buildings (ALT #48138)

* Thu Apr 18 2024 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt3
- fix typo in License field
- update Url field

* Tue Sep 05 2023 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt2
- fix lxqt-transupdate for use lupdate-qt5

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- New version 0.13.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt1
- new version 0.12.0

* Mon Sep 26 2022 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt2
- add upstream patch for fix find gio-unix-2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1
- new version 0.11.0

* Thu Mar 24 2022 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt2
- fix for glib2 >= 2.71.1

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- new version 0.10.0

* Thu Apr 29 2021 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt2
- use macros for e2k arch

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.8.0-alt1
- new version 0.8.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Sat Jan 26 2019 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- new version 0.6.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1.1
- Rebuilt with qt 5.11

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- new version 0.5.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt2
- fix BR:
- E2K: avoid lcc-unsupported options

* Tue Sep 26 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- initial release (based on fedora package)


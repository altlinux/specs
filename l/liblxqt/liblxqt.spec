# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: liblxqt
Version: 2.0.0
Release: alt1

Summary: Core utility library for LxQt components
License: LGPL-2.1
Group: Graphical desktop/Other

Url: https://github.com/lxqt/liblxqt
Source: %name-%version.tar
Patch: liblxqt-2.0.0-fix_translate_load.patch

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt6-base-devel qt6-tools-devel
# qt6-x11extras-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: lxqt2-build-tools libqt6xdg-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libpolkitqt6-qt6-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)

Requires: qt6-svg

Provides: librazorqt = %version
Obsoletes: librazorqt < 0.7.0

Provides: %name-data = %version
Obsoletes: %name-data < 0.11.0
Obsoletes: lxqt-backlight_backend < %EVR
Obsoletes: lxqt-l10n < %EVR

%description
%summary.

%package devel
Summary: Development headers for LXQt library
Group: Development/C++
Requires: %name = %version
Requires: lxqt2-build-tools

%description devel
This package provides the development files for LXQt library.

%prep
%setup
%patch -p1

%build
%cmake -DUPDATE_TRANSLATIONS=ON \
	
%cmake_build

%install
%cmake_install

%files
%_libdir/*.so.*
%doc AUTHORS CHANGELOG COPYING README.md
%_bindir/lxqt-backlight_backend
%dir %_datadir/lxqt
%_datadir/lxqt/*
%_datadir/polkit-1/actions/org.lxqt.backlight.pkexec.policy

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Mon Jul 08 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0.

* Thu Nov 16 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt2
- cleanup BR

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Sat Jun 06 2020 Anton Midyukov <antohami@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Mon Mar 23 2020 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt3
- rebuilt with libqtxdg-0.2.0

* Sat Dec 14 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt2
- fix load qt5 translation (Thanks zerg@)

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Sat Jan 26 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1.1
- Rebuilt with qt 5.11

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0
- data subpackage superseded by lxqt-l10n

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0 built against qt5

* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace librazorqt

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release


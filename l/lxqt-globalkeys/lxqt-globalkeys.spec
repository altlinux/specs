# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-globalkeys
Version: 0.14.0
Release: alt1

Summary: Service used to register global keyboard shortcuts
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: rpm-build-xdg libqtxdg-devel
BuildRequires: libqt5-widgets
BuildRequires: kf5-kwindowsystem-devel

Provides: razorqt-globalkeyshortcuts = %version
Obsoletes: razorqt-globalkeyshortcuts < 0.7.0

Conflicts: lxqt-common <= 0.11.0

%description
%summary

%package devel
Summary: Development headers for %name
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/*.so.*
%_xdgconfigdir/*/*
%_datadir/lxqt/translations/lxqt-config-globalkeyshortcuts/
%_desktopdir/*.desktop
%doc AUTHORS CHANGELOG LICENSE README.md

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-globalkeyshortcuts

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release


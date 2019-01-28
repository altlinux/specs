# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libqtxdg
Version: 3.3.0
Release: alt1

Summary: Qt implementation of freedesktop.org xdg specs
License: LGPL
Group: System/Libraries

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-svg-devel libmagic-devel

%description
%summary

%package devel
Summary: Development headers for QtXdg library
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for qtxdg library
which implements functions of the XDG Specifications in Qt.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*
%_qt5_plugindir/*/*.so

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Sat Jan 26 2019 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt1.1
- Rebuilt with qt 5.11

* Tue May 22 2018 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt1
- new version 3.2.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 3.1.0-alt1
- 3.1.0

* Tue Sep 26 2017 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1
- 3.0.0
  + see http://lxqt.org/release/2017/09/22/libqtxdg-300/

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 2.0.0-alt1
- 2.0.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0 built against qt5

* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- 0.5.3
  + thanks jleclanche for rapid update so the standalone
    library package version is greater than 0.5.2 which
    was bundled with razorqt
- spec generalization while at that
- updated the Url:

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- initial standalone release


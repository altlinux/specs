Name: libqtxdg
Version: 2.0.0
Release: alt1

Summary: Qt implementation of freedesktop.org xdg specs
License: LGPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

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
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
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


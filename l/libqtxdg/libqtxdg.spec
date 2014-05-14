Name: libqtxdg
Version: 0.5.3
Release: alt1

Summary: Qt implementation of freedesktop.org xdg specs
License: LGPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libqt4-devel libmagic-devel

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
%_datadir/%name/

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- 0.5.3
  + thanks jleclanche for rapid update so the standalone
    library package version is greater than 0.5.2 which
    was bundled with razorqt
- spec generalization while at that
- updated the Url:

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- initial standalone release


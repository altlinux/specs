Name: liblxqt-mount
Version: 0.9.0
Release: alt1

Summary: Library used to manage removable devices
License: LGPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel

%description
%summary

%package devel
Summary: Development headers for LXQt-mount library
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for LXQt-mount library.

%prep
%setup
# FIXME: https://github.com/lxde/lxde-qt/issues/299 (updated for 0.9.0 too)
sed -i 's,^set(MINOR_VERSION 8)$,set(MINOR_VERSION 9),' CMakeLists.txt

%build
%cmake_insource
%make_build

%install
%makeinstall_std
# FIXME: kludge to get pkgconfig file straight (relevant as of 0.9.0)
sed -i 's,^Version:.*$,Version: %version,' %buildroot%_pkgconfigdir/*.pc

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_libdir/cmake/*/

%changelog
* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0
- pkgconfig file fixup

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release


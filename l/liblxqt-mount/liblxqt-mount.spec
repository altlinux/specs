Name: liblxqt-mount
Version: 0.7.0
Release: alt1

Summary: Library used to manage removable devices
License: LGPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel

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
* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release


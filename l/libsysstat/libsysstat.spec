Name: libsysstat
Version: 0.1.0
Release: alt1

Summary: Library used to query system info and statistics
License: LGPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libqt4-devel

%description
%summary

%package devel
Summary: Development headers for %name
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for %name
which is used to query system info and statistics.

%prep
%setup
# https://github.com/lxde/lxde-qt/issues/75
sed -i 's,RAZOR_VERSION,SYSSTAT_VERSION,' cmake/create_pkgconfig_file.cmake

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
* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release


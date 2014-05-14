Name: liblxqt
Version: 0.7.0
Release: alt2

Summary: Core utility library for LXDE-Qt components
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libqt4-devel
BuildRequires: libqtxdg-devel

Provides: librazorqt = %version
Obsoletes: librazorqt < 0.7.0

%description
%summary

%package data
Summary: Shared data for LXQt
Group: Graphical desktop/Other
BuildArch: noarch

%description data
This package provides shared data files for LXQt library.

%package devel
Summary: Development headers for LXQt library
Group: Development/C++
Requires: %name = %version

%description devel
This package provides the development files for LXQt library.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS

%files data
%_datadir/lxqt/

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace librazorqt

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release


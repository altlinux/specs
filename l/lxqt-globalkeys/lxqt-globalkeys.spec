Name: lxqt-globalkeys
Version: 0.7.0
Release: alt2

Summary: Service used to register global keyboard shortcuts
License: LGPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: liblxqt-devel libqt4-devel

Provides: razorqt-globalkeyshortcuts = %version
Obsoletes: razorqt-globalkeyshortcuts < 0.7.0

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
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/*.so.*
%_datadir/lxqt/*
%_desktopdir/*.desktop
%doc AUTHORS

%files devel
%_libdir/*.so
%_includedir/*/
%_pkgconfigdir/*.pc
%_datadir/cmake/*/

%changelog
* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- replace razorqt-globalkeyshortcuts

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release


Name: libsysstat
Version: 0.3.2
Release: alt1

Summary: Library used to query system info and statistics
License: LGPL
Group: System/Libraries

Url: http://lxqt.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: qt5-base-devel qt5-tools-devel

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
* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Nov 03 2015 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- 0.3.1

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- 0.3.0 built against qt5

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2
- use untagged upstream commit g151ef16 (NB: API change)

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.1.0-alt1
- initial release


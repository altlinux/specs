%define _name kpmcore

Name: lib%_name
Version: 3.3.0
Release: alt1

Summary: Library for managing partitions
Group: System/Libraries
License: GPLv3
Url: https://github.com/KDE/%_name

Source: %url/archive/%_name-%version.tar.gz

Provides: %_name = %version-%release

%define blkid_ver 2.30

BuildRequires: gcc-c++ extra-cmake-modules rpm-build-kf5
BuildRequires: libatasmart-devel libblkid-devel >= %blkid_ver libparted-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel

%description
%_name is a Library for managing partitions. Common code for KDE
Partition Manager and other projects.

%package devel
Summary: Development files for icclib
Group: Development/C
Requires: %name = %version-%release
Provides: %_name-devel = %version-%release

%description devel
%_name is a Library for managing partitions. Common code for KDE
Partition Manager and other projects.

This package provides headers and libraries for development applications
using %_name.

%prep
%setup -n %_name-%version

%build
%K5build

%install
%K5install

%files
%_K5lib/*.so.*
%_libdir/qt5/plugins/*.so
%_K5srv/pmdummybackendplugin.desktop
%_K5srv/pmlibpartedbackendplugin.desktop
%_K5srvtyp/pmcorebackendplugin.desktop

%files devel
%_includedir/%_name/
%_K5lib/cmake/KPMcore/
%_K5link/*.so


%changelog
* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- first build for Sisyphus


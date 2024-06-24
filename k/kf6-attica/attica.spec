%define rname attica

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 Open Collaboration Services API
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel

%description
Attica is a Qt library that implements the Open Collaboration Services API.
It grants easy access to the services such as querying information about persons and contents.
The library is used in KNewStuff3 as content provider.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6attica
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6attica
KF6 library


%prep
%setup -n %rname-%version
#find ./ -type f -and \( -name \*.cmake -or -name \*.h \) | \
#while read f ; do
#    sed -i 's|CMAKE_LIBATTICA_VERSION_|ATTICA_VERSION_|g' $f
#done

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/attica_version.h
%_K6inc/Attica/
%_K6link/lib*.so
%_K6lib/cmake/KF6Attica
%_pkgconfigdir/*.pc

%files -n libkf6attica
%_K6lib/libKF6Attica.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build


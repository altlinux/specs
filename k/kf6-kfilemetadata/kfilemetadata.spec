%define rname kfilemetadata

%def_enable exiv2

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 extracting text and metadata from different files
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-multimedia-devel
BuildRequires: ebook-tools-devel libpoppler-qt6-devel libtag-devel
%if_enabled exiv2
BuildRequires: libexiv2-devel
%endif
BuildRequires: libattr-devel
BuildRequires: libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel
BuildRequires: kf6-karchive-devel kf6-ki18n-devel kf6-kconfig-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kcodecs-devel

%description
KFileMetaData provides a simple library for extracting the text and metadata
from a number of different files. This library is typically used by file
indexers to retreive the metadata.

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

%package -n libkf6filemetadata
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6filemetadata
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/kfilemetadata_version.h
%_K6inc/KFileMetaData/
%_K6link/lib*.so
%_K6lib/cmake/KF6FileMetaData

%files -n libkf6filemetadata
%_K6lib/libKF6FileMetaData.so.*
%_K6plug/kf6/kfilemetadata/


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build


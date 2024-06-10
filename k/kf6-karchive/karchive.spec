%define rname karchive

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 compression and decompression of data
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Jan 20 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt6-core libqt6-test libstdc++-devel python-base ruby ruby-stdlibs zlib-devel
#BuildRequires: bzlib-devel extra-cmake-modules gcc-c++ liblzma-devel python-module-google qt6-base-devel rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-base-devel qt6-tools-devel
BuildRequires: bzlib-devel extra-cmake-modules gcc-c++ liblzma-devel zlib-devel libzstd-devel

%description
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR. It also provides transparent
compression and decompression of data, like the GZip format,
via a subclass of QIODevice.

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

%package -n libkf6archive
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6archive
KF6 library


%prep
%setup -n %rname-%version

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
#%_K6inc/karchive_version.h
%_K6inc/KArchive/
%_K6link/lib*.so
%_K6lib/cmake/KF6Archive

%files -n libkf6archive
%_K6lib/libKF6Archive.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build


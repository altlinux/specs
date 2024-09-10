%define rname kdoctools

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 creating documentation from DocBook
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: docbook-style-xsl

Source: %rname-%version.tar
Patch1: alt-find-docbookxml.patch
Patch2: alt-doc-dirs-fallback.patch

# Automatically added by buildreq on Wed Feb 11 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds elfutils libcloog-isl4 libgpg-error libqt6-core libstdc++-devel libxml2-devel pkg-config python-base xml-common xml-utils
#BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf6-karchive-devel kf6-ki18n-devel libxslt-devel python-module-google qt6-base-devel ruby ruby-stdlibs xsltproc
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ kf6-karchive-devel kf6-ki18n-devel libxslt-devel qt6-base-devel xsltproc
BuildRequires: docbook-style-xsl xml-utils
BuildRequires: perl-URI

%description
Provides tools to generate documentation in various format from DocBook files.

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
Requires: %name-common = %version-%release
Requires: %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
BuildArch: noarch
Requires: %name-devel
%description devel-static
Static libraries for %name.

%package -n libkf6doctools
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6doctools
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md

%files
%_bindir/*6
%_K6bin/checkXML6
%_K6bin/meinproc6
%_K6data/kdoctools/

%files devel
%_K6inc/KDocTools/
%_K6link/lib*.so
%_K6lib/cmake/KF6DocTools

%files devel-static
#%_K6lib/lib*.a

%files -n libkf6doctools
%_K6lib/libKF6DocTools.so.*


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build


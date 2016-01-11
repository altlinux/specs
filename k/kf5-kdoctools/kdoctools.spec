%define rname kdoctools

Name: kf5-%rname
Version: 5.18.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 creating documentation from DocBook
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-find-docbookxml.patch

# Automatically added by buildreq on Wed Feb 11 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds elfutils libcloog-isl4 libgpg-error libqt5-core libstdc++-devel libxml2-devel pkg-config python-base xml-common xml-utils
#BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-ki18n-devel libxslt-devel python-module-google qt5-base-devel ruby ruby-stdlibs xsltproc
BuildRequires(pre): rpm-build-kf5
BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-ki18n-devel libxslt-devel qt5-base-devel xsltproc
BuildRequires: perl-URI

%description
Provides tools to generate documentation in various format from DocBook files.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %version-%release
Requires: docbook-style-xsl
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-devel
%description devel-static
Static libraries for %name.

%package -n libkf5doctools
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5doctools
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING.LIB README.md

%files
%_bindir/*5
%_K5bin/checkXML5
%_K5bin/meinproc5
%_K5data/kdoctools/

%files devel
%_K5inc/XsltKde/
%_K5lib/cmake/KF5DocTools

%files devel-static
%_K5lib/lib*.a

%changelog
* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- test

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt0.1
- initial build

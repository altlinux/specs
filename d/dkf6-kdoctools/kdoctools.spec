%define rname kdoctools

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 creating documentation from DocBook
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: docbook-style-xsl

Source: %name-%version.tar
Patch1: alt-find-docbookxml.patch
Patch2: alt-doc-dirs-fallback.patch

# Automatically added by buildreq on Wed Feb 11 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds elfutils libcloog-isl4 libgpg-error libqt6-core libstdc++-devel libxml2-devel pkg-config python-base xml-common xml-utils
#BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf6-karchive-devel kf6-ki18n-devel libxslt-devel python-module-google qt6-base-devel ruby ruby-stdlibs xsltproc
BuildRequires(pre): rpm-build-dkf6
BuildRequires: deepin-extra-cmake-modules dqt6-tools-devel
BuildRequires: dkf6-karchive-devel dkf6-ki18n-devel
BuildRequires: libxslt-devel xsltproc
BuildRequires: docbook-style-xsl xml-utils
BuildRequires: perl-URI

# find libraries
%add_findprov_lib_path %_DK6lib

%description
Provides tools to generate documentation in various format from DocBook files.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
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

%package -n libdkf6doctools
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libdkf6doctools
KF6 library


%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1

%build
%DK6build

%install
%DK6install
%find_lang %name --with-kde --all-name
%DK6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_DK6data/man/
%_DK6data/man/*

%files
%exclude %_bindir/*6
%_DK6bin/checkXML6
%_DK6bin/meinproc6
%_DK6data/kdoctools/

%files devel
%_DK6inc/KDocTools/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6DocTools

%files devel-static
#%_DK6lib/lib*.a

%files -n libdkf6doctools
%_DK6lib/libKF6DocTools.so.*


%changelog
* Thu Aug 27 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

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


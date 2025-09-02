%define Name KBibTeX
%define oname kbibtex

%define soname 0
Name: kbibtex
Version: 0.10.0
Release: alt1
Summary: A BibTeX editor for Qt5 and KDE5
License: %gpl2plus
Group: Publishing
URL: https://apps.kde.org/kbibtex/
Requires: %name-core
Requires: qt5-wayland
Conflicts: kde3-kbibtex

Source: %oname-%version.tar
BuildRequires(pre): rpm-build-licenses rpm-build-kf5 rpm-macros-cmake
BuildRequires: qt5-networkauth-devel
BuildRequires: gcc-c++
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: libpoppler-qt5-devel
BuildRequires: libxslt-devel xml-utils xorg-cf-files
BuildRequires: libicu-devel

%description
%Name is a BibTeX editor for Qt5 and KDE5 to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. As %Name is using KDE's KParts technology.

%package -n lib%{oname}config%soname
Summary: %Name config libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}config%soname
%Name config libraries.

%package -n lib%{oname}data%soname
Summary: %Name data libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}data%soname
%Name data libraries.

%package -n lib%{oname}global%soname
Summary: %Name global libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}global%soname
%Name global libraries.

%package -n lib%{oname}gui%soname
Summary: %Name gui libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}gui%soname
%Name gui libraries.

%package -n lib%{oname}io%soname
Summary: %Name io libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}io%soname
%Name io libraries.

%package -n lib%{oname}networking%soname
Summary: %Name networking libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}networking%soname
%Name networking libraries.

%package -n lib%{oname}processing%soname
Summary: %Name processing libraries
Group: System/Libraries
Requires: kbibtex-common
Obsoletes: libkbibtexpart9 < %EVR

%description -n lib%{oname}processing%soname
%Name processing libraries.


%package common
Summary: Common files for %Name
Group: Publishing
Conflicts: libkbibtexpart9 < %EVR

%description common
Common files for %Name


%package core
Summary: Core files for %Name
Group: Publishing
Provides: libkbibtexpart9 = %EVR
Obsoletes: libkbibtexpart9 < %EVR

%description core
Core files for %Name


%package devel
Summary: Development files for %Name
Group: Development/Other

%description devel
Development files for %Name

%prep
%setup -n %oname-%version

# Bump CXX standard in CMakeLists.txt to required by libicu74 to build with
# extended unicode support.
sed -i '/CMAKE_CXX_STANDARD/s/11/17/' CMakeLists.txt

%build
%K5build

%install
%K5cmake
%K5install

%find_lang --with-kde %oname

%files
%_datadir/%oname
%_K5bin/%oname
%_K5icon/*/*/apps/*
%_datadir/metainfo/*

%files -n lib%{oname}config%soname
%_libdir/libkbibtexconfig.so.%soname
%_libdir/libkbibtexconfig.so.*

%files -n lib%{oname}data%soname
%_libdir/libkbibtexdata.so.%soname
%_libdir/libkbibtexdata.so.*

%files -n lib%{oname}global%soname
%_libdir/libkbibtexglobal.so.%soname
%_libdir/libkbibtexglobal.so.*

%files -n lib%{oname}gui%soname
%_libdir/libkbibtexgui.so.%soname
%_libdir/libkbibtexgui.so.*

%files -n lib%{oname}io%soname
%_libdir/libkbibtexio.so.%soname
%_libdir/libkbibtexio.so.*

%files -n lib%{oname}networking%soname
%_libdir/libkbibtexnetworking.so.%soname
%_libdir/libkbibtexnetworking.so.*

%files -n lib%{oname}processing%soname
%_libdir/libkbibtexprocessing.so.%soname
%_libdir/libkbibtexprocessing.so.*


%files common -f %oname.lang
%_K5xdgapp/*
%_K5xdgmime/*
%_datadir/qlogging-categories5/*

%files core
%_K5xmlgui/%oname
%_K5xmlgui/%{oname}part
%_K5plug/*.so
%_K5srv/*

%files devel
%_libdir/cmake/*
%_includedir/*
%_K5link/lib*.so


%doc LICENSE README.md TODO.md

%changelog
* Fri Aug 22 2025 Ilya Muhamadeev <nicourced@altlinux.org> 0.10.0-alt1
- New version.
- Upstream link fix.

* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 0.9-alt1.1
- require libkbibtexpart9 again
- obsoletes libkbibtexpart4 (needed for upgrade)
- fix descriptions

* Tue Sep 17 2019 Anton Midyukov <antohami@altlinux.org> 0.9-alt1
- build last stable release for Qt5 and KDE5 (Closes: 36079)

* Wed Jun 26 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.1-alt1
- build last stable release for Qt4 and KDE4

* Mon Jun 24 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3.91-alt1
- update to last stable release for Qt3 and KDE3

* Sun Jun 23 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3-alt2
- build with Trinity libraries

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.2.3-alt1
- new version

* Wed Mar 11 2009 Led <led@altlinux.ru> 0.2.1.91-alt1
- 0.2.2.91 (0.2.2 Beta 2)

* Sun Feb 01 2009 Led <led@altlinux.ru> 0.2.1.90-alt1
- 0.2.2.90 (0.2.2 Beta 1)

* Sun Dec 28 2008 Led <led@altlinux.ru> 0.2.1.81-alt1
- 0.2.1.81
- cleaned up spec

* Sun Oct 26 2008 Led <led@altlinux.ru> 0.2.1.80-alt2
- fixed build with g++ 4.3

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.2.1.80-alt1
- 0.2.1.80
- updated kbibtex-0.2.1.80-alt-makefile.patch
- added kbibtex-0.2.1.80-alt-format.patch

* Thu Jun 26 2008 Led <led@altlinux.ru> 0.2.1-alt1
- initial build

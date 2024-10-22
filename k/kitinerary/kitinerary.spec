%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%_K6if_ver_gteq %ubt_id M110
%def_disable phonenumber
%else
%def_disable phonenumber
%endif

%define rname kitinerary

%define sover 6
%define libkpimitinerary libkpim6itinerary%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Itinerary data model
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-zonetab.patch
Patch2: alt-old-poppler.patch

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libpoppler-devel libxml2-devel xsltproc zlib-devel
BuildRequires: libzxing-cpp-devel
%if_enabled phonenumber
BuildRequires: libphonenumber-devel
%endif
BuildRequires: kf6-kcontacts-devel kmime-devel kpkpass-devel
BuildRequires: kf6-karchive-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kcalendarcore-devel

%description
A library containing itinerary data model and itinerary extraction code.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpimitinerary
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpimitinerary
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DBUILD_TESTING:BOOl=ON \
    #

%install
%K6install
%find_lang %name --all-name
for f in %buildroot/%_K6xdgmime/*itinerary*.xml ; do
    DST=`basename "$f" | sed 's|.xml$|6.xml|'`
    mv $f %buildroot/%_K6xdgmime/"$DST"
done

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
%_K6xdgmime/*itinerary*.xml

%files devel
%_K6inc/KPim6/kitinerary_version.h
%_K6inc/KPim6/??tinerary/
%_K6link/lib*.so
%_K6lib/cmake/KPim*Itinerary/

%files -n %libkpimitinerary
%_K6exec/kitinerary*
%_K6lib/libKPim6Itinerary.so.%sover
%_K6lib/libKPim6Itinerary.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build


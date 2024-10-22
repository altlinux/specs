%define optflags_lto %nil

%define rname okular
%def_disable progress
%def_disable msits
%def_enable mobile

%define sover 2
%define libokularcore libokular6core%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init no_altplace

Group: Office
Summary: Document Viewer
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-core
Provides: kde5-okular = %EVR
Obsoletes: kde5-okular < %EVR

Source: %rname-%version.tar
Source10: alt-loading-ru.po
Patch1: alt-chm-encoding.patch
Patch2: alt-def-memory-level.patch
Patch3: alt-print-truncate-title.patch
Patch4: alt-add-indication-for-document-loading-process.patch
Patch5: alt-cryptopro-verifying.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-phonon-devel qt6-svg-devel
BuildRequires: qt6-speech-devel
BuildRequires: zlib-devel libdiscount-devel
BuildRequires: ebook-tools-devel libdjvu-devel libjpeg-devel libpoppler-qt6-devel libqca-qt6-devel libspectre-devel libtiff-devel
BuildRequires: libzip-devel
%if_enabled msits
BuildRequires: libchm-devel
%endif
BuildRequires: kf6-purpose-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kpty-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-threadweaver-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma6-libkscreen-devel plasma6-activities-devel
BuildRequires: kde6-libkexiv2-devel

%description
Document viewer; support different kinds of documents.

%package mobile
Summary: Mobile Document Viewer
Group: Office
Requires: %name-common >= %EVR
Requires: kf6-kdeclarative kf6-kirigami
Provides: kde5-okular-mobile = %EVR
Obsoletes: kde5-okular-mobile < %EVR
%description mobile
Document viewer; support different kinds of documents.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common >= %EVR
Provides: kde5-okular-common = %EVR
Obsoletes: kde5-okular-common < %EVR
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common >= %EVR
Requires: kde-runtime
Provides: kde5-okular-core = %EVR
Obsoletes: kde5-okular-core < %EVR
%description core
Core files for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libokularcore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libokular5core11 < %EVR
%description -n %libokularcore
%name library


%prep
%setup -n %rname-%version
%if_enabled msits
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%if_enabled progress
%patch4 -p2
%endif
#%patch5 -p2 -b .csp
sed -i '/^add_subdirectory.*ooo/d' generators/CMakeLists.txt
sed -i '/^find_package.*QMobipocket/d' CMakeLists.txt

tmp_file=`mktemp`
msgcat --use-first po/ru/okular.po %SOURCE10 >"$tmp_file"
cat "$tmp_file" >po/ru/okular.po
rm -f "$tmp_file"

%build
%K6build \
%if_enabled mobile
    -DOKULAR_UI=both \
%else
    -DOKULAR_UI=desktop \
%endif
    -DLIBZIP_INCLUDE_DIR=%_includedir/libzip \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -Ddiscount_INCLUDE_DIR=%_includedir \
    -Ddiscount_LIBRARIES=%_libdir/libmarkdown.so \
    -Ddiscount_FOUND:BOOL=TRUE \
    #

%install
%K6install

if [ -n "`ls -1d %buildroot/%_datadir/qlogging-categories6/*.*categories`" ] ; then
    mkdir -p %buildroot/%_K6xdgconf/
    mv %buildroot/%_datadir/qlogging-categories6/*.*categories %buildroot/%_K6xdgconf/
fi

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/hicolor/*/apps/okular.*
%config(noreplace) %_K6xdgconf/*.*categories

%files
%_K6bin/okular
%_K6xdgapp/org.kde.okular.desktop
%_K6xdgapp/okularApplication_*.desktop
%_datadir/metainfo/org.kde.okular.appdata.xml

%if_enabled mobile
%files mobile
%_K6bin/okularkirigami
%_K6xdgapp/org.kde.okular.kirigami.desktop
%_K6xdgapp/org.kde.mobile.okular_*.desktop
%_datadir/metainfo/org.kde.okular.kirigami.appdata.xml
%else
%exclude %_datadir/kpackage/genericqml/org.kde.mobile.okular/
%exclude %_K6data/kpackage/genericqml/org.kde.mobile.okular/
%exclude %_K6xdgapp/org.kde.mobile.okular.desktop
%exclude %_K6xdgapp/org.kde.mobile.okular_*.desktop
%endif

%files core
%_datadir/okular/
%_K6qml/org/kde/okular/
%_K6plug/okular_generators/
%_K6plug/kf6/parts/okularpart.so
%_datadir/kconf_update/okular*
%_K6cfg/*okular*
%_K6cfg/*settings*
%if_enabled msits
%_K6plug/kf6/kio/kio_msits.so
%endif
%_datadir/metainfo/org.kde.okular-*.metainfo.xml

%files devel
%_K6inc/okular/
%_K6link/lib*.so
%_K6lib/cmake/Okular?/

%files -n %libokularcore
%_K6lib/libOkular6Core.so.%sover
%_K6lib/libOkular6Core.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build


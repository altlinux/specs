%define rname libksieve

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define sover 6
%define libkpim6kmanagesieve libpim6kmanagesieve%sover
%define libkpim6ksieveui libpim6ksieveui%sover
%define libkpim6ksieve libpim6ksieve%sover
%define libkpim6ksievecore libpim6ksievecore%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-tools-devel qt6-declarative-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: boost-devel libsasl2-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel kidentitymanagement-devel kimap-devel kmailtransport-devel kmime-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel   kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-syntax-highlighting-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: kpimtextedit-devel kde6-libkdepim-devel pimcommon-devel
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel

%description
%summary.

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

%package -n %libkpim6kmanagesieve
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6kmanagesieve
%name library

%package -n %libkpim6ksieveui
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libkf5ksieveui5 < %EVR
%description -n %libkpim6ksieveui
%name library

%package -n %libkpim6ksieve
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6ksieve
%name library

%package -n %libkpim6ksievecore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpim6ksievecore
%name library

%prep
%setup -n %rname-%version

%if_disabled qtwebengine
sed -i 's|WebEngineWidgets||' CMakeLists.txt
sed -i 's|WebEngine||' CMakeLists.txt
for subd in \
    src/ksieveui \
    #
do
    rs=`basename ${subd}`
    dir=`dirname ${subd}`
    sed -i "/add_subdirectory(${rs})/d" ./${dir}/CMakeLists.txt
    rm -rf ./$subd
done
%endif

%build
%K6build \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data sieve knsrcfiles
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/KSieve/
%_includedir/KPim6/K*Sieve*/
%_K6link/lib*.so
%_libdir/cmake/KPim*Sieve*/

%if_enabled qtwebengine
%files -n %libkpim6ksieveui
%_K6lib/libKPim6KSieveUi.so.%sover
%_K6lib/libKPim6KSieveUi.so.*
%_K6data/sieve/
%_K6data/knsrcfiles/*sieve*
%endif

%files -n %libkpim6kmanagesieve
%_K6lib/libKPim6KManageSieve.so.%sover
%_K6lib/libKPim6KManageSieve.so.*
%files -n %libkpim6ksieve
%_K6lib/libKPim6KSieve.so.%sover
%_K6lib/libKPim6KSieve.so.*
%files -n %libkpim6ksievecore
%_K6lib/libKPim6KSieveCore.so.%sover
%_K6lib/libKPim6KSieveCore.so.*



%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build


%define rname messagelib

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define sover 6
%define libkpim6messagecomposer libkpim6messagecomposer%sover
%define libkpim6messagecore libkpim6messagecore%sover
%define libkpim6messageviewer libkpim6messageviewer%sover
%define libkpim6messagelist libkpim6messagelist%sover
%define libkpim6messageparser libkpim6messageparser%sover
%define libkpim6mimetreeparser libkpim6mimetreeparser%sover
%define libkpim6webengineviewer libkpim6webengineviewer%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE6 %rname library
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar
Patch1: alt-gpgme17.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-tools-devel qt6-declarative-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libqca-qt6-devel
BuildRequires: libgpgme-devel libassuan-devel libldap-devel libsasl2-devel
BuildRequires: boost-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel 
BuildRequires: kf6-kdoctools-devel kf6-kguiaddons-devel kf6-kcalendarcore-devel kf6-kcontacts-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-syntax-highlighting-devel kf6-knewstuff-devel kf6-ktexttemplate-devel
BuildRequires: kf6-ktextaddons-devel
BuildRequires: akonadi-search-devel grantleetheme-devel
BuildRequires: akonadi-devel akonadi-mime-devel akonadi-contacts-devel akonadi-notes-devel
BuildRequires: kidentitymanagement-devel kimap-devel kldap-devel kmailtransport-devel kmbox-devel
BuildRequires: kmime-devel kpimtextedit-devel kde6-libgravatar-devel kde6-libkdepim-devel kde6-libkleo-devel
BuildRequires: pimcommon-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%if_enabled qtwebengine
Requires: qt6-webengine-devel
%endif
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpim6messagecomposer
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpim6messagecomposer
%name library

%package -n %libkpim6messagecore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpim6messagecore
%name library

%package -n %libkpim6messageviewer
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5messageviewer5 < %EVR
%description -n %libkpim6messageviewer
%name library

%package -n %libkpim6messagelist
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpim6messagelist
%name library

%package -n %libkpim6messageparser
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkf5messageparser5 < %EVR
%description -n %libkpim6messageparser
%name library

%package -n %libkpim6mimetreeparser
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpim6mimetreeparser
%name library

%package -n %libkpim6webengineviewer
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkpim6webengineviewer
%name library

%prep
%setup -n %rname-%version
#%patch1 -p1

%if_disabled qtwebengine
sed -i 's|WebEngineWidgets||' CMakeLists.txt
sed -i 's|WebEngine||' CMakeLists.txt
for subd in \
    messageviewer \
    webengineviewer \
    templateparser \
    messagecomposer \
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
    -DQGpgme_DIR=%_libdir/cmake/Gpgmepp/ \
    #

%install
%K6install
%K6install_move data libmessageviewer messagelist messageviewer kconf_update
%K6install_move data org.kde.syntax-highlighting knsrcfiles
%find_lang %name --with-kde --all-name

mkdir -p %buildroot/%_K6plug/pim6

%files common -f %name.lang
%doc LICENSES/*
%dir %_K6plug/pim6/
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/KPim6/*
%_K6link/lib*.so
%_K6lib/cmake/*/

%if_enabled qtwebengine
%files -n %libkpim6messagecomposer
%_K6lib/libKPim6MessageComposer.so.%sover
%_K6lib/libKPim6MessageComposer.so.*
%files -n %libkpim6webengineviewer
%_K6lib/libKPim6WebEngineViewer.so.%sover
%_K6lib/libKPim6WebEngineViewer.so.*
%files -n %libkpim6messageviewer
%_K6lib/libKPim6MessageViewer.so.%sover
%_K6lib/libKPim6MessageViewer.so.*
%dir %_K6plug/pim6/messageviewer/
%dir %_K6plug/pim6/messageviewer/headerstyle/
%dir %_K6plug/pim6/messageviewer/kf6/
%dir %_K6plug/pim6/messageviewer/kf6/ktexttemplate/
%_K6plug/pim6/messageviewer/headerstyle/*.so
%_K6plug/pim6/messageviewer/kf6/ktexttemplate/*.so
%_K6data/knsrcfiles/
%_K6data/libmessageviewer/
%_K6data/messageviewer/
%_K6data/messagelist/
%_K6notif/*.notifyrc
%files -n %libkpim6messageparser
%_K6lib/libKPim6TemplateParser.so.%sover
%_K6lib/libKPim6TemplateParser.so.*
%_K6data/org.kde.syntax-highlighting/
%_K6cfg/*template*.kcfg
%endif
%files -n %libkpim6messagecore
%_K6lib/libKPim6MessageCore.so.%sover
%_K6lib/libKPim6MessageCore.so.*
%files -n %libkpim6messagelist
%_K6lib/libKPim6MessageList.so.%sover
%_K6lib/libKPim6MessageList.so.*
%files -n %libkpim6mimetreeparser
%_K6lib/libKPim6MimeTreeParser.so.%sover
%_K6lib/libKPim6MimeTreeParser.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build


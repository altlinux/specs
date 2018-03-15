# obsileted koffice version
%define koffice_ver 4:2.3.70

Name: calligra-plan
Version: 3.1.0
Release: alt1%ubt
Epoch: 0
%K5init
%define libname lib%name

Group: Office
Summary: A project planner
License: GPLv2+ / LGPLv2+
Provides: koffice-kplato = %koffice_ver
Obsoletes: koffice-kplato < %koffice_ver
Requires: %name-common = %version-%release
Requires: calligra-core
Requires: kf5-kreport

Source: http://download.kde.org/stable/calligra/%version/calligraplan-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: kf5-karchive-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kcmutils-devel
BuildRequires: kf5-kio-devel kf5-knotifications-devel kf5-kparts-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-kactivities-devel kf5-khtml-devel kde5-kholidays-devel kf5-kdiagram-devel
BuildRequires: kf5-kjs-devel kf5-kitemmodels-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel kde5-akonadi-devel kde5-akonadi-contacts-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: zlib-devel

%description
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Conflicts: libflake-devel
%description devel
Header files and libraries needed for %name development

%package -n %libname
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libname
%name libraries

%prep
%setup -n calligraplan-%version

%build
%K5build \
    -DPACKAGERS_BUILD=OFF \
    -DBUILD_TESTING=OFF \
    -DTEMPLATES_INSTALL_DIR:PATH=%_K5tmpl \
    #

%install
%K5install

## unpackaged files
rm -frv %buildroot/%_datadir/locale/x-test/

%find_lang --with-kde --all-name %name

%files common -f %name.lang
%_K5icon/*/*/*/*

%files devel
%_K5link/lib*.so

%files
%dir %_K5plug/calligraplan/
%dir %_K5plug/calligraplan/parts/
%dir %_K5plug/calligraplan/formatfilters/
%dir %_K5plug/calligraplan/schedulers/
%config(noreplace) %_K5xdgconf/calligraplan*rc
%_K5bin/calligraplan
%_K5bin/calligraplanwork
%_K5lib/libkdeinit5_calligraplan.so
%_K5lib/libkdeinit5_calligraplanwork.so
%_K5plug/calligraplan/parts/calligraplanpart.so
%_K5plug/calligraplan/formatfilters/planicalexport.so
%_K5plug/calligraplan/formatfilters/plankplatoimport.so
%_K5plug/calligraplan/schedulers/libplantjscheduler.so
%_K5plug/calligraplanworkpart.so
%_datadir/calligraplan/
%_datadir/calligraplanwork/
%_K5xmlgui/calligraplan/
%_K5xmlgui/calligraplanwork/
%_K5cfg/calligraplansettings.kcfg
%_K5cfg/calligraplanworksettings.kcfg
%_K5xdgapp/org.kde.calligraplan.desktop
%_K5xdgapp/org.kde.calligraplanwork.desktop

%files -n %libname
%_K5lib/lib*.so.*

%changelog
* Tue Mar 13 2018 Oleg Solovyov <mcpain@altlinux.org> 0:3.1.0-alt1%ubt
- initial build for ALT

%define rname plasma-settings

Name: %rname
Version: 25.11.0
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Settings application for Plasma Mobile
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami
Requires: %name-core
Provides: kde5-plasma-settings = %EVR
Obsoletes: kde5-plasma-settings < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-kpackage-devel kf6-kcmutils-devel kf6-kitemmodels-devel
#kf6-plasma-framework-devel
BuildRequires: pkgconfig(gobject-2.0) pkgconfig(gio-2.0)

%description
Settings application for Plasma Mobile.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common
Provides: kde5-plasma-settings-core = %EVR
Obsoletes: kde5-plasma-settings-core < %EVR
%description core
Core files needed for %rname

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kpackage
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6xdgapp/*plasmasettings*.desktop
%_K6data/plasma-settings/
%_iconsdir/hicolor/*/apps/*plasmasettings*.*
%_datadir/metainfo/*plasmasettings*.xml

%files core
%_K6bin/plasma-settings


%changelog
* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 25.11.0-alt1
- initial build

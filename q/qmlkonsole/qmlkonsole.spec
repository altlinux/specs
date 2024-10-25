%define rname qmlkonsole

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Mobile terminal application
Url: http://www.kde.org
License: GPL-2.0-or-later

#Requires: qt6-qmltermwidget
Requires: kf6-kirigami-addons
Provides:  kde5-qmlkonsole = %EVR
Obsoletes: kde5-qmlkonsole < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-5compat-devel qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-kconfig-devel kf6-ki18n-devel kf6-kirigami-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kpty-devel

%description
Terminal application offering additional keyboard buttons useful on touch devices.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/qmlkonsole
%_K6xdgapp/*qmlkonsole*.desktop
%_K6cfg/*terminalsettings*
%_K6icon/*/*/apps/*qmlkonsole*
%_datadir/metainfo/*.xml

%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


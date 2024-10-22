%define rname kamera

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Digital cameras support for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kamera = %EVR
Obsoletes: kde5-kamera < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libgphoto2-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-kcmutils-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data solid
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6xdgapp/*amera*.desktop
%_K6plug/plasma/kcms/systemsettings_qwidgets/*amera*.so
%_K6plug/kf6/kio/*amera*.so
%_K6data/solid/actions/*amera*.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build


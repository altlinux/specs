%define rname systemsettings

%define systemsettingsview_sover 3
%define libsystemsettingsview libsystemsettingsview%systemsettingsview_sover

Name: %rname
Version: 6.1.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 settings
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt6-declarative kf6-kirigami
Provides: plasma5-systemsettings = %EVR
Obsoletes: plasma5-systemsettings < %EVR
Provides: plasma5-systemsettings-common = %EVR
Obsoletes: plasma5-systemsettings-common < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: plasma-workspace-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-krunner-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kirigami-devel
BuildRequires: kf6-kdeclarative-devel kf6-kpackage-devel kf6-kcrash-devel kf6-kitemmodels-devel
BuildRequires: plasma6-activities-devel plasma6-activities-stats-devel
%description
KDE System Settings


%prep
%setup -n %rname-%version

sed -i '/EnabledByDefault/s|true|false|' runner/systemsettingsrunner.json

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data systemsettings kpackage kglobalaccel locale

ln -s systemsettings %buildroot/%_K6bin/systemsettings5

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/*
%_K6plug/kf6/krunner/*.so
%_K6data/systemsettings/
%_K6data/kglobalaccel/*systemsettings*
%_K6xdgapp/*systemsettings*.desktop
%_datadir/zsh/site-functions/_*
%_datadir/metainfo/*.xml


%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


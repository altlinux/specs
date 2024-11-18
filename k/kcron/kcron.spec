%define rname kcron

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Task Scheduler
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kcron = %EVR
Obsoletes: kde5-kcron < %EVR

#Requires: /usr/sbin/crond

Source: %rname-%version.tar
Patch1: alt-reset-button.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-kcmutils-devel

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/plasma/kcms/systemsettings_qwidgets/*cron*.so
%_K6xdgapp/*cron*.desktop
%_datadir/qlogging-categories6/*.*categories
#
%_K6exec/kauth/*kcron*
%_K6dbus_sys_srv/*kcron*.service
%_K6dbus/system.d/*kcron*.conf
%_datadir/polkit-1/actions/*kcron*.policy
%_datadir/metainfo/*.xml


%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


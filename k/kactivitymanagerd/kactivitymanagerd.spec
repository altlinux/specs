%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname kactivitymanagerd

Name: %rname
Version: 6.1.4
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: Core component for the KDE Activity concept
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-kactivitymanagerd = 1:%version-%release
Obsoletes: plasma5-kactivitymanagerd < 1:%version-%release

Source: %rname-%version.tar
Patch1: alt-def-activity-name.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel boost-devel extra-cmake-modules
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-kcrash-devel

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    #

%install
%K6install
%K6install_move data krunner

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6libexecdir/kactivitymanagerd
%_K6lib/libkactivitymanagerd_*.so
%_K6plug/kactivitymanagerd*/
%_K6dbus_srv/*ctivity?anager*.service
%_userunitdir/*.service
%_K6data/krunner/dbusplugins/plasma-runnners-activities.desktop



%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


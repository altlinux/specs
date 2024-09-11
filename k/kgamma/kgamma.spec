%define rname kgamma

Name: kgamma
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Color profiling
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-kgamma = %EVR
Obsoletes: plasma5-kgamma < %EVR

Source: %rname-%version.tar
Patch1: alt-config-path.patch.patch
Patch2: alt-xf86gammacfg-args-clear.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: libXxf86vm-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kcmutils-devel

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%K6install_move data kgamma
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/plasma/kcminit/*kgamma*.so
%_K6plug/plasma/kcms/*systemsettings*/*kgamma*.so
%_K6data/kgamma/
%_K6xdgapp/*kgamma*.desktop


%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


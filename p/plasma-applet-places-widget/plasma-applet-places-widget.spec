%define rname plasma-applet-places-widget

Name: %rname
Version: 1.4
Release: alt10
%K6init

Group: Graphical desktop/KDE
Summary:  User places widget
Url: https://github.com/dfaust/plasma-applet-places-widget
License: GPL-2.0
BuildArch: noarch

Requires: kf6-filesystem
Provides: kde5-plasma-applet-places-widget = %EVR
Obsoletes: kde5-plasma-applet-places-widget < %EVR

Source: %rname-%version.tar
Source1: ru.po
Patch1: alt-metadata.patch
Patch2: alt-auto-width.patch
Patch3: alt-defaults.patch

BuildRequires(pre): rpm-build-kf6 qt6-declarative-devel
BuildRequires: extra-cmake-modules kf6-ki18n-devel kf6-kpackage-devel kf6-kservice-devel kf6-kwindowsystem-devel
BuildRequires: plasma6-lib-devel

%description
Plasma widget that gives access to user places.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

mkdir -p po/ru
install -m 0644 %SOURCE1 po/ru/plasma_applet_org.kde.placesWidget.po

cat >>CMakeLists.txt <<__EOF__
find_package(KF6I18n CONFIG REQUIRED)
ki18n_install(po)
__EOF__


%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%_K6data/plasma/plasmoids/org.kde.placesWidget/
%_datadir/metainfo/*placesWidget*.xml

%changelog
* Wed Jul 17 2024 Sergey V Turchin <zerg@altlinux.org> 1.4-alt10
- initial build for KDE 6

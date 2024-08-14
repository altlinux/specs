%define rname flatpak-kcm

Name: %rname
Version: 6.1.2
Release: alt1
%K6init

Group: System/Configuration/Packaging
Summary: KDE Flatpak Permissions Management
Url: http://www.kde.org
License: BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later

#Requires: flatpak
Provides: plasma5-flatpak-kcm = %EVR
Obsoletes: plasma5-flatpak-kcm < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-svg-devel qt6-declarative-devel
BuildRequires: libflatpak-devel
BuildRequires: kf6-kitemmodels-devel kf6-kcmutils-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kpackage-devel

%description
The KCM allows changing what permissions have been granted to installed Flatpak applications.

%prep
%setup -n %rname-%version

%build
%K6build \
    #

%install
%K6install
%K6install_move data kpackage
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/plasma/kcms/systemsettings/*flatpak*.so
%_K6xdgapp/*flatpak*.desktop

%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


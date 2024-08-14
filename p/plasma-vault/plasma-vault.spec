%define rname plasma-vault

Name: plasma-vault
Version: 6.1.2
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: Encrypted vaults support for KDE Plasma
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: /usr/bin/fusermount
#Requires: fuse-encfs >= 1.9.1
#Requires: fuse-cryfs >= 0.9.6

Provides: plasma5-vault = 1:%version-%release
Obsoletes: plasma5-vault < 1:%version-%release

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kpackage-devel kf6-kitemmodels-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-networkmanager-qt-devel
BuildRequires: plasma6-lib-devel plasma6-activities-devel plasma6-libksysguard-devel

%description
%name provides encrypted vaults.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/kf6/kfileitemaction/*.so
%_K6plug/kf6/kded/*vault*.so
%_K6plug/plasma/applets/*vault*.so
%_K6data/plasma/plasmoids/*vault*/
%_datadir/metainfo/*.xml

%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


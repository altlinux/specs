%define rname alligator

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: RSS/Atom feed reader
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami-addons
Provides:  kde5-alligator = %EVR
Obsoletes: kde5-alligator < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-syndication-devel
BuildRequires: kf6-kirigami-addons-devel

%description
Alligator is a convergent RSS/Atom feed reader.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/alligator
%_K6xdgapp/*alligator*.desktop
%_K6icon/hicolor/*/apps/alligator.*
%_datadir/metainfo/*.xml

%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


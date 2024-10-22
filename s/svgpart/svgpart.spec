%define rname svgpart

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: SVG Part
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-svgpart = %EVR
Obsoletes: kde5-svgpart < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-kio-devel kf6-kparts-devel kf6-ktextwidgets-devel

%description
KDE SVG Part.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/kf6/parts/svgpart.so
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build


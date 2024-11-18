%define rname kmag

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: %rname is a small utility to magnify a part of the screen
License: GPL-2.0-or-later
Url: https://www.kde.org/applications/utilities/kmag

Provides:  kde5-kmag = %EVR
Obsoletes: kde5-kmag < %EVR

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel kf6-kauth-devel
BuildRequires: libqaccessibilityclient-qt6-devel

%description
%summary. %rname is very useful for people with visual disabilities and for
those working in the fields of image analysis, web development etc.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data %rname
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/%rname
%_K6xdgapp/org.kde.%{rname}.desktop
%_K6icon/hicolor/*/*/%{rname}*.*
%_K6data/%rname/
%_datadir/metainfo/*kmag*.xml

%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


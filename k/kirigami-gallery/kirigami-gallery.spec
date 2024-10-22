%define rname kirigami-gallery

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Widget Browser for Kirigami
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-kirigami-gallery = %EVR
Obsoletes: kde5-kirigami-gallery < %EVR

#Requires: qml6(org.kde.kitemmodels)
Requires: libkf6itemmodels

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kirigami-devel


%description
Application which uses all features from kirigami,
including links to the sourcecode, tips on how to use
the components and links to the corresponding
HIG pages and code examples on invent.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files -f %name.lang
%doc LICENSE*
%_K6bin/*
%_K6xdgapp/*.desktop
#%_datadir/metainfo/*gallery*.xml

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build


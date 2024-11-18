%define rname kmousetool

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: %rname is a program that clicks the mouse for you
Url: https://www.kde.org/applications/utilities/kmousetool 
License: GPL-2.0-or-later

Provides:  kde5-kmousetool = %EVR
Obsoletes: kde5-kmousetool < %EVR

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules libXtst-devel libXext-devel libXt-devel
BuildRequires: qt6-declarative-devel qt6-multimedia-devel
BuildRequires: qt6-phonon-devel
BuildRequires: kf6-kxmlgui-devel kf6-knotifications-devel kf6-kdbusaddons-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kauth-devel kf6-kwindowsystem-devel

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kmousetool
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kmousetool
%_K6xdgapp/org.kde.kmousetool.desktop
%_K6icon/hicolor/*/*/kmousetool*.*
%_K6data/kmousetool/
%_datadir/metainfo/*kmousetool*.xml

%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


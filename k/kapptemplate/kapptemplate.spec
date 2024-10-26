%define rname kapptemplate

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE applications templates
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kapptemplate = %EVR
Obsoletes: kde5-kapptemplate < %EVR

Source: %rname-%version.tar
Patch1: alt-wordwrap.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel

%description
KAppTemplate provide a skeleton and example of what the code typically looks like.


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kdevappwizard
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kapptemplate
%_K6data/kdevappwizard/
%_K6cfg/kapptemplate*
%_K6icon/*/*/apps/kapptemplate.*
%_K6xdgapp/*kapptemplate.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


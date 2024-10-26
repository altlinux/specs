%define rname kdesdk-thumbnailers

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE SDK Thumbnailers
Url: http://www.kde.org
License: GPL-2.0-only or GPL-3.0-only or LicenseRef-KDE-Accepted-GPL

Provides:  kde5-sdk-thumbnailers = %EVR
Obsoletes: kde5-sdk-thumbnailers < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel


%description
%summary.


%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6plug/kf?/thumbcreator/*othumb*.so
%_K6cfg/*.kcfg


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


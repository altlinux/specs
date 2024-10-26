%define rname keysmith

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Two-factor authenticator
Url: http://www.kde.org
License: GPL-3.0-or-later

Provides:  kde5-keysmith = %EVR
Obsoletes: kde5-keysmith < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libsodium-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-kwindowsystem-devel
BuildRequires: kf6-qqc2-desktop-style-devel

%description
Keysmith is an application to generate two-factor authentication (2FA)
tokens when logging in to your (online) accounts.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKF_IGNORE_PLATFORM_CHECK=ON \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/keysmith
%_K6xdgapp/org.kde.keysmith.desktop
%_K6icon/*/*/*/keysmith.*
%_datadir/metainfo/*.xml


%changelog
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


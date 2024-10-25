%define rname kalk

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Convergent calculator
Url: http://www.kde.org
License: GPL-3.0-or-later

#Requires: qt6-feedback
Provides:  kde5-kalk = %EVR
Obsoletes: kde5-kalk < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
#BuildRequires: qt6-feedback-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: flex bison
BuildRequires: libvulkan-devel
BuildRequires: libqalculate-devel
BuildRequires: libmpfr-devel libgmp-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-kunitconversion-devel

%description
Kalk is a convergent calculator application.
Although it is mainly targeted for mobile platforms.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kalk
%_K6xdgapp/*kalk*desktop
%_K6icon/*/*/apps/*kalk*
%_datadir/metainfo/*.xml

%changelog
* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build


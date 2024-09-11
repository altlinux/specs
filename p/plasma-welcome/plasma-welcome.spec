%define rname plasma-welcome

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: First start wizard for Plasma
Url: http://www.kde.org
License: GPL-2.0-or-later

# PowerfulWhenNeeded
Requires: kf6-knewstuff

Provides: plasma5-welcome = %EVR
Obsoletes: plasma5-welcome < %EVR

Source: %rname-%version.tar
Patch2: alt-check-auth.patch
Patch3: alt-add-pre-distro-pages.patch
Patch4: alt-discover-apps.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kdeclarative-devel kf6-ki18n-devel kf6-kirigami-devel
BuildRequires: kf6-knewstuff-devel kf6-knotifications-devel kf6-kpackage-devel kf6-kcmutils-devel kf6-ksvg-devel
BuildRequires: plasma6-lib-devel
BuildRequires: accounts-qt6-devel
# kaccounts-integration-devel signon-devel

%description
A Friendly onboarding wizard for Plasma.

%prep
%setup -n %rname-%version
%patch2 -p1
#%patch3 -p1
%patch4 -p1

%build
%K6build

%install
%K6install
mkdir -p %buildroot/%_datadir/plasma-welcome-extra-pages{,-pre}
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%dir %_datadir/plasma-welcome-extra-pages/
%dir %_datadir/plasma-welcome-extra-pages-pre/
%_K6bin/plasma-welcome
%_K6plug/kf6/kded/*welcome*.so
%_K6xdgapp/*plasma-welcome*.desktop
%_datadir/metainfo/*.xml

%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build


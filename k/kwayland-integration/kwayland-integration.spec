%define rname kwayland-integration

Name: %rname
Version: 6.1.5
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Wayland integration plugins
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-kwayland-integration = %EVR
Obsoletes: plasma5-kwayland-integration < %EVR
Requires: xorg-xwayland qt5-wayland

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-base-devel-static qt5-wayland-devel
BuildRequires: libvulkan-devel
BuildRequires: pkgconfig(wayland-protocols) plasma-wayland-protocols
BuildRequires: kf5-kidletime-devel kf5-kwindowsystem-devel kf5-kguiaddons-devel
BuildRequires: kf5-kwayland-devel


%description
Provides integration plugins for various KDE frameworks for the wayland windowing system.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%find_lang %name --with-kde --all-name

%files  -f %name.lang
%doc LICENSES/*
%_K5plug/kf5/*/*Wayland*.so
%_datadir/qlogging-categories5/*.*categories


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


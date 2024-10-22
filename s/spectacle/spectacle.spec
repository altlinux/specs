%define rname spectacle
%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif
%define service_name app-org.kde.spectacle

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: The KDE Screenshot Utility
Url: http://www.kde.org
License: LGPL-2.0-or-later AND GPL-2.0-or-later

Provides: kde5-spectacle = %EVR
Obsoletes: kde5-spectacle < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-multimedia-devel
BuildRequires: qt6-wayland-devel plasma-wayland-protocols
BuildRequires: pipewire-libs-devel plasma6-kpipewire-devel
BuildRequires: libopencv-devel
BuildRequires: libxcbutil-cursor-devel libxcbutil-devel libxcbutil-image-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-knewstuff-devel kf6-kglobalaccel-devel
BuildRequires: kf6-purpose-devel kf6-kirigami-devel kf6-kstatusnotifieritem-devel kf6-prison-devel
BuildRequires: plasma6-libkscreen-devel plasma6-kwayland-devel plasma6-layer-shell-qt-devel
BuildRequires: kde6-kcolorpicker-devel kde6-kimageannotator-devel

%description
Spectacle is screenshot taking utility for the KDE desktop. Spectacle
can also be used in non-KDE X11 desktop environments.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data kglobalaccel kconf_update locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/spectacle
%_K6conf_bin/*spectacle*
%_K6conf_up/*spectacle*
%_K6xdgapp/org.kde.spectacle.desktop
%_K6icon/hicolor/*/apps/spectacle.*
%_K6notif/spectacle.notifyrc
%_K6data/kglobalaccel/*spectacle*.desktop
%_K6dbus_srv/org.kde.Spectacle.service
%_K6conf_up/*.upd
%_datadir/qlogging-categories6/*.*categories
%_K6dbus_srv/org.kde.spectacle.service
%_userunitdir/%service_name.service
%_datadir/metainfo/*.xml

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build


%define rname wacomtablet

Name: plasma-wacomtablet
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Config Module for Wacom Tablets
License: GPL-2.0-or-later
URL: https://invent.kde.org/plasma/wacomtablet
VCS: https://invent.kde.org/plasma/wacomtablet.git

Provides: kde5-kcm-wacomtablet = %EVR
Obsoletes: kde5-kcm-wacomtablet < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: libXi-devel libxcb-devel
BuildRequires: libwacom-devel xorg-drv-wacom-devel
BuildRequires: libgudev-devel libpcre2-devel libffi-devel libevdev-devel zlib-devel bzlib-devel
BuildRequires: libpng-devel libbrotli-devel libexpat-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kconfig-devel kf6-kxmlgui-devel kf6-knotifications-devel kf6-kdoctools-devel kf6-kpackage-devel
BuildRequires: kf6-kservice-devel kf6-kcolorscheme-devel kf6-kwindowsystem-devel kf6-kcmutils-devel kf6-kio-devel
BuildRequires: plasma6-lib-devel plasma6-plasma5support-devel

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button / pen layouts per profile.

For hardware support have a look at https://linuxwacom.github.io/

All tablets can be set up as long as they are found with the wacom kernel
module.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K6bin/kde_wacom_tabletfinder
%_K6plug/kf6/kded/wacomtablet.so
%_K6plug//plasma/kcms/systemsettings_qwidgets/*wacomtablet*.so
%_K6plug//plasma5support/dataengine/*wacomtablet*.so
%_K6xdgapp/*.desktop
%_K6data/dbus-1/interfaces/org.kde.Wacom.xml
%_K6data/plasma/plasmoids/*wacomtablet*
%_K6notif/wacomtablet.notifyrc
%_K6data/wacomtablet/
%_K6data/plasma5support/services/*wacomtablet*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%changelog
* Mon Sep 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- initial build

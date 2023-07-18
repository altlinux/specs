%define rname kcm-wacomtablet

Name: kde5-kcm-wacomtablet
Version: 3.2.0
Release: alt1
%K5init altplace

Summary: KDE Config Module for Wacom Tablets
License: GPL-2.0-or-later
Group: System/Libraries
URL: https://invent.kde.org/system/wacomtablet

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-plasma-framework-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kservice-devel
BuildRequires: libXi-devel
BuildRequires: libxcb-devel
BuildRequires: libwacom-devel
BuildRequires: xorg-drv-wacom-devel

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button / pen layouts per profile.

For hardware support have a look at http://www.linuxwacom.sourceforge.net

All tablets can be set up as long as they are found with the wacom kernel
module.

%prep
%setup -n %rname-%version
#Fix build with Qt 5.15
sed -i '24a #include <QPainterPath>' src/kcmodule/pressurecurvewidget.cpp

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/kde_wacom_tabletfinder
%_K5plug/kf5/kded/wacomtablet.so
%_K5plug/plasma/dataengine/plasma_engine_wacomtablet.so
%_K5plug/kcm_wacomtablet.so
%_K5xdgapp/*.desktop
%_K5xdgconf/wacomtablet.categories
%_K5data/dbus-1/interfaces/org.kde.Wacom.xml
%_K5data/plasma/plasmoids/*
%_K5data/plasma/services/wacomtablet.operations
%_K5notif/wacomtablet.notifyrc
%_K5srv/*.desktop
%_datadir/metainfo/*.xml
%_datadir/wacomtablet/*

%changelog
* Sun Jul 16 2023 Anton Kurachenko <srebrov@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.

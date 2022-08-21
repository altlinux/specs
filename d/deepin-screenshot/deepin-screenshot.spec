Name:           deepin-screenshot
Version:        5.0.0
Release:        alt1

Summary:        Deepin Screenshot Tool

License:        GPLv3
Group:          Graphics
Url:            https://github.com/linuxdeepin/deepin-screenshot

# Source-url:   https://github.com/martyr-deepin/deepin-screenshot/archive/refs/tags/%{version}.tar.gz
Source:         %name-%version.tar
Source1:        %name-appdata.xml

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt5-base-devel
BuildRequires:  qt5-x11extras-devel
BuildRequires:  dtk5-widget-devel
BuildRequires:  dtk5-common
BuildRequires:  libdtkwm-devel
BuildRequires:  libxcbutil-devel
BuildRequires:  libappstream-glib

Requires:       deepin-turbo
Requires:       icon-theme-hicolor

%description
Provide a quite easy-to-use screenshot tool. Features:
  * Global hotkey to triggle screenshot tool
  * Take screenshot of a selected area
  * Easy to add text and line drawings onto the screenshot

%prep
%setup -q -n %name-%version

# fix for Qt 5.15
sed -i '1i #include <QPainterPath>' src/widgets/shapeswidget.cpp

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -Dm644 %SOURCE1 %buildroot%_datadir/metainfo/%name.appdata.xml

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.appdata.xml

%files
%doc README.md
%_bindir/%name
%_datadir/metainfo/%name.appdata.xml
%_datadir/dbus-1/services/com.deepin.Screenshot.service
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Sun Aug 21 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 5.0.0-alt1
- init version (5.0.0) with rpmgs script ALT #32414

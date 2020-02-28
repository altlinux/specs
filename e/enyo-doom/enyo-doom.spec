Name: enyo-doom
Version: 1.1.1
Release: alt1
Summary: Frontend for Doom engines
Summary(ru_RU.UTF-8): Оболочка для движков Doom
Group: Games/Arcade
License: GPLv2
Url: https://gitlab.com/sdcofer70/enyo-doom
Packager: Artyom Bystrov <arbars@altlinux.org>
Source: %name-%version.tar

BuildRequires: qt5-base-devel
BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: libqt5-core
BuildRequires: libqt5-gui
BuildRequires: libqt5-network
BuildRequires: libqt5-widgets
BuildRequires: ImageMagick-tools

%description
Enyo-Doom is a GUI launcher for Doom engines.
It is a relaunch of the gDoomsday project under a different name with more functionality.
The source release is usable in any modern GNU/Linux distribution with Qt).
The original release used GTK+, but was rewritten to use Qt for ease of maintenance
and cross-platform compatibility.

%description -l ru_RU.UTF-8
Enyo-Doom - графическая оболочка для движков Doom.
Данный проект - перезапуск другого проекта - gDoomsday под другим названием и с большим функционалом.
Данная программа может быть запущена в любой современной GNU/Linux-системе с Qt.
Оригинальный проект был написан на GTK+, но был переписан на Qt ради упрощения поддержки
и кросс-платформенности.

%prep
%setup -n %name-%version

%build
%cmake_insource
%make_build

%install
%makeinstall_std

# install menu icons
for N in 16 32 48 64 128;
do
convert share/enyo_icon.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Feb 28 2020 Artyom Bystrov <arbars@altlinux.org> 1.1.1-alt1
- initial build for ALT Sisyphus

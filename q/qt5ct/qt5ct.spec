Name: qt5ct
Version: 1.5
Release: alt1

Summary: Qt5 Configuration Tool
Summary(ru_RU.UTF-8): Инструмент для настройки оформления приложений Qt5
License: BSD
Group: System/Configuration/Other
Url: https://sourceforge.net/projects/qt5ct
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name/%name-%version.tar
# Source-url: https://sourceforge.net/projects/qt5ct/files/qt5ct-%version.tar.bz2/download

BuildRequires(pre): rpm-macros-qt5
BuildRequires: libinput-devel
BuildRequires: libmtdev-devel
BuildRequires: libts-devel
BuildRequires: libxkbcommon-devel
BuildRequires: python3-module-zope
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-connectivity-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-phonon-devel
BuildRequires: qt5-quick1-devel
BuildRequires: qt5-sensors-devel
BuildRequires: qt5-serialport-devel
BuildRequires: qt5-speech-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-wayland-devel
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-websockets-devel
BuildRequires: qt5-x11extras-devel

%description
This applications allows users to configure Qt5 settings (theme,
font, icons, etc.) under DE/WM without Qt integration.

%description -l ru_RU.UTF-8
Это приложение позволяет пользователям настраивать параметры Qt5 (тема,
шрифт, значки и т. д.) в DE / WM без интеграции с Qt.

%prep
%setup
echo "export QT_QPA_PLATFORMTHEME='%name'" > %name.sh
echo "setenv QT_QPA_PLATFORMTHEME '%name'" > %name.csh

%build
%qmake_qt5
%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

install -Dm 0755 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -Dm 0755 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

%files
%doc AUTHORS ChangeLog COPYING README
%config %_sysconfdir/profile.d/%name.*sh
%_bindir/%name
%_datadir/%name
%dir %_libdir/qt5/plugins/platformthemes/
%_libdir/qt5/plugins/platformthemes/lib%name.so
%_libdir/qt5/plugins/styles/libqt5ct-style.so
%_desktopdir/%name.desktop

%changelog
* Sun Dec 05 2021 Evgeny Chuck <koi@altlinux.org> 1.5-alt1
- new version (1.5) with rpmgs script
- Update spec for version 1.5
  + added package description in Russian
  + minor fixes in spec

* Wed Aug 19 2020 Ivan A. Melnikov <iv@altlinux.org> 1.1-alt1
- New version

* Fri Feb 01 2019 Ivan A. Melnikov <iv@altlinux.org> 0.37-alt1
- New version
- Make /etc/profile.d/qt5ct* executable (closes: #35769)

* Thu Oct 19 2017 Sergey V Turchin <zerg@altlinux.org> 0.30-alt1.1
- NMU: build with Qt 5.9

* Tue Jan 31 2017 Hihin Ruslan <ruslandh@altlinux.ru> 0.30-alt1
- New Version

* Sat Jun 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.24-alt1
- initial build for ALT Linux Sisyphus

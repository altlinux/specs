Name: qt5ct
Version: 0.24
Release: alt1
Summary: Qt5 Configuration Tool
License: BSD

Group: System/Configuration/Other
Url: https://sourceforge.net/projects/qt5ct
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name/%name-%version.tar

BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Sat Jun 04 2016
# optimized out: gcc-c++ libGL-devel libqt5-core libqt5-gui libqt5-widgets libqt5-xml libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-tools qt5-webchannel-devel
BuildRequires: python-module-junos-eznc python3-module-zope qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel
BuildRequires: qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel

%description
This applications allows users to configure Qt5 settings (theme,
font, icons, etc.) under DE/WM without Qt integration.

%prep
%setup
echo "export QT_QPA_PLATFORMTHEME='%name'" > %name.sh
echo "setenv QT_QPA_PLATFORMTHEME '%name'" > %name.csh

%build
%qmake_qt5
%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

install -Dm 0644 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -Dm 0644 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

%files
%doc AUTHORS ChangeLog COPYING README TODO
%config %_sysconfdir/profile.d/%name.*sh
%_bindir/%name
%dir %_libdir/qt5/plugins/platformthemes/
%_libdir/qt5/plugins/platformthemes/lib%name.so
%_desktopdir/%name.desktop

%changelog
* Sat Jun 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.24-alt1
- initial build for ALT Linux Sisyphus


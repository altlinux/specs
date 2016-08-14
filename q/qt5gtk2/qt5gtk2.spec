Name: qt5gtk2
Version: 0.1
Release: alt1
Summary: GTK+2.0 integration plugins for Qt5
License: GPLv2

Group: System/Configuration/Other
Url: https://bitbucket.org/trialuser02/qt5gtk2
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name/%name-%version.tar

BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Sun Aug 14 2016
# optimized out: fontconfig fontconfig-devel gcc-c++ glib2-devel libEGL-devel libGL-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libstdc++-devel libudev-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-xmlpatterns-devel xorg-xproto-devel
BuildRequires: libGConf-devel libgtk+2-devel libinput-devel libmtdev-devel libts-devel libxkbcommon-devel python3-module-zope qt5-base-devel-static qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel
BuildRequires: qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel

%description
Qt5Gtk2 - GTK+2.0 integration plugins for Qt5

%prep
%setup
echo "export QT_QPA_PLATFORMTHEME='%name'" > %name.sh
echo "setenv QT_QPA_PLATFORMTHEME '%name'" > %name.csh

%build
export PLUGINDIR=.
%qmake_qt5 
%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

install -Dm 0644 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -Dm 0644 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

%files
%doc AUTHORS ChangeLog README
%config %_sysconfdir/profile.d/%name.*sh
%_libdir/qt5/plugins/platformthemes/lib%name.so
%_libdir/qt5/plugins/styles/lib%name-style.so

%changelog
* Sun Aug 14 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus




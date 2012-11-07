%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%define rname lightdm-kde
Name: lightdm-kde-greeter
Version: 0.3.0
Release: alt1

Group: Graphical desktop/Other
Summary: LightDM KDE4 Greeter
Url: http://www.kde.org/
License: GPLv3+

Requires: lightdm
Provides: lightdm-greeter

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Jul 25 2012 (-bi)
# optimized out: alternatives automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glib2-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins liblightdm-gobject liblightdm-qt libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ kde4libs-devel libicu libqt3-devel lightdm-devel python-module-distribute qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel
BuildRequires: kde-common-devel
BuildRequires: lightdm-devel

%description
This package provides a KDE-based LightDM greeter engine.

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install

%K4find_lang --with-kde %name
%K4find_lang --with-kde --append --output=%name.lang kcm_lightdm
%K4find_lang --with-kde --append --output=%name.lang lightdm_theme_classic
%K4find_lang --with-kde --append --output=%name.lang lightdm_theme_userbar

cd %buildroot
# Add alternatives for xgreeters
mkdir -p ./%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/lightdm-kde-greeter.desktop\t300\n' >./%_altdir/lightdm-kde-greeter

%files -f %name.lang
%_altdir/lightdm-kde-greeter
%_sbindir/lightdm-kde-greeter
%_datadir/xgreeters/lightdm-kde-greeter.desktop
%_K4dbus_system/org.kde.kcontrol.kcmlightdm.conf
%_K4lib/kcm_lightdm.so
%_K4exec/kcmlightdmhelper
%_K4exec/lightdm-kde-greeter-rootimage
%_K4dbus_sys_services/org.kde.kcontrol.kcmlightdm.service
%_K4apps/lightdm-kde-greeter/
%_K4srv/kcm_lightdm.desktop
%_datadir/polkit-1/actions/org.kde.kcontrol.kcmlightdm.policy

%changelog
* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Wed Jul 25 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- initial build

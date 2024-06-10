%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}

%define lng_list af ar as ast be be@latin bg bn bn_IN br bs ca ca@valencia crh cs csb cy da de el en en_GB en_US eo es es_AR et eu fa fi fr fy ga gd gl gu ha he hi hne hr hsb hu hy ia id is it ja ka kk km kn ko ku lb lt lv mai mk ml mr ms my nb nds ne nl nn oc or pa pl ps pt pt_BR ro ru se si sk sl sq sr sr@ijekavian sr@ijekavianlatin sr@latin sv ta te tg th tok tr tt ug uk uz uz@cyrillic vi wa xh zh_CN zh_HK zh_TW

%define major 6
%define minor 0
%define bugfix 0

Name: kf6-filesystem
Version: %major.%minor.%bugfix
Release: alt1
%K6init no_altplace

Summary: The basic directory layout for KF6
License: GPL-2.0-or-later
Group: System/Base

Requires: filesystem qt6-base-common

#Source1: kde6

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-xdg

%description
The %name package is one of the basic KF6 packages that is installed on
a %distribution system; %name contains the basic directory layout
for the KDE 6, including the correct permissions for the directories.

%install
mkdir -p %buildroot/%_libdir

mkdir -p %buildroot/%_kf6_bin
mkdir -p %buildroot/%_kf6_sbin

mkdir -p %buildroot/%_kf6_icon/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128,scalable}/{actions,apps,devices,emblems,emotes,mimetypes,places,resources,status}
mkdir -p %buildroot/%_K6mod
mkdir -p %buildroot/%_K6exec
mkdir -p %buildroot/%_K6start
mkdir -p %buildroot/%_K6app
mkdir -p %buildroot/%_K6emo
mkdir -p %buildroot/%_K6snd
mkdir -p %buildroot/%_K6tmpl/.source
mkdir -p %buildroot/%_K6wall
mkdir -p %buildroot/%_K6conf
mkdir -p %buildroot/%_K6cfg
mkdir -p %buildroot/%_K6cf_upd
mkdir -p %buildroot/%_K6data/{color-schemes,solid/{actions,devices},widgets/pics,plasma/{packages,shells,updates,layout-templates}}
mkdir -p %buildroot/%_K6data/dbus-1/{interfaces,services,system-services}
mkdir -p %buildroot/%_K6dbus_iface
mkdir -p %buildroot/%_K6dbus_srv
mkdir -p %buildroot/%_K6dbus_sys_srv
#
mkdir -p %buildroot/%_K6notif
mkdir -p %buildroot/%_K6srv/ServiceMenus
mkdir -p %buildroot/%_K6srvtyp
mkdir -p %buildroot/%_K6xmlgui

mkdir -p %buildroot/%_kf6_xdgapp
mkdir -p %buildroot/%_desktopdir/kf6
mkdir -p %buildroot/%_K6xdgdir
mkdir -p %buildroot/%_K6xdgmenu

mkdir -p %buildroot/%_K6inc
mkdir -p %buildroot/%_K6link
mkdir -p %buildroot/%_K6plug/kf6/{kio_dnd,parts}
mkdir -p %buildroot/%_K6cf_bin

mkdir -p %buildroot/%_K6xdgconf/{autostart,colors,menus,ui}

mkdir -p %buildroot/%_datadir/{qlogging-categories6,}

mkdir -p %buildroot/%_K6data/{katepart6,knotifications6,kservicetypes6,kxmlgui6,knsrcfiles,ksmserver}
mkdir -p %buildroot/%_K6data/{kpackage/genericqml,plasma/kinfocenter,kio_desktop/DesktopLinks}
mkdir -p %buildroot/%_K6data/{kservices6/ServiceMenus,icons/breeze,icons/breeze-dark}

for l in %lng_list
do
    mkdir -p %buildroot/%_datadir/locale/$l/LC_SCRIPTS
    mkdir -p %buildroot/%_K6i18n/$l/{LC_MESSAGES,LC_SCRIPTS}
done

mkdir -p %buildroot/%_K6doc
for l in %lng_list
do
    mkdir -p %buildroot/%_K6doc/$l
done


ln -s `relative %_kf6_bin %_K6data/bin` %buildroot/%_K6data/bin
ln -s `relative %_libdir %_K6data/lib` %buildroot/%_K6data/lib

#mkdir -p %buildroot/%_bindir/
#install -m 0756 %SOURCE1 %buildroot/%_bindir/kde6

# install dbus dirs
mkdir -p %buildroot/{%_K6conf_dbus_sessd,%_K6conf_dbus_sysd}

%files
#%_bindir/kde6
%_datadir/*6/
%_datadir/locale/*/LC_SCRIPTS/
%_K6plug/kf6
#%dir %_sysconfdir/kf6
#%dir %_sysconfdir/kf6/*
#%dir %_sysconfdir/kf6/*/*
#%config(noreplace) %_sysconfdir/kf6/*/*
#%dir %_kf6_xdgconf/autostart/
#%dir %_kf6_xdgconf/menus/
#%dir %_K6_xdgconf/colors/
#%dir %_K6_xdgconf/ui/
%dir %_kf6_bin
%dir %_kf6_sbin
%dir %_K6cf_bin
#%dir %_K6exec
%dir %_K6inc
%dir %_libdir/kf6/
%dir %_K6link
%dir %_K6link
%dir %_K6doc
%dir %_desktopdir/kf6

%changelog
* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- initial build

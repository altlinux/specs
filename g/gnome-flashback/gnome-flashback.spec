%define ver_major 3.14
%define _libexecdir %_prefix/libexec

Name: gnome-flashback
Version: %ver_major.0
Release: alt1

Summary: GNOME Flashback session
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeFlashback

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%define glib_ver 2.40.0
%define gtk_ver 3.12.0
%define desktop_ver 3.12.0
%define dbus_glib_ver 0.76
%define gsds_ver 3.12.0


PreReq: xinitrc
Requires: gnome-session gnome-settings-daemon gnome-panel gnome-applets metacity3.0
Requires: libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-gnome3
Requires: dbus-tools-gui
Requires: gnome-filesystem
Requires: xdg-user-dirs
Requires: gnome-icon-theme gnome-icon-theme-symbolic
Requires: gnome-screensaver

BuildRequires: rpm-build-gnome gnome-common intltool
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libdbus-glib-devel >= %dbus_glib_ver
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libcanberra-gtk3-devel libpulseaudio-devel
BuildRequires: libXext-devel

%description
GNOME Flashback provides unofficial session and helper application.

This session consists of gnome-applets, gnome-flashback, gnome-panel and
metacity. And all other modules that are used in official GNOME session.

Helper application main job is to provide all features that is need for
our session, but has been removed from GNOME and/or moved to mutter or
gnome-shell.

NOTE: This session is not supported by GNOME in any way!

%prep
%setup

%build
%autoreconf
%configure \
    --disable-schemas-compile

%make_build

%install
%makeinstall_std
cat <<__START_GNOME_FLASHBACK__ >start%name
#!/bin/sh

. %_datadir/gnome-session/startgnome-common

exec %_libexecdir/%name-metacity "\$@"
__START_GNOME_FLASHBACK__

install -pD -m755 start%name %buildroot%_bindir/start%name

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/09GnomeFlashback
NAME=Gnome-Flashback
ICON=%_iconsdir/gnome.svg
DESC=Gnome Flashback
EXEC=%_bindir/start%name
SCRIPT:
exec %_bindir/start%name
__EOF__

ln -sf gnome-applications.menu %buildroot/%_xdgmenusdir/%name-applications.menu

%find_lang --with-gnome --output=%name.lang %name

%check
%make check

%files -f %name.lang
%_bindir/%name
%_bindir/start%name
%_libexecdir/%name-compiz
%_libexecdir/%name-metacity
%_desktopdir/%name.desktop
%_desktopdir/%name-init.desktop
%_datadir/gnome-session/sessions/%name-compiz.session
%_datadir/gnome-session/sessions/%name-metacity.session
#%config %_sysconfdir/X11/wmsession.d/09GnomeFlashback
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_xdgmenusdir/%name-applications.menu
%_datadir/xsessions/%name-metacity.desktop
%doc AUTHORS NEWS README

%exclude %_datadir/xsessions/%name-compiz.desktop


%changelog
* Mon Oct 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- first build for Sisyphus


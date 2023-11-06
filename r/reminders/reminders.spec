%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name Reminders
%define ver_major 5.0
%define beta .rc
%define rdn_name io.github.remindersdevs.Reminders

%def_disable check

Name: reminders
Version: %ver_major
Release: alt0.9%beta

Summary: Reminders, an open source reminder app
License: GPL-3.0
Group: Office
Url: https://github.com/remindersdevs/Reminders

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version%beta.tar.gz
%else
Vcs: https://github.com/remindersdevs/Reminders.git
Source: %_name-%version%beta.tar
%endif
Patch1: %_name-5.0.rc-install.patch

%define adwaita_ver 1.2

Requires: typelib(Adw) = 1

BuildArch: noarch

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir rpm-build-xdg
BuildRequires: meson yelp-tools
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(libadwaita-1) gir(Adw)
%{?_enable_check:BuildRequires:}

%description
%summary
Features:
- Set recurring reminders
- Schedule notifications
- Sort, filter, and search for reminders
- Mark reminders as important or complete
- Organize reminders using lists
- Optionally play a sound when notifications are sent
- Optionally sync with Microsoft To Do
- Optionally sync with CalDAV servers
- Import and export ical/ics files

%prep
%setup -n %_name-%version%beta
%patch1 -b .orig

%build
%meson
%meson_build

%install
%meson_install

cp %buildroot%_xdgconfigdir/autostart/%rdn_name.Service.desktop \
   %buildroot%_desktopdir/%rdn_name.Service.desktop

%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%_xdgconfigdir/autostart/%rdn_name.Service.desktop
%_bindir/%name
%_libexecdir/%name-service
%python3_sitelibdir_noarch/%name/
%_datadir/sounds/%name/
%_desktopdir/%rdn_name.desktop
%_desktopdir/%rdn_name.Service.desktop
%_datadir/dbus-1/interfaces/%rdn_name.Service.xml
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/services/%rdn_name.Service.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* REMINDERS_SERVICE*

%changelog
* Sun Nov 05 2023 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt0.9.rc
- first build for Sisyphus (v5.0.rc-7-gf649ea6)



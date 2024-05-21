%def_enable snapshot
%define _name pika-backup
%define ver_major 0.7
%define xdg_name org.gnome.World.PikaBackup

# cargo test failed
%def_disable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: Keep your data safe
License: GPL-3.0
Group: Archiving/Backup
Url: https://apps.gnome.org/PikaBackup

Vcs: https://gitlab.gnome.org/World/pika-backup.git
Source: %name-%version.tar
Source1: %name-%version-cargo.tar

%define gtk_ver 4.12.5
%define adwaita_ver 1.4.0

Requires: borg fuse3 libsecret python3(pyfuse3)

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson rust-cargo yelp-tools git
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli /usr/bin/glib-compile-schemas desktop-file-utils}

%description
Doing backups the easy way. Plugin your USB drive and let the Pika do the rest for you.

- Create backups locally and remotely
- Set a schedule for regular backups
- Save time and disk space because Pika Backup does not need to copy known data again
- Encrypt your backups
- List created archives and browse through their contents
- Recover files or folders via your file browser

Pika Backup is designed to save your personal data and does not support
complete system recovery. Pika Backup is powered by the well-tested
BorgBackup software.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_xdgconfigdir/autostart/%xdg_name.Monitor.desktop
%_bindir/%name
%_bindir/%name-monitor
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.Monitor.desktop
%_datadir/dbus-1/services/%xdg_name.Api.service
%_datadir/dbus-1/services/%xdg_name.Monitor.service
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Tue May 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- first build for Sisyphus (v0.7.2-4-g67acb4e)




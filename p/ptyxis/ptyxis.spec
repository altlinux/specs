%define glib2_version 2.78
%define gtk4_version 4.12
%define vte291_version 0.77
%define json_glib_version 1.4.0
%define libadwaita_version 1.5.0
%define libportal_gtk4_version 0.7.1
%define pcre_version 10.21

Name: ptyxis
Version: 47.0
Release: alt1

Summary: Ptyxis is a terminal for GNOME with first-class support for containers
License: GPL-3.0
Group: Terminals

Url: https://gitlab.gnome.org/chergert/ptyxis

# Source-url: https://gitlab.gnome.org/chergert/ptyxis/-/archive/%version/%version.tar.gz
Source: %name-%version.tar

ExcludeArch: i586

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-systemd

BuildRequires: pkgconfig(gio-unix-2.0) >= %glib2_version
BuildRequires: pkgconfig(gtk4) >= %gtk4_version
BuildRequires: pkgconfig(vte-2.91-gtk4) >= %vte291_version
BuildRequires: pkgconfig(libadwaita-1) >= %libadwaita_version
BuildRequires: pkgconfig(libportal-gtk4) >= %libportal_gtk4_version
BuildRequires: pkgconfig(json-glib-1.0) >= %json_glib_version
BuildRequires: pkgconfig(libpcre2-8) >= %pcre_version
BuildRequires: libgraphene-devel
BuildRequires: itstool
BuildRequires: meson

Provides: Terminal = %version-%release
Provides: x-terminal-emulator

%description
%summary

%prep
%setup

%build
%meson -Dgeneric=terminal
%meson_build

%install
%meson_install
%find_lang --with-gnome  %name

%files -f %name.lang
%doc README.md NEWS
%doc COPYING
%_bindir/ptyxis
%_libexecdir/ptyxis-agent
%_datadir/metainfo/org.gnome.Ptyxis.metainfo.xml
%_desktopdir/org.gnome.Ptyxis.desktop
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/services
%_datadir/dbus-1/services/org.gnome.Ptyxis.service
%_datadir/glib-2.0/schemas/org.gnome.Ptyxis.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_man1dir/ptyxis.1.xz

%changelog
* Fri Sep 20 2024 Boris Yumankulov <boria138@altlinux.org> 47.0-alt1
- new version 47.0

* Mon Sep 16 2024 Boris Yumankulov <boria138@altlinux.org> 46.6-alt1.1
- add terminal provides (ALT Bug: 51463)

* Sun Aug 11 2024 Boris Yumankulov <boria138@altlinux.org> 46.6-alt1
- new version 46.6

* Thu Jul 11 2024 Boris Yumankulov <boria138@altlinux.org> 46.5-alt1
- new version 46.5

* Sun Jun 30 2024 Boris Yumankulov <boria138@altlinux.org> 46.4-alt1
- new version 46.4

* Thu Jun 20 2024 Boris Yumankulov <boria138@altlinux.org> 46.3-alt1
- new version 46.3
- add libvte-ptyxis subpackage

* Sun Jun 09 2024 Boris Yumankulov <boria138@altlinux.org> 46.2-alt1
- initial build for ALT Sisyphus


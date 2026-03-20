%define glib2_version 2.78
%define gtk4_version 4.12
%define vte291_version 0.77
%define json_glib_version 1.4.0
%define libadwaita_version 1.5.0
%define libportal_gtk4_version 0.7.1
%define pcre_version 10.21
%define _unpackaged_files_terminate_build 1

%def_enable check

Name: ptyxis
Version: 50.1
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
BuildRequires: /proc

%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: %_bindir/appstream-util
%endif

Provides: Terminal = %version-%release
Provides: x-terminal-emulator
Provides: xvt

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

mkdir -p %buildroot%_altdir
cat << __EOF__ > %buildroot%_altdir/%name
%_bindir/x-terminal-emulator	%_bindir/%name	36
%_bindir/xvt	%_bindir/%name	36
__EOF__

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/org.gnome.Ptyxis.metainfo.xml
desktop-file-validate %buildroot%_desktopdir/org.gnome.Ptyxis.desktop

%files -f %name.lang
%doc README.md NEWS
%doc COPYING
%_bindir/%name
%_libexecdir/%name-agent
%_datadir/metainfo/org.gnome.Ptyxis.metainfo.xml
%_desktopdir/org.gnome.Ptyxis.desktop
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/services
%_datadir/dbus-1/services/org.gnome.Ptyxis.service
%_datadir/glib-2.0/schemas/org.gnome.Ptyxis.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_man1dir/%name.1.xz
%_altdir/%name

%changelog
* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 50.1-alt1
- new version 50.1

* Tue Jan 27 2026 Boris Yumankulov <boria138@altlinux.org> 49.3-alt1
- new version 49.3

* Fri Nov 07 2025 Boris Yumankulov <boria138@altlinux.org> 49.2-alt1
- new version 49.2

* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 49.1-alt1
- new version 49.1

* Thu Jul 10 2025 Boris Yumankulov <boria138@altlinux.org> 48.5-alt1
- new version 48.5 (ALT bug: 54776)

* Sat May 31 2025 Boris Yumankulov <boria138@altlinux.org> 48.4-alt1
- new version 48.4

* Sat May 10 2025 Boris Yumankulov <boria138@altlinux.org> 48.3-alt1
- new version 48.3

* Fri Mar 28 2025 Boris Yumankulov <boria138@altlinux.org> 48.1-alt1
- new version 48.1

* Sun Feb 16 2025 Boris Yumankulov <boria138@altlinux.org> 47.10-alt1
- new version 47.10
- add forget xvt alternative

* Wed Dec 25 2024 Boris Yumankulov <boria138@altlinux.org> 47.6-alt1
- new version 47.6
- add x-terminal-emulator alternative
- replace ptyxis to %%name macro
- enable check
- add /proc to BuildRequires

* Tue Nov 26 2024 Boris Yumankulov <boria138@altlinux.org> 47.5-alt1
- new version 47.5

* Sun Nov 03 2024 Boris Yumankulov <boria138@altlinux.org> 47.4-alt1
- new version 47.4

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


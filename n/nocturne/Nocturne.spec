%define oname com.jeffser.Nocturne

Name: nocturne
Version: 0.7.1
Release: alt1

Summary: An Adwaita Music Player / Library Manager
License: GPL-3.0-or-later
Group: Sound

Url: https://github.com/Jeffser/Nocturne
Vcs: https://github.com/Jeffser/Nocturne

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar
Source1: ru.po

%add_python3_path %_datadir/%name/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson pkgconfig(gtk4) pkgconfig(libadwaita-1) gettext-tools
BuildRequires: typelib(Adw) blueprint-compiler /usr/bin/appstreamcli

%description
Nocturne is a Navidrome / Jellyfin client that brings all your music
together in one place, Nocturne not only connects to existing instances
but it's capable of installing and managing it's own Navidrome instance.

%prep
%setup
cp -a %SOURCE1 po/

%build
%meson
%meson_build

%install
%meson_install
for locale in de es ru; do  
 msgfmt po/${locale}.po -o po/${locale}.mo
 install -Dm 0644 po/${locale}.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%name.mo
done

%find_lang %name --all-name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%oname.desktop
%_datadir/dbus-1/services/%oname.service
%_datadir/glib-2.0/schemas/%oname.*
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%oname.*
%_datadir/%name
%doc *.md

%changelog
* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt2
- fixed locales
- added russian locale

* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- 0.6.0 -> 0.7.0

* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux.


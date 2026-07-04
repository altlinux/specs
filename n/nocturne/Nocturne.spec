%define _unpackaged_files_terminate_build 1
%define oname com.jeffser.Nocturne

Name: nocturne
Version: 1.3.1
Release: alt1

Summary: A modern Navidrome / Jellyfin client
License: GPL-3.0-or-later
Group: Sound

Url: https://github.com/Jeffser/Nocturne
Vcs: https://github.com/Jeffser/Nocturne

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

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

%build
%meson
%meson_build

%install
%meson_install

%find_lang --all-name --output=%name.lang %name

%files -f %name.lang
%_bindir/%{name}*
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/%oname.*
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%oname.*
%_datadir/%name
%_datadir/gnome-shell/search-providers/%oname.search-provider.ini
%doc *.md

%changelog
* Sat Jul 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1

* Fri Jun 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.0-alt1
- automatic build: 1.2.2 -> 1.3.0

* Tue Jun 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2

* Wed May 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1

* Tue May 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.2.0-alt1
- 1.1.1 -> 1.2.0

* Tue May 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.1-alt1
- 1.1.0 -> 1.1.1

* Sun May 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0

* Thu May 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.1-alt1
- 1.0.0 -> 1.0.1

* Tue May 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- 0.9.7 -> 1.0.0

* Thu Apr 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.7-alt1
- 0.9.6 -> 0.9.7

* Tue Apr 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.6-alt1
- 0.9.5 -> 0.9.6

* Sun Apr 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.5-alt1
- 0.9.0 -> 0.9.5

* Fri Apr 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.9.0-alt1
- 0.8.5 -> 0.9.0

* Wed Apr 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.5-alt1
- 0.8.0 -> 0.8.5

* Tue Apr 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0

* Mon Apr 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt2
- updated to git.ecc43593fd

* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1

* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt2
- fixed locales
- added russian locale

* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- 0.6.0 -> 0.7.0

* Sat Apr 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux.


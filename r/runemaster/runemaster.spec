%define _unpackaged_files_terminate_build 1

%define appname io.github.johnfactotum.Runemaster

Name: runemaster
Version: 1.2.0
Release: alt1

Summary: Unleash the magic of Unicode characters
License: GPL-3.0-or-later
Group: Publishing
Url: https://github.com/johnfactotum/runemaster

Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: cmake
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

Requires: libgtk4-gir
Requires: libadwaita-gir

BuildArch: noarch

%description
Unleash the magic of Unicode characters.

Features:

* Browse Unicode characters, by block or script, color coded by
  general category.
* See details for each character, including cross references,
  comments, HTML entities, and compose key sequences.
* Compose and edit text in the scratchpad. Apply normalization,
  change casing, and see the code point breakdown.

%prep
%setup
sed -i "s|io.github.johnfactotum.Runemaster.svg|%_iconsdir/hicolor/scalable/apps/%{appname}.svg|" README.md
sed -i "s|^Categories=.*|Categories=Office;Publishing;|" io.github.johnfactotum.Runemaster.desktop

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md screenshot.png
%_bindir/runemaster
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%dir %_datadir/%{appname}
%_datadir/%{appname}/%{appname}.gresource
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Thu Apr 09 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

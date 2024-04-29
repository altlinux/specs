%define _name textpieces
%define ver_major 3.4
%define rdn_name com.github.liferooter.textpieces

# Validate appstream file        FAIL
%def_disable check

Name: %_name
Version: %ver_major.1
Release: alt2

Summary: Transform text without using random websites
License: GPL-3.0-or-later
Group: Text tools
Url: https://apps.gnome.org/Textpieces

Vcs: https://github.com/liferooter/textpieces.git
Source0: %name-%version.tar

Patch0: textpieces-v3.4.1.b22e86b-alt-bp-CustomToolPage-file-fix.patch
Patch1: textpieces-v3.4.1.b22e86b-alt-bp-Editor-file-fix.patch
Patch2: textpieces-v3.4.1.b22e86b-alt-bp-NewToolPage-file-fix.patch
Patch3: textpieces-v3.4.1.b22e86b-alt-bp-Preferences-file-fix.patch
Patch4: textpieces-v3.4.1.b22e86b-alt-bp-SearchBar-file-fix.patch

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson vala-tools blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0) pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(gtksourceview-5) gir(GtkSource) = 5
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Do a lot of text transformations, such as:

Calculate hashes
Encode text
Decode text
Remove trailing spaces and lines
Count lines, symbols and words
Format JSON and XML
Escape and unescape strings
Convert JSON to YAML and vice versa
Filter lines
Replace substrings and regular expressions
...and so on.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/appdata/%rdn_name.appdata.xml
%doc README.*

%changelog
* Tue Apr 30 2024 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- prepared for Sisyphus

* Sun Apr 28 2024 Semen Fomchenkov <armatik@altlinux.org> 3.4.1-alt1
- First Build

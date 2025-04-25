%define _unpackaged_files_terminate_build 1
%define app_id io.github.revisto.drum-machine

Name: drum-machine
Version: 1.3.1
# git describe --tags upstream/master
Release: alt1.56.gc8d4f3b

Summary: Create and play drum beats
License: GPL-3.0-or-later
Group: Sound

Url: https://github.com/revisto/drum-machine
Vcs: https://github.com/revisto/drum-machine
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gtk-update-icon-cache
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: libgio
BuildRequires: python3
%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

Requires: python3(gi)
Requires: typelib(Adw)
Requires: typelib(Gtk)
Requires: python3(mido)
Requires: python3(pygame)

BuildArch: noarch

%description
Drum Machine is a modern and intuitive application for creating, playing, and
managing drum patterns. Perfect for musicians, producers, and anyone interested
in rhythm creation, this application provides a simple interface for drum
pattern programming. Have fun!

Features:
- Intuitive grid-based pattern editor
- Adjustable BPM control
- Volume control for overall mix
- Save and load preset patterns
- Multiple drum sounds including kick, snare, hi-hat, and more
- Keyboard shortcuts for quick access to all functions

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/applications/%app_id.desktop
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Wed Apr 23 2025 David Sultaniiazov <x1z53@altlinux.org> 1.3.1-alt1.56.gc8d4f3b
- Initial build

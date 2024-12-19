# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-arcmenu
Version: 63
Release: alt1
Summary: Application menu for GNOME Shell
License: GPL-2.0-or-later
Group:  Graphical desktop/GNOME
Url: https://gitlab.com/arcmenu/ArcMenu
Vcs: https://gitlab.com/arcmenu/ArcMenu
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 47.0
BuildRequires: %_bindir/glib-compile-schemas

%description
ArcMenu is an application menu for GNOME Shell, designed to provide a more
familiar user experience and workflow. This extension has many features,
including various menu layout styles, GNOME search, quick access to system
shortcuts, and much more!

%prep
%setup
%autopatch -p1

%build
%make_build

%install
%makeinstall_std
%find_lang arcmenu

%files -f arcmenu.lang
%_datadir/gnome-shell/extensions/arcmenu@arcmenu.com
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.arcmenu.gschema.xml
%doc README.md

%changelog
* Thu Dec 19 2024 Anton Midyukov <antohami@altlinux.org> 63-alt1
- initial build

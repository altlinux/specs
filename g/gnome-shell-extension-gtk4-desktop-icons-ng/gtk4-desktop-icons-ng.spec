# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-gtk4-desktop-icons-ng
Version: 87
Release: alt1
Summary: Extension for the GNOME Shell that renders icons on the desktop

License: GPL-3.0-or-later
Group:  Graphical desktop/GNOME
Url: https://gitlab.com/smedius/desktop-icons-ng
Vcs: https://gitlab.com/smedius/desktop-icons-ng
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 40.0
Requires: nautilus >= 3.38.0
Requires: file-roller >= 3.38.0
BuildRequires: %_bindir/glib-compile-schemas
BuildRequires: meson

%description
Gtk4 Desktop Icons NG is an extension and a program together for the GNOME Shell
that renders icons on the desktop. It is a fork from DING.
Desktop Icons NG (DING) by Sergio Costas itself is a fork/rewrite of the
official 'Desktop Icons' extension, originally by Carlos Soriano.

This new Gtk4 extension was originally submitted upstream to the DING project as
a merge request. It was not merged for quite some time with development
continuing on both branches simultaneously. The branches started diverging
significantly, and further, the new commit's in the original DING branch were
not easily adaptable to changes already made in this gtk4 branch. That made it
very difficult to rebase and merge all the new changes to the original branch.

A mutual decision was therefore made to continue independent development of both
branches. Important bug fixes from branches are still back ported and
forward-ported between them. Therefore there are two extensions available, the
classic DING that uses Gtk 3, and this newer fork based on Gtk 4 and libadwaita.

This fork of DING is ported to use the Gtk4 toolkit, and now has been ported to
libadwaita. This, and the original DING can both be installed together, but only
one can be activated at a time in the extension Manager. They use different
install directories and GSettings schemas, therefore preferences set in one will
not carrry through to the other. This is to avoid trampling on the stable branch
and isolate errors from this branch.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang gtk4-ding

# remove apparmor config
rm -r %buildroot%_sysconfdir/apparmor.d

%files -f gtk4-ding.lang
%_datadir/gnome-shell/extensions/gtk4-ding@smedius.gitlab.com
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.gtk4-ding.gschema.xml
%doc README.md

%changelog
* Thu Dec 19 2024 Anton Midyukov <antohami@altlinux.org> 87-alt1
- initial build

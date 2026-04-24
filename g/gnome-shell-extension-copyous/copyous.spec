%define _unpackaged_files_terminate_build 1
%define _name copyous
%define uuid %_name@boerdereinar.dev
%define xdg_name org.gnome.shell.extensions.%_name

Name: gnome-shell-extension-%_name
Version: 2.0.1
Release: alt1
Summary: Modern Clipboard Manager for GNOME
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/boerdereinar/copyous
Vcs: https://github.com/boerdereinar/copyous

Source0: %name-%version.tar
Source1: node_modules.tar
Source2: submodules.tar

Patch0: %name-%version-alt.patch

BuildArch: noarch

Requires: libgda6-gir
Requires: libgda6-sqlite
Requires: libgsound-gir

BuildRequires: node
BuildRequires: gnome-shell
BuildRequires: git
BuildRequires: sqlite3
BuildRequires: jq

%description
Modern clipboard manager for GNOME Shell. Supports storing and browsing 
clipboard history of text, code, images, files, links, characters and colors.
Allows pasting from history, pinning favorite items, grouping, quick search,
opening at mouse pointer or cursor, and offers a clean UI + full settings via
GNOME preferences.

%prep
%setup -q -n %name-%version -a1 -a2
%autopatch -p1

%build
%make

%install
install -d %buildroot%_datadir/gnome-shell/extensions/%uuid
unzip -q dist/%uuid.zip -d %buildroot%_datadir/gnome-shell/extensions/%uuid

# fix install gsettings schemas
mkdir -p %buildroot%_datadir/glib-2.0/schemas
mv %buildroot%_datadir/gnome-shell/extensions/%uuid/schemas/*.xml \
	%buildroot%_datadir/glib-2.0/schemas
rm -vr %buildroot%_datadir/gnome-shell/extensions/%uuid/schemas

%find_lang %uuid

%files -f %uuid.lang
%_datadir/gnome-shell/extensions/%uuid
%_datadir/glib-2.0/schemas/*.xml

%changelog
* Fri Apr 24 2026 Vladislav Petrukhin <vladp@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Tue Feb 24 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.3.0-alt2
- Fix install gsettings schemas

* Mon Jan 19 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Mon Dec 08 2025 Vladislav Petrukhin <vladp@altlinux.org> 1.1.3-alt1
- Initial build.

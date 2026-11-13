%define _unpackaged_files_terminate_build 1

%def_with check

Name: mate-clipboard
Version: 2.0.1
Release: alt1

Summary: A clipboard manager for MATE with Wayland and X support
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/mate-clipboard

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(wayland-protocols)

%description
A clipboard history applet for the MATE panel, written in Vala.
It works on MATE under **both X11** and **Wayland** (Wayfire, or
any compositor with the data-control protocol).

Features:

* Clipboard history: text, images and copied files
* Search: type to filter the history instantly
* Panel applet: click it to open the history next to the panel
* Keyboard shortcut: open the history at the mouse pointer (X11)
  or next to the applet
* Encrypted history: stored encrypted with XChaCha20-Poly1305,
  with the key kept in your login keyring
* Image thumbnails: small previews, stored separately from the
  full image
* Primary selection: optionally track the mouse selection and
  keep it in sync
* Content filtering: skip text matching a regular expression,
  and anything password managers mark as secret

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md
%_libdir/mate-panel/libmate-clipman-applet.so
%_datadir/glib-2.0/schemas/org.mate.clipman.gschema.xml
%_datadir/mate-panel/applets/org.mate.panel.ClipmanApplet.mate-panel-applet

%changelog
* Fri Nov 13 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus

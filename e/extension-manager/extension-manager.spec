Name: extension-manager
Version: 0.4.2
Release: alt2

Summary: A utility for browsing and installing GNOME Shell Extensions
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/mjakeman/extension-manager

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libbacktrace-devel
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(pygobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: typelib(Adw) 
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(text-engine-0.1)
BuildRequires: pkgconfig(blueprint-compiler)

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

With Extension Manager you can:
* Browsing and searching extensions from extensions.gnome.org
* Installation and Removal
* Enabling and Disabling
* Updating in-app 
* Screenshots & Images
* Ratings & Comments

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_datadir/applications/*.desktop
%_datadir/glib-2.0/schemas/com.mattjakeman.ExtensionManager.gschema.xml
%_datadir/icons/*/*/*/*.svg
%_datadir/metainfo/*.appdata.xml

%changelog
* Mon Jul 10 2023 Roman Alifanov <ximper@altlinux.org> 0.4.2-alt2
- build without removing backtrace-supported.h

* Mon Jun 26 2023 Roman Alifanov <ximper@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus.

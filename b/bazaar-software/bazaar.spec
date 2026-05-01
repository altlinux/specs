%define _unpackaged_files_terminate_build 1
%define app_id io.github.kolunmi.Bazaar
%define _name bazaar
%define libname bge

Name: bazaar-software
Version: 0.7.15
Release: alt1

Summary: Discover and install applications
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

URL: https://github.com/kolunmi/bazaar
VCS: https://github.com/kolunmi/bazaar
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: meson
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libdex-1)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(xmlb)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glycin-2)
BuildRequires: pkgconfig(glycin-gtk4-2)
BuildRequires: pkgconfig(md4c)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(malcontent-0)
BuildRequires: python3(babel)

Requires: flatpak

ExcludeArch: i586

%description
A new app store for Linux with a focus on discovering and installing
applications and addons from Flatpak remotes, particularly Flathub.

It emphasizes supporting the developers who make the Linux desktop possible.
Bazaar features a "curated" tab that can be configured by distributors to allow
for a more localized experience.

%package -n lib%libname
Summary: Bazaar GTK Extensions
Group: Development/C++

%description -n lib%libname
%summary.

%package -n lib%libname-devel
Summary: Headers for %name
Group: Development/C++

%description -n lib%libname-devel
%summary.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%check
%meson_test

%files -f %_name.lang
%_bindir/%{_name}*
%_userunitdir/%app_id.service
%_desktopdir/%app_id.desktop
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/gnome-shell/search-providers/%app_id.search-provider.ini
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml

%files -n lib%libname
%_bindir/%libname-demo
%_libdir/lib%libname-%version.so

%files -n lib%libname-devel
%_includedir/%libname
%_pkgconfigdir/%libname-%version.pc

%changelog
* Tue Apr 28 2026 David Sultaniiazov <x1z53@altlinux.org> 0.7.15-alt1
- 0.7.15.
- Add flatpak requirement.

* Mon Jan 19 2026 David Sultaniiazov <x1z53@altlinux.org> 0.7.5-alt1
- Initial build.

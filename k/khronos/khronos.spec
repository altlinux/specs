%def_enable snapshot
%define _name khronos
%define ver_major 3.7
%define rdn_name io.github.lainsce.Khronos

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Track each task's time in a simple inobtrusive way
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/lainsce/khronos

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/lainsce/khronos.git
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4),
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)

%description
Start tracking any task's "during" time and start-stop as you go,
with notifications.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc AUTHORS README*


%changelog
* Wed Nov 30 2022 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- first build for Sisyphus (3.7.0-15-gc97c3c2)




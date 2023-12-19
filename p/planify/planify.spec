%def_enable snapshot
%define _name planify
%define ver_major 4.3
%define rdn_name io.github.alainm23.%_name

%def_enable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: Planify
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/alainm23/planify

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/alainm23/planify.git
Source: %_name-%version.tar
%endif

# to avoid conflict between webki2gtk{4.1,6.0}-debuginfo
%add_debuginfo_skiplist %_bindir/%rdn_name

%define adwaita_ver 1.4
%define ecal_ver 3.45.1

Requires: lib%_name = %EVR
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson vala-tools
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libecal-2.0) >= %ecal_ver
BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: evolution-data-server-vala
BuildRequires: pkgconfig(libical-glib)
BuildRequires: pkgconfig(libportal-gtk4)

%description
Planner with Todoist support.

%package -n lib%_name
Summary: Planify shared library
Group: System/Libraries

%description -n lib%_name
This package contains shared library needed Planify to work.

%package -n lib%_name-devel
Summary: Planify development files
Group: Development/C
Requires: lib%_name = %EVR

%description -n lib%_name-devel
This package contains files necessary to develop Planify plugins.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%_name.lang %rdn_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%rdn_name
%_bindir/%rdn_name.quick-add
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*

%files -n lib%_name
%_libdir/lib%name.so.*

%files -n lib%_name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%_name.pc
%_vapidir/%_name.*

%changelog
* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- first build for Sisyphus (4.2.1-7-g8e7515f3)



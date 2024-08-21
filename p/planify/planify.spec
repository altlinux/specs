%def_disable snapshot
%define _name planify
%define ver_major 4.10
%define rdn_name io.github.alainm23.%_name

%def_enable check

Name: %_name
Version: %ver_major.8
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

%define gtk_ver 4.13.7
%define adwaita_ver 1.4
%define ecal_ver 3.45.1

Requires: lib%_name = %EVR
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson vala-tools %{?_disable_snapshot:git}
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libecal-2.0) >= %ecal_ver
BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: evolution-data-server-vala
BuildRequires: pkgconfig(libical-glib)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(gxml-0.20)
BuildRequires: pkgconfig(libsecret-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

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
%meson %{?_disable_snapshot:-Dprofile=default}
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
%_datadir/gtksourceview-5/language-specs/markdownpp.lang
%_datadir/gtksourceview-5/styles/markdown.xml
%_datadir/gtksourceview-5/styles/markdown_dark.xml
%doc README*

%files -n lib%_name
%_libdir/lib%name.so.*

%files -n lib%_name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%_name.pc
%_vapidir/%_name.*

%changelog
* Wed Aug 21 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.8-alt1
- 4.10.8

* Fri Aug 09 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.7-alt1
- 4.10.7

* Tue Aug 06 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.6-alt1
- 4.10.6

* Sat Aug 03 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.5-alt1
- 4.10.5

* Thu Aug 01 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.4-alt1
- 4.10.4

* Wed Jul 31 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.2-alt1
- 4.10.2

* Tue Jul 30 2024 Yuri N. Sedunov <aris@altlinux.org> 4.10.0-alt1
- 4.10.0

* Fri Jul 12 2024 Yuri N. Sedunov <aris@altlinux.org> 4.9.0-alt1
- 4.9.0

* Mon Jun 24 2024 Yuri N. Sedunov <aris@altlinux.org> 4.8.4-alt1
- 4.8.4

* Tue Jun 04 2024 Yuri N. Sedunov <aris@altlinux.org> 4.8.2-alt1
- 4.8.2

* Sat Jun 01 2024 Yuri N. Sedunov <aris@altlinux.org> 4.8-alt1
- updated to 4.8-1-gb7323667

* Thu May 23 2024 Yuri N. Sedunov <aris@altlinux.org> 4.7.4-alt2
- updated to 4.7.4-5-g72ae6d16

* Sun May 19 2024 Yuri N. Sedunov <aris@altlinux.org> 4.7.4-alt1
- 4.7.4

* Sat May 11 2024 Yuri N. Sedunov <aris@altlinux.org> 4.7.2-alt1
- 4.7.2

* Thu May 02 2024 Yuri N. Sedunov <aris@altlinux.org> 4.7-alt1
- updated to 4.7-3-g6659323b

* Tue Apr 16 2024 Yuri N. Sedunov <aris@altlinux.org> 4.6-alt1
- updated to 4.6-2-g311942b4

* Sat Mar 30 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.12-alt1
- 4.5.12

* Fri Mar 29 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.11-alt1
- 4.5.11

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.10-alt1
- 4.5.10

* Fri Mar 22 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.8-alt1
- 4.5.8

* Tue Mar 19 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.4-alt1
- 4.5.4

* Wed Mar 06 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.2-alt1
- 4.5.2

* Thu Feb 22 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5-alt1
- 4.5

* Thu Jan 11 2024 Yuri N. Sedunov <aris@altlinux.org> 4.4-alt1
- updated to 4.4-2-gb0d21d71

* Thu Dec 21 2023 Yuri N. Sedunov <aris@altlinux.org> 4.3.2-alt1
- 4.3.2

* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 4.3.1-alt1
- 4.3.1

* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- first build for Sisyphus (4.2.1-7-g8e7515f3)



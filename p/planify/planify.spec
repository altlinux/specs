%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name planify
%define ver_major 4.19
%define rdn_name io.github.alainm23.%_name

%def_enable man
%def_disable check

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: Planify
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://useplanify.com

Vcs: https://github.com/alainm23/planify.git

%if_disabled snapshot
Source: https://github.com/alainm23/planify/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define gtk_ver 4.18
%define adwaita_ver 1.7
%define ecal_ver 3.45.1

Requires: lib%_name = %EVR
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson vala-tools %{?_disable_snapshot:git}
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libspelling-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libecal-2.0) >= %ecal_ver
BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: evolution-data-server-vala
BuildRequires: pkgconfig(libical-glib)
BuildRequires: pkgconfig(icu-uc)
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
%meson %{?_disable_snapshot:-Dprofile=default} \
    %{subst_enable_meson_bool man manpage}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%_name.lang %rdn_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%rdn_name
%_bindir/%rdn_name.cli
%_bindir/%rdn_name.quick-add
%_libexecdir/%rdn_name-search-provider
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%{?_enable_man:%_man1dir/%{name}*.1*}
%doc README*

%files -n lib%_name
%_libdir/lib%name.so.*

%files -n lib%_name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%_name.pc
%_vapidir/%_name.*

%changelog
* Tue May 19 2026 Yuri N. Sedunov <aris@altlinux.org> 4.19.3-alt1
- updated to v4.19.3-5-gf03ded37c

* Fri May 15 2026 Yuri N. Sedunov <aris@altlinux.org> 4.19.2-alt1
- 4.19.2

* Sun Apr 26 2026 Yuri N. Sedunov <aris@altlinux.org> 4.19.1-alt1
- 4.19.1

* Tue Apr 21 2026 Yuri N. Sedunov <aris@altlinux.org> 4.19.0-alt1
- 4.19.0

* Thu Mar 19 2026 Yuri N. Sedunov <aris@altlinux.org> 4.18.3-alt1
- 4.18.3

* Sun Feb 08 2026 Yuri N. Sedunov <aris@altlinux.org> 4.18.0-alt1
- 4.18.0

* Sat Dec 27 2025 Yuri N. Sedunov <aris@altlinux.org> 4.17.0-alt1
- 4.17.0

* Thu Nov 27 2025 Yuri N. Sedunov <aris@altlinux.org> 4.16.1-alt1
- 4.16.1

* Fri Nov 07 2025 Yuri N. Sedunov <aris@altlinux.org> 4.15.2-alt1
- 4.15.2

* Thu Oct 16 2025 Yuri N. Sedunov <aris@altlinux.org> 4.15.1-alt1
- 4.15.1

* Tue Sep 30 2025 Yuri N. Sedunov <aris@altlinux.org> 4.14.1-alt1
- 4.14.1

* Sat Sep 20 2025 Yuri N. Sedunov <aris@altlinux.org> 4.14.0-alt1
- 4.14.0

* Fri Aug 29 2025 Yuri N. Sedunov <aris@altlinux.org> 4.13.4-alt1
- 4.13.4

* Sat Aug 09 2025 Yuri N. Sedunov <aris@altlinux.org> 4.13.2-alt1
- 4.13.2

* Sun Jul 20 2025 Yuri N. Sedunov <aris@altlinux.org> 4.13.0-alt1
- 4.13.0

* Mon Jul 07 2025 Yuri N. Sedunov <aris@altlinux.org> 4.12.2-alt2
- 4.12.2-8-gec5e4782 (updated russian translation)

* Wed Jun 18 2025 Yuri N. Sedunov <aris@altlinux.org> 4.12.2-alt1
- 4.12.2

* Sat Apr 05 2025 Yuri N. Sedunov <aris@altlinux.org> 4.12.0-alt1.1
- fixed FTBFS

* Wed Feb 05 2025 Yuri N. Sedunov <aris@altlinux.org> 4.12.0-alt1
- 4.12.0

* Wed Nov 06 2024 Yuri N. Sedunov <aris@altlinux.org> 4.11.6-alt1
- 4.11.6

* Tue Oct 15 2024 Yuri N. Sedunov <aris@altlinux.org> 4.11.5-alt1
- 4.11.5

* Sat Sep 21 2024 Yuri N. Sedunov <aris@altlinux.org> 4.11.4-alt1
- 4.11.4

* Sun Sep 15 2024 Yuri N. Sedunov <aris@altlinux.org> 4.11.2-alt1
- 4.11.2

* Fri Aug 30 2024 Yuri N. Sedunov <aris@altlinux.org> 4.11.0-alt1
- 4.11.0

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



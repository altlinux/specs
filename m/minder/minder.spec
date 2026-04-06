%def_disable snapshot

%define _name Minder
%define ver_major 2.0
%define rdn_name com.github.phase1geo.minder

%def_enable check

Name: minder
Version: %ver_major.8
Release: alt1

Summary: Mind-mapping application
License: GPL-2.0-or-later
Group: Office
Url: https://github.com/phase1geo/Minder

Vcs: https://github.com/phase1geo/Minder.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.80
%define gtk_ver 4.18

Requires(pre): shared-mime-info

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libmarkdown)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libwebp)
BuildRequires: vapi(granite-7)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Quickly create visual mind-maps using the keyboard and automatic layout.

%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_iconsdir/hicolor/*/mimetypes/application-%rdn_name.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%_xdgmimedir/packages/%rdn_name.xml
%doc AUTHORS* README*


%changelog
* Mon Apr 06 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.8-alt1
- 2.0.8

* Mon Feb 02 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Mon Jan 19 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Dec 23 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Fri Dec 19 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Tue Dec 16 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Dec 09 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0 (ported to GTK4/Granite-7)

* Fri Nov 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Thu Apr 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.16.4-alt1
- 1.16.4

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt1
- 1.16.3

* Sun Jan 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Thu Jan 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.6-alt1
- first build for Sisyphus (1.15.6-2-g3a35139)



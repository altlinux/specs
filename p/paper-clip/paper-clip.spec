%def_enable snapshot
%define _name Paper-Clip
%define binary_name pdf-metadata-editor
%define ver_major 4.0
%define rdn_name io.github.diegoivan.pdf_metadata_editor

%def_enable check

Name: paper-clip
Version: %ver_major
Release: alt1

Summary: PDF metadata editor for GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/Diego-Ivan/Paper-Clip

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/Diego-Ivan/Paper-Clip.git
Source: %_name-%version.tar
%endif

%define gtk_ver 4.10
%define adwaita_ver 1.2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(exempi-2.0)

%description
%summary

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %binary_name

%check
%__meson_test

%files -f %binary_name.lang
%_bindir/%binary_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Sat Dec 16 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- updated to v4.0-5-g6e784e0

* Sun Nov 05 2023 Yuri N. Sedunov <aris@altlinux.org> 3.6-alt1
- 3.6

* Mon Oct 09 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Tue Oct 03 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5-alt1
- updated to v3.5-1-gff3a532

* Fri Aug 04 2023 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- first build for Sisyphus



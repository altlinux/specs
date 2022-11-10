%def_disable snapshot
%define ver_major 3.42
%define xdg_name org.gnome.gnome-latex

%def_enable gtk_doc
# appdata.xml incomplete
%def_disable check

Name: gnome-latex
Version: %ver_major.0
Release: alt1

Summary: Integrated LaTeX Environment for the GNOME desktop
Group: Publishing
License: GPL-3.0
Url: https://gitlab.gnome.org/swilmet/gnome-latex

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/swilmet/gnome-latex.git
Source: %name-%version.tar
%endif

Requires: %_bindir/latexmk dconf

%define gtk_ver 3.24
%define gtksource_ver 4.8.4
%define tepl_ver 6.2.0
%define amtk_ver 5.4.1
%define vala_ver 0.46.5

BuildRequires: vala-tools >= %vala_ver
BuildRequires: autoconf-archive libappstream-glib-devel yelp-tools intltool
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview4-devel >= %gtksource_ver
BuildRequires: pkgconfig(tepl-6) >= %tepl_ver
BuildRequires: libamtk-devel >= %amtk_ver
BuildRequires: libgspell-devel libgee0.8-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libdconf-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgtksourceview4-gir-devel libtepl-gir-devel
BuildRequires: libgee0.8-gir-devel libgspell-gir-devel

%description
GNOME-LaTeX is an Integrated LaTeX Environment for GNOME. The main features are:
  * Configurable buttons to compile, convert and view a document in one click
  * LaTeX commands auto-completion
  * Side panel with the document structure, LaTeX symbols and an integrated
    file browser
  * Template managing
  * Menus with the most commonly used LaTeX commands
  * Easy projects management
  * Spell checking

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation for %name.

%prep
%setup

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-code-coverage
%make_build

%install
%makeinstall_std
%find_lang %name --with-gnome

%check
%make check

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/icons/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS README NEWS HACKING

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/*
%endif

%changelog
* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Wed May 04 2022 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Fri Apr 22 2022 Yuri N. Sedunov <aris@altlinux.org> 3.39.1-alt1
- 3.39.1

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt2
- 3.38.0-13-g703c2c9 (ported to Tepl-6)

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Sep 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.37.2-alt1
- 3.37.2

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.35.0-alt0.1
- updated to 3.32.0-23-g327309e

* Sun Mar 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Aug 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun May 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Sun Apr 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.2-alt1
- first build for Sisyphus


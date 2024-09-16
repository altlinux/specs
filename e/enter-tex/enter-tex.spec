%def_disable snapshot
%define ver_major 3.47
%define oldname gnome-latex
%define xdg_name org.gnome.enter_tex

%def_enable gtk_doc
%def_enable check

Name: enter-tex
Version: %ver_major.0
Release: alt1

Summary: Integrated LaTeX Environment for the GNOME desktop
Group: Publishing
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/swilmet/gnome-latex

Vcs: https://gitlab.gnome.org/swilmet/enter-tex.git

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Obsoletes: %oldname < 47
Provides: %oldname = %EVR

Requires: %_bindir/latexmk dconf

%define gtk_ver 3.24
%define gtksource_ver 299.3.0
%define tepl_ver 6.11.0
%define amtk_ver 5.9.0
%define vala_ver 0.46.5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson yelp-tools
BuildRequires: vala-tools >= %vala_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgedit-gtksourceview-devel >= %gtksource_ver
BuildRequires: pkgconfig(libgedit-tepl-6) >= %tepl_ver
BuildRequires: libgedit-amtk-devel >= %amtk_ver
BuildRequires: libgspell-devel libgee0.8-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libdconf-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgedit-gtksourceview-gir-devel libgedit-tepl-gir-devel
BuildRequires: libgee0.8-gir-devel libgspell-gir-devel
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: xvfb-run /usr/bin/appstreamcli desktop-file-utils}

%description
Enter TeX is a TeX/[LaTeX](https://www.latex-project.org/) text editor. The
application was previously named LaTeXila and then GNOME LaTeX. Its development
started in 2009.

Enter TeX is an Integrated LaTeX Environment for GNOME. The main features are:
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
Obsoletes: %oldname-devel-doc < 47
Provides: %oldname-devel-doc = %EVR

%description devel-doc
This package contains documentation for %name.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool gtk_doc gtk_doc}
%nil
%meson_build src/gtex/Gtex-1.gir
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/icons/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%_man1dir/%name.1.*
%doc README* NEWS

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/*
%endif

%changelog
* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 3.47.0-alt1
- 3.47.0

* Sat Jul 29 2023 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Sat Jun 24 2023 Yuri N. Sedunov <aris@altlinux.org> 3.45.1-alt1
- 3.45.1

* Mon Jan 02 2023 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

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


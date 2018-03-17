%define ver_major 3.27
%define xdg_name org.gnome.gnome-latex

%def_enable gtk_doc

Name: gnome-latex
Version: %ver_major.2
Release: alt1

Summary: Integrated LaTeX Environment for the GNOME desktop
Group: Publishing
License: GPLv3+
Url: https://wiki.gnome.org/Apps/GNOME-LaTeX

Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define gtk_ver 3.22
%define gtksource_ver 3.99.7
%define tepl_ver 3.99.1

BuildRequires: libappstream-glib-devel yelp-tools intltool
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgtksourceview4-devel >= %gtksource_ver
BuildRequires: libtepl-devel >= %tepl_ver
BuildRequires: libgspell-devel libgee0.8-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: vala-tools

#Requires: latexmk

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
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc}
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
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS README NEWS HACKING

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/*
%endif


%changelog
* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.2-alt1
- first build for Sisyphus


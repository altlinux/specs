%define _name gedit-latex
%define ver_major 3.4
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins-latex
Version: %ver_major.1
Release: alt1

Summary: LATEX plugin for GEdit
License: GPLv3
Group: Editors
Url: https://live.gnome.org/Gedit/LaTeXPlugin/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

# From configure.in
%define glib_ver 2.28.0
%define gtk_ver 3.3.15
%define gedit_ver 3.4.0

BuildPreReq: rpm-build-gnome >= 0.6

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gnome-doc-utils >= 0.3.2
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gedit-devel >= %gedit_ver

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

This package contains gedit-latex is a plugin that provides features to
ease the edition of latex documents.

%prep
%setup -q -n %_name-%version

%build
%configure \
    --disable-static \
    --disable-schemas-compile

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang --with-gnome %_name

%files -f %_name.lang
%gedit_pluginsdir/latex.plugin
%dir %gedit_pluginsdir/latex/
%gedit_pluginsdir/latex/*
%_datadir/gedit/plugins/*
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml

%changelog
* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- first build for Sisyphus


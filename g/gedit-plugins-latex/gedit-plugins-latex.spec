%define _name gedit-latex
%define ver_major 3.20
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins-latex
Version: %ver_major.0
Release: alt1

Summary: LATEX plugin for GEdit
License: GPLv3
Group: Editors
Url: https://wiki.gnome.org/Apps/Gedit/LaTeXPlugin

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

# use python3
AutoReqProv: nopython
%define __python %nil
%define  gedit_pluginsdir %_libdir/gedit/plugins
%add_python3_path %gedit_pluginsdir

%define glib_ver 2.28.0
%define gtk_ver 3.3.15
%define gedit_ver 3.20.0

Requires: gedit >= %gedit_ver

BuildPreReq: rpm-build-gnome >= 0.6 rpm-build-python3

BuildPreReq: intltool >= 0.35.0
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gedit-devel >= %gedit_ver

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

This package contains gedit-latex is a plugin that provides features to
ease the edition of latex documents.

%prep
%setup -n %_name-%version

%build
%configure \
    --disable-static \
    --disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name

%files -f %_name.lang
%gedit_pluginsdir/latex.plugin
%dir %gedit_pluginsdir/latex/
%gedit_pluginsdir/latex/*
%_datadir/gedit/plugins/*
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml

%changelog
* Mon May 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- first build for Sisyphus


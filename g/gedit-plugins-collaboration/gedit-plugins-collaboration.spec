%define _name gedit-collaboration
%define ver_major 3.4
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins-collaboration
Version: %ver_major.0
Release: alt1

Summary: Collaboration plugin for GEdit
License: GPL
Group: Editors
Url: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.xz

# From configure.in
%define glib_ver 2.28.0
%define gtk_ver 3.3.15
%define gedit_ver 3.0.0
%define infinity_ver 0.5

BuildPreReq: rpm-build-gnome >= 0.6

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gnome-doc-utils >= 0.3.2
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gedit-devel >= %gedit_ver
BuildPreReq: libinfinity-gtk3-devel >= %infinity_ver

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

This package provides plugin support for collaborative editing in gedit.
It uses libinfinity %infinity_ver and should work with any infinote
%infinity_ver server.

Once installed and activated, you can use the side pane to view remote
servers with shared documents.


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
%gedit_pluginsdir/collaboration.plugin
%gedit_pluginsdir/libcollaboration.so
%_datadir/gedit/plugins/*
%config %_datadir/glib-2.0/schemas/org.gnome.gedit.plugins.collaboration.gschema.xml

%exclude %gedit_pluginsdir/*.la

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus


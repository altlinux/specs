%define _name gedit-cossa
%define ver_major 3.2
%define gedit_pluginsdir %_libdir/gedit/plugins

Name: gedit-plugins-cossa
Version: %ver_major.0
Release: alt2

Summary: GTK+3 themes previewer for GEdit
License: GPL
Group: Editors
Url: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar

# From configure.in
%define glib_ver 2.28.0
%define gtk_ver 3.2.0
%define gedit_ver 3.0.0

BuildPreReq: rpm-build-gnome >= 0.6

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gnome-doc-utils >= 0.3.2
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gedit-devel >= %gedit_ver
BuildRequires: gnome-common

%description
gEdit is a small but powerful text editor designed expressly for GNOME.

Cossa is a CSS previewer for GTK+3 themes, integrating with Gedit so
the edited CSS is promptly visible in the various samples. Cossa may
be easily extended with more samples and allows zooming these to help
get the tiny details right.


%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure \
    --disable-static

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang --with-gnome %_name


%files -f %_name.lang
%_bindir/cossa-standalone-previewer
%gedit_pluginsdir/cossa.plugin
%gedit_pluginsdir/libcossa.so*
%_datadir/gedit/plugins/*

%exclude %gedit_pluginsdir/*.la

%changelog
* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git (31973a3)

* Sun Nov 13 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus


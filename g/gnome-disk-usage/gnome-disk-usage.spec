%define _name baobab
%define ver_major 3.6
%set_typelibdir %_libdir/%_name/girepository-1.0

Name: gnome-disk-usage
Version: %ver_major.3
Release: alt1

Summary: The GNOME disk usage analyser.
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/projects/Baobab

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.xz

Provides: baobab = %version-%release

%define gtk_ver 3.5.9
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: rpm-build-gnome intltool yelp-tools itstool xmllint
BuildRequires: vala-tools gobject-introspection-devel libgtk+3-gir-devel

%description
Baobab is a graphical tool to analyse disk usage in local and remote
filesystems.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

pushd %buildroot%_bindir
ln -s baobab gnome-disk-usage
popd

%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_bindir/gnome-disk-usage
%_desktopdir/%_name.desktop
%_iconsdir/hicolor/*/apps/%_name.*
%_iconsdir/hicolor/scalable/actions/*.svg
%_man1dir/%_name.1.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml

%changelog
* Thu Nov 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Apr 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Feb 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2


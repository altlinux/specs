%define _unpackaged_files_terminate_build 1

%define _name baobab
%define __name org.gnome.baobab
%define ver_major 3.26
%set_typelibdir %_libdir/%_name/girepository-1.0

Name: gnome-disk-usage
Version: %ver_major.1
Release: alt2

Summary: The GNOME disk usage analyser.
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Baobab

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

Provides: baobab = %version-%release

%define gtk_ver 3.20.0
%define vala_ver 0.23.3
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: rpm-build-gnome yelp-tools itstool xmllint libappstream-glib-devel
BuildRequires: vala-tools >= %vala_ver gobject-introspection-devel libgtk+3-gir-devel

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
%_desktopdir/%__name.desktop
%_iconsdir/hicolor/*/apps/%_name.*
%_iconsdir/hicolor/scalable/apps/%_name-symbolic.svg
%_man1dir/%_name.1.*
%_datadir/dbus-1/services/%__name.service
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/metainfo/%__name.appdata.xml

%changelog
* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt2
- fixed %%files section

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Oct 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Sep 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.90-alt1
- 3.17.90

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Jan 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

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


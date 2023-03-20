%define _unpackaged_files_terminate_build 1

%define _name baobab
%define xdg_name org.gnome.baobab
%define ver_major 44
%define beta %nil
%set_typelibdir %_libdir/%_name/girepository-1.0

Name: gnome-disk-usage
Version: %ver_major.0
Release: alt1%beta

Summary: The GNOME disk usage analyser.
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Baobab

Source: %gnome_ftp/%_name/%ver_major/%_name-%version%beta.tar.xz

Provides: baobab = %version-%release

%define gtk4_ver 4.4.0
%define vala_ver 0.23.3
%define adwaita_ver 1.2

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: yelp-tools xmllint libappstream-glib-devel
BuildRequires: vala-tools >= %vala_ver gobject-introspection-devel libgtk4-gir-devel

%description
Baobab is a graphical tool to analyse disk usage in local and remote
filesystems.

%prep
%setup -n %_name-%version%beta

%build
%meson
%meson_build

%install
%meson_install

pushd %buildroot%_bindir
ln -s baobab gnome-disk-usage
popd

%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_bindir/gnome-disk-usage
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_man1dir/%_name.1.*
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* NEWS

%changelog
* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc (ported to GTK4)

* Tue Sep 21 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Jul 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.35.2-alt1
- 3.35.2

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.35.1-alt1
- 3.35.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

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


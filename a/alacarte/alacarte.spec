%define ver_major 3.50

Name: alacarte
Version: %ver_major.0
Release: alt1

Summary: Menu editor for GNOME
License: LGPL-2.0
Group: Graphical desktop/GNOME
Url: https://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

%define menus_ver 3.5.3

Requires: typelib(Gtk) = 3.0

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: libgnome-menus-devel >= %menus_ver
BuildRequires: python3-module-pygobject3-devel
BuildRequires: docbook-dtds docbook-style-xsl xsltproc

%description
Alacarte is a menu editor for GNOME using the freedesktop.org menu
specification.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%python3_sitelibdir_noarch/Alacarte/
%_bindir/*
%_datadir/applications/*
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/%name.1.*
%doc README* AUTHORS NEWS

%changelog
* Sat Sep 23 2023 Yuri N. Sedunov <aris@altlinux.org> 3.50.0-alt1
- 3.50.0

* Tue Jul 11 2023 Yuri N. Sedunov <aris@altlinux.org> 3.44.3-alt1
- 3.44.3

* Sat Jun 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.2-alt1
- 3.44.2

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.1-alt1
- 3.44.1

* Tue Nov 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Thu Mar 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Mar 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.91-alt1
- 3.11.91

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- 3.7.90

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Sun Sep 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.5-alt1
- 3.5.5

* Fri Jun 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4
- removed XFCE specific patches

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.2-alt2.1
- Rebuild with Python-2.7

* Tue Sep 20 2011 Mikhail Efremov <sem@altlinux.org> 0.13.2-alt2
- Make alacarte able to work in Xfce (closes: #26344).

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt2
- build as noarch

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Mon May 04 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Sun Mar 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.11.10-alt1
- 0.11.10
- removed obsolete %%{update,clean}_menus
- removed unneeded icons
- updated {build,}reqs

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11.6-alt1
- 0.11.6

* Thu Aug 07 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11.5-alt3
- remove noarch

* Sun Aug 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11.5-alt1
- Initial build for ALTLinux


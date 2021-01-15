%define ver_major 0.21
%define gegl_ver_major 0.4

Name: dibuja
Version: %ver_major.12
Release: alt1

Summary: Gtk based basic paint program
License: GPLv3
Group: Graphics
Url: https://launchpad.net/%name

Source: %url/trunk/%version/+download/%name-%version.tar.gz

BuildRequires: gcc-c++ libgtk+2-devel libgegl-devel >= %gegl_ver_major
BuildRequires: libexiv2-devel

%description
Dibuja is a program for quick small editing and drawing.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/gegl-%gegl_ver_major/*.so
%_desktopdir/%name.desktop
%_datadir/%name/
%_defaultdocdir/%name/
%_datadir/pixmaps/%name.*
%doc README

%exclude %_libdir/gegl-%gegl_ver_major/*.la


%changelog
* Fri Jan 15 2021 Yuri N. Sedunov <aris@altlinux.org> 0.21.12-alt1
- 0.21.12

* Mon Jun 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Fri Mar 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Jan 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sun Apr 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- fixed docdir

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus


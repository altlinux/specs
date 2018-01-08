%define ver_major 0.6
%define gegl_ver_major 0.3

Name: dibuja
Version: %ver_major.0
Release: alt1

Summary: Gtk based basic paint program
License: GPLv3
Group: Graphics
Url: https://launchpad.net/%name

Source: %url/trunk/%version/+download/%name-%version.tar.gz

BuildRequires: intltool libgtk+2-devel libgegl%gegl_ver_major-devel

%description
Dibuja is a program for quick small editing and drawing.

%prep
%setup

%build
%configure --with-gegl-%gegl_ver_major
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
* Mon Jan 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sun Apr 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- fixed docdir

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus


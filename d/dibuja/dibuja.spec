%define ver_major 0.2
Name: dibuja
Version: %ver_major.1
Release: alt2

Summary: Gtk based basic paint program
License: GPLv3
Group: Graphics
Url: https://launchpad.net/%name

Source: %url/trunk/%version/+download/%name-%version.tar.gz

BuildRequires: intltool libgtk+2-devel libgegl-devel

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
%_libdir/gegl-0.2/*.so
%_desktopdir/%name.desktop
%_datadir/%name/
%_defaultdocdir/%name/
%_datadir/pixmaps/dibuja.*

%exclude %_libdir/gegl-0.2/*.la


%changelog
* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- fixed docdir

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus


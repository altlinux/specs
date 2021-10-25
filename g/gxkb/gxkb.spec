Name: gxkb
Version: 0.9.3
Release: alt1

Summary: X11 keyboard indicator and switcher
License: GPL-2.0
Group: System/X11
Url: http://sourceforge.net/projects/%name/

Source: http://download.sourceforge.net/%name/%name-%version.tar.gz

Requires: setxkbmap

BuildRequires: libgtk+3-devel libxklavier-devel libwnck3-devel

%description
GXKB shows a flag of current keyboard in a systray area and allows you to
switch to another one. It's written in C and uses the GTK library.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_datadir/pixmaps/%name.xpm
%_man1dir/%name.1.*
%doc README* doc/AUTHORS doc/NEWS

%changelog
* Mon Oct 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed May 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Sun Apr 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Wed Dec 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0 (ported to GTK3)

* Wed Jul 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Sat Jan 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sun Aug 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sat Mar 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.9-alt1
- 0.7.9

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.8-alt1
- 0.7.8

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt1
- 0.7.6

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- first build for Sisyphus


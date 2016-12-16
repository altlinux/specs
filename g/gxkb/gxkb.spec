Name: gxkb
Version: 0.7.8
Release: alt1

Summary: Keyboard indicator and switcher
License: GPLv2
Group: System/X11
Url: http://sourceforge.net/projects/%name/

Source: http://download.sourceforge.net/%name/%name-%version.tar.gz

BuildRequires: libgtk+2-devel libxklavier-devel libwnck-devel

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
%doc doc/AUTHORS doc/NEWS

%changelog
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


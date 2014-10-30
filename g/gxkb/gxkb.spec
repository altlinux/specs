Name: gxkb
Version: 0.7.3
Release: alt1

Summary: Keyboard indicator and switcher
License: GPLv2
Group: System/X11
Url: http://sourceforge.net/projects/%name/

Source: http://sourceforge.net/projects/%name/files/%name-%version.tar.gz

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
install -pD -m644 debian/%name.desktop %buildroot%_desktopdir/%name.desktop
install -pD -m644 debian/%name.xpm %buildroot%_datadir/pixmaps/%name.xpm

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_datadir/pixmaps/%name.xpm
%doc AUTHORS NEWS

%changelog
* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- first build for Sisyphus


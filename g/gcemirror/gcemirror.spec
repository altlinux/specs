Name: gcemirror
Version: 0.2
Release: alt2
Packager: Mobile Development Team <mobile@packages.altlinux.org>
Summary: GTK remote viewer for synCE
License: Freeware
Group: Networking/Remote access

Url: http://synce.sourceforge.net
Source: %name-%version.tar.gz

BuildRequires: intltool xorg-xproto-devel
BuildRequires: libgtk+2-devel >= 2.14
BuildRequires: libsynce-devel
BuildRequires: librapi-devel >= 0.13

%description
A GTK based remote viewer and controller, in the vein of VNC. 

The display of the Windows CE device is captured and transfered
to the desktop where it gets displayed in a window. The user now
can interact via this windows by using the mouse and the keyboard
of the desktop.

%prep
%setup -q

%build
%configure --disable-static

%make_build

%install
%make DESTDIR=%buildroot install
%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog
%_bindir/*
%_man1dir/*
%_datadir/synce/screensnap.exe.*

%changelog
* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt2
- rebuild

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- 0.2

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- built for ALT Linux

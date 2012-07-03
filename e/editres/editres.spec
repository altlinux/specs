Name: editres
Version: 1.0.5
Release: alt1.1

Summary: a dynamic resource editor for X Toolkit applications
License: MIT/X11
Group: System/X11

Url: http://cgit.freedesktop.org/xorg/app/editres/
Source: %name-%version.tar.bz2

# Doesn't build withouth this
# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
Editres is a tool that allows users and application developers to view the full widget hierarchy of any X Toolkit application that speaks the Editres protocol. In addition, editres will help the user construct resource specifications, allow the user to apply the resource to the application and view the results dynamically. Once the user is happy with a resource specification editres will append the resource string to the user's X Resources file.

%prep
%setup -q

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc ChangeLog AUTHORS README
%_bindir/*
%_man1dir/*
%_x11appconfdir/*

%changelog
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Fri Sep 24 2010 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Fri Nov 21 2008 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up
- sync with upstream up to aw7 downgrade patch

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- XOrg7 initial build


Name: xedit
Version: 1.2.0
Release: alt1

Summary: Simple text editor for X
License: MIT/X11
Group: Editors

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: xorg-proto-devel xorg-util-macros

# Automatically added by buildreq on Fri Mar 06 2009
BuildRequires: libXaw-devel

%description
Simple text editor for X

%prep
%setup -q

%build
%autoreconf
%configure --disable-xprint

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc ChangeLog AUTHORS README
%_bindir/*
%_man1dir/*
%_x11appconfdir/*
%dir %_x11x11libdir/%name
%_x11x11libdir/%name/*

%changelog
* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Sat Mar 07 2009 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Initial build from scratch


Name: mobile-broadband-provider-info
Version: 20120614
Release: alt1

Summary: Mobile Broadband Service Provider Database
License: Creative Commons Public Domain
Group: System/Configuration/Networking
Packager: Yuri N. Sedunov <aris@altlinux.org>

BuildArch: noarch

Url: http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
# http://svn.gnome.org/viewvc/mobile-broadband-provider-info
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%version/%name-%version.tar.xz

%description
This package contains mobile broadband settings for different service providers
in different countries.

%prep
%setup -q
subst 's@$(libdir)/pkgconfig@%_datadir/pkgconfig@' Makefile*

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_datadir/%name
%_datadir/pkgconfig/*
%doc ChangeLog COPYING NEWS README

%changelog
* Thu Jun 14 2012 Yuri N. Sedunov <aris@altlinux.org> 20120614-alt1
- updated to 20120614 ftp release

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 20110511-alt1
- updated to 20110511 ftp release

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 20110218-alt1
- updated to 20110218 ftp release

* Mon May 10 2010 Yuri N. Sedunov <aris@altlinux.org> 20100510-alt1
- updated to 20100510 ftp release

* Sat Jan 23 2010 Yuri N. Sedunov <aris@altlinux.org> 20100122-alt1
- updated to 20100122 ftp release

* Sat Sep 19 2009 Yuri N. Sedunov <aris@altlinux.org> 20090918-alt1
- updated to 20090918 ftp release

* Tue Jul 07 2009 Yuri N. Sedunov <aris@altlinux.org> 20090707-alt1
- updated to 20090707 ftp release
- changed source url

* Tue Apr 21 2009 Yuri N. Sedunov <aris@altlinux.org> 20090309-alt1
- updated to current rev. 95 (ALT#19711)

* Thu Sep 04 2008 Yuri N. Sedunov <aris@altlinux.org> 20080822-alt1.1
- move *.pc to %%_datadir/pkgconfig

* Thu Sep 04 2008 Yuri N. Sedunov <aris@altlinux.org> 20080822-alt1
- first build for Sisyphus.

%define xorgver 7.6
%define xf86 XFree86

%def_disable pdf
%def_disable txt
%def_disable html
%def_disable ps

Name: xorg-docs
Version: 1.7
Release: alt1
Serial: 1
Summary: Documentation on various X11 programming interfaces
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

Provides: %xf86-doc = 4.4 xorg-x11-doc = %xorgver
Obsoletes: %xf86-doc xorg-x11-doc

BuildArch: noarch

BuildRequires: docbook-utils docbook-utils-print xorg-sgml-doctools xorg-util-macros

%description
xorg-x11-doc provides a great deal of extensive PostScript documentation
on the various X APIs, libraries, and other interfaces.  If you need
low level X documentation, you will find it here.  Topics include the
X protocol, the ICCCM window manager standard, ICE session management,
the font server API, etc.

%prep
%setup

%build
%autoreconf
%configure \
	--build=%_arch-alt-linux \
	--host=%_arch-alt-linux \
	--enable-man \
	%{subst_enable pdf} \
	%{subst_enable txt} \
	%{subst_enable html} \
	%{subst_enable ps} \
	--with-x11docdir=%_docdir/%name-%version
%make

%install
%make DESTDIR=%buildroot install

%files
%doc %_docdir/%name
%_man7dir/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1:1.7-alt1
- Autobuild version bump to 1.7

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1:1.6.99.901-alt1
- Autobuild version bump to 1.6.99.901

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1:1.6-alt1
- Autobuild version bump to 1.6

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1:1.4-alt2.1
- Automatic buildreqfix
- Autobuild watchfile added

* Wed Jul 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4-alt2
- GIT snapshot 2007-05-30
- rename security.7 to xsecurity.7

* Wed Jan 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.4-alt1
- 1.4

* Wed Nov 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3-alt1
- 1.3

* Tue May 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2-alt1
- Xorg-7.1

* Fri Dec 30 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0


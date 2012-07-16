Name: printoxx
Version: 2.8.1
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Software for digital image printing
License: GPLv2+
Group: Graphics

Url: http://kornelix.squarespace.com/printoxx/
Source: http://kornelix.squarespace.com/storage/downloads/printoxx-%version.tar.gz
Source1: printoxx.desktop
Source2: printoxx16.png
Source3: printoxx32.png
Patch: printoxx-asneeded.patch
Patch1: printoxx-2.8.1-alt-glib2.patch

# Automatically added by buildreq on Wed Jul 01 2009
BuildRequires: gcc-c++ libgtk+2-devel

%description
Printoxx is a free open source Linux program for printing one or more image
files with a user-defined page layout. Images can be added to a layout page
using the mouse to select and drop into place. Images can be moved around and
resized using the mouse. Adding text (titles, notes) works the same way. Any
font can be used.

%prep
%setup
%patch -p1
%patch1 -p2

%build
%define _optlevel 3
subst 's/-O3 /%optflags /; s/@g++/g++/' Makefile
%make_build PREFIX=/usr DOCDIR=%_datadir/printoxx/doc

%install
%make_install PREFIX=/usr DOCDIR=%_datadir/printoxx/doc DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/printoxx.desktop
install -pD -m644 icons/printoxx.png %buildroot%_pixmapsdir/printoxx.png
install -pD -m644 icons/printoxx.png %buildroot%_liconsdir/printoxx.png
install -pD -m644 %_sourcedir/printoxx16.png %buildroot%_miconsdir/printoxx.png
install -pD -m644 %_sourcedir/printoxx32.png %buildroot%_niconsdir/printoxx.png
install -pD -m644 doc/printoxx.man %buildroot%_man1dir/printoxx.1

%files
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_datadir/printoxx
%_man1dir/*

%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt1.1
- Fixed build

* Mon Aug 30 2010 Victor Forsiuk <force@altlinux.org> 2.8.1-alt1
- 2.8.1

* Thu Aug 26 2010 Victor Forsiuk <force@altlinux.org> 2.8-alt1
- 2.8
- Install manpage.

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 2.7-alt1
- 2.7

* Thu Mar 25 2010 Victor Forsiuk <force@altlinux.org> 2.5-alt1
- 2.5

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 2.4-alt1
- 2.4

* Tue Feb 16 2010 Victor Forsiuk <force@altlinux.org> 2.3.1-alt1
- 2.3.1

* Mon Feb 08 2010 Victor Forsiuk <force@altlinux.org> 2.3-alt1
- 2.3

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Jul 01 2009 Victor Forsyuk <force@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Mar 10 2009 Victor Forsyuk <force@altlinux.org> 1.9.1-alt1
- 1.9.1

* Mon Jan 12 2009 Victor Forsyuk <force@altlinux.org> 1.8-alt1
- 1.8

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 1.7.1-alt1
- 1.7.1

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 1.6-alt1
- 1.6

* Tue Sep 23 2008 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Sep 15 2008 Victor Forsyuk <force@altlinux.org> 1.3.2-alt1
- 1.3.2

* Mon Sep 01 2008 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- Initial build.

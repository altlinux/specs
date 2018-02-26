Name: dvdisaster
Version: 0.72.3
Release: alt2

Summary: Additional error protection for CD/DVD media
License: GPLv2+
Group: File tools

URL: http://www.dvdisaster.com/
Source: http://dvdisaster.net/downloads/dvdisaster-%version.tar.bz2
Source1: dvdisaster.desktop

# Automatically added by buildreq on Tue Mar 08 2011
BuildRequires: bzlib-devel libgtk+2-devel libpng-devel

Requires: %name-help = %version
BuildRequires: desktop-file-utils

%description
dvdisaster provides a margin of safety against data loss on CD and DVD media
caused by aging or scratches. It creates error correction data, which is used
to recover unreadable sectors if the disc becomes damaged at a later time.

%package help
Summary: Help files for %name
Group: File tools
BuildArch: noarch

%description help
Help files for %name.

%prep
%setup

subst 's/\@\$/\$/' GNUmakefile.template
subst 's/-O2/%optflags/' configure

subst 's~glib/gstrfuncs.h~glib.h~' memtrack.c dvdisaster.h

%build
./configure --prefix=/usr --with-embedded-src-path=no --docdir=%_docdir --with-nls=yes
%make_build

%install
%make_install install \
	BUILDROOT=%buildroot LOCALEDIR=%_prefix/share/locale MANDIR=%_mandir

rm -f %buildroot%_bindir/dvdisaster-uninstall.sh
install -pD -m644 contrib/dvdisaster16.png %buildroot%_miconsdir/dvdisaster.png
install -pD -m644 contrib/dvdisaster32.png %buildroot%_niconsdir/dvdisaster.png
install -pD -m644 contrib/dvdisaster48.png %buildroot%_liconsdir/dvdisaster.png
install -pD -m644 contrib/dvdisaster48.png %buildroot%_pixmapsdir/dvdisaster.png
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/dvdisaster.desktop

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--remove-category=Utility \
	--remove-category=Archiving \
	--add-category=AudioVideo \
	--add-category=DiscBurning \
	%buildroot%_desktopdir/dvdisaster.desktop

%files -f %name.lang
%_bindir/dvdisaster
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_desktopdir/*
%_man1dir/*
%lang(de) %_mandir/de/man1/*
%lang(it) %_mandir/it/man1/*
%lang(cs) %_mandir/cs/man1/*

%files help
# Do not remove docs below - documentation accessed from GUI!
#%doc documentation/en documentation/images
# file COPYING accessed from Help->License menu item in GUI, so we package it
#%doc COPYING
%_defaultdocdir/dvdisaster-%version

%changelog
* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 0.72.3-alt2
- Fix glib include compile problem.

* Tue Dec 13 2011 Victor Forsiuk <force@altlinux.org> 0.72.3-alt1
- 0.72.3

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.72.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for dvdisaster

* Tue Mar 08 2011 Victor Forsiuk <force@altlinux.org> 0.72.1-alt2
- Refresh BuildRequires.

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 0.72.1-alt1
- 0.72.1
- Split big help files to noarch package to save bandwidth and repo space.

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.72-alt1
- 0.72

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 0.72-alt0.1.rc1
- 0.72 rc1.

* Tue Jan 20 2009 Victor Forsyuk <force@altlinux.org> 0.70.6-alt2
- Remove obsolete install time scripts.

* Sat Mar 29 2008 Victor Forsyuk <force@altlinux.org> 0.70.6-alt1
- 0.70.6

* Fri Feb 29 2008 Victor Forsyuk <force@altlinux.org> 0.70.5-alt1
- 0.70.5

* Mon Feb 05 2007 Victor Forsyuk <force@altlinux.org> 0.70.4-alt1
- 0.70.4

* Tue Dec 12 2006 Victor Forsyuk <force@altlinux.org> 0.70.3-alt1
- 0.70.3

* Tue Oct 24 2006 Victor Forsyuk <force@altlinux.org> 0.70.2-alt1
- 0.70.2

* Fri Jul 28 2006 Victor Forsyuk <force@altlinux.ru> 0.70-alt1
- 0.70

* Wed Apr 05 2006 Victor Forsyuk <force@altlinux.ru> 0.66-alt1
- 0.66
- Refresh build requirements.

* Tue Jan 17 2006 Victor Forsyuk <force@altlinux.ru> 0.65-alt1
- 0.65
- Fixed GUI help items access.

* Fri Aug 26 2005 Victor Forsyuk <force@altlinux.ru> 0.63-alt1
- 0.63
- Build with NLS messages.

* Mon Jul 11 2005 Victor Forsyuk <force@altlinux.ru> 0.62-alt1
- 0.62

* Mon Apr 25 2005 Victor Forsyuk <force@altlinux.ru> 0.61-alt1
- 0.61

* Tue Apr 12 2005 Victor Forsyuk <force@altlinux.ru> 0.60-alt1
- Initial build for Sisyphus.

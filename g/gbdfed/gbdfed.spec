Name: gbdfed
Version: 1.6
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A BDF font editor that can import/export other font formats
License: Freely distributable
Group: Publishing

URL: http://www.math.nmsu.edu/~mleisher/Software/gbdfed
Source: %url/gbdfed-%version.tbz2
Source1: gbdfed.desktop
Source2: gbdfed16x16.png
Source3: gbdfed32x32.png
Source4: gbdfed48x48.png

# Automatically added by buildreq on Tue Oct 19 2010
BuildRequires: imake libICE-devel libgtk+2-devel xorg-cf-files

%description
gbdfed lets you interactively create new bitmap font files or modify existing
ones. It allows editing multiple fonts and multiple glyphs, it allows cut and
paste operations between fonts and glyphs and editing font properties. The
editor works natively with BDF fonts.

%prep
%setup

subst 's/getline/get_line/g' bdfgname.c
subst 's/-DG.K_DISABLE_DEPRECATED//' Makefile.in

%build
%configure
%make_build

%install
%makeinstall_std

install -pD -m644 %_sourcedir/gbdfed.desktop %buildroot%_desktopdir/gbdfed.desktop
install -pD -m644 %_sourcedir/gbdfed16x16.png %buildroot%_miconsdir/gbdfed.png
install -pD -m644 %_sourcedir/gbdfed32x32.png %buildroot%_niconsdir/gbdfed.png
install -pD -m644 %_sourcedir/gbdfed48x48.png %buildroot%_liconsdir/gbdfed.png

%files
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*

%changelog
* Tue Oct 19 2010 Victor Forsiuk <force@altlinux.org> 1.6-alt2
- Remove GDK_DISABLE_DEPRECATED and GTK_DISABLE_DEPRECATED to allow
  build with recent libgtk+ (2.22).

* Fri Jun 11 2010 Victor Forsiuk <force@altlinux.org> 1.6-alt1
- 1.6 (fixed FTBFS with GTK+ 2.20).

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 1.5-alt2
- Fix FTBFS due to conflicting declarations.

* Tue Mar 10 2009 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- 1.5

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt2
- Remove obsolete install time scripts.

* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt1
- 1.4

* Mon Oct 15 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt2
- Fix FTBFS with libgtk+ 2.11+ due to added deprecation guards in filesel.h.

* Mon May 14 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt1
- 1.3

* Wed Nov 22 2006 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- 1.2

* Tue Sep 26 2006 Victor Forsyuk <force@altlinux.ru> 1.1-alt1
- 1.1
- Refreshed build requirements.
- Switch menu to freedesktop style.
- Add application icon.

* Thu Jan 19 2006 Victor Forsyuk <force@altlinux.ru> 1.0-alt1
- Initial build.

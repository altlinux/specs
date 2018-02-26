Name: xbanner
Version: 1.31
Release: alt1
Epoch: 1

Summary: A program for customizing the look of the standard XDM interface
License: GPLv2+
Group: Graphical desktop/Other
Url: http://www.spade.com/linux/XBanner/
Packager: Stanislav Ievlev <inger@altlinux.ru>

#Source: ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner1.31.tar.bz2
Source: XBanner1.31.tar
Source1: xbanner.defaults
Source2: xbanner.man

Patch: xbanner-1.31-deb-alt.patch

# Automatically added by buildreq on Wed Apr 23 2008
BuildRequires: imake libX11-devel xorg-cf-files

%description
The XBanner program allows the display of text, patterns and images
in the root window, so users can customize the XDM style login screen
and/or the normal X background.

Install XBanner if you'd like to change the look of your X login screen
and/or X background.

%prep
%setup -q -n XBanner%version
%patch -p1
install -pm644 %_sourcedir/xbanner.{defaults,man} .

%build
xmkmf -a
sed -i 's|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = %optflags|' Makefile
sed -i 's|CDEBUGFLAGS = .*|CDEBUGFLAGS = %optflags|' Makefile
make CFLAGS="%optflags" BINDIR=%_bindir XLIBDIR=%_libdir

%install
%make_install install install.man DESTDIR=%buildroot

%files
%_bindir/*
%_man1dir/*
%config(noreplace) %_x11appconfdir/*
%doc *.xpm samples docs/*

%changelog
* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.31-alt1
- Merged fixes from Debian xbanner package.
- Updated release numbering.

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 1.31-ipl17mdk
- rebuild with gcc3

* Mon Mar 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.31-ipl16mdk
- Rebuilt
- Cleanup specfile
- Change default resource file

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.31-14mdk
- automatically added BuildRequires

* Mon May 15 2000 David BAUDENS <baudens@mandrakesoft.com> 1.31-13mdk
- Fix build for i486
- Use %%{_tmppath} for BuildRoot

* Mon Mar 27 2000 DindinX <odin@mandrakesoft.com> 1.31-12mdk
- Fix config, group and other specs goodies

* Fri Jan 28 2000 Francis Galiegue <francis@mandrakesoft.com>
- Added %%defattr

* Wed Jan 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31-10mdk
- Fix build as non root.

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environment

* Tue Apr 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix bug with the xdm_bg reference in ad files.

* Wed Apr 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adtations.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Wed Jan 27 1999 Preston Brown <pbrown@redhat.com>
- removed shadow-penguin thingie, replaced with real shadowman (tm reasons)
- cleanups

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- cleaned up spec, built for 5.2

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

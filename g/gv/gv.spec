Name: gv
Version: 3.7.3
Release: alt1
Serial: 1

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: An enhanced front-end for the ghostscript PostScript(TM) interpreter
License: GPL
Group: Publishing
Url: http://www.gnu.org/software/gv/

Source: http://ftp.gnu.org/gnu/gv/%{name}-%{version}.tar.bz2

Source100: %name.png
Source101: gvcat

Requires: ghostscript-module-X >= 7.05
Provides: ghostview = %version
Obsoletes: ghostview
Requires: file

# Automatically added by buildreq on Sun Mar 27 2011 (-bi)
# optimized out: elfutils fontconfig glibc-pthread libICE-devel libSM-devel libX11-devel libXext-devel libXt-devel xorg-xproto-devel
BuildRequires: ImageMagick-tools bzlib-devel flex imake libXaw3d-devel libXinerama-devel libXmu-devel libXpm-devel xorg-cf-files zlib-devel

%description
Gv provides a user interface for the ghostscript PostScript(TM)
interpreter.  Derived from the ghostview program, %name can display
PostScript and PDF documents using the X Window System.

Install the %name package if you'd like to view PostScript and PDF documents
on your system.  You'll also need to have the ghostscript package
installed, as well as the X Window System.

%prep
%setup -q

find -type f -print0 |
	xargs -r0 %__grep -FZl 'gzip -d -c' |
	xargs -r0 %__subst 's|gzip -d -c|%_datadir/%name/gvcat|g'

find -type f -print0 |
	xargs -r0 %__grep -FZl 'gzipped, zipped or compressed' |
	xargs -r0 %__subst 's/gzipped, zipped or compressed/gzipped, bzipped, zipped or compressed/g'

find -type f -print0|
	xargs -r0 %__grep -FZl 'GraphicsAlphaBits' |
	xargs -r0 %__subst 's/-dGraphicsAlphaBits=2/-dGraphicsAlphaBits=4/g'

%build
%configure --with-scratch-dir=~/tmp/
## --enable-scrollbar-code
%make

%install
%__mkdir_p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir,%_datadir/%name,%_x11bindir,%_sysconfdir/X11/app-defaults/}
%makeinstall

install -m644 %SOURCE100 -D %buildroot%_liconsdir/gv.png
convert -geometry 32x32 %SOURCE100 %buildroot%_niconsdir/gv.png
convert -geometry 16x16 %SOURCE100 %buildroot%_miconsdir/gv.png

install -p -m755 %SOURCE101 %buildroot%_datadir/%name

%__ln_s -nf %name %buildroot%_x11bindir/ghostview

install -d %buildroot/%_desktopdir
cat > %buildroot/%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Type=Application
Icon=%name
Name=Ghostview
GenericName=PostScript/PDF Viewer
GenericName[ru]=Просмотр файлов PostScript/PDF
MimeType=application/postscript;application/pdf;
Categories=Graphics;Viewer;
StartupWMClass=GV
Exec=gv %%f
EOF

mv %buildroot/%_datadir/%name/GV %buildroot%_sysconfdir/X11/app-defaults/

%files
%doc README
%config(noreplace) %_sysconfdir/X11/app-defaults/GV
%_bindir/*
%_man1dir/*
%_datadir/%name
%_desktopdir/*
%_infodir/*.info*
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png

%changelog
* Fri Feb 17 2012 Vladislav Zavjalov <slazav@altlinux.org> 1:3.7.3-alt1
- 3.7.3

* Mon Oct 03 2011 Vladislav Zavjalov <slazav@altlinux.org> 1:3.7.2-alt1
- 3.7.2

* Sun Mar 27 2011 Vladislav Zavjalov <slazav@altlinux.org> 1:3.7.1-alt3
- update BuildRequires

* Wed Nov 03 2010 Vladislav Zavjalov <slazav@altlinux.org> 1:3.7.1-alt2
- rebuild with set-versioned libXaw3d

* Wed Nov 03 2010 Vladislav Zavjalov <slazav@altlinux.org> 1:3.7.1-alt1
- 3.7.1

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:3.6.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for gv
  * obsolete-call-in-post-install-info for gv
  * update_menus for gv
  * postclean-05-filetriggers for spec file

* Tue Sep 09 2008 Stanislav Ievlev <inger@altlinux.org> 1:3.6.5-alt1
- 3.6.5

* Wed Jul 02 2008 Stanislav Ievlev <inger@altlinux.org> 1:3.6.4-alt1
- 3.6.4
- replace menufile with desktop-file

* Fri Jul 06 2007 Stanislav Ievlev <inger@altlinux.org> 1:3.6.3-alt1
- 3.6.3

* Wed Nov 15 2006 Stanislav Ievlev <inger@altlinux.org> 1:3.6.1-alt4
- fix overflow

* Sat Feb  4 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.6.1-alt3
- rebuilt against new Xaw3d

* Fri May 06 2005 Stanislav Ievlev <inger@altlinux.org> 1:3.6.1-alt2
- don't use broken scrollbar from Xaw3d

* Tue Jan 11 2005 Stanislav Ievlev <inger@altlinux.org> 1:3.6.1-alt1
- 3.6.1

* Mon Apr 26 2004 Stanislav Ievlev <inger@altlinux.org> 1:3.5.8-alt5
- Added missing provides (ghostview = version)
- move app-default samples (%_x11libdir/%name/*.ad) to documentation directory
- fixed #3625

* Fri Oct 11 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.5.8-alt4
- Fixed multiply buffer overflows due to unsafe sscanf() usage.
  Previous (1:3.5.8-alt2) fix appears to be incomplete.

* Fri Sep 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.5.8-alt3
- Added buildrequires.
- Enhanced gvcat helper.
- Fixed tmp handling.
- Additional convention enforcement on patch file names.
- Use subst instead of perl in %%build.

* Mon Sep 23 2002 Stanislav Ievlev <inger@altlinux.ru> 1:3.5.8-alt2
- Fixed multiply buffer overflows due to unsafe sscanf() code.

* Mon Jun 17 2002 AEN <aen@logic.ru> 1:3.5.8-alt1
- requires gs >= 7.05
- alpha patch removed

* Tue Mar 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.5.8-ipl16mdk
- Fixed configuration file attributes.
- Relocated app-defaults.

* Mon Mar 11 2002 Stanislav Ievlev <inger@altlinux.ru> 3.5.8-ipl15mdk
- Rebuilt
- added some patches (quote,alpha,noplatform) to fix some bugs

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.8-ipl14mdk
- Added icons from MDK.
- Updated menu: title and long title.

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.8-ipl13mdk
- Added: bzip2 support.
- RE adaptions.

* Thu Jul 20 2000 Fran�ois Pons <fpons@mandrakesoft.com> 3.5.8-13mdk
- fixed requires to ghostscript-module-X.
- build release.

* Fri May 26 2000 Adam Lebsack <adam@mandrakesoft.com> 3.5.8-12mdk
- Imake bugfix for XFree86-4.0

* Tue Apr 11 2000 Fran�ois Pons <fpons@mandrakesoft.com> 3.5.8-11mdk
- added menu entry and icon.

* Fri Apr 07 2000 Fran�ois Pons <fpons@mandrakesoft.com> 3.5.8-10mdk
- Updated Group.

* Tue Nov 23 1999 Fran�ois PONS <fpons@mandrakesoft.com>
- Build release.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Mon Jan 23 1999 Michael Maher <mike@redhat.com>
- fixed bug #272, changed group

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built pacakge for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- we are installin a symlink to ghostview

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 3.5.8

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 15 1997 Erik Troan <ewt@redhat.com>
- added ghostscript requirement, added errlist patch for glibc.


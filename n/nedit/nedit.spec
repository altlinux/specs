Name: nedit
Version: 5.5
#%%define rc_ver RC2
Release: alt3.qa1
%define srcname %name-%version%{?rc_ver:%rc_ver}%{?!rc_ver:-src}

Summary: A text editor for the X Window System
License: GPL
Group: Editors
Url: http://www.nedit.org/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.nedit.org/pub/NEdit/v5_5/ or ftp://ftp.nedit.org/pub/NEdit/beta/
Source: ftp.nedit.org:/pub/NEdit/v5_5/%srcname.tar
Source1: %name.desktop
Source2: %name-16x16.png
Source3: %name-32x32.png
Source4: %name-48x48.png

Patch1: %name-5.4rc1-alt-makefile.patch
Patch2: %name-5.5-alt-fonts.patch
Patch3: %name-5.5-alt-tmp.patch
Patch4: %name-5.5-varfix.patch
Patch5: %name-5.5-nc-manfix.patch
Patch6: %name-5.5-visfix.patch

# Automatically added by buildreq on Tue May 23 2006
BuildRequires: libX11-devel libXext-devel libXmu-devel libXp-devel openmotif-devel

%description
NEdit is a multi-purpose text editor for the X Window System, which combines a
standard, easy to use, graphical user interface with the thorough functionality
and stability required by users who edit text eighthours a day.  It provides
intensive support for development in a wide variety of languages, text processors,
and other tools, but at the same time can be used productively by just about anyone
who needs to edit text.

%prep
%setup -q %{?rc_ver:-n %srcname}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 
%patch5 -p1

# Change nedit.shell default from /bin/csh to /bin/sh.
find doc -type f -print0 |
	xargs -r0 grep -FZl /bin/csh |
	xargs -r0 subst -p s,/bin/csh,/bin/sh,g --
find -type f -name \*.h -print0 |
	xargs -r0 grep -FZl /bin/csh |
	xargs -r0 subst -p s,/bin/csh,/bin/sh,g --
find -type f -name \*.c -print0 |
	xargs -r0 grep -FZl /bin/csh |
	xargs -r0 subst -p 's,"/bin/csh","/bin/sh",g' --

%build
%add_optflags -DBUILD_UNTESTED_NEDIT -DBUILD_BROKEN_NEDIT
%make_build linux YACC='bison -y'
cp -p doc/nedit.{doc,txt}
bzip2 -9f doc/{faq,nedit}.txt

%install
install -pD -m755 source/%name %buildroot%_bindir/%name
install -pD -m755 source/nc %buildroot%_bindir/nedit-client
install -pD -m644 doc/%name.man %buildroot%_man1dir/%name.1
install -pD -m644 doc/nc.man %buildroot%_man1dir/nedit-client.1
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.png

%files
%_x11bindir/*
%_x11mandir/man?/*
%_desktopdir/%name.desktop
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%doc README ReleaseNotes doc/NEdit.ad doc/*.txt.bz2

%changelog
* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 5.5-alt3.qa1
NMU: converted menu to desktop file

* Thu Jul 01 2010 Anton Farygin <rider@altlinux.ru> 5.5-alt3
- added some fixes from Fedora
- /usr/bin/nc renamed to /usr/bin/nedit-client due to fix for 
  conflict with netcat

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.5-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for nedit
  * postclean-05-filetriggers for spec file

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 5.5-alt2.1
- NMU:
  * updated build dependencies

* Tue May 23 2006 Dmitry V. Levin <ldv@altlinux.org> 5.5-alt2
- Fixed build with new *iconsdir macros.
- Relocated from /usr/X11R6 to /usr.
- Updated build dependencies.

* Mon Mar 14 2005 Dmitry V. Levin <ldv@altlinux.org> 5.5-alt1
- Updated to 5.5 release.
- Updated patches.
- Change nedit.shell default from /bin/csh to /bin/sh.
- Packaged nedit help documentation.

* Wed May 05 2004 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt3
- Rebuilt with openmotif-2.2.3.

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt2
- Updated to 5.4 release.
- Enable build with -Werror.

* Sun Oct 26 2003 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt1RC2
- Updated to 5.4RC2, updated patches.

* Wed Oct 01 2003 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt1RC1
- Updated to 5.4RC1, updated patches.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt2
- Rebuilt in new environment.

* Wed Jun 26 2002 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt1
- 5.3 release, updated icons.

* Fri May 24 2002 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt0.1RC1
- 5.3RC1, updated patches.

* Fri Apr 12 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt3
- Rebuilt with openmotif-2.2.2.

* Fri Mar 15 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt2
- Fixed build.

* Tue Oct 30 2001 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- 5.2, updated patches.

* Fri Oct 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.1.1-ipl13mdk
- Rebuilt with lesstif-0.93.12.

* Wed Mar 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.1.1-ipl12mdk
- Create tmpfiles in more secure way.
- Specfile cleanup.
- Built with openmotif-devel for release.

* Mon Dec 18 2000 AEN <aen@logic.ru>
- build with new Lesstif
- gcc296 patch

* Mon Dec 11 2000 AEN <aen@logic.ru>
- cleanup spec
- fonts patch
- sync with RE

* Mon Oct 02 2000 Daouda Lo <daouda@mandrakesoft.com> 5.1.1-9mdk
- icons should be transparents
- provide large icon
- more macrozif..

* Mon Oct 02 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 5.1.1-8mdk
- Include docs.
- Install man page.
- Include RPM_OPT_FLAGS in CFLAGS.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 5.1.1-7mdk
- automatically added BuildRequires

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.1.1-6mdk
- rebuild it with macros

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 5.1.1-5mdk
- BuildRequires: lesstif-devel
- Use tmppath macros.

* Tue May 09 2000 Daouda Lo <daouda@mandrakesoft.com> 5.1.1-4mdk
- 32x32 icon
- menu entry was messed up in %files section

* Tue Apr 11 2000 Daouda Lo <daouda@mandrakesoft.com> 5.1.1-3mdk
- add icon.

* Thu Apr 06 2000 Daouda Lo <daouda@mandrasoft.com> 5.1.1-1mdk
- first release for Linux Mandrake
- located in Office group

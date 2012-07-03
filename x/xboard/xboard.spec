Name: xboard
Version: 4.5.2
Release: alt1

Summary: An X Window System graphical chessboard
License: GPL
Group: Games/Boards

# git://git.savannah.gnu.org/xboard.git
Url: http://www.gnu.org/software/xboard/
Source0: ftp://ftp.gnu.org/pub/gnu/xboard/%name-%version.tar
Source1: xboard-16x16.png
Source2: xboard-32x32.png
Source3: xboard-48x48.png
Source4: xboard.desktop
Source5: xboard.ad
Packager: Stanislav Ievlev <inger@altlinux.org>

Requires: %name-theme
# xboard 4.4 uses fairymax as default engine,
# special runtime configuration needed for GNU Chess
Requires: fairymax

# Automatically added by buildreq on Sun Oct 11 2009
BuildRequires: flex groff-base imake libXaw-devel libXpm-devel xorg-cf-files

%set_verify_info_method none

%description
Xboard is an X Window System based graphical chessboard which can be
used with the GNUchess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

%package theme-default
Summary: default theme for xboard
Group: Graphics
License: GPL
Provides: %name-theme
Requires: %name
Conflicts: xboard-theme-eyes xboard-theme-fantasy xboard-theme-freak
Conflicts: xboard-theme-prmi xboard-theme-skulls xboard-theme-spatial
BuildArch: noarch

%description theme-default
default theme for xboard

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

#icon
install -Dpm644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -Dpm644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -Dpm644 %SOURCE3 %buildroot%_liconsdir/%name.png
install -Dpm644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
install -Dpm644 %SOURCE5 %buildroot%_sysconfdir/X11/app-defaults/XBoard

#default theme
install -d %buildroot%_datadir/%name/theme
cp -a pixmaps/*.xpm %buildroot%_datadir/%name/theme

%files
%doc AUTHORS COPYING COPYRIGHT ChangeLog* NEWS TODO
%doc FAQ.html README
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%_bindir/*
%_man6dir/*
%_infodir/*.info*
%_desktopdir/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%_iconsdir/*/*/*/*.svg

%files theme-default
%_datadir/%name/theme

%changelog
* Mon Jul 11 2011 Michael Shigorin <mike@altlinux.org> 4.5.2-alt1
- 4.5.2

* Mon Oct 11 2010 Michael Shigorin <mike@altlinux.org> 4.4.4-alt2
- backdating repocop fixup build changelog record

* Sat Oct 09 2010 Michael Shigorin <mike@altlinux.org> 4.4.4-alt1
- 4.4.4
- added an SVG icon
- added formal theme conflicts

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.2.7-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for xboard
  * update_menus for xboard
  * postclean-05-filetriggers for spec file

* Wed Oct 21 2009 Michael Shigorin <mike@altlinux.org> 4.4.1-alt0.2
- require fairymax instead of chess

* Mon Oct 12 2009 Michael Shigorin <mike@altlinux.org> 4.4.1-alt0.1
- NMU: 4.4.1 git snapshot 7734c79f4d6e76e3d80f7ff42aea9e891102bc99
  (as-needed issue fixed upstream, see also savannah bug #27672)
- moved to gear-based build
- updated docs file list

* Sun Oct 11 2009 Michael Shigorin <mike@altlinux.org> 4.4.0-alt1
- NMU: 4.4.0 (closes: #21891)
- fix an --as-needed issue
- theme package made noarch
- disable info verify (breaks package build for no reason)
- drop info patch (merged upstream)
- drop obsolete macros/requires
- spec cleanup
- buildreq

* Mon Oct 29 2007 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt4
- fix requires

* Thu Oct 18 2007 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt3
- add app-defaults file with right defaults
- allow multiple themes now

* Mon Feb 27 2006 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt2
- updated buildreq, fixed icons path

* Tue Jan 27 2004 Stanislav Ievlev <inger@altlinux.org> 4.2.7-alt1
- 4.2.7

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.6-alt2
- rebuild with gcc3

* Mon May 27 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.6-alt1
- 4.2.6

* Tue Sep 11 2001 Sergey V Turchin <zerg@altlinux.ru> 4.2.3-alt2
- fix menu

* Thu Apr 05 2001 Stanislav Ievlev <inger@altlinux.ru> 4.2.3-alt1
- Upgrade to 4.2.3

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Sun Oct 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.1.0-1mdk
- new and shiny source.

* Wed Aug 16 2000 David BAUDENS <baudens@mandrakesoft.com> 4.0.7-5mdk
- Fix menu entry

* Wed Aug 16 2000 Enzo Maggi <enzo@mandrakesoft.com> 4.0.7-4mdk
- Minor bug fix in the spec

* Tue Aug 14 2000 Enzo Maggi <enzo@mandrakesoft.com> 4.0.7-3mdk
- introduced the %_mandir, %_bindir, %_infodir etc.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.7-2mdk
- automatically added BuildRequires

* Thu Jun 13 2000 Florin Grad <florin@mandrakesoft.com> 4.0.7-1mdk
- "new" release

* Fri May 05 2000 Florin Grad <florin@mandrakesoft.com> 4.0.5-2mdk
- fix the menu integration

* Sat Apr 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0.5-1mdk
- Updated to 4.0.5
- New groups
- Added docs
- added menu funtions to spec file

* Fri Nov 12 1999 Damien Kroktine <damien@mandrakesoft.com>
- Mandrake release

* Wed Sep  8 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.3

* Sat Aug 14 1999 Bill Nottingham <notting@redhat.com>
- change requires: to virtual 'chessprogram'

* Thu Aug 12 1999 Bill Nottingham <notting@redhat.com>
- require gnuchess so it will work out of the box

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.2

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file
- built package for 6.0

* Sat Jul 11 1998 Mike Wangsmo <wanger@redhat.com>
- updated to a new version
- buildrooted the package too

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

Name: rogue
Version: 5.4.4
Release: alt1.qa2
Packager: Fr. Br. George <george@altlinux.ru>
Group: Games/Adventure
License: BSD
Url: http://rogue.rogueforge.net
Source0: http://rogue.rogueforge.net/files/rogue5.4/%name%version-src.tar.gz
Source1: %name.desktop
Source2: %name.png

BuildRequires: desktop-file-utils
BuildRequires: ncurses-devel

Summary: The original graphical adventure game

%description
The one, the only, the original graphical adventure game that spawned an entire genre.

Rogue 5.4 was developed between 1983 and 1984. The most common release of 5.4 is found on the BSD 4.3 Unix distribution tape (June 1986) as archived on the CSRG Archives CD Set and only as a binary executable.

This is the final version of the original (Toy, Arnold, Wichman) rogue developed for the UNIX operating system. The source code was recovered by Ken Arnold and posted on Sourceforge which I then copied and restored here. 

%prep
%define _gamesvar %_var/games
%setup -q -c -n %name-%version

%build
%configure --enable-setgid=games --enable-scorefile=%_gamesvar/roguelike/rogue54.scr --enable-lockfile=%_gamesvar/roguelike/rogue54.lck --bindir=%_gamesbindir
make %_smp_mflags

%install
make install DESTDIR=%buildroot

desktop-file-install --dir %buildroot%_desktopdir --vendor "" %SOURCE1
install -p -D -m 644 %SOURCE2 %buildroot%_niconsdir/%name.png

%files
%attr(2711,games,games) %_gamesbindir/%name
%_man6dir/%name.6.gz
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%dir %attr(0775,games,games) %_gamesvar/roguelike
%config(noreplace) %attr(0664,games,games) %_gamesvar/roguelike/rogue54.scr
%doc LICENSE.TXT %name.doc %name.html %name.me

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.4.4-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for rogue
  * update_menus for rogue
  * postclean-05-filetriggers for spec file

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 5.4.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for rogue

* Mon Oct 15 2007 Fr. Br. George <george@altlinux.ru> 5.4.4-alt1
- Version up
- Upstream moved from SF

* Sun Sep 23 2007 Fr. Br. George <george@altlinux.ru> 5.4.2-alt2
- Desktop file fixed

* Sun Jun 17 2007 Fr. Br. George <george@altlinux.ru> 5.4.2-alt1
- Initial build for ALT

* Sat Mar 3 2007 Wart <wart at kobold.org> 5.4.2-8
- Use better sourceforge download url
- Use more precise desktop file categories

* Mon Aug 28 2006 Wart <wart at kobold.org> 5.4.2-7
- Rebuild for Fedora Extras

* Tue May 16 2006 Wart <wart at kobold.org> 5.4.2-6
- Added empty initial scoreboard file.

* Mon May 15 2006 Wart <wart at kobold.org> 5.4.2-5
- Better setuid/setgid handling (again) (BZ #187392)

* Thu Mar 30 2006 Wart <wart at kobold.org> 5.4.2-4
- Better setuid/setgid handling (BZ #187392)
- Resize desktop icon to match directory name

* Mon Mar 13 2006 Wart <wart at kobold.org> 5.4.2-3
- Added icon for .desktop file.

* Sun Mar 12 2006 Wart <wart at kobold.org> 5.4.2-2
- Added missing BR: ncurses-devel, desktop-file-utils

* Sat Feb 25 2006 Wart <wart at kobold.org> 5.4.2-1
- Initial spec file.

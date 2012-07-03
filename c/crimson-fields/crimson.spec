%define sname crimson
Name:		crimson-fields
Version:	0.5.3
Release:	alt1
License:	GPL
Group:		Games/Strategy
URL:		http://crimson.seul.org
Source:		http://crimson.seul.org/files/%{sname}-%{version}.tar.bz2
#Source2: %name.png
Summary:	A hex-based tactical war game
BuildRequires:	libSDL_mixer-devel libSDL-devel libSDL_ttf-devel gcc-c++
Packager: Fr. Br. George <george@altlinux.ru>
Obsoletes:	%sname <= 0.5.2
Conflicts:	%sname <= 0.5.2

%description
Crimson Fields is a tactical war game in the tradition of Battle Isle for
one or two players.

The outcome of the war lies in your hands. You decide which units are
sent to the front lines, and when to unleash the reserves. Your mission
objectives range from defending strategically vital locations to simply
destroying all enemy forces in the area. Protect supply convoys or raid
enemy facilities to uncover technological secrets or fill your storage
bays so you can repair damaged units or build new ones in your own
factories. Lead your troops to victory!

Tools are available to create custom maps and campaigns. You can also play
the original Battle Isle maps if you have a copy of the game.

%prep
%setup -n %sname-%version

%build
%configure --enable-cfed --enable-bi2cf --enable-comet --enable-cf2bmp
%make_build

%install
%makeinstall
install -d %buildroot%_liconsdir/
install -m 644 gfx/%sname.png %buildroot%_liconsdir/

%files 
%doc COPYING NEWS README* THANKS TODO music/COPYING.MUSIC
%_bindir/*
%_datadir/%sname
%_datadir/pixmaps/*
%doc %_mandir/man6/*
%_liconsdir/%sname.png
%_datadir/applications/%sname.desktop

%changelog
* Thu Mar 19 2009 Fr. Br. George <george@altlinux.ru> 0.5.3-alt1
- Version up

* Sun Sep 28 2008 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Version up
- #13199 fix (renamed to crimson-fields)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for crimson

* Tue Oct 16 2007 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Version up
- Upstream moved from SF

* Wed Aug 17 2005 Fr. Br. George <george@altlinux.ru> 0.4.8-alt1
- Upping version

* Mon Feb 07 2005 Fr. Br. George <george@altlinux.ru> 0.4.6-alt1
- Upping version

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.5-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Nov 22 2004 Fr. Br. George <george@altlinux.ru> 0.4.5-alt1
- Minor version upping

* Mon Oct 11 2004 Fr. Br. George <george@altlinux.ru> 0.4.4-alt1
- Initial ALT build

* Tue Apr 20 2004 Jens Granseuer <jensgr@gmx.net>
- include COPYING.MUSIC

* Sun Feb 22 2004 Jens Granseuer <jensgr@gmx.net>
- require SDL_ttf

* Sat Sep 20 2003 Jens Granseuer <jensgr@gmx.net>
- distribute icon
- use system directories

* Fri Aug 22 2003 Jens Granseuer <jensgr@gmx.net>
- updated URLs

* Sat Dec 7 2002 Jens Granseuer <jensgr@gmx.net>
- update for 0.3.0
- build and install the new bi2cf tool by default

* Fri Jun 28 2002 Jens Granseuer <jensgr@gmx.net>
- renamed ChangeLog to NEWS

* Wed Apr 24 2002 Jens Granseuer <jensgr@gmx.net>
- added THANKS and TODO files to docs

* Sun Jul 22 2001 Jens Granseuer <jensgr@gmx.net>
- use CXXFLAGS instead of CFLAGS

* Thu May 17 2001 Jens Granseuer <jensgr@gmx.net>
- include manual pages

* Sun Apr 22 2001 Jens Granseuer <jensgr@gmx.net>
- require SDL 1.1.5

* Wed Mar 7 2001 Jens Granseuer <jensgr@gmx.net>
- updated to 0.1.1
- set Group to Amusements/Games

* Thu Mar 1 2001 Jens Granseuer <jensgr@gmx.net>
- initial public release


Name: angband
Version: 4.1.2
Release: alt1

Summary: Angband is a "graphical" dungeon adventure game
Summary(ru_RU.UTF-8): 	Angband - приключенческая игра.
License: Moria/Angband license
Group: Games/Adventure
Source: %name-%version.tar.gz
Url: http://rephial.org

# Automatically added by buildreq on Fri Sep 21 2012
# optimized out: gnu-config libICE-devel libncurses-devel libtinfo-devel termutils xorg-kbproto-devel xorg-xproto-devel
BuildRequires: imake libSM-devel libX11-devel libncursesw-devel xorg-cf-files

%description
Angband is a "graphical" dungeon adventure game using textual characters
to represent the walls and floors of a dungeon and the inhabitants therein,
in the vein of "rogue", "hack", "nethack" and "moria"

%description -l ru_RU.UTF-8
Angband - приключенческая игра. Для изображения стен подземелья, а так же его
обитателей используются алфавитно-цифровые символы, доступные на любом терминале.
Игра является прямым потомком игры moria.

%prep
%setup

cat > %name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Angband
Comment=Angband is a "graphical" dungeon adventure game
Comment[ru]=Angband - приключенческая игра
Icon=%name
#Exec=%_bindir/%name
Exec=%name -mx11
Terminal=false
Categories=Game;AdventureGame;
EOF

%build
%autoreconf
%configure --enable-x11 --enable-curses --disable-sdl
%make_build

%install
%makeinstall_std DESTDIR=%buildroot
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc copying.txt readme.txt thanks.txt changes.txt faq.txt
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/*
#attr(02711,games,games) %_bindir/%name
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 4.1.2-alt1
- Autobuild version bump to 4.1.2

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 4.1.0-alt1
- Autobuild version bump to 4.1.0

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 4.0.5-alt1
- Autobuild version bump to 4.0.5

* Mon Jan 18 2016 Fr. Br. George <george@altlinux.ru> 4.0.4-alt1
- Autobuild version bump to 4.0.4

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 3.5.1-alt1
- Autobuild version bump to 3.5.1

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 3.5.0-alt1
- Autobuild version bump to 3.5.0
- Fix paths

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 3.4.1-alt1
- Autobuild version bump to 3.4.1
- Heavy path fixes (no more shared hiscores supported by upstream)

* Sat Sep 22 2012 Fr. Br. George <george@altlinux.ru> 3.4.0-alt1
- Version up

* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.qa3
- Fixed build

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1.qa2
- NMU: added ru comment in .desktop

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1.qa1
NMU: converted menu to desktop file

* Sun Oct 03 2009 Alexey Voinov <voins@altlinux.ru> 3.1.1-alt1
- new version 3.1.1.1626
- /usr/games -> /usr
- update_menus removed

* Mon Feb 11 2008 Alexey Voinov <voins@altlinux.ru> 3.0.9-alt1
- new version (3.0.9)
- make install totally broken, install by hand
- vns4 patch replaced with quick&dirty hack, that just works
- unused world-writable 'user' directory removed (#7991)
- url updated
- buildreqs updated
- russian description fixed (#11855)

* Mon May 29 2006 Alexey Voinov <voins@altlinux.ru> 3.0.6-alt2
- buildreq updated

* Sun Jul 24 2005 Alexey Voinov <voins@altlinux.ru> 3.0.6-alt1
- new version (3.0.6)
- vns patch updated

* Fri Oct 22 2004 Alexey Voinov <voins@altlinux.ru> 3.0.5-alt1
- new version (3.0.5)
- vns patch updated

* Sun Mar 07 2004 Alexey Voinov <voins@altlinux.ru> 3.0.4-alt1
- new version (3.0.4)
- 32x32 tiles updated
- vns patch updated

* Thu Oct 09 2003 Alexey Voinov <voins@altlinux.ru> 3.0.3-alt3
- buildreqs fixed (fixes bug #3088)

* Sat Sep 13 2003 Alexey Voinov <voins@altlinux.ru> 3.0.3-alt2
- now builds with hasher.

* Tue Feb 25 2003 Alexey Voinov <voins@voins.program.ru> 3.0.3-alt1
- new version (3.0.3)
- new tiles 32x32 packaged
- menu entry changed to startangband with new tiles.

* Tue Jan 21 2003 Stanislav Ievlev <inger@altlinux.ru> 3.0.1-alt2
- made buildable.

* Wed Oct 23 2002 Alexey Voinov <voins@voins.program.ru> 3.0.1-alt1
- new version(3.0.1)
- vns3 patch updated
- url updated

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0.0-alt1.1
- fixed suid/sgid file permissions

* Mon Jun 10 2002 Alexey Voinov <voins@voins.program.ru> 3.0.0-alt1
- new version(3.0.0)
- .vns3 patch updated

* Mon Jan 07 2002 Alexey Voinov <voins@voins.program.ru> 2.9.3-alt4
- directories rearranged (no more writes to /usr)
- remove data directory when uninstall
- remove directories from old install (data,save,apex)
- copy old savefiles into new location
- description and Summary updated and translated

* Mon Sep 17 2001 Alexey Voinov <voins@voins.program.ru> 2.9.3-alt3
- 2 bugfixes applied
- little spec cleanup
- menu fixed

* Thu Sep 13 2001 Alexey Voinov <voins@voins.program.ru> 2.9.3-alt2
- menu file added

* Fri Aug 17 2001 Alexey Voinov <voins@voins.program.ru> 2.9.3-alt1
- new version

* Sun Mar 13 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

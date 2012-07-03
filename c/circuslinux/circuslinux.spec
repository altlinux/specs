Summary: Cute breakout-like
Name: circuslinux
Version: 1.0.3
Release: alt7
License: GPL
Url: http://newbreedsoftware.com/circus-linux/
Group: Games/Arcade
Source0: ftp://ftp.billsgames.com/unix/x/circus-linux/src/%name-%version.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Sep 22 2009
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel

%description
"Circus Linux!" is based on the Atari 2600 game "Circus Atari" by Atari,
released in 1980.  Gameplay is similar to "Breakout" and "Arkanoid"- you
slide a device left and right to bounce objects into the air which destroy
a wall.

%prep
%setup -q

%define _optlevel 3
%add_optflags %optflags_notraceback %optflags_fastmath
sed -i 's/| pentium2-/| x86_* | pentium2-/' config.sub

%build
%set_autoconf_version 2.5
%set_automake_version 1.4

#./autogen.sh
aclocal
automake --foreign -a
autoconf
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build bindir=%_gamesbindir datadir=%_gamesdatadir

cat > %name.desktop <<@@@
[Desktop Entry]
Categories=Game;ArcadeGame;
Name=CircusLinux
Comment=Turn arcanoid into circus!
Icon=%name
Exec=%name
Terminal=false
Type=Application
@@@

%install
%makeinstall bindir=%buildroot%_gamesbindir datadir=%buildroot%_gamesdatadir
install -D -m0644 data/images/circuslinux-icon.xpm %buildroot%_niconsdir/%name.xpm
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop

%files
%doc AUTHORS.txt CHANGES.txt README.txt FAQ.txt
%_gamesbindir/%name
%_gamesdatadir/%name
%_niconsdir/%name.xpm
%_desktopdir/%name.desktop

%changelog
* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.0.3-alt7
- Fix *64 build
- Fix repocop warnings

* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 1.0.3-alt6
- Repocop fixes

* Mon Dec 18 2006 Fr. Br. George <george@altlinux.ru> 1.0.3-alt5
- Remove %%optflags_kernel to fix x86_64 build
- Do not use ./autogen.sh to fix x86_64 build

* Tue Jun 14 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.3-alt4
- build requires updated (autoconf_2.5)

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 1.0.3-alt3
- build requires fix

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 1.0.3-alt2
- rebuild (gcc 3.2)

* Sun Feb 10 2002 Rider <rider@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri Aug 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.1-ipl7mdk
- Rebuild with new SDL
- Some spec cleanup
- Fixed CFLAGS

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 1.0.1-ipl6mdk
- Rebuild with SDL-1.2.0

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 1.0.1-ipl5mdk
- fix BuildPreReq

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz> 1.0.1-ipl4mdk
- Build for RE
- adding menu

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-4mdk
- rebuild for new libSDL_mixer

* Wed Nov  8 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-3mdk
- capitalize summary

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 1.0.1-1mdk
- initial spec

# end of file

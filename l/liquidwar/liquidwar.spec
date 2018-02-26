# Liquid War sports i386 assembler extensions, that don't work on
# anything but i386.
%ifarch i586
%define configureasm --enable-asm
%else
%define configureasm --disable-asm
%endif

Name: liquidwar
Version: 5.6.4
Release: alt4

Group: Games/Arcade
Summary: Liquid War is a unique multiplayer wargame
License: GPL
Url: http://www.ufoot.org/liquidwar/v5

#Requires: #{get_dep liballegro}

Source: http://www.ufoot.org/archive/%name-%version.tar.gz
Source2: %name.16.xpm
Source3: %name.32.xpm
Source4: %name.48.xpm
Patch: %name-wwwsrv-buffer-overflow.patch

# Automatically added by buildreq on Sun Sep 03 2006 (-bi)

BuildRequires: liballegro-devel linux-libc-headers
BuildRequires: python-modules python-modules-email python-modules-encodings python-modules-xml
Requires: /usr/bin/sound_wrapper

# tetex-dvips tetex-latex

%description
Liquid War is a wargame. But it is different from common wargames.

When playing Liquid War, one has to eat one's opponent. There can be from
2 to 6 players. There are no weapons, the only thing you have to do is to
move a cursor in a 2-D battlefield. This cursor is followed by your army,
which is composed by a great many little fighters. Fighters are represented
by small colored squares. All the fighters who have the same color belong
to the same team. One very often controls several thousands fighters at the
same time. And when fighters from different teams meet, they eat each
other, it is as simple as that.

%prep
%setup -q
%patch
sed -i '/^liquidwar-mapgen:/,$s/EXTERN_LIBS)/EXTERN_LIBS) -lm/' src/Makefile.in

%build
%autoreconf
#autoconf

%configure \
	%configureasm \
	--datadir=%_datadir \
	--disable-doc-txt \
	--disable-doc-html \
	--disable-doc-info \
	--disable-doc-ps \
	--disable-doc-pdf

%make_build -C doc
%make_build \
	DATADIR=%_gamesdatadir/%name \
	ALCFLAGS="-I/usr/liclude \
	-DCONFIG_UNIX_CFG=\".liquidwarrc\" \
	-DCONFIG_UNIX_DAT=\"%_gamesdatadir/%name/liquidwar.dat\" \
	-DCONFIG_UNIX_MAP=\"%_gamesdatadir/%name/map/\" \
	-DCONFIG_UNIX_TEX=\"%_gamesdatadir/%name/texture/\""

%install
perl -pi -e 's#install_custom_texture install_icon install_gpl#install_custom_texture #' Makefile
%makeinstall gamedir=%buildroot/%_gamesbindir datadir=%buildroot/%_datadir docdir=%buildroot/%_docdir/%name-%version

rm -rf %buildroot/%_bindir

mkdir -p -m755 %buildroot/%_mandir/man6
cp doc/man/%{name}.man %buildroot/%_mandir/man6/%name.6
ln -s %name.6 %buildroot/%_mandir/man6/%name-server.6

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Liquid War
Comment=Liquid War is a unique multiplayer wargame
Icon=%{name}
Exec=sound_wrapper %_gamesbindir/%name
Terminal=false
Categories=Game;ArcadeGame;
EOF
cat > %buildroot%_desktopdir/%{name}-server.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Liquid War - server
Comment=Liquid War is a unique multiplayer wargame
Icon=%{name}
Exec=%_gamesbindir/%name-server
Terminal=true
Categories=Game;ArcadeGame;
EOF

mkdir -p %buildroot/%_iconsdir %buildroot/%_miconsdir %buildroot/%_liconsdir
install -m 644 %SOURCE2 %buildroot/%_miconsdir/%name.xpm
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.xpm
install -m 644 %SOURCE4 %buildroot/%_liconsdir/%name.xpm

%files
%_gamesbindir/*
%doc README*
%_gamesdatadir/%name
%_desktopdir/*.desktop
%_mandir/man6/*
%_datadir/pixmaps/%name.xpm
%_iconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm

%changelog
* Tue May 29 2012 Fr. Br. George <george@altlinux.ru> 5.6.4-alt4
- DSO list completion

* Tue May 29 2012 Fr. Br. George <george@altlinux.ru> 5.6.4-alt3
- DSO list completion

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 5.6.4-alt2.qa2
- NMU: .desktop files should use /usr/bin/sound_wrapper

* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 5.6.4-alt2.qa1
- NMU: converted menu to desktop file

* Tue Mar 22 2011 Fr. Br. George <george@altlinux.ru> 5.6.4-alt2
- Resurrected from orhpaned

* Tue Jul 21 2009 Mikhail Yakshin <greycat@altlinux.org> 5.6.4-alt1
- 5.6.4
- fixed buffer overflow error (thanks to new gcc and ldv@)
- builds with new gcc
- disabled asm for everything but i586

* Fri Sep 01 2006 Mikhail Yakshin <greycat@altlinux.org> 5.6.3-alt1
- new version
- build fixes

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 5.6.2-alt1
- new version

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 5.5.9-alt1
- new version

* Wed Dec 25 2002 Sergey V Turchin <zerg@altlinux.ru> 5.5.8-alt1
- new version

* Wed Oct 16 2002 Sergey V Turchin <zerg@altlinux.ru> 5.5.7-alt1
- new version
- build vith gcc3.2

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 5.5.6-alt1
- new version

* Thu Jun 13 2002 Sergey V Turchin <zerg@altlinux.ru> 5.5.0-alt1
- new version

* Fri Apr 12 2002 Sergey V Turchin <zerg@altlinux.ru> 5.4.5-alt1
- new version

* Thu Jan 31 2002 Sergey V Turchin <zerg@altlinux.ru> 5.4.3-alt1
- new version

* Thu Dec 20 2001 Sergey V Turchin <zerg@altlinux.ru> 5.4.2-alt2
- rebuild with new allegro

* Tue Aug 07 2001 Sergey V Turchin <zerg@altlinux.ru> 5.4.2-alt1
- new version

* Fri Jul 27 2001 Sergey V Turchin <zerg@altlinux.ru> 5.4.0-2mdk
- build for ALT

* Wed Jul 11 2001 Yves Duret <yduret@mandrakesoft.com> 5.4.0-2mdk
- i suck

* Tue Jul 10 2001 Yves Duret <yduret@mandrakesoft.com> 5.4.0-1mdk
- first mandrake version (games found by our pambon)

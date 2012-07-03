%define		libpath		/usr/lib/angband
%define		varpath		/var/lib/angband

Name:		angband
Version: 	3.1.1
Release: 	alt1.qa3

Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	Angband is a "graphical" dungeon adventure game
Summary(ru_RU.KOI8-R): 	Angband - приключенческая игра.
License:	Moria/Angband license
Group:		Games/Adventure
Source:		%name-%version.tar
Source1:	%name-graf.tar.bz2
Source2:	graf-32x32-304.tar.bz2
Patch: angband-3.1.1-alt-DSO.patch
URL:		http://rephial.org

# Automatically added by buildreq on Mon Feb 11 2008
BuildRequires: imake libSDL-devel libSDL_mixer-devel libSM-devel libX11-devel libncurses-devel xorg-cf-files

%description
Angband is a "graphical" dungeon adventure game using textual characters
to represent the walls and floors of a dungeon and the inhabitants therein,
in the vein of "rogue", "hack", "nethack" and "moria"

%description -l ru_RU.KOI8-R
Angband - приключенческая игра. Для изображения стен подземелья, а так же его 
обитателей используются алфавитно-цифровые символы, доступные на любом терминале.
Игра является прямым потомком игры moria. 

%prep
%setup -q -a1 -a2
%patch -p2

%build
%configure --enable-x11 --enable-curses --disable-sdl --with-libpath=%libpath
make
 
%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%varpath/{apex,bone,data,save}
mkdir -p $RPM_BUILD_ROOT/%libpath/{edit,file,help,info,pref,xtra/{font,graf,sound}}
cp src/angband $RPM_BUILD_ROOT/%_bindir
cp lib/edit/*.txt $RPM_BUILD_ROOT/%libpath/edit/
cp lib/file/*.txt $RPM_BUILD_ROOT/%libpath/file/
cp lib/help/*.{txt,hlp} $RPM_BUILD_ROOT/%libpath/help/
cp lib/pref/*.prf $RPM_BUILD_ROOT/%libpath/pref/
cp lib/xtra/font/*.{txt,fon} $RPM_BUILD_ROOT/%libpath/xtra/font/
cp lib/xtra/graf/*.{png,bmp} $RPM_BUILD_ROOT/%libpath/xtra/graf/
cp lib/xtra/sound/*.{wav,cfg} $RPM_BUILD_ROOT/%libpath/xtra/sound/

cp angband-graf/*.bmp $RPM_BUILD_ROOT/%libpath/xtra/graf/
cp {mask32,32x32}.bmp $RPM_BUILD_ROOT%libpath/xtra/graf

touch $RPM_BUILD_ROOT%varpath/apex/scores.raw

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Angband
Comment=Angband is a "graphical" dungeon adventure game
Comment[ru]=Angband - п©я─п╦п╨п╩я▌я┤п╣п╫я┤п╣я│п╨п╟я▐ п╦пЁя─п╟
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=%name -mx11 -- -g -b
Terminal=false
Categories=Game;AdventureGame;
EOF

%post
if [ -d %libpath/apex/ ]; then
	for f in %libpath/apex/*; do
		[ -e $f ] && install -m0664 -g games -o games $f %varpath/apex/
	done
	rm -rf %libpath/apex
fi
if [ -d %libpath/data/ ]; then
	rm -rf %libpath/data
fi
if [ -d %libpath/save/ ]; then
	for f in %libpath/save/*; do
		[ -e $f ] && install -m0664 -g games -o games $f %varpath/save/
	done
	rm -rf %libpath/save
fi

%preun
if [ -d %varpath/data/ ]; then
	rm -rf %varpath/data/*
fi

%files
%doc copying.txt readme.txt thanks.txt changes.txt faq.txt
%attr(02711,games,games) %_bindir/%name
%attr(0755,games,games) %dir %libpath
%attr(0755,games,games) %dir %varpath
%attr(0775,games,games) %dir %varpath/apex/
%attr(0664,games,games) %config(noreplace) %varpath/apex/*
%attr(0070,games,games) %dir %varpath/bone/
%attr(0775,games,games) %dir %varpath/data/
%attr(0070,games,games) %dir %varpath/save/
%dir %libpath/edit/
%dir %libpath/file/
%dir %libpath/help/
%dir %libpath/info/
%dir %libpath/pref/
%dir %libpath/xtra/
%dir %libpath/xtra/graf/
%dir %libpath/xtra/font/
%dir %libpath/xtra/sound/
%libpath/edit/*
%libpath/file/*
%libpath/help/*
%libpath/pref/*
%libpath/xtra/graf/*
%libpath/xtra/font/*
%libpath/xtra/sound/*
%_desktopdir/%name.desktop

%changelog
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

%define		libpath		/usr/lib/zangband/
%define		varpath		/var/lib/zangband/
%define		vsuffix		pre1

Name:		zangband
Version: 	2.7.5
Release: 	alt0.3.qa2


Summary:	ZAngband is one of the many angband variants
Summary(ru_RU.KOI8-R): ZAngband - игра, вариант игры Angband
License:	Moria/Angband license
Group:		Games/Adventure
URL:		http://www.zangband.org
Packager: 	Alexey Voinov <voins@altlinux.ru>


Source:		%name-%version%vsuffix.tar.bz2
Source1:	%name.z-config.h
Patch:		%name-2.7.5pre1-alt-vns1.patch
Patch1:		%name-2.7.0-price.patch

# Automatically added by buildreq on Mon May 05 2008
BuildRequires: gtk+-devel libX11-devel libXext-devel libXaw-devel libncurses-devel

%description
ZAngband is one of the many variants of the freeware roguelike
computer roleplaying game Angband

%description -l ru_RU.KOI8-R
ZAngband один из многих вариантов ролевой игры Angband.

%prep
%setup -q -n %name
%patch -p1 -b .vns
#%patch1 -p1 -b .price
cp %SOURCE1 src/z-config.h
cp src/makefile.std src/Makefile
rm -f src/makefile

%build
cd src
make CFLAGS="$RPM_OPT_FLAGS -DUSE_XAW -DUSE_GCU -DUSE_VCS -DUSE_TRANSPARENCY"
 
%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%libpath,%varpath}

install -m755 src/zangband $RPM_BUILD_ROOT%_bindir/%name

install -d $RPM_BUILD_ROOT%varpath/apex
install -m644 lib/apex/z_scores.raw $RPM_BUILD_ROOT%varpath/apex/scores.raw

install -d $RPM_BUILD_ROOT%varpath/bone
install -d $RPM_BUILD_ROOT%varpath/data

install -d $RPM_BUILD_ROOT%libpath/edit
install -m644 lib/edit/*.txt $RPM_BUILD_ROOT%libpath/edit

install -d $RPM_BUILD_ROOT%libpath/script
install -m644 lib/script/*.lua $RPM_BUILD_ROOT%libpath/script

install -d $RPM_BUILD_ROOT%libpath/file
install -m644 lib/file/*.txt $RPM_BUILD_ROOT%libpath/file

install -d $RPM_BUILD_ROOT%libpath/help
install -m644 lib/help/*.txt $RPM_BUILD_ROOT%libpath/help
install -m644 lib/help/*.hlp $RPM_BUILD_ROOT%libpath/help

install -d $RPM_BUILD_ROOT%libpath/info

install -d $RPM_BUILD_ROOT%varpath/save

install -d $RPM_BUILD_ROOT%libpath/pref
install -m644 lib/pref/*.prf $RPM_BUILD_ROOT%libpath/pref

install -d $RPM_BUILD_ROOT%varpath/user

install -d $RPM_BUILD_ROOT%libpath/xtra
install -d $RPM_BUILD_ROOT%libpath/xtra/font
install -m644 lib/xtra/font/*.FON $RPM_BUILD_ROOT%libpath/xtra/font
install -m644 lib/xtra/font/*.fnt $RPM_BUILD_ROOT%libpath/xtra/font
install -m644 lib/xtra/font/*.txt $RPM_BUILD_ROOT%libpath/xtra/font
install -d $RPM_BUILD_ROOT%libpath/xtra/graf
install -m644 lib/xtra/graf/*.bmp $RPM_BUILD_ROOT%libpath/xtra/graf
install -d $RPM_BUILD_ROOT%libpath/xtra/help
install -d $RPM_BUILD_ROOT%libpath/xtra/music
install -d $RPM_BUILD_ROOT%libpath/xtra/sound
install -m644 lib/xtra/sound/sound.cfg $RPM_BUILD_ROOT%libpath/xtra/sound

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=ZAngband
Comment=ZAngband is one of the many angband variants
Comment[ru]=ZAngband - п╦пЁя─п╟, п╡п╟я─п╦п╟п╫я┌ п╦пЁя─я▀ Angband
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=%name -g
Terminal=false
Categories=Game;AdventureGame;
EOF

%post
if [ -d %libpath/data ]; then
	rm -rf %libpath/data
fi
if [ -d %libpath/save ]; then
	for f in %libpath/save/*; do
		[ -e $f ] && install -m0664 -g games -o games $f %varpath/save/
	done
	rm -rf %libpath/save
fi

%preun
if [ -d %varpath/data ]; then
	rm -rf %varpath/data/*
fi

%files
%doc readme z_update.txt z_faq.txt
%dir %varpath
%attr(02711,games,games) %_bindir/%name
%attr(0755,games,games) %dir %varpath
%attr(0755,games,games) %dir %libpath
%attr(0775,games,games) %dir %varpath/apex/
%attr(0664,games,games) %config(noreplace) %varpath/apex/*
%attr(0070,games,games) %dir %varpath/bone/
%attr(0775,games,games) %dir %varpath/data/
%attr(0070,games,games) %dir %varpath/save/
%attr(0775,games,games) %dir %varpath/user/
%dir %libpath/edit/
%dir %libpath/file/
%dir %libpath/help/
%dir %libpath/info/
%dir %libpath/pref/
%dir %libpath/script/
%dir %libpath/xtra/
%dir %libpath/xtra/font/
%dir %libpath/xtra/graf/
%dir %libpath/xtra/sound/
%dir %libpath/xtra/music/
%dir %libpath/xtra/help/
%libpath/edit/*
%libpath/file/*
%libpath/help/*
%libpath/pref/*
%libpath/script/*
%libpath/xtra/font/*
%libpath/xtra/graf/*
%libpath/xtra/sound/*
%_desktopdir/%name.desktop

%changelog
* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt0.3.qa2
- NMU: added ru comment in .desktop

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt0.3.qa1
NMU: converted menu to desktop file

* Sun Aug 30 2009 Alexey Voinov <voins@altlinux.ru> 2.7.5-alt0.3
- /usr/games -> /usr
- update_menus call removed

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.7.5-alt0.2.1
- NMU:
  * updated build dependencies

* Mon May 05 2008 Alexey Voinov <voins@altlinux.ru> 2.7.5-alt0.2
- directory permissions fixed, directory ownership fixed
- buildreq updated

* Sun Jun 05 2005 Alexey Voinov <voins@altlinux.ru> 2.7.5-alt0.1
- new version (2.7.5pre1)

* Sat Mar 06 2004 Alexey Voinov <voins@altlinux.ru> 2.7.4b-alt1
- new version 2.7.4b [note 2.7.4b > 2.7.4]

* Sat Sep 13 2003 Alexey Voinov <voins@altlinux.ru> 2.7.2-alt5
- spec clean up
- buildreq fixed

* Wed Mar 26 2003 Alexey Voinov <voins@voins.program.ru> 2.7.2-alt4
- new cvs snapshot (2.7.3pre2) [lot of bugs fixed]

* Sat Mar 22 2003 Alexey Voinov <voins@voins.program.ru> 2.7.2-alt3
- new cvs snapshot (22-Mar-2003) (post 2.7.3pre1)

* Sat Mar 08 2003 Alexey Voinov <voins@voins.program.ru> 2.7.2-alt2
- new cvs snapshot (08-Mar-2003)
- vns1 patch updated

* Tue Jan 04 2003 Alexey Voinov <voins@voins.program.ru> 2.7.2-alt1
- new version (2.7.2)
- vns1 patch updated
- price patch removed

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 2.7.0-alt2.1
- fixed suid/sgid file permissions

* Fri Jun 21 2002 Alexey Voinov <voins@voins.program.ru> 2.7.0-alt2
- .price patch added (show basic prices in inventory)

* Sun Jan 20 2002 Alexey Voinov <voins@voins.program.ru> 2.7.0-alt1
- 2.7.0-final

* Sun Jan 07 2002 Alexey Voinov <voins@voins.program.ru> 2.7.0-alt0.pre2
- 2.7.0-pre2 (from cvs)
- all patches combined into one (vns)
- directories rearranged (no more writes to /usr)
- rights to data directory back to 0775
- spec clean up
- remove data directory when uninstall
- remove directories from old install (data,save). 
- copy old savefiles into new location
- description and Summary updated and translated

* Wed Sep 26 2001 Alexey Voinov <voins@voins.program.ru>
- getlogin patch added (should not create ZAngband directory in cwd)
- temporary 0777 rights to lib/zangband/data

* Tue Sep 18 2001 Alexey Voinov <voins@voins.program.ru> 2.6.2-alt4
- menu fixed
- little spec cleanup

* Thu Sep 13 2001 Alexey Voinov <voins@voins.program.ru> 2.6.2-alt3
- menu file added

* Mon Sep 10 2001 Alexey Voinov <voins@voins.program.ru>
- initial build 

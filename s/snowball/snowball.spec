Name: snowball
Version: 0.2
Release: alt1.1

Summary: Snowball is a free (GPL) jump'n'run game

License: GPL
Group: Games/Arcade
Url: http://snowball.retrovertigo.de/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://snowball.retrovertigo.de/%name.tar

# python version independent
Requires: python-module-pygame

BuildArchitectures: noarch

%add_python_req_skip credits editor font game gimmick highscore level options

%description
Snowball is a free (GPL) jump'n'run game inspired by games like "Solomon's
Key" or "Spherical".  Guide Tux the penguin through the levels and help
him to bring the snowball save to the exit. Create iceblocks, collect
keys, use transporters and beware of traps and monsters!

%prep
%setup -n %name

%build

%install
mkdir -p %buildroot/%_gamesdatadir/%name/
cp -pr ./ %buildroot/%_gamesdatadir/%name/

mkdir -p %buildroot%_gamesbindir/
cat >%buildroot%_gamesbindir/%name <<EOF
#!/bin/sh
cd %_gamesdatadir/%name
/usr/bin/env python %name.py
EOF

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=snowball
Comment=%summary
Icon=%{name}
Exec=%_gamesbindir/%name
#Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%attr(0755,root,root) %_gamesbindir/%name
#%doc authors.txt highscore.txt
%_gamesdatadir/%name/
#%_iconsdir/*
%_desktopdir/%{name}.desktop

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 20 2011 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- cleanup spec
- fix /usr/games/snowball permissions (ALT bug #25765)

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt0.1.qa2
- NMU: converted debian menu to freedesktop

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for snowball
  * postclean-05-filetriggers for spec file

* Sun Mar 19 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt0.1
- initial build for ALT Linux Sisyphus

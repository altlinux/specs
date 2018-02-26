Name: zephulor
Version: 0.9a
Release: alt5.1.1

Summary: Zephulor - game written in Python

License: LGPL
Group: Games/Arcade
Url: http://www.hollowworks.com/apz/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.hollowworks.com/downloads/adventuresonplanetzephulor/files/%name-source.tar.bz2
Patch: %name.patch

%setup_python_module %name
%add_python_lib_path %_gamesdatadir/%name

BuildArchitectures: noarch

%description
Planet Zephulor is a side scrolling platform arcade game under development.
Currently the game spans 15 levels. 

%prep
%setup -q -n %name-source
%patch
%__subst "s|!/bin/env|!/usr/bin/env|" *.py

%build

%install
mkdir -p %buildroot/%_gamesdatadir/%name
cp -pr ./ %buildroot/%_gamesdatadir/%name

mkdir -p %buildroot%_desktopdir
cat >%buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Zephulor
GenericName=
Comment=Planet Zephulor
Icon=zephulor
Exec=%_gamesbindir/%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%__mkdir_p %buildroot%_gamesbindir
cat >%buildroot%_gamesbindir/%name <<EOF
#!/bin/sh
cd %_gamesdatadir/%name
./%name.py
EOF

%files
%attr (0755, root root) %_gamesbindir/*
%_gamesdatadir/%name
#%_iconsdir/*
%_desktopdir/%name.desktop

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9a-alt5.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9a-alt5.1
- Rebuilt with python 2.6

* Wed Sep 16 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9a-alt5
- fix desktop file (repocop warnings)

* Fri Dec 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9a-alt4
- fix build
- replace menu file with desktop one

* Sat Feb 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9a-alt3
- build with correct buildrequires and requires

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9a-alt2
- rebuild with python 2.4

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9a-alt1
- first build for ALT Linux Sisyphus

Name: pyraider
Version: 0.1
Release: alt1.qa3.1

Summary: PyRaider - game written in Python

License: GPL
Group: Games/Arcade
Url: http://www.pygame.org/gamelets/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

# python version independent
Requires: python-module-pygame
BuildArch: noarch

%description
PyRaider

%prep
%setup -q
rm -f pygame2exe.py
%build

%install
mkdir -p %buildroot/%_gamesdatadir/%name
cp -pr ./ %buildroot/%_gamesdatadir/%name

mkdir -p %buildroot%_gamesbindir
cat >%buildroot%_gamesbindir/%name <<EOF
#!/bin/sh
cd %_gamesdatadir/%name
python game.py
EOF

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=PyRaider
Comment=%summary
Icon=%{name}
Exec=%_gamesbindir/%name
#Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%attr (0755, root root) %_gamesbindir/*
%_gamesdatadir/%name
#%_iconsdir/*
%_desktopdir/%{name}.desktop

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.qa3.1
- Rebuild with Python-2.7

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.qa3
- NMU: converted menu to desktop

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for pyraider
  * postclean-05-filetriggers for spec file

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.2
- Rebuilt with python 2.6

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1.1
- add require for pygame

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- first build for ALT Linux Sisyphus

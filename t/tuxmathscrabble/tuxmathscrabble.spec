%define oname TuxMathScrabble
Name: tuxmathscrabble
Version: 0.7.4
Release: alt1.1

Summary: A math version of the popular board game for ages 4-40

Packager: Vitaly Lipatov <lav@altlinux.ru>

Group: Games/Boards
Url: http://sourceforge.net/projects/tuxmathscrabble/
License: GPLv3

BuildArch: noarch

%define pythonlibs %python_sitelibdir/%oname

%add_python_req_skip %oname

Source: http://prdownloads.sourceforge.net/tuxmathscrabble/%name-%version.tar

Patch: TuxMathScrabble-0.7.4-fixpath.patch

# Automatically added by buildreq on Sun Jul 06 2008
BuildRequires: python-base

# due font links
Requires: fonts-ttf-freefont

%description
TuxMathScrabble is an OpenSource math version of the popular board game for
ages 4-40. it challenges young people to construct compound equations and
consider multiple abstract possibilities. There are 4 skill levels, the
hardest uses numbers up to 20 and supports division as well as
add/subtract/multiply. Upon completing a successful move little Tux's
pop-out of the most recently moved tiles and do a little dance. Tux moves
his own pieces as well as performing various animated antics.

%prep
%setup
%patch

# replace font with links
rm -f Font/arial.ttf
rm -f Font/arialbd.ttf
ln -s /usr/share/fonts/ttf/freefont/FreeSans.ttf Font/arial.ttf
ln -s /usr/share/fonts/ttf/freefont/FreeSansBold.ttf Font/arialbd.ttf

%install
mkdir -p %buildroot%pythonlibs/
cp -a %oname/* %buildroot%pythonlibs/

mkdir -p %buildroot%_gamesdatadir/%oname/
cp -f .tms_config_master %buildroot%_gamesdatadir/%oname/
cp -a Font %buildroot%_gamesdatadir/%oname/

install -D %name.py %buildroot%_gamesbindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=TuxMathScrabble
Comment=Fun game to learn math
Exec=%_gamesbindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%files
%_gamesbindir/%name
%pythonlibs/
%_gamesdatadir/%oname/
%_desktopdir/%name.desktop

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.4-alt1.1
- Rebuild with Python-2.7

* Wed May 25 2011 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt1
- build new version (ALT bug #21109)

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.4-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for tuxmathscrabble
  * postclean-05-filetriggers for spec file

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt2
- remove times.ttf from package

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt1
- initial build for ALT Linux Sisyphus

* Tue Dec 18 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.0-0.2mdv2008.1
+ Revision: 132015
- New version 0.5.0 Rc2
  Fix patch in Environment.py ( patch from PCLinuxOS )

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:0.5.0-0.1mdv2008.1
+ Revision: 119664
- New pre version of 0.5.0

* Fri Dec 14 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:0.4.5-1mdv2008.1
+ Revision: 119591
- New version 0.4.5

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Dec 01 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.0.4-2mdv2007.0
+ Revision: 89589
- Fix File List
- New version 3.0.4
- import tuxmathscrabble-2.7-1mdk

* Mon Jan 17 2005 Michael Scherer <misc@mandrake.org> 2.7-1mdk
- misc cleanup
- from jean-sebastien HUBERT <jshubert@free.fr>
  - first release for Linux-Mandrake


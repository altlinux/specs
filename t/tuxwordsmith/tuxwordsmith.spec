%define oname TuxWordSmith
%define pkgdata %_gamesdatadir/%oname

Name: tuxwordsmith
Version: 0.6.7
Release: alt1.1.1

Summary: Scrabble like game for young children

Packager: Vitaly Lipatov <lav@altlinux.ru>

Group: Games/Educational
License: GPL
Url: http://www.asymptopia.org/staticpages/index.php?page=TuxWordSmith

Source: %oname-%version.tgz
Source1: %oname.desktop
Source2: %oname.png
Patch: %name.patch

# Automatically added by buildreq on Mon Jul 07 2008
BuildRequires: python-base

%description
TuxWordSmith is similar to the classic word game "Scrabble", but with unicode
support for multiple languages and character sets. The game is currently
distributed with forty-two (42) dictionary resources for playing
Language[i]-Language[j] "Scrabble".

For example, if configured to use the French-German dictionary, then the
distribution of available tiles will be computed based on frequency of
occurance of each character of Language[i] (French), and for each submission
the corresponding definition will be given in Language[j] (German).

The latest release includes support for the Greek and Cyrillic (Russian,
Ukranian) character sets, thus making it possible to play Scrabble in Greek,
Russian and Ukranian, as well as a host of other languages which use latin
characters.

%prep
%setup -q -n %oname
%patch
#find -type d -name .svn -print0 | xargs -0 rm -rf {} \;

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%python_sitelibdir/
mkdir -p %buildroot%pkgdata

cp -R Globals %buildroot%pkgdata
cp -R Font %buildroot%pkgdata
cp -R xdxf %buildroot%pkgdata
#cp -R %oname %buildroot%pkgdata

# install binfile
install -m755 %name %buildroot%_bindir/%name
cp -R %oname %buildroot/%python_sitelibdir/

# install EduApp modules
#cp -r asymptopia_0_1_3 %buildroot/%python_sitelibdir/

# below is the desktop file and icon stuff.
install -Dm 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dm 644 %SOURCE2 %buildroot%_pixmapsdir/%name.png
#mkdir -p /var/games/%oname/Globals/globals/
#>/var/games/%oname/Globals/globals/config

%files
%doc README* VERSION CHANGES LICENSE VERSION
%_bindir/%name
%python_sitelibdir/%oname/
#%python_sitelibdir/asymptopia_0_1_3
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
#%config(noreplace) /var/games/%oname/Globals/globals/config
%pkgdata/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.7-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt1.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.7-alt1
- new version 0.6.7 (with rpmrb script)

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- initial build for ALT Linux Sisyphus

* Mon Apr 21 2008 lars@linux-schulserver.de
- initial version 0.5.3

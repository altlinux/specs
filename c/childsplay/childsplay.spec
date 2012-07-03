%define realname childsplay_sp
%define alphabet_ver 0.9.1
%define old_alphabet_ver 0.9


Name: childsplay
Version: 1.6
Release: alt1.1

License: GPLv3+
Group: Games/Educational
Url: http://www.schoolsplay.org/

Summary: Suite of educational games for young children

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.gz
Source1: %name.desktop
Source10: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_bg-%alphabet_ver.tgz
Source11: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_ca-%alphabet_ver.tgz
Source12: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_de-%alphabet_ver.tgz
Source13: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_el-%old_alphabet_ver.tgz
Source14: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_en_GB-%alphabet_ver.tgz
Source15: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_es-%alphabet_ver.tgz
Source16: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_fr-%alphabet_ver.tgz
Source17: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_it-%alphabet_ver.tgz
Source18: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_lt-%alphabet_ver.tgz
Source19: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_nb-%alphabet_ver.tgz
Source20: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_nl-%alphabet_ver.tgz
Source21: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_pt-%alphabet_ver.tgz
Source22: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_ro-%alphabet_ver.tgz
Source23: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_ru-%alphabet_ver.tgz
Source24: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_sl-%alphabet_ver.tgz
Source25: http://downloads.sourceforge.net/schoolsplay/alphabet_sounds_sv-%alphabet_ver.tgz

BuildArch: noarch

%add_python_lib_path %_datadir/%name/

BuildRequires: python-devel >= 2.5 
BuildRequires: python-module-pygtk-devel >= 2.0 
BuildRequires: python-module-numpy libnumpy-devel
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-pygame-devel >= 1.7
BuildRequires: libSDL-devel >= 1.2
BuildRequires: libSDL_image-devel >= 1.2
BuildRequires: libSDL_ttf-devel >= 2.0
BuildRequires: libSDL_mixer-devel >= 1.2
BuildRequires: libogg-devel 
BuildRequires: gettext-tools 

Provides:      childsplay_sp = %version-%release
Provides:      childsplay_plugins = %version-%release
Obsoletes:     childsplay_plugins <= 0.90

%description
Childsplay is a suite of educational games for young children. It's
written in Python and uses the SDL-libraries. The aim is to be
educational and at the same time be fun to play.

Some activities make use of language dependent voice samples, these sounds are
available as childsplay-alphabet_sounds packages. For those you'll have to
install the childsplay-alphabet_sounds package for the languages you intend to
use. For example childsplay-alphabet_sounds_nl.
Available alphabet sounds packages:
childsplay-alphabet_sounds_bg
childsplay-alphabet_sounds_ca
childsplay-alphabet_sounds_de
childsplay-alphabet_sounds_el
childsplay-alphabet_sounds_en_GB
childsplay-alphabet_sounds_es
childsplay-alphabet_sounds_fr
childsplay-alphabet_sounds_lt
childsplay-alphabet_sounds_nb
childsplay-alphabet_sounds_nl
childsplay-alphabet_sounds_pt
childsplay-alphabet_sounds_ro
childsplay-alphabet_sounds_ru
childsplay-alphabet_sounds_sl
childsplay-alphabet_sounds_sv


%package alphabet_sounds_bg
Summary:        Bulgarian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_bg
Bulgarian alphabet sounds for Childsplay

%package alphabet_sounds_ca
Summary:        Catalan alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_ca
Catalan alphabet sounds for Childsplay

%package alphabet_sounds_de
Summary:        German alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_de
German alphabet sounds for Childsplay

%package alphabet_sounds_el
Summary:        New Greek alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_el
new Greek alphabet sounds for Childsplay

%package alphabet_sounds_en_GB
Summary:        British English alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_en_GB
British English alphabet sounds for Childsplay

%package alphabet_sounds_es
Summary:        Spanish alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_es
Spanish alphabet sounds for Childsplay

%package alphabet_sounds_fr
Summary:        French alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_fr
French alphabet sounds for Childsplay

%package alphabet_sounds_it
Summary:        Italian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_it
Italian alphabet sounds for Childsplay

%package alphabet_sounds_lt
Summary:        Lithuanian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_lt
Lithuanian alphabet sounds for Childsplay

# I do not know which language 'nb' is :/
%package alphabet_sounds_nb
Summary:        nb alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_nb
nb alphabet sounds for Childsplay

%package alphabet_sounds_nl
Summary:        Dutch alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_nl
Dutch alphabet sounds for Childsplay

%package alphabet_sounds_pt
Summary:        Portuguese alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_pt
Portuguese alphabet sounds for Childsplay

%package alphabet_sounds_ro
Summary:        Romanian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_ro
Romanian alphabet sounds for Childsplay

%package alphabet_sounds_ru
Summary:        Russian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_ru
Russian alphabet sounds for Childsplay

%package alphabet_sounds_sl
Summary:        Slovenian alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_sl
Slovenian alphabet sounds for Childsplay

%package alphabet_sounds_sv
Summary:        Swedish alphabet sounds for Childsplay
Group: Games/Educational
Requires:       %name = %version-%release
%description alphabet_sounds_sv
Swedish alphabet sounds for Childsplay


%prep
%setup -q -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24 -a 25
# setup.py is unusable
rm -f setup.py
# fixup the python scripts to call python directly and make them executable
subst 's!/usr/bin/env python!%_bindir/python!' bin/%name
# fix wrong end of line encoding
sed -i -e 's|\r||g' doc/license.txt
# lang lt miss subdir
pushd  alphabet_sounds_lt-%alphabet_ver/AlphabetSounds
mkdir lt
mv *.* lt
popd

# set pathes 
echo "## Automated file please do not edit" > SPBasePaths.py
echo "# This module holds all the paths needed for %name." >> SPBasePaths.py
echo "DOCDIR = '%_datadir/doc/%name-%version'" >> SPBasePaths.py
echo "PYTHONCPDIR = '%python_sitelibdir/%realname'" >> SPBasePaths.py
echo "BASEDIR = '%_datadir/%realname'" >> SPBasePaths.py
echo "SHARELIBDATADIR = '%_datadir/%realname'" >> SPBasePaths.py
echo "ALPHABETDIR = '%_datadir/%realname/alphabetsounds'" >> SPBasePaths.py
echo "LOCALEDIR = '%_datadir/locale'" >> SPBasePaths.py

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%python_sitelibdir/%realname/lib
mkdir -p %buildroot%_datadir/locale
mkdir -p %buildroot%_datadir/%realname

cp -a bin/%name  %buildroot%_bindir

cp -a lib/CPData %buildroot%_datadir/%realname
cp -a lib/SPData %buildroot%_datadir/%realname
cp -a alphabetsounds %buildroot%_datadir/%realname
cp -a locale/* %buildroot%_datadir/locale

cp -a *.py %buildroot%python_sitelibdir/%realname
cp -a gui %buildroot%python_sitelibdir/%realname
cp -a lib/*.py %buildroot%python_sitelibdir/%realname/lib
cp -a ocempgui %buildroot%python_sitelibdir/%realname

#Alphabet sounds
for sounds in bg ca de en_GB es fr it lt nb nl ro ru sl sv; do
  cp -a alphabet_sounds_$sounds-%alphabet_ver/AlphabetSounds/$sounds %buildroot%_datadir/%realname/alphabetsounds
done
for sounds in ca de es fr it nl ru sl; do
  cp -a alphabet_sounds_$sounds-%alphabet_ver/FlashCardsSounds/$sounds %buildroot%_datadir/%realname/CPData/FlashcardsData/names
done
#el language has not been updated on 0.9.1 :(
cp -a alphabet_sounds_el-%old_alphabet_ver/AlphabetSounds/el %buildroot%_datadir/%realname/alphabetsounds

mkdir -p %buildroot%_desktopdir/
install -m644 %SOURCE1 %buildroot%_desktopdir/
mkdir -p %buildroot%_datadir/icons/hicolor/64x64/apps/
install -m644 lib/SPData/menu/default/logo_cp_64x64.png %buildroot%_datadir/icons/hicolor/64x64/apps/%name.png

%find_lang %name

%files -f %name.lang
%doc Changelog COPYING doc/* README
%_bindir/%name
%dir %_datadir/%realname
%_datadir/%realname/SPData
%dir %_datadir/%realname/CPData
%_datadir/%realname/CPData/*.*
%_datadir/%realname/CPData/BilliardData
%_datadir/%realname/CPData/FallinglettersData
%_datadir/%realname/CPData/FindsoundData
%_datadir/%realname/CPData/FishtankData
%dir %_datadir/%realname/CPData/FlashcardsData
%_datadir/%realname/CPData/FlashcardsData/cards
%dir %_datadir/%realname/CPData/FlashcardsData/names
%_datadir/%realname/CPData/FlashcardsData/sounds
%_datadir/%realname/CPData/FlashcardsData/names/en
%_datadir/%realname/CPData/LMemoryData
%_datadir/%realname/CPData/MemoryData
%_datadir/%realname/CPData/PackidData
%_datadir/%realname/CPData/PongData
%_datadir/%realname/CPData/PuzzleData
%_datadir/%realname/CPData/SoundmemoryData
%dir %_datadir/%realname/alphabetsounds
%_datadir/%realname/alphabetsounds/en
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/locale/*/LC_MESSAGES/childsplay_sp.mo
%python_sitelibdir/%realname

%files alphabet_sounds_bg
%doc  alphabet_sounds_bg-%alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/bg

%files alphabet_sounds_ca
%doc  alphabet_sounds_ca-%alphabet_ver/copyright  alphabet_sounds_ca-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/ca
%_datadir/%realname/alphabetsounds/ca

%files alphabet_sounds_de
%doc  alphabet_sounds_de-%alphabet_ver/copyright  alphabet_sounds_de-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/de
%_datadir/%realname/alphabetsounds/de

%files alphabet_sounds_el
%doc  alphabet_sounds_el-%old_alphabet_ver/copyright  alphabet_sounds_el-%old_alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/el

%files alphabet_sounds_en_GB
%doc  alphabet_sounds_en_GB-%alphabet_ver/copyright  alphabet_sounds_en_GB-%alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/en_GB

%files alphabet_sounds_es
%doc  alphabet_sounds_es-%alphabet_ver/copyright  alphabet_sounds_es-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/es
%_datadir/%realname/alphabetsounds/es

%files alphabet_sounds_fr
%doc  alphabet_sounds_fr-%alphabet_ver/copyright  alphabet_sounds_fr-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/fr
%_datadir/%realname/alphabetsounds/fr

%files alphabet_sounds_it
%doc  alphabet_sounds_it-%alphabet_ver/copyright  alphabet_sounds_it-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/it
%_datadir/%realname/alphabetsounds/it

%files alphabet_sounds_lt
%doc  alphabet_sounds_lt-%alphabet_ver/copyright  alphabet_sounds_lt-%alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/lt

%files alphabet_sounds_nb
%doc  alphabet_sounds_nb-%alphabet_ver/copyright  alphabet_sounds_nb-%alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/nb

%files alphabet_sounds_nl
%doc  alphabet_sounds_nl-%alphabet_ver/copyright  alphabet_sounds_nl-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/nl
%_datadir/%realname/alphabetsounds/nl

%files alphabet_sounds_ro
%doc  alphabet_sounds_ro-%alphabet_ver/copyright  alphabet_sounds_ro-%alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/ro

%files alphabet_sounds_ru
%doc  alphabet_sounds_ru-%alphabet_ver/copyright  alphabet_sounds_ru-%alphabet_ver/GPL-2
%_datadir/%realname/CPData/FlashcardsData/names/ru
%_datadir/%realname/alphabetsounds/ru

%files alphabet_sounds_sl
%_datadir/%realname/alphabetsounds/sl
%_datadir/%realname/CPData/FlashcardsData/names/sl

%files alphabet_sounds_sv
%doc  alphabet_sounds_sv-%alphabet_ver/copyright  alphabet_sounds_sv-%alphabet_ver/GPL-2
%_datadir/%realname/alphabetsounds/sv


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-2.7

* Thu Aug 18 2011 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version 1.6 (thanks kostyalamer) (closes: #26072)
- Put alphabet sounds in separate packages

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.90.2-alt1.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.90.2-alt1
- new version 0.90.2 (with rpmrb script)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.90.1-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for childsplay

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.90.1-alt2.1
- Rebuilt with python-2.5.

* Tue Dec 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.90.1-alt2
- add patch for fix bug #13571 (thanks to Slava Semushin php-coder@)
- fix desktop file permissions

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.90.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)


Name: anki2
Version: 2.1.12
Release: alt3.1

Summary: Flashcard program for using space repetition learning

Group: Games/Educational
License: AGPLv3+ and GPLv3+ and MIT and BSD
Url: https://apps.ankiweb.net/

# Source-url: https://apps.ankiweb.net/downloads/current/anki-%version-source.tgz
Source: %name-%version.tar

Patch: remove-distutils-for-python-3.12.patch

ExcludeArch: %not_qt5_qtwebengine_arches

Conflicts: anki < %version-%release

BuildRequires(pre): rpm-build-python3 rpm-macros-qt5-webengine

%add_python3_path %_datadir/anki/

%py3_requires pyaudio
%py3_requires sqlite3

Requires: mpv

# Automatically added by buildreq on Sat Apr 13 2019 (-bi)
BuildRequires: desktop-file-utils python3

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
%setup
%patch -p2
#rm -r thirdparty

%build
sed -e 's:@PREFIX@:%_prefix:' tools/runanki.system.in > tools/runanki.system

%install
install -pD -m755 tools/runanki.system %buildroot%_bindir/anki

touch touch-%_arch

mkdir -p %buildroot%_datadir/anki
cp -a anki aqt web locale %buildroot%_datadir/anki/

mkdir -p %buildroot%_man1dir
install -pm644 anki.1 %buildroot%_man1dir/

mkdir -p %buildroot%_datadir/mime/packages
install -pm644 anki.xml %buildroot%_datadir/mime/packages/

mkdir -p %buildroot%_datadir/pixmaps
install -pm644 designer/icons/anki.png %buildroot%_datadir/pixmaps/

mkdir -p %buildroot%_desktopdir
desktop-file-install --remove-category=KDE --dir %buildroot%_desktopdir \
	anki.desktop

%find_lang anki --with-qt

# hack against nonstandart place
LANGFILE=$(pwd)/anki.lang
cd %buildroot
for i in $(find .%_datadir/anki/locale/ -mindepth 1 -type d -maxdepth 1 | sed -e "s|^\.||") ; do
    lang="%%lang($(echo "$(basename $i)" | sed -e "s|_.*||")) "
    [ "$lang" = "%%lang(en)" ] && lang=''
    echo "$lang%%dir $i" >> $LANGFILE
    echo "$lang%%dir $i/LC_MESSAGES" >> $LANGFILE
done

%files -f anki.lang
%_bindir/anki
%_desktopdir/anki.desktop
%_datadir/pixmaps/anki.png
%_datadir/mime/packages/anki.xml
%dir %_datadir/anki/
%_datadir/anki/anki/
%_datadir/anki/aqt/
%_datadir/anki/web/
%_datadir/anki/locale/
%_man1dir/anki.*
%doc touch-%_arch LICENSE* README*

%changelog
* Fri Oct 20 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.12-alt3.1
- NMU: dropped dependency on distutils.

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.12-alt3
- using not_qt5_qtwebengine_arches macro

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.12-alt2
- build according qtwebengine arches

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.12-alt1
- NMU: new version (2.1.12) with rpmgs script
- switched to python3 and Qt5, add mpv require

* Sat Apr 13 2019 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.50-alt4
- NMU: really fixed build of this miserable package.

* Sat Apr 13 2019 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt3
- fix build

* Mon Feb 25 2019 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt2
- fix build

* Tue Apr 17 2018 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt1
- first build for Sisyphus


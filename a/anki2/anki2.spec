Name: anki2
Version: 2.0.50
Release: alt4
Summary: Flashcard program for using space repetition learning

Group: Games/Educational
License: AGPLv3+ and GPLv3+ and MIT and BSD
Url: https://apps.ankiweb.net/
Source: %name-%version.tar
BuildArch: noarch

Conflicts: anki < %version-%release

%py_requires pyaudio
%py_requires sqlite3

# Automatically added by buildreq on Sat Apr 13 2019 (-bi)
BuildRequires: desktop-file-utils python-modules

%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
%setup
rm -r thirdparty

%install
install -pD -m755 runanki %buildroot%_bindir/anki

mkdir -p %buildroot%_datadir/anki
cp -a anki aqt designer locale %buildroot%_datadir/anki/

mkdir -p %buildroot%_man1dir
install -pm644 anki.1 %buildroot%_man1dir/

mkdir -p %buildroot%_datadir/mime/packages
install -pm644 anki.xml %buildroot%_datadir/mime/packages/

mkdir -p %buildroot%_datadir/pixmaps
install -pm644 designer/icons/anki.png %buildroot%_datadir/pixmaps/

mkdir -p %buildroot%_desktopdir
desktop-file-install --remove-category=KDE --dir %buildroot%_desktopdir \
	anki.desktop

%find_lang anki

%files -f anki.lang
%_bindir/anki
%_desktopdir/anki.desktop
%_datadir/pixmaps/anki.png
%_datadir/mime/packages/anki.xml
%_datadir/anki
%_man1dir/anki.*
%doc LICENSE* README*

%changelog
* Sat Apr 13 2019 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.50-alt4
- NMU: really fixed build of this miserable package.

* Sat Apr 13 2019 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt3
- fix build

* Mon Feb 25 2019 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt2
- fix build

* Tue Apr 17 2018 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt1
- first build for Sisyphus


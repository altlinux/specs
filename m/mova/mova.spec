Name: mova
Version: 4.0alt
Release: alt4

Summary: Scripts for manipulating mova format dictionaries
Summary(ru_RU.KOI8-R): Скрипт для работы со словарями в формате mova

License: GPL
Group: System/Internationalization
Url: http://mueller-dic.chat.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %url/script_mova.tar.bz2
Source1: mova_16x16.xpm
Source2: mova-README.alt
Source3: Movarc
Source4: mova-README.speech

Patch1: mova-4.0-alt-config.patch
Patch2: mova-4.0-alt-dont_beep.patch
Patch3: mova-4.0-alt-doc-location.patch
Patch4: mova-4.0-alt-festival.patch
Patch5: mova-4.0-alt-pager.patch
Patch6: mova-4.0-alt-blank.patch
Patch7: mova-4.0-alt-font.patch

Requires: xfonts-phonetic

%description
Mova scipts help user to use mova format dictionaries like
English/Russian dictionary by V. K. Mueller.  MOVA scripts
use standard UNIX utilities: grep, sed, fmt.  Also groff,
less are used for console work.  These utilities search the
plain-text file of the dictionary and place output lines in
GUI.  There is also client movaTK for X Window System.

%description -l ru_RU.KOI8-R
Скрипты Mova облегчают жизнь пользователю при работе со словарями
в формате mova.  Скрипты MOVA используют стандартные UNIX утилиты:
grep, sed, fmt.  Также groff и less используются для работы в
текстовом режиме.  Это утилиты ищут текстовом файле (а это и есть
формат MOVA) нужные строчки, обрабатывают их и выдают на экран.
В пакет включены как текстовый клиент (mova), так и клиент для
X Window System (movaTK).

%prep
%setup -q -c
%patch1
%patch2
%patch3
%patch4
%patch5 -p1
%patch6

mv usr/local/* .%prefix/
chmod -R u+w .
install -pD -m644 %SOURCE2 doc/README.alt
install -pD -m644 %SOURCE4 doc/README.speech


%install
mkdir -p doc
install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -pD -m644 .%_datadir/%name/icons/mova_32x32.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m644 .%_datadir/%name/icons/mova_48x48.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m644 .%_datadir/%name/*.txt doc
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/mova/Movarc

# work around koi8-r only scripts
cd .%_bindir
mv movaTK movaTK-real
mv movaMTK movaMTK-real
cat <<EOF >movaTK
#!/bin/sh
LANG=ru_RU.KOI8-R LC_CTYPE=ru_RU.KOI8-R \$0-real "\$@"
EOF
cat <<EOF >movaMTK
#!/bin/sh
LANG=ru_RU.KOI8-R LC_CTYPE=ru_RU.KOI8-R \$0-real "\$@"
EOF
chmod a+x *
cd -

%__cp -a .%_bindir %buildroot%_bindir

%files
%_sysconfdir/mova/
%_bindir/*
%_liconsdir/*.xpm
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%doc doc/*

%changelog
* Sun Apr 23 2006 Vitaly Lipatov <lav@altlinux.ru> 4.0alt-alt4
- fix phonetic font path (bug #9450), thanks to viy@

* Sun Feb 26 2006 Vitaly Lipatov <lav@altlinux.ru> 4.0alt-alt3
- fix icons dir using

* Sat Feb 12 2005 Vitaly Lipatov <lav@altlinux.ru> 4.0alt-alt2.1
- add LC_CTYPE for backward compatibility (see bug #6025)

* Sat Feb 05 2005 Vitaly Lipatov <lav@altlinux.ru> 4.0alt-alt2
- fix bug #6025
- enable russian input again

* Sun Dec 19 2004 Vitaly Lipatov <lav@altlinux.ru> 4.0alt-alt1
- Fix: check string from X selection
- fix dir /etc/mova packing
- change release to alt

* Mon Nov 10 2003 Vitaly Lipatov <lav@altlinux.ru> 4.0-ipl7.2
- Fix previous patch
- remove dependences to bash from /usr/bin/mova

* Wed Sep 24 2003 Vitaly Lipatov <lav@altlinux.ru> 4.0-ipl7.1
- Add patch against movaTK freezes when it started with empty X clipboard

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 4.0-ipl7
- Fixed groff/grotty compatibility issue.
- Specfile cleanup.
- Additional convention enforcement on patch file names.
- Updated Url, Packager, summary and description.

* Mon Jul  9 2001 Peter Novodvorsky <nidd@altlinux.ru> 4.0-ipl6
- Fixed fonts in Movarc

* Sat Apr 13 2001 Lev Levitin <lev@altlinux.ru> ipl5
- Added festival support to movaMTK

* Tue Feb 21 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl4
- Added xfonts-phonetic to requires.

* Tue Feb 20 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> ipl3
- fixed bug with documentation location

* Sun Feb  4 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl2
- added global configuration file capability

* Thu Feb  1 2001 Dmitry Levin <ldv@fandra.org> ipl1
- spec written from a scratch.

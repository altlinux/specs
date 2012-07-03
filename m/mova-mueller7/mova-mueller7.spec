Name: mova-mueller7
Version: 1.2
Release: alt2.qa3

Summary: V.K. Mueller English-Russian Dictionary, 7 Edition: mova format
Summary(ru_RU.KOI8-R): Англо-русский словарь Мюллера, редакция 7: формат mova

License: GPL
Group: Text tools
Url: http://www.chat.ru/~muller_dic/

%define dict_file       Mueller7GPL
BuildRequires: dict-tools

Source: %dict_file.tgz
Source3: Movarc_Mueller7GPL

BuildArchitectures: noarch

Requires: mova
Provides: mueller7-mova
Obsoletes: mueller7-mova

%description
Electronic version of V.K. Mueller English-Russian Dictionary, 7 Edition
in mova format. You can use it with programs from mova package.

%description -l ru_RU.KOI8-R
Электронная версия англо-русского словаря Мюллера 7-ой редакции.
в формате mova. Для его использования требуются программы из пакета
mova.

%prep
%setup -q -c

%build
mkdir rpmdoc
mv usr/local/share/mova/*.txt rpmdoc/

%install
install -p -m644 -D usr/local/share/dict/%dict_file.koi %buildroot%_datadir/dict/%dict_file.koi
install -p -m644 -D usr/local/share/dict/%dict_file.koi.hash %buildroot%_datadir/dict/%dict_file.koi.hash
install -p -m644 -D %SOURCE3 %buildroot%_sysconfdir/mova/Movarc_Mueller7GPL.koi

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Mova Mueller7 Eng-Rus
Comment=English/Russian dictionary by V.K.Mueller
Icon=mova
Exec=/usr/bin/movaTK -W Mueller7GPL.koi
Terminal=false
Categories=Office;TextTools;Dictionary;
EOF

%files
%_datadir/dict/*
%_desktopdir/%{name}.desktop
%_sysconfdir/mova/*
%doc rpmdoc/*

%changelog
* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2.qa3
NMU: polished desktop file

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2.qa2
- NMU: converted debian menu to freedesktop

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for mova-mueller7
  * postclean-05-filetriggers for spec file

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix phonetic-font path (bug #9450)

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- cleanup and fix spec (menu, bug #5630)
- rename to mova-mueller7 to accordance dictionary policy

* Thu Oct 17 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.2-ipl7
- remove mueller7-dict package

* Thu Apr 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-ipl6
- fixed install scripts

* Mon Sep 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.2-ipl5
- Fixed menu entry

* Mon Jul 9  2001 Nidd <nidd@altlinux.ru> 1.2-ipl4
- Fixed phonetic-font name in Movarc_Mueller7GPL

* Mon May 8  2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> 1.2-ipl3
- Changed movaTK to movaMTK

* Wed Feb 21 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl2
- Added /usr/sbin before dictdconfig in case that user doesn't have
/usr/sbin in path.

* Sun Feb 4 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl1
- Spec rewritten
- mova and dict compatibility
- menu system integration

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org>
- RE adaptions.

* Sat Apr 22 2000 Dmitry V. Levin <ldv@fandra.org>
- sil_ipa-fonts in separate package.
- renamed to mueller7, to avoid conflicts with other mueller dictionaries.

* Sat Apr 22 2000 Dmitry V. Levin <ldv@fandra.org>
- 0.9

* Wed Nov 10 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision

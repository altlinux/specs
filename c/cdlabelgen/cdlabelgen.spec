Name: cdlabelgen
Version: 4.2.0
Release: alt1

Summary: Program for generating frontcards and traycards for CDs
License: BSD
Group: Archiving/Cd burning

Url: http://www.aczoom.com/tools/cdinsert/
Source: http://www.aczoom.com/pub/tools/%name-%version.tgz
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildArch: noarch
BuildRequires: perl-podlators

Summary(ru_RU.KOI8-R): Программа для создания обложек к CD
Summary(uk_UA.KOI8-U): Програма для створення обкладинок для CD

%description
cdlabelgen is a program for generating frontcards and traycards for CDs.

Use it to make labels for your archive CDs, CDs full of oggs, or
even make a label for that CD that you lost the case for!

This package is used by the gcombust frontend to cd burning.

%description -l ru_RU.KOI8-R
cdlabelgen позволяет генерировать обложки для CD.

Пригодится для облагораживания коллекции дисков с ogg, архивами,
ну и восстановления той самой потерянной коробочки!

Также используется в gcombust.

%description -l uk_UA.KOI8-U
cdlabelgen дозволя╓ генерувати обкладинки для CD.

Знадобиться для покращення колекц╕╖ диск╕в з ogg, арх╕вами,
та й поновлення отого втраченого опакунку для диску!

Також використову╓ться в combust.

%prep
%setup

%build
pod2man cdlabelgen.pod > cdlabelgen.1

%install
mkdir -p %buildroot{%_bindir,%_datadir/cdlabelgen,%_man1dir}
install -pm755 cdlabelgen %buildroot%_bindir
install -pm644 postscript/* %buildroot%_datadir/cdlabelgen
install -pm644 cdlabelgen.1 %buildroot%_man1dir

%files
%doc ChangeLog INSTALL README INSTALL.WEB cdinsert.pl
%_bindir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sun Feb 20 2011 Ilya Mashkin <oddity@altlinux.ru> 4.1.0-alt2
- fix build

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 4.1.0-alt1
- 4.1.0

* Mon Nov 05 2007 Michael Shigorin <mike@altlinux.org> 4.0.0-alt1
- 4.0.0
- spec macro abuse cleanup
- added Packager:

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 3.6.0-alt3
- one-byter to fix #5621 (cosmetic; thanks lav@)

* Sun Sep 18 2005 Michael Shigorin <mike@altlinux.org> 3.6.0-alt2
- fixed Url:, thanks to Vitaly Lipatov (lav@)

* Sat Sep 03 2005 Michael Shigorin <mike@altlinux.org> 3.6.0-alt1
- 3.6.0 (major feature enhancements)

* Mon Jan 17 2005 Michael Shigorin <mike@altlinux.ru> 3.5.0-alt1
- 3.5.0 (major feature enhancements)

* Tue Nov 25 2003 Michael Shigorin <mike@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Sat Nov 01 2003 Michael Shigorin <mike@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Mar 26 2003 Michael Shigorin <mike@altlinux.ru> 2.5.0-alt1
- built for ALT Linux (resurrection ;-)
- merged spec with 2.4.0-avl (RH-based)
- spec cleanup

* Thu Nov 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5.0-1mdk
- 2.5.0
- move manpage

* Mon Oct 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.4.0-1mdk
- 2.4.0

* Mon May 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.3.0-1mdk
- 2.3.0
- new url
- maintain templates files in /usr/share despite what makefiles does

* Sat Jul 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-3mdk
- url

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5.0-2mdk
- rebuild

* Mon Oct  2 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.5.0-1mdk
- First spec file for Mandrake distribution.
- Override BASE_DIR in make install

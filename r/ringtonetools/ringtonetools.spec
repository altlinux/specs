Name: ringtonetools
Version: 2.26
Release: alt1

Summary: Tool for converting ringtones and logos for mobile phones
License: Distributable
Group: Sound

Url: http://ringtonetools.mikekohn.net
Source: http://http://www.mikekohn.com/%name/%name-%version.tar.gz

Summary(ru_RU.KOI8-R): Утилита для конвертирования мелодий и лого для мобильных телефонов
Summary(uk_UA.KOI8-U): Утил╕та для конвертування мелод╕й та лого для моб╕льних телефон╕в

%description
Ringtone tools will convert from the following formats: rtttl,
rtx, imelody, midi, wav, bmp, text and can turn them into wav,
kws, mot, pdb, nokia, rtttl, samsung, midi, ems.  With these
formats you can load Nokia, Kyocera, Motorola, Samsung, and
other phones with ringtones and logos.

THIS MAY NOT BE USED IN COMMERCIAL ENVIRONMENTS WITHOUT
PERMISSION OF THE AUTHOR.  PLEASE READ THE LICENSE.

%description -l ru_RU.KOI8-R
%name поддерживает следующие форматы: rtttl, rtx, imelody, midi, wav, bmp,
текст и может превращать их в wav, kws, mot, pdb, nokia, rtttl, samsung, midi,
ems.

Это позволяет загружать их в телефоны, поддерживающие данную функциональность
-- например, Nokia, Kyocera, Motorola, Samsung и некоторые другие.

ЭТА ПРОГРАММА НЕ МОЖЕТ ИСПОЛЬЗОВАТЬСЯ В КОММЕРЧЕСКИХ ЦЕЛЯХ 
БЕЗ РАЗРЕШЕНИЯ АВТОРА.  ПРОЧТИТЕ ЛИЦЕНЗИЮ.

%description -l uk_UA.KOI8-U
%name п╕дтриму╓ так╕ формати: rtttl, rtx, imelody, midi, wav, bmp, текст та
може перетворювати ╕х на wav, kws, mot, pdb, nokia, rtttl, samsung, midi, ems.

Це дозволя╓ завантажувати ╕х у телефони, що п╕дтримують таку функц╕ональн╕сть
-- наприклад, Nokia, Kyocera, Motorola, Samsung та деяк╕ ╕нш╕.

ЦЯ ПРОГРАМА НЕ МОЖЕ ВИКОРИСТОВУВАТИСЯ У КОМЕРЦ╤ЙНИХ Ц╤ЛЯХ 
БЕЗ ДОЗВОЛУ АВТОРА.  ПРОЧИТАЙТЕ Л╤ЦЕНЗ╤Ю.

%prep
%setup -q

%build
%make FLAGS="%optflags"

%install
%__install -pD -m0755 %name %buildroot%_bindir/%name

%files
%doc LICENSE docs/* samples/
%_bindir/*

%changelog
* Sun Dec 11 2005 Michael Shigorin <mike@altlinux.org> 2.26-alt1
- 2.26

* Tue Mar 22 2005 Michael Shigorin <mike@altlinux.ru> 2.23-alt1
- 2.23 (security fix)

* Mon Jul 26 2004 Michael Shigorin <mike@altlinux.ru> 2.21-alt1
- 2.21 (minor bugfixes)

* Sat Jun 26 2004 Michael Shigorin <mike@altlinux.ru> 2.20-alt1
- 2.20

* Wed Sep 17 2003 Michael Shigorin <mike@altlinux.ru> 2.16-alt1
- 2.16 (minor feature enhancements)

* Tue Aug 12 2003 Michael Shigorin <mike@altlinux.ru> 2.14-alt1
- 2.14

* Mon Jul 14 2003 Michael Shigorin <mike@altlinux.ru> 2.13-alt1
- 2.13 (iMelody output reportedly fixed)

* Tue Jul 08 2003 Michael Shigorin <mike@altlinux.ru> 2.12-alt1
- 2.12

* Fri Mar 21 2003 Michael Shigorin <mike@altlinux.ru> 2.11-alt1
- 2.11 (wav output fixed)

* Wed Feb 12 2003 Michael Shigorin <mike@altlinux.ru> 2.09-alt1
- 2.09

* Thu Dec 19 2002 Michael Shigorin <mike@altlinux.ru> 2.07-alt1
- built for ALT Linux


Name: xrcode
Version: 1.0
Release: alt3

Url: ftp://oskin.macomnet.ru/pub/linux/misc
License: GPL
Group: Text tools

# xcode.c and rcode.tar.gz; patched here
Source: %name.tar.bz2
Patch: xcode-gcc41.patch

Summary: Xcode and recode for recoding files between cyrillic codepages
Summary(ru_RU.KOI8-R): Xcode и recode для конвертирования текстов в кириллических кодировках
Summary(uk_UA.KOI8-U): Xcode та recode для конвертування текст╕в в кириличних кодуваннях

%description
rcode - Text recoder (Koi8<->Alternative<->Windows<->ISO).
        And from HEX-style ("=EF=F0") to normal,
        and from HTML-style ("&...;") to normal.
        Made by Serge Bajin (bsv/cntc.dubna.su).

xcode - This program tries to determine input document encoding
        and to convert it to koi8, CP-1251 or cp866.
        Written  by Andrey V. Lukyanov on May 14, 1997
        Last modified on May 18, 1997

These tools modified by Serhii Hlodin (hlodin/lutsk.bank.gov.ua) for
CP1125 codepage support (also known as modified CP866 for Ukraine)

%description -l ru_RU.KOI8-R
rcode - конвертор текста (Koi8<->Alternative<->Windows<->ISO).
        Также из HEX ("=EF=F0") и HTML entities ("&...;").
	Автор: Serge Bajin (bsv/cntc.dubna.su).

xcode - конвертор с автоопределением кодировки текста и последующим
        преобразованием в koi8, CP-1251 или cp866.
	Автор: Andrey V. Lukyanov 14 мая 1997 г.
	Последние изменения: 18 мая 1997 г.

%description -l uk_UA.KOI8-U
rcode - конвертор тексту (Koi8<->Alternative<->Windows<->ISO).
        Також з HEX ("=EF=F0") й HTML entities ("&...;").
	Автор: Serge Bajin (bsv/cntc.dubna.su).

xcode - конвертор с автовизначенням кодування тексту ╕ наступним
	перетворенням в koi8, CP-1251 або cp866.
	Автор: Andrey V. Lukyanov 14 травня 1997 р.
	Останн╕ зм╕ни: 18 травня 1997 р. 

%prep
%setup -q -cn xrcode
%patch

%build
make

%install
install -pD -m755 xcode %buildroot%_bindir/xcode
install -m755 recode %buildroot%_bindir/rcode

%files
%_bindir/*

# TODO: In function `main': the use of `tmpnam' is dangerous, better use `mkstemp'

%changelog
* Mon Jun 05 2006 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- fixed build with gcc4 (thanks vsu@, gns@ and morozov@ for advice)
- minor spec cleanup

* Wed Aug 04 2004 Michael Shigorin <mike@altlinux.ru> 1.0-alt2
- added Url:
- minor spec cleanup

* Mon May 26 2003 Michael Shigorin <mike@altlinux.ru> 1.0-alt1
- built for ALT Linux

* Fri Jul 12 2002 Serhii Hlodin <hlodin@hlodin.lutsk.bank.gov.ua>
- Renamed recode to rcode

* Tue Apr 23 2002 Serhii Hlodin <hlodin@lutsk.bank.gov.ua>
- Initial build.


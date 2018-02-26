Name: fortunes-ru-elders-sophrony
Version: 20070406
Release: alt2

Summary: Quotations from the book by Archimandrite Sophrony (Sakharov)
Summary(ru_RU.KOI8-R): Цитаты из книг Архимандрита Софрония (Сахарова)

Group: Games/Other
License: Public domain
Url: http://sophrony.narod.ru/videt01.htm

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Mon Jun 20 2005 (-bb)
BuildRequires: fortune-mod

%description
Quotations from the book by Archimandrite Sophrony (Sakharov)

%description -l ru_RU.KOI8-R
Цитаты из книг Архимандрита Софрония (Сахарова)

%prep
%setup -q

%install
mkdir -p %buildroot%_gamesdatadir/fortune

iconv -f koi8-r -t utf8 --replace='?' <README.koi8-r >README
i=ru-elders-sophrony
test -r $i.txt
cat $i.txt | \
iconv -f koi8-r -t utf8 --replace='?' \
	>%buildroot%_gamesdatadir/fortune/${i}
strfile %buildroot%_gamesdatadir/fortune/${i}

%files
%doc README
%_gamesdatadir/fortune/ru*

%changelog
* Fri Jul 25 2008 Vitaly Lipatov <lav@altlinux.ru> 20070406-alt2
- fix contents recoding

* Fri Apr 06 2007 Vitaly Lipatov <lav@altlinux.ru> 20070406-alt1
- initial build for ALT Linux Sisyphus

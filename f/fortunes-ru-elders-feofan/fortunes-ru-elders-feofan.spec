Name: fortunes-ru-elders-feofan
Version: 20050913
Release: alt0.3

Summary: Councels of Elders in Russian: Feofan
Summary(ru_RU.KOI8-R): Поучения Старцев: Феофан Затворник

Group: Games/Other
License: Public domain
Url: http://pagez.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Mon Jun 20 2005 (-bb)
BuildRequires: fortune-mod

Obsoletes: fortune-ru-elders-feofan
Provides: fortune-ru-elders-feofan

%description
Councels of Elders in Russian: Feofan

%description -l ru_RU.KOI8-R
Поучения Старцев: Феофан Затворник

%prep
%setup -q

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune

iconv -f koi8-r -t utf8 --replace='?' <README.koi8-r >README
i=ru-elders-feofan
cat $i.txt | \
iconv -f koi8-r -t utf8 --replace='?' \
	>%buildroot%_gamesdatadir/fortune/${i}
strfile %buildroot%_gamesdatadir/fortune/${i}

%files
%doc README
%_gamesdatadir/fortune/ru*

%changelog
* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 20050913-alt0.3
- rename package (fix bug #8117)

* Tue Sep 13 2005 Vitaly Lipatov <lav@altlinux.ru> 20050913-alt0.1
- first build for ALT Linux Sisyphus

%define dict_name	mueller7
%define dict_file       Mueller7GPL

Name: dict-%dict_name-utf8
Version: 1.2
Release: alt4

Summary: V.K. Mueller English-Russian Dictionary, 7 Edition: dict format
Summary(ru_RU.KOI8-R): Англо-русский словарь Мюллера, редакция 7: формат dict
License: GPL
Group: Text tools
Url: http://www.chat.ru/~muller_dic/
BuildArchitectures: noarch

Source: %dict_file.tgz
Source1: to-dict.sh
Source2: mueller2utf8

PreReq: dictd >= 1.7.1
Obsoletes: %dict_name-dict
Obsoletes: dictd-%dict_name-utf8

BuildRequires: libltdl perl-Unicode-Map8 perl-Unicode-String dict-tools >= 1.9.1-alt2

%description 
Electronic version of V.K. Mueller English-Russian Dictionary, 7 Edition
in dict format and utf8 encoding. You can use it with your favourite dict client.

%description -l ru_RU.KOI8-R
Электронная версия англо-русского словаря Мюллера 7-ой редакции
в формате dict и кодировке utf8. Вы можете использовать его со своим любимым
dict клиентом.

%prep
%setup -q -c

%build
cd usr/local/share/dict

export LANG=ru_RU.KOI8-R

cat %dict_file.koi | sed 's/и  пр. et cetera и прочее/и пр.  et cetera и прочее/' | 
perl -e "use locale;" -pne 's/\bбукв\./_букв./g; s/\bвм\./_вм./g; 
s/\bгл\./_гл./g; s/\bи пр\./_и_пр./g; s/\bобыкн\./_обыкн./g; 
s/\bок\./_ок./g; s/\bособ\./_особ./g; s/\bотриц\./_отриц./g;
s/\bпреим\./_преим./g; s/\bраспр\./_распр./g; s/\bсущ\./_.сущ/g;
s/\bтж\./_тж./g; s/\bупотр\./_употр./g; s/\bусил\./_усил./g; ' > %dict_file.fixed

export DICTFMT_OPT="--locale ru_RU.UTF-8"
export LANG=C
/bin/sh %SOURCE1 --src-data %dict_file.fixed %dict_name.koi # && rm -f %dict_file.koi %dict_file.fixed
%SOURCE2 %dict_name.koi > %dict_name.data

/bin/sh %SOURCE1 --data-dict %dict_name.data %dict_name && rm -f %dict_name.data
/bin/sh %SOURCE1 --expand-index %dict_name.index %dict_name.index.exp
cd ../../../..

%install
install -p -m644 -D usr/local/share/dict/%dict_name.dict.dz $RPM_BUILD_ROOT%_datadir/dictd/%dict_name.dict.dz
install -p -m644 -D usr/local/share/dict/%dict_name.index.exp $RPM_BUILD_ROOT%_datadir/dictd/%dict_name.index

%post
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%postun
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%files 
%_datadir/dictd/*

%changelog
* Thu Jan 29 2004 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt4
- fix error in spec file
- syntax fixes in dict file
- update build requires
- copyright info in mueller2utf8 script added

* Thu Jan 30 2003 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt3
- fix bug #0001703: preuninstall script turns dictd off
- build with standard dictfmt and locale ru_RU.UTF-8

* Mon Oct 14 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt2
- rename to dict-mueller7-utf8
- add missing PreReq: dictd

* Fri Sep 20 2002 Alexey Dyachenko <alexd@altlinux.ru> 1.2-alt1
- Translation to UTF-8 encoding.
- initial revision
- spec based on mueller7-mova package

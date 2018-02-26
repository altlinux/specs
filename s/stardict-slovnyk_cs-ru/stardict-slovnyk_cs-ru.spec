%define dict_name		slovnyk_cs-ru
%define dict_file		cs-cz_ru-ru
%define locale			ru_RU
%define dict_eng_name		Czech-Russian


Name: stardict-%dict_name
Version: 0.1
Release: alt1

Summary: Dictionary: Slovnyk %dict_eng_name
License: GPLv2+
Group: Text tools
Requires: stardict >= 2.4.2
Url: http://www.slovnyk.org/
BuildArch: noarch
Source: slovnyk_%dict_file.csv.gz
Packager: Egor Glukhov <kaman@altlinux.org>

BuildRequires: dict-tools stardict-tools

%description
Dictionary: Slovnyk %dict_eng_name

%prep
%setup -c -T

%build
gzip -d -c %SOURCE0 > slovnyk_%dict_file.csv
LC_ALL=C LC_COLLATE=%locale.UTF8 LC_CTYPE=%locale.UTF8 slovnyktodict.awk -v dictname=%dict_name slovnyk_%dict_file.csv
gzip %dict_name.idx
dictzip %dict_name.dict

%install

install -p -m644 -D %dict_name.dict.dz %buildroot%_datadir/stardict/dic/%dict_name.dict.dz
install -p -m644 -D %dict_name.idx.gz %buildroot%_datadir/stardict/dic/%dict_name.idx.gz
install -p -m644 -D %dict_name.ifo %buildroot%_datadir/stardict/dic/%dict_name.ifo

%files
%_datadir/stardict/dic/*

%changelog
* Sat Jul 17 2010 Egor Glukhov <kaman@altlinux.org> 0.1-alt1
- Initial build

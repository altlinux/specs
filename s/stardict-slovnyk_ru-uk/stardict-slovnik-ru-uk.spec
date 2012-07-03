%define dict_name		slovnyk_ru-uk
%define dict_file		ru-ru_uk-ua
%define locale			ru_RU
%define dict_eng_name		Russian-Ukrainian


Name: stardict-%dict_name
Version: 0.1
Release: alt6

Summary: Dictionary: Slovnyk %dict_eng_name
License: GPL
Group: Text tools
Requires: stardict >= 2.4.2
Url: http://www.slovnyk.org/
BuildArchitectures: noarch
Source: http://www.slovnyk.org/csv/slovnyk_%dict_file.csv.gz

# Automatically added by buildreq on Mon Sep 22 2008
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

install -p -m644 -D %dict_name.dict.dz $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.dict.dz
install -p -m644 -D %dict_name.idx.gz $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.idx.gz
install -p -m644 -D %dict_name.ifo $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.ifo

%files
%_datadir/stardict/dic/*

%changelog
* Mon Sep 22 2008 Alex Murygin <murygin@altlinux.ru> 0.1-alt6
- new format (using slovnyktodict.awk)
- removed ru translation from spec

* Wed Nov 26 2003 Alex Murygin <murygin@altlinux.ru> 0.1-alt5
- new format
- minor spec cleaning
- urls changed

* Wed Oct 15 2003 Alex Murygin <murygin@altlinux.ru> 0.1-alt4
- commpress dictionaries

* Sat Sep 20 2003 Alex Murygin <murygin@altlinux.ru> 0.1-alt3
- fixed buildreq
- spec cleaning

* Wed May 21 2003 Alex Murygin <murygin@altlinux.ru> 0.1-alt2
- new stardict format

* Tue May 06 2003 Alex Murygin <murygin@altlinux.ru> 0.1-alt1
- initial build


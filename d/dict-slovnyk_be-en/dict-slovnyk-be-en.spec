%define dict_name		slovnyk_be-en

Name: dict-%dict_name
Version: 0.1
Release: alt2

Summary: Dictionary: Slovnyk Belorussian-English
License: GPL
Group: Text tools

#Url: http://www.mova.org/~cheusov/dict/
Url: rsync://dictd.xdsl.by/dicts
Source0: %dict_name.dict.dz
Source1: %dict_name.index
Packager: Michael Shigorin <mike@altlinux.org>

Requires(post,postun): dictd
BuildArch: noarch
Summary(ru_RU.KOI8-R): Словарь Slovnyk белорусско-английский

%description
Dictionary: Slovnyk Belorussian-English

%description -l ru_RU.KOI8-R
Словарь Slovnyk белорусско-английский

%install
install -pD -m644 %SOURCE0 %buildroot%_datadir/dictd/%dict_name.dict.dz
install -pD -m644 %SOURCE1 %buildroot%_datadir/dictd/%dict_name.index

%post -n dict-%dict_name
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%postun -n dict-%dict_name
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload


%files
%_datadir/dictd/%{dict_name}*

%changelog
* Sat Dec 16 2006 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- rebuild/takeover/cleanup/fix (#2612)
- fix PreReq with targeted Requires()

* Thu Mar 20 2003 Alexey Dyachenko <alexd@altlinux.ru> 0.1-alt1
- initial build


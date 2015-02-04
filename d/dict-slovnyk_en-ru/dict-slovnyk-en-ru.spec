%define dict_name		slovnyk_en-ru

Name: dict-%dict_name
Version: 0.1
Release: alt3

Summary: Dictionary: Slovnyk English-Russian
License: GPL
Group: Text tools

#Url: http://www.mova.org/~cheusov/dict/
Url: rsync://dictd.xdsl.by/dicts
Source0: %dict_name.dict.dz
Source1: %dict_name.index
Packager: Michael Shigorin <mike@altlinux.org>

Requires(post,postun): dictd
BuildArch: noarch
Summary(ru_RU.KOI8-R): Словарь Slovnyk англо-русский

%description
Dictionary: Slovnyk English-Russian

%description -l ru_RU.KOI8-R
Словарь Slovnyk англо-русский

%install
install -pD -m644 %SOURCE0 %buildroot%_datadir/dictd/%dict_name.dict.dz
install -pD -m644 %SOURCE1 %buildroot%_datadir/dictd/%dict_name.index



%files
%_datadir/dictd/%{dict_name}*

%changelog
* Wed Feb 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3
- removed post/un in favor of filetrigger

* Sat Dec 16 2006 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- rebuild/takeover/cleanup/fix (#5076)
- fix PreReq with targeted Requires()

* Thu Mar 20 2003 Alexey Dyachenko <alexd@altlinux.ru> 0.1-alt1
- initial build


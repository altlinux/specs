Name: hunspell-kk
Version: 0.1
Release: alt2
Summary: Kazakh Language Dictionary for Hunspell
Summary(ru_RU.UTF-8): Орфографический cловарь казахского языка для Hunspell
Summary(kk_KZ.UTF-8): Hunspell арналған Орфографиялық қазақ тілі сөздігі
License: GPL2
Group: Text tools
Url: https://addons.mozilla.org/ru/firefox/addon/14049
BuildArch: noarch

Requires:libhunspell

Packager: Ildar Mulyukov <ildar@altlinux.ru>

#https://addons.mozilla.org/ru/firefox/addons/policy/0/14049/63483
Source: addon-14049-latest.xpi

# Automatically added by buildreq on Sat Oct 17 2009 (-bi)
BuildRequires: unzip

%description
This dictionary has been developed under the OpenOffice:Lingucomponent:Spell
Checking/Dictionaries subproject.

%description -l ru_RU.UTF-8
Словарь подготовлен в рамках подпроекта OpenOffice:Lingucomponent:Spell
Checking/Dictionaries.

%description -l kk_KZ.UTF-8
Сөздік OpenOffice:Lingucomponent:Spell Checking/Dictionaries ішкі жобасы
шеңберінде әзірленген.

%prep
%setup -c

%build
cat dictionaries/kz.aff \
	| tr -d '\r' \
	| sed "s|^\xEF\xBB\xBF||" > kk_KZ.aff
tail -n +2 dictionaries/kz.dic \
	| tr -d '\r' \
	| sed "s| */|/|" \
	| LANG=kk_KZ.UTF-8 sort \
	| tee kk_KZ.dic.words \
	| wc -l > kk_KZ.dic
cat kk_KZ.dic.words >> kk_KZ.dic

%install
mkdir -p %buildroot%_datadir/myspell/
install -m 644 kk_KZ.??? %buildroot%_datadir/myspell/

%files
%_datadir/myspell/*
%doc README_kz.txt

%changelog
* Sat Oct 24 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt2
- fixed words order and cleaned up files

* Sat Oct 17 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1
- 1st build for ALTLinux

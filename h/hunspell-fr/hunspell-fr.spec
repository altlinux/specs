Name: hunspell-fr
Summary: French hunspell dictionaries
Version: 2.0.5
Serial: 1
Release: alt2
Group: Text tools
License: LGPLv2
URL: http://dico.savant.free.fr/

Source0: http://dico.savant.free.fr/_download/fr_FR_2-0-5.zip

Requires: libhunspell

BuildArch: noarch
BuildRequires: unzip

%description
French (France, Belgium, etc.) hunspell dictionaries.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fISO8859-15 -tUTF-8 fr_FR.aff > %buildroot%_datadir/myspell/fr_FR.aff
iconv -fISO8859-15 -tUTF-8 fr_FR.dic > %buildroot%_datadir/myspell/fr_FR.dic
subst 's|^SET ISO8859-15|SET UTF-8|' %buildroot%_datadir/myspell/fr_FR.aff

cd %buildroot%_datadir/myspell
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
	ln -s fr_FR.aff $lang.aff
	ln -s fr_FR.dic $lang.dic
done

%files
%doc README_fr_FR.txt
%_datadir/myspell/*

%changelog
* Tue Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.5-alt2
- converted to UTF-8

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.5-alt1
- project moved to http://dico.savant.free.fr and a new release

* Wed Jul 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 20060915-alt1
- initial release

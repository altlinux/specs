Name: hunspell-es
Summary: Spanish hunspell dictionaries
Version: 20081215
Release: alt1
License: LGPLv3+ or GPLv3+ or MPLv1.1
Group: Text tools
URL: http://es.openoffice.org/programa/diccionario.html

Requires: hunspell

Source0: http://es.openoffice.org/files/documents/73/3001/es_ANY.zip

BuildArch: noarch
BuildRequires: unzip

%description
Spanish (Spain, Mexico, etc.) hunspell dictionaries.

%prep
%setup -q -c -n es_ES

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fISO8859-1 -tUTF-8 es_ANY.aff > %buildroot%_datadir/myspell/es_ES.aff
iconv -fISO8859-1 -tUTF-8 es_ANY.dic > %buildroot%_datadir/myspell/es_ES.dic
subst 's|^SET ISO8859-1|SET UTF-8|' %buildroot%_datadir/myspell/es_ES.aff

cd %buildroot%_datadir/myspell
es_ES_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"
for lang in $es_ES_aliases; do
	ln -s es_ES.aff $lang.aff
	ln -s es_ES.dic $lang.dic
done

%files
%doc README.txt
%_datadir/myspell/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20081215-alt1
- initial release


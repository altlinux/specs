Name: hyphen-es
Summary: Spanish hyphenation rules
Version: 20040810
Release: alt1
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+

Requires: libhyphen

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_es_ES.zip

BuildArch: noarch
BuildRequires: unzip

%description
Spanish hyphenation rules.

%prep
%setup -q -c

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/hyphen
iconv -fISO8859-1 -tUTF-8 hyph_es_ES.dic > %buildroot%_datadir/hyphen/hyph_es_ES.dic
subst 's|^ISO8859-1|UTF-8|' %buildroot%_datadir/hyphen/hyph_es_ES.dic

cd %buildroot%_datadir/hyphen/
es_ES_aliases="es es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"
for lang in $es_ES_aliases; do
	ln -s hyph_es_ES.dic hyph_$lang.dic
done

%files
%doc README*
%_datadir/hyphen/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20040810-alt1
- initial release


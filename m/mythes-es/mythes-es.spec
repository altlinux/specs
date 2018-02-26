Name: mythes-es
Summary: Spanish thesaurus
Version: 20090306
Release: alt1
Group: Text tools
URL: http://openthes-es.berlios.de
License: LGPLv2+

Source0: http://openthes-es.berlios.de/download/OOo2-thes_es_ES.tar.bz2

BuildArch: noarch
BuildRequires: unzip

%description
Spanish thesaurus.

%prep
%setup -q -c

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/mythes
install -m644 th_es_ES_v2.* %buildroot%_datadir/mythes

cd %buildroot%_datadir/mythes/
es_ES_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"
for lang in $es_ES_aliases; do
        ln -s th_es_ES_v2.idx "th_"$lang"_v2.idx"
        ln -s th_es_ES_v2.dat "th_"$lang"_v2.dat"
done

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090306-alt1
- initial release


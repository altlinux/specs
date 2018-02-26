# first 256 bytes of ASCII
############################################################
############################################################
############################################################
############################################################
#define dict_name	eng-fra
%define dict_name	fra-eng
%define stardict_name	dictd_www.freedict.de_%dict_name
#define dict_sum_en English-Franch
%define dict_sum_en French-English
#define dict_sum_ru Англо-французский
#define dict_des_ru англо-французского
%define dict_sum_ru Французско-английский
%define dict_des_ru французского-английского

BuildRequires: dict-tools
%def_without stardict
%if_with stardict
BuildRequires: stardict-tools >= 2.4.2
%endif

Name: dict-%dict_name
Version: 0.1
Release: alt1

Summary: %dict_sum_en Dictionary: dictd format
Summary(ru_RU.CP1251): %dict_sum_ru словарь: формат dictd
License: GPL
Group: Text tools
PreReq: dictd
Url: http://www.freedict.de

Source: %dict_name.tar.gz

BuildArchitectures: noarch

%description
Electronic version of %dict_sum_en Dictionary, in dictd format. 
You can use it with your favourite dict client.

%description -l ru_RU.CP1251
Электронная версия %dict_des_ru словаря в формате dictd.
Вы можете использовать его со своим любимым dict клиентом.

%if_with stardict
%package -n stardict-%stardict_name
Summary: %dict_sum_en Dictionary: stardict format
Summary(ru_RU.CP1251): %dict_sum_ru словарь: формат stardict
License: GPL
Group: Text tools
PreReq: stardict

%description -n stardict-%stardict_name
Electronic version of %dict_sum_en Dictionary, in stardict format. 
You can use it with your favourite stardict client.

%description -n stardict-%stardict_name -l ru_RU.CP1251
Электронная версия %dict_des_ru словаря в формате stardict.
Вы можете использовать его со своим любимым stardict клиентом.
%endif

%prep
%setup -q -c

%install
install -p -m644 -D %dict_name.dict.dz $RPM_BUILD_ROOT%_datadir/dictd/%dict_name.dict.dz
install -p -m644 -D %dict_name.index $RPM_BUILD_ROOT%_datadir/dictd/%dict_name.index

%if_with stardict
dictzip -d %dict_name.dict.dz
WORDCOUNT=`dictd2dic %dict_name | grep count | awk '{print $2}'`
[ -f %stardict_name.idx.gz ] && gunzip %stardict_name.idx.gz
IDXSIZE=`ls -l %stardict_name.idx | awk '{print $5}'`
cat >%stardict_name.ifo <<EOF
StarDict's dict ifo file
version=2.4.2
wordcount=$WORDCOUNT
idxfilesize=$IDXSIZE
bookname=%stardict_name
date=`date '+%%Y.%%m.%%d'`
sametypesequence=m
EOF
#gzip %stardict_name.idx

install -p -m644 -D %stardict_name.dict.dz $RPM_BUILD_ROOT%_datadir/stardict/dic/%stardict_name.dict.dz
install -p -m644 -D %stardict_name.idx    $RPM_BUILD_ROOT%_datadir/stardict/dic/%stardict_name.idx
install -p -m644 -D %stardict_name.ifo $RPM_BUILD_ROOT%_datadir/stardict/dic/%stardict_name.ifo
%endif


%post -n dict-%dict_name
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%postun -n dict-%dict_name
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%files
%_datadir/dictd/%{dict_name}*

%if_with stardict
%files -n stardict-%stardict_name
%_datadir/stardict/dic/*
%endif

%changelog
* Sat Jun 03 2006 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- temporarily disabled building of stardict dictionaries
- initial build for Alt Linux

# Local Variables:
# coding: cp1251
# End:

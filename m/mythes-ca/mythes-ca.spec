Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: mythes-ca
Summary: Catalan thesaurus
Version: 2.3.1
Release: alt1_1
Source: https://github.com/Softcatala/sinonims-cat/releases/latest/download/thesaurus-ca.oxt
URL: http://www.softcatala.org/wiki/Projectes/Openthesaurus-ca
License: CC-BY-4.0
BuildArch: noarch
Requires: libmythes
Source44: import.info

%description
Catalan thesaurus.

%prep
%setup -q -c

%build
for i in release_note-ca.txt dictionaries/README_th_ca.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_ca_ES.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ca_ES_v2.dat
cp -p dictionaries/th_ca_ES.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ca_ES_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s th_ca_ES_v2.dat "th_"$lang"_v2.dat"
        ln -s th_ca_ES_v2.idx "th_"$lang"_v2.idx"
done
popd


%files
%doc dictionaries/README_th_ca.txt LICENCES-fr.txt LICENSES-en.txt LICENCIAS-es.txt LLICENCIES-ca.txt release_note-ca.txt
%{_datadir}/mythes/*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_1
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_27
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_5
- import by fcmass


Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fj
Summary: Fijian hunspell dictionaries
Version: 1.2
Release: alt2_28
#Source: http://www.foss.usp.ac.fj/OOo_fj/OOo_fj_FJ.zip
Source: https://addons.mozilla.org/firefox/downloads/file/84397/fijian_spelling_dictionary-%{version}-fx+tb+sm.xpi
URL: http://www.iosn.net/pacific-islands/usp-microgrants/fijian-spellchecker
License: LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
BuildArch: noarch
BuildRequires: hunspell-utils libhunspell-devel
Source44: import.info


%description
Fijian hunspell dictionaries.

%prep
%setup -q -c


%build
cd dictionaries
for i in README_fj_FJ.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
chmod -x fj_FJ.*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/fj_FJ.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fj.aff
cp -p dictionaries/fj_FJ.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fj.dic


%files
%doc dictionaries/README_fj_FJ.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Fri Sep 08 2023 Igor Vlasenko <viy@altlinux.org> 1.2-alt2_28
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_11
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_5
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4
- update to new release by fcimport

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3
- new release by fedoraimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_2
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2
- import from Fedora by fcimport


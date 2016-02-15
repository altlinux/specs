# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-om
Summary: Oromo hunspell dictionaries
#Epoch: 1
Version: 0.04
Release: alt2_9
Group: Text tools
Source: http://borel.slu.edu/obair/%{name}-%{version}.oxt
URL: http://borel.slu.edu/crubadan/apps.html
License: LGPLv3+
BuildArch: noarch
Requires: hunspell
Source44: import.info

%description
Oromo hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/om_ET.* $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
om_ET_aliases="om_KE"
for lang in $om_ET_aliases; do
        ln -s om_ET.aff $lang.aff
        ln -s om_ET.dic $lang.dic
done

%files
%doc dictionaries/README_om_ET.txt LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- import from Fedora by fcimport


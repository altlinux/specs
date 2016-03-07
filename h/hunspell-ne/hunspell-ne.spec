Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-ne
Summary: Nepali hunspell dictionaries
Version: 20080425
Release: alt2_13
Source: http://nepalinux.org/downloads/ne_NP_dict.zip
URL: http://nepalinux.org/downloads
License: LGPLv2
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Nepali hunspell dictionaries.

%prep
%setup -q -c -n ne_NP_dict
sed -i 's|चलन/चल्ती/15,22|चलनचल्ती/15,22|g' ne_NP.dic
sed -i 's|निजामती/I15,22|निजामती/15,22|g' ne_NP.dic

# Remove ^M and trailing whitespace characters
sed -i 's/\r//;s/[ \t]*$//' ne_NP.dic

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ne_NP_aliases="ne_IN"
for lang in $ne_NP_aliases; do
        ln -s ne_NP.aff $lang.aff
        ln -s ne_NP.dic $lang.dic
done
popd

%files
%doc README_ne_NP.txt 
%{_datadir}/myspell/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_13
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_9
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_5
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20080425-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20080425-alt1_2
- import from Fedora by fcimport


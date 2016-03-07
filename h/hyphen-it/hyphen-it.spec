Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-it
Summary: Italian hyphenation rules
%global upstreamid 20071127
Version: 0.%{upstreamid}
Release: alt1_14
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_it_IT.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPLv2+
BuildArch: noarch
Requires: libhyphen
Provides: hyphen-la = 0.%{upstreamid}-3%{?dist}
Source44: import.info

%description
Italian hyphenation rules.

%prep
%setup -q -c -n hyphen-it
chmod -x *

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_it_IT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
#http://extensions.services.openoffice.org/project/dict-la uses the it_IT for Latin
#so we'll do the same
it_IT_aliases="it_CH la_VA"
for lang in $it_IT_aliases; do
        ln -s hyph_it_IT.dic "hyph_"$lang".dic"
done


%files
%doc README_hyph_it_IT.txt
%{_datadir}/hyphen/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_14
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_8
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_7
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20071127-alt1_6
- import by fcmass


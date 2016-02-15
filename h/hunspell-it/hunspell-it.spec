# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hunspell-it
Summary: Italian hunspell dictionaries
%define upstreamid 20070901
Version: 2.4
Release: alt2_0.13.%{upstreamid}
Source: http://downloads.sourceforge.net/sourceforge/linguistico/italiano_2_4_2007_09_01.zip
Group: Text tools
URL: http://linguistico.sourceforge.net
License: GPLv3+
BuildArch: noarch
Requires: hunspell
#dic contains free-form text inside the .dic, i.e. "error: line 3: bad flagvector"
#  https://sourceforge.net/tracker/?func=detail&aid=2994177&group_id=128318&atid=711333
Patch0: hunspell-it-sf2994177.cleandic.patch
Source44: import.info

%description
Italian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-it
%patch0 -p0 -b .cleandic

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s it_IT.aff $lang.aff
        ln -s it_IT.dic $lang.dic
done


%files
%doc it_IT_README.txt it_IT_COPYING it_IT_AUTHORS it_IT_license.txt it_IT_notes.txt
%{_datadir}/myspell/*

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.13.20070901
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.12.20070901
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.11.20070901
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.10.20070901
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.9.20070901
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.8.20070901
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.7.20070901
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_0.6.20070901
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_0.6.20070901
- import from Fedora by fcimport


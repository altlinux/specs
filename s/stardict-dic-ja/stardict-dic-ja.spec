Name: stardict-dic-ja
Summary: Japanese(ja) dictionaries for StarDict
Version: 2.4.2
Release: alt2_14
Group: Text tools
# Upstream calls this the "EDRDG" license
# but it is just CC-BY-SA
# http://www.edrdg.org/edrdg/newlic.html
License: CC-BY-SA
URL: http://stardict.sourceforge.net

Source0: http://downloads.sourceforge.net/stardict/stardict-edict-2.4.2.tar.bz2
Source1: http://downloads.sourceforge.net/stardict/stardict-jmdict-en-ja-2.4.2.tar.bz2
Source2: http://downloads.sourceforge.net/stardict/stardict-jmdict-ja-en-2.4.2.tar.bz2

BuildArchitectures: noarch

Requires: stardict stardict-plugin-espeak stardict-plugin-spell
Source44: import.info

%description
Japanese(ja) dictionaries for StarDict.
These dictionaries are included currently:
edict, jmdict-en-ja, jmdict-ja-en.
You can download more at: http://stardict.sourceforge.net

%prep
%setup -c -T -n %{name}-%{version}
%setup -q -n %{name}-%{version} -D -T -a 0
%setup -q -n %{name}-%{version} -D -T -a 1
%setup -q -n %{name}-%{version} -D -T -a 2

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
cp -rf stardict-* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/

%files
%{_datadir}/stardict/dic/*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_13
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_7
- initial release by fcimport


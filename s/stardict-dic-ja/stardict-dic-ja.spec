Name: stardict-dic-ja
Summary: Japanese(ja) dictionaries for StarDict
Version: 2.4.2
Release: alt2_8
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

Requires: stardict >= 2.4.2
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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_7
- initial release by fcimport


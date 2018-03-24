Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-ta
Summary: Tamil hunspell dictionaries
Version: 1.0.0
Release: alt1_9
Epoch:   1
Source: http://anishpatil.fedorapeople.org/ta_in.%{version}.tar.gz
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Tamil hunspell dictionaries.

%prep
%setup -q -c -n ta_IN


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ta_IN/*.dic ta_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc ta_IN/README
%doc --no-dereference ta_IN/LICENSE ta_IN/Copyright
%{_datadir}/myspell/*

%changelog
* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_9
- new version

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_7
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_5
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20100226-alt2_2
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20100226-alt1_2
- import from Fedora by fcimport


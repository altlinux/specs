Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hunspell-pa
Summary: Punjabi hunspell dictionaries
Version: 1.0.0
Release: alt1_9
Epoch: 1
Source: http://anishpatil.fedorapeople.org/pa_in.%{version}.tar.gz
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Punjabi hunspell dictionaries.

%prep
%setup -q -c -n pa_IN

iconv -f ISO-8859-1 -t UTF-8 pa_IN/Copyright > pa_IN/Copyright.utf8
mv pa_IN/Copyright.utf8 pa_IN/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p pa_IN/*.dic pa_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc pa_IN/README
%doc --no-dereference pa_IN/COPYING pa_IN/Copyright
%{_datadir}/myspell/*

%changelog
* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_9
- new version

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_8
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20050726-alt1_5
- import from Fedora by fcimport


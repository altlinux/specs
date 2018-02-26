Name: hunspell-pa
Summary: Punjabi hunspell dictionaries
Version: 20050726
Release: alt2_7
Source: http://hunspell.sourceforge.net/pa-demo.tar.gz
Group: Text tools
URL: http://hunspell.sourceforge.net
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Punjabi hunspell dictionaries.

%prep
%setup -q -c -n pa-demo
iconv -f ISO-8859-1 -t UTF-8 pa/Copyright > pa/Copyright.utf8
mv pa/Copyright.utf8 pa/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv pa/pa.dic pa/pa_IN.dic
mv pa/pa.aff pa/pa_IN.aff
cp -p pa/*.dic pa/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc pa/README pa/COPYING pa/Copyright
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_7
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_5
- rpm Group changed to Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20050726-alt1_5
- import from Fedora by fcimport


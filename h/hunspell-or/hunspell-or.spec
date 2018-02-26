Name: hunspell-or
Summary: Oriya hunspell dictionaries
Version: 20050726
Release: alt2_7
Source: http://hunspell.sourceforge.net/or-demo.tar.gz
Group: Text tools
URL: http://hunspell.sourceforge.net
License: LGPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Oriya hunspell dictionaries.

%prep
%setup -q -c -n or-demo
iconv -f ISO-8859-1 -t UTF-8 or/Copyright > or/Copyright.utf8
mv or/Copyright.utf8 or/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv or/or.dic or/or_IN.dic
mv or/or.aff or/or_IN.aff
cp -p or/*.dic or/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc or/README or/COPYING or/Copyright
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


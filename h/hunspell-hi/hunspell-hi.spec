Name: hunspell-hi
Summary: Hindi hunspell dictionaries
Version: 20050726
Release: alt2_9
Source: http://hunspell.sourceforge.net/hi-demo.tar.gz
Group: Text tools
URL: http://hunspell.sourceforge.net
License: GPLv2+
BuildArch: noarch

Requires: hunspell
Source44: import.info

%description
Hindi hunspell dictionaries.

%prep
%setup -q -c -n hi-demo
iconv -f ISO-8859-1 -t UTF-8 hi/Copyright > hi/Copyright.utf8
mv hi/Copyright.utf8 hi/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv hi/hi.dic hi/hi_IN.dic
mv hi/hi.aff hi/hi_IN.aff
cp -p hi/*.dic hi/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc hi/README hi/COPYING hi/Copyright
%{_datadir}/myspell/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_9
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_8
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20050726-alt2_7
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 20050726-alt1_7
- import from Fedora by fcimport


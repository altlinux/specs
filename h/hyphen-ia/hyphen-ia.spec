Group: Text tools
Name: hyphen-ia
Summary: Interlingua hyphenation rules
%global upstreamid 20050628
Version: 0.%{upstreamid}
Release: alt1_11
Source: http://www.ctan.org/get/language/hyphenation/iahyphen.tex
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/iahyphen.html
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-ia-cleantex.patch
Source44: import.info

%description
Interlingua hyphenation rules.

%prep
%setup -T -q -c -n hyphen-ia
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1
echo "Created with substring.pl by substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1" > README
echo "---" >> README
head -n 25 iahyphen.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ia.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_11
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_9
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_5
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20050628-alt1_3
- import by fcmass


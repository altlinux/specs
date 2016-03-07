Group: Text tools
Name: hyphen-lt
Summary: Lithuanian hyphenation rules
%global upstreamid 20100531
Version: 0.%{upstreamid}
Release: alt1_10
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-lt.tex?view=co#/hyph-lt.tex
URL: http://tug.org/tex-hyphen
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-lt-cleantex.patch
Source44: import.info

%description
Lithuanian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-lt
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-lt.tex hyph_lt_LT.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-lt.tex hyph_lt_LT.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 45 hyph-lt.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_lt_LT.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_10
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_6
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_4
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_3
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass


Name: hyphen-grc
Summary: Ancient Greek hyphenation rules
%define upstreamid 20110913
Version: 0.%{upstreamid}
Release: alt1_8
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex?view=co
Source: hyph-grc.tex
Group: Text tools
URL: http://tug.org/tex-hyphen
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-grc-cleantex.patch
Source44: import.info

%description
Ancient Greek hyphenation rules.

%prep
%setup -T -q -c -n hyphen-grc
cp -p %{SOURCE0} hyph-grc.tex
%patch0 -p0 -b .clean

%build
grep -v "^%" hyph-grc.tex | tr ' ' '\n' > temp.tex
substrings.pl temp.tex temp.dic UTF-8
LANG=el_GR.utf8 uniq temp.dic > hyph_grc_GR.dic
echo "created with substring.pl by substrings.pl hyph-grc.tex hyph_grc_GR.dic UTF-8" > README
echo "---" >> README
head -n 37 hyph-grc.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_grc_GR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_7
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_3
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110913-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass


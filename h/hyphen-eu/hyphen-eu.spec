# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-eu
Summary: Basque hyphenation rules
%define upstreamid 20110620
Version: 0.%{upstreamid}
Release: alt1_2
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex?view=co
Source: hyph-eu.tex
Group: Text tools
URL: http://tp.lc.ehu.es/jma/basque.html
License: LPPL
BuildArch: noarch
BuildRequires: libhyphen-devel
Requires: libhyphen
Patch0: hyphen-eu-cleantex.patch
Source44: import.info

%description
Basque hyphenation rules.

%prep
%setup -T -q -c -n hyphen-eu
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
grep -v "^%" hyph-eu.tex | tr ' ' '\n' > temp.tex
substrings.pl temp.tex hyph_eu_ES.dic ISO8859-1
echo "Created with substring.pl by substrings.pl hyph-eu.tex hyph_eu_ES.dic ISO8859-1" > README
echo "---" >> README
head -n 34 hyph-eu.tex >> README

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_eu_ES.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%files
%doc README
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.20110620-alt1_1
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.20100531-alt1_2
- import by fcmass

